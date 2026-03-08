---
layout: post
title: "Deploying Doc Router on Kubernetes: From Docker Compose to EKS and Digital Ocean"
date: 2026-03-07 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/deploying-doc-router-kubernetes-splash.png
categories: [tech, kubernetes, devops, docrouter]
description: "Production-grade Kubernetes support for Doc Router: key decisions, Helm chart, worker merging, graceful shutdown, and multi-cloud deployment."
---

We recently added production-grade Kubernetes support to Doc Router. This post walks through the key decisions and challenges we encountered along the way.

If you're new to Kubernetes, start with [Kubernetes for Docker Users: A Practical Primer]({% post_url 2026-03-05-kubernetes-for-docker-users-primer %}), which covers the core concepts — Pods, Deployments, Services, Namespaces, Secrets, PVCs, Helm, and Kind — before diving into this post. For packaging and GitOps (Kustomize, Helm, Flux), see [Kubernetes Packaging and Deployment]({% post_url 2026-03-06-kubernetes-packaging-helm-gitops %}).

## Why Kubernetes?

Doc Router was originally deployed using Docker Compose, which worked well for single-node setups. As we started onboarding enterprise customers with availability and scalability requirements, we needed:

- **Horizontal scaling** — multiple replicas behind a load balancer
- **Automated failover** — pods restarted on failure without manual intervention
- **Rolling deployments** — zero-downtime upgrades
- **Resource isolation** — CPU and memory limits per component

## Architecture

The production deployment consists of two main workloads:

- **Frontend** — Next.js server (SSR + API routes via NextAuth)
- **Backend** — FastAPI application with embedded background workers

Both run as Kubernetes Deployments behind a shared nginx ingress with TLS terminated by cert-manager (Let's Encrypt).

MongoDB can run outside the cluster (MongoDB Atlas) or in-cluster via our [`mongodb-atlas-local`](https://github.com/analytiq-hub/analytiq-charts) Helm chart — see [Self-Hosted MongoDB on Kubernetes with Atlas Search]({% post_url 2026-03-08-self-hosted-mongodb-kubernetes-atlas-search %}) for the install guide. AWS S3 remains an external dependency.

## Helm Chart

We packaged the deployment as a Helm chart (`deploy/charts/doc-router`) published to GitHub Container Registry (ghcr.io) as an OCI artifact. The chart is versioned independently of the Docker images, so we can update deployment configuration without rebuilding the application.

Key design decisions:

- **Single `values.yaml`** with sensible defaults — operators override only what differs per cluster
- **ConfigMap for non-secret config** — `NEXTAUTH_URL`, `FASTAPI_ROOT_PATH`, worker count, S3 bucket
- **Kubernetes Secret for credentials** — MongoDB URI, API keys, NextAuth secret — created by the deploy script, never stored in the chart
- **Ingress host derived from `APP_HOST`** — a single variable drives the entire URL configuration

## Choosing a Container Registry

We evaluated two natural options: **Amazon ECR** (since we're already on AWS/EKS) and **GitHub Container Registry (ghcr.io)** (since our source is on GitHub).

**ECR** has one significant operational advantage for EKS: nodes authenticate via IAM role, so there is no image pull secret to manage. Costs are low — $0.10/GB stored, with no data transfer charge for pulls within the same AWS region. However, ECR is tightly coupled to AWS. A second deployment on Digital Ocean or a customer's on-premises cluster would need separate registry credentials and mirroring, making it a poor fit for a multi-cloud or self-hosted product.

**ghcr.io** is cloud-neutral — any cluster anywhere can pull images with a single token. It integrates naturally with GitHub Actions (the `GITHUB_TOKEN` secret already has `packages: write` permission), so publishing images is zero-configuration. The chart package also appears directly on the repository's GitHub page alongside the source code and releases, which is the right home for an open-source project.

The catch: ghcr.io packages are **private by default** for organizations, and GitHub's free tier includes only 500 MB storage and 1 GB transfer per month. For clusters that pull large images repeatedly, those limits are reached quickly. Making packages public eliminates the cost entirely, but requires an organization admin to enable public package creation in the org settings — it is disabled by default.

We chose ghcr.io and made our packages public. The images contain no secrets — only application code — so public visibility is appropriate and keeps infrastructure simple. Clusters pull anonymously with no credentials required.

For customers who need private images (for example, an enterprise build with proprietary integrations), the `REGISTRY_PROVIDER` variable in the overlay `.env` file can be switched to `aws` or `do` to use ECR or Digital Ocean Container Registry instead, with registry login handled automatically by the deploy scripts.

## Merging Workers into FastAPI

The original architecture ran the background workers (OCR, LLM, KB indexing, webhooks) as a separate process alongside uvicorn. In Kubernetes, this meant each backend pod ran two Python processes, consuming ~375 MB of memory.

We merged the workers into the FastAPI lifespan using `asyncio.create_task`:

```python
@asynccontextmanager
async def lifespan(app):
    # startup
    worker_tasks = start_workers(n_workers)
    yield
    # shutdown
    for task in worker_tasks:
        task.cancel()
    await asyncio.gather(*worker_tasks, return_exceptions=True)
```

This halved per-pod memory usage (~190 MB) and eliminated the process management overhead. The workers share the same event loop as the API, which is safe because all worker I/O is already async.

## Worker Polling Optimization

With multiple replicas, each pod runs a full set of worker coroutines polling MongoDB queues. At idle with 4 workers per pod, that was ~80 MongoDB queries per second cluster-wide.

We implemented exponential backoff with shared state across parallel workers:

```python
_queue_idle_sleep: dict[str, float] = {}  # shared across all workers on a queue

# on idle: back off
sleep = _queue_idle_sleep.get("ocr", POLL_MIN_SLEEP)
await asyncio.sleep(sleep)
_queue_idle_sleep["ocr"] = min(sleep * 2, POLL_MAX_SLEEP)

# on message found: reset for all workers on this queue
_queue_idle_sleep["ocr"] = POLL_MIN_SLEEP
```

This reduces idle polling to near-zero while keeping response latency low when work arrives.

## Graceful Shutdown

When Kubernetes scales down a pod (HPA scale-in or rolling update), it sends SIGTERM. We needed in-flight jobs to be marked as failed rather than silently abandoned.

Since workers are asyncio tasks, cancellation arrives as `asyncio.CancelledError` — a `BaseException`, not caught by `except Exception`. We added explicit handling in each worker:

```python
try:
    await ad.msg_handlers.process_ocr_msg(analytiq_client, msg)
except asyncio.CancelledError:
    logger.warning(f"Worker cancelled mid-flight on msg {msg.get('_id')}, marking failed")
    await ad.queue.delete_msg(analytiq_client, "ocr", str(msg["_id"]), status="failed")
    raise  # allow the task to actually cancel
```

The failed job can then be retried on another pod.

## Database Migrations as a Helm Pre-Upgrade Hook

Running database migrations safely in a multi-replica environment requires that migrations complete before any new application code starts serving traffic. In Docker Compose this is handled by startup ordering, but in Kubernetes rolling updates, new pods can start before old ones are gone — with no guarantee about migration timing.

We solved this with a Helm hook Job that runs `migrate.py` using the same backend image, annotated to execute before the upgrade rolls out:

```yaml
annotations:
  "helm.sh/hook": pre-upgrade,pre-rollback
  "helm.sh/hook-weight": "-5"
  "helm.sh/hook-delete-policy": hook-succeeded,before-hook-creation
```

The `pre-upgrade` hook ensures migrations run and complete successfully before Helm touches any Deployment. If the migration Job fails, Helm aborts the upgrade entirely — the old version keeps running. `hook-delete-policy: hook-succeeded` cleans up the completed Job automatically, keeping the namespace tidy. The `before-hook-creation` policy ensures the old Job is removed if a previous run left one behind.

One subtlety: at pre-upgrade time, the ConfigMap has not yet been updated by Helm (hooks run before regular resources). The migration Job therefore mounts only the Secret — which contains `MONGODB_URI` — and not the ConfigMap:

```yaml
envFrom:
- secretRef:
    name: doc-router-secrets
# ConfigMap intentionally omitted — not yet updated at hook time
```

This means `migrate.py` must be written to need only the database connection string, with no dependency on application config values.

The result is a safe, atomic upgrade sequence: **migrate → roll out new pods → terminate old pods** — with automatic rollback if the migration fails.

## HPA Tuning

We configured Horizontal Pod Autoscaler on the backend with both CPU and memory targets:

```yaml
metrics:
- type: Resource
  resource:
    name: cpu
    target:
      type: Utilization
      averageUtilization: 80
- type: Resource
  resource:
    name: memory
    target:
      type: Utilization
      averageUtilization: 80
```

A subtle issue: HPA scale-down uses `ceil(currentReplicas × currentUtil / targetUtil)`. With 5 pods at 72% memory utilization against an 80% target, `ceil(5 × 72/80) = ceil(4.5) = 5` — the ceiling arithmetic created a deadlock where the cluster could never scale below 5 pods.

The fix was increasing the memory request from 512 Mi to 768 Mi. After the worker merge reduced actual usage to ~190 MB, utilization dropped to ~25% — well below the threshold — and the cluster scaled back down to the minimum of 2 replicas.

## Environment Configuration

Next.js `NEXT_PUBLIC_*` variables are baked into the browser bundle at build time, not injected at runtime. This caused a subtle bug: our local `.env.local` file set `NEXT_PUBLIC_FASTAPI_FRONTEND_URL=http://127.0.0.1:8000`. Because `.env.local` wasn't listed in `.dockerignore`, it was copied into the Docker build context and read by Next.js during `npm run build` — silently overriding the intended production value and baking the localhost URL into every image.

We fixed this in two steps:

1. **Exclude all `.env.*` files from the Docker build context** by adding `**/.env.*` to `.dockerignore`, so local development env files can never leak into images.

2. **Remove `NEXT_PUBLIC_FASTAPI_FRONTEND_URL` entirely.** Rather than baking an absolute URL into the bundle, the frontend now always calls `/fastapi` — a relative path that works from any hostname. Next.js rewrites proxy `/fastapi/:path*` to the backend service URL at the server layer:

```js
// next.config.mjs
async rewrites() {
  return [{
    source: '/fastapi/:path*',
    destination: `${process.env.FASTAPI_BACKEND_URL}/fastapi/:path*`,
  }];
}
```

`FASTAPI_BACKEND_URL` is a server-side runtime variable (not `NEXT_PUBLIC_`) pointing to the in-cluster backend service (`http://backend.<namespace>.svc.cluster.local:8000`). It is never exposed to the browser. The result is a truly environment-agnostic frontend image that requires no rebuild when moving between clusters.

## CI/CD Pipeline

### Structure

We use three GitHub Actions workflows:

- **`backend-tests.yml`** — runs Python tests against a local MongoDB Atlas instance (with vector search via `mongodb-atlas-local`) plus TypeScript tests. Triggered by `workflow_call` or `workflow_dispatch`.
- **`frontend-build.yml`** — runs `npm run build` for the Next.js frontend. Also triggered by `workflow_call` or `workflow_dispatch`.
- **`ci.yml`** — runs both test workflows on every pull request to `main`.
- **`release.yml`** — triggered on semver tags (`v[0-9]*.[0-9]*.[0-9]*`). Runs both test workflows first, then builds and pushes Docker images if they pass.

### Why semver tags, not branch pushes

An early version of the pipeline ran tests on every push to `main` and triggered builds from there. This caused two problems:

1. **Tests ran twice per release** — once on the branch push, once triggered by the tag.
2. **The tag trigger didn't wait for tests** — if a tag was pushed immediately after a commit, the build could race ahead of a still-running test run.

The current design avoids both: `release.yml` is only triggered by a semver tag, and the `build-push` job declares `needs: [test-backend, test-frontend]`, so Docker images are never built unless all tests pass on that exact commit. Tests run exactly once per release.

The `ci.yml` workflow handles the PR gate separately — developers get test feedback on their branch without triggering a build.

### Reusable test workflows

Making the test workflows `workflow_call`-able (rather than duplicating the job definitions in both `ci.yml` and `release.yml`) keeps the test logic in one place. Both workflows call the same definitions; any change to the test steps is automatically reflected in both gates.

`workflow_dispatch` is kept on each test workflow so that individual test suites can be re-run manually from the GitHub Actions UI without needing to push a commit or tag.

### Image tagging

The build step computes image tags from the git tag:

```yaml
TAG="${{ github.ref_name }}"          # e.g. v27.0.1-rc2 or v27.0.1
FRONTEND_TAGS="${FRONTEND}:${TAG}"
# :latest only for stable releases (no pre-release suffix)
if [[ "$TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  FRONTEND_TAGS="${FRONTEND_TAGS},${FRONTEND}:latest"
fi
```

Release candidates (`v27.0.1-rc2`) get a versioned tag only. Stable releases (`v27.0.1`) also update `:latest`. This means a cluster running `:latest` auto-updates on the next `helm upgrade`, while a cluster pinned to a specific tag is unaffected.

### Helm chart publishing is manual

The Helm chart is published separately with `./deploy/scripts/publish-chart.sh <overlay>`. We kept this manual for two reasons: the chart version is independent of the app version (you might push 10 image releases without any chart changes), and publishing the chart is a deliberate operator action — it should not happen automatically on every tag.

## Egress IPs and External Service Whitelisting

A practical difference between EKS and DOKS emerged when connecting to MongoDB Atlas, which requires IP whitelisting for all incoming connections.

**On EKS**, the cluster's private node group sits behind a single NAT gateway. All outbound traffic from every pod — regardless of which node it runs on — exits through one stable public IP. Adding that single IP to MongoDB Atlas's allowlist is all that's needed, and the IP never changes when nodes are replaced or the cluster scales.

**On DOKS**, there is no NAT gateway by default. Each node is assigned its own public IP, and pods reach the internet directly through the node they're scheduled on. This means:

- There is no single egress IP — the source address MongoDB sees depends on which node the backend pod happens to be running on.
- With two nodes, you need two IPs in the allowlist. With autoscaling, new nodes get new IPs, and the allowlist breaks until you add them.

For a fixed-size dev cluster, the workaround is to whitelist all current node IPs. For a production DOKS cluster with autoscaling, the correct solution is to provision a **Digital Ocean Load Balancer as a NAT gateway**, routing all cluster egress through a single stable IP. This adds ~$12/month but is the only reliable option when the external service requires a static source address.

For our dev cluster (`doc-router-dev`), we whitelist the two node IPs directly. For production DOKS deployments, a managed NAT gateway is required.

## Overlay-based Deploy Scripts

Rather than a one-size-fits-all deploy script, we use an overlay pattern:

```
.env              # shared defaults (local dev values)
.env.eks-test     # overrides for the test EKS cluster
.env.eks-prod     # overrides for production
```

The deploy scripts (`k8s-deploy.sh`, `build-push.sh`) accept an overlay name and source both files, with the overlay taking precedence. A single variable — `APP_HOST` — drives all URL configuration, making it straightforward to add a new environment. `k8s-deploy.sh` is idempotent — it uses `helm upgrade --install` and handles both fresh installs and rolling updates without any distinction.

## What's Next

- **On-premises distribution** — Helm chart and images are public on ghcr.io; self-hosted MongoDB is available via the [`mongodb-atlas-local`](https://github.com/analytiq-hub/analytiq-charts) chart (see [Self-Hosted MongoDB on Kubernetes with Atlas Search]({% post_url 2026-03-08-self-hosted-mongodb-kubernetes-atlas-search %})); documentation for a one-command on-prem install is the next step
- **Offline license keys** — JWT-based licenses signed with a private key, verified against a public key baked into the image, for air-gapped installations
- **Multi-cloud support** — Digital Ocean Kubernetes is now supported alongside EKS; Azure Kubernetes Service support is planned

---

*Andrei Radulescu-Banu is the founder of [DocRouter.AI](https://docrouter.ai) (document processing with LLMs) and [SigAgent.AI](https://sigagent.ai) (Claude Agent monitoring). His company [AnalytiqHub.com](https://analytiqhub.com) provides consulting services for cloud and AI engineering.*
