---
layout: post
title: "Kubernetes for Docker Users: A Practical Primer"
date: 2026-03-05 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/kubernetes-docker-users-primer-splash.png
categories: [tech, kubernetes, devops]
description: "If you've used Docker Compose, you already understand the core idea. Kubernetes takes that same idea and extends it to run across a cluster of machines, with built-in handling for failures, scaling, and upgrades."
---

If you've used Docker Compose, you already understand the core idea: define your services, wire them together with a network, and let the runtime manage the processes. Kubernetes takes that same idea and extends it to run across a cluster of machines, with built-in handling for failures, scaling, and upgrades.

Here's how the key concepts map across.

## From containers to Pods

In Docker Compose, the unit of work is a container. In Kubernetes, it is a **Pod** — a group of one or more containers that always run together on the same machine and share a network namespace. Most Pods contain a single container, but some use sidecars: a main process plus a helper (a log shipper, a proxy, or in our case the `mongot` search process alongside `mongod`).

Pods are ephemeral. When a Pod dies, Kubernetes replaces it with a new one — possibly on a different machine, with a new IP address. You never SSH into a Pod or rely on its IP being stable.

## Deployments — the equivalent of a Compose service

A **Deployment** tells Kubernetes: "keep N replicas of this Pod running at all times." If a Pod crashes, the Deployment controller starts a replacement. If you push a new image, it performs a rolling update — starting new Pods before terminating old ones so traffic is never interrupted.

In Docker Compose terms, a Deployment is your `service:` block plus restart policies and rolling update logic built in.

## Services — stable internal addresses

Because Pod IPs change on every restart, Kubernetes introduces **Services**: stable DNS names and virtual IPs that front a group of Pods. A Service named `backend` in the `doc-router` namespace is reachable at `backend.doc-router.svc.cluster.local` from anywhere in the cluster, regardless of how many backend Pods exist or where they are running.

This replaces the automatic DNS that Docker Compose sets up between containers on the same network.

## Namespaces — isolation within a cluster

A **Namespace** is a logical partition of the cluster. Resources in different namespaces don't collide even if they share a name. A typical setup uses separate namespaces for each concern: `doc-router` for the application, `mongodb` for the database, `ingress-nginx` for the load balancer, `cert-manager` for TLS certificates.

In Docker Compose terms, a namespace is roughly equivalent to a separate Compose project — distinct networks and name scopes.

## ConfigMaps and Secrets — environment variables at scale

Docker Compose lets you set `environment:` variables inline or via an `.env` file. Kubernetes separates non-sensitive config from sensitive config:

- **ConfigMap** — key-value pairs mounted as environment variables or files. Used for things like `FASTAPI_ROOT_PATH`, worker count, S3 bucket name.
- **Secret** — base64-encoded values stored (optionally encrypted at rest) separately from your app manifests. Used for database URIs, API keys, and auth secrets. Pods reference Secrets by name; the values are injected at runtime, never baked into the image.

## PersistentVolumeClaims — durable storage

Docker Compose uses named volumes (backed by the local filesystem) to persist data across container restarts. Kubernetes uses **PersistentVolumeClaims (PVCs)**: a request for a piece of storage of a given size and access mode. The cluster fulfils the claim by provisioning a real volume — an EBS disk on AWS, a DO Block Storage volume on Digital Ocean — and mounting it into the Pod.

PVCs survive Pod restarts and rescheduling. If a database Pod moves to a different node, the volume is detached and reattached automatically. Storage is provisioned dynamically by a **StorageClass**, which specifies the provisioner (e.g. `ebs.csi.aws.com` on EKS) and volume type.

## Ingress and the load balancer

In Docker Compose you typically expose one port from one container. In Kubernetes, multiple Services need to be reachable from the outside under different paths or hostnames, all through a single external IP.

**ingress-nginx** is a Kubernetes controller that runs an nginx reverse proxy inside the cluster. When deployed on EKS, it automatically provisions an AWS Network Load Balancer with a stable public IP. You define **Ingress** rules — "route `/fastapi` to the backend Service, everything else to the frontend Service" — and ingress-nginx handles the routing. On a new cluster, the load balancer is the only resource with a public IP; everything else is internal.

## cert-manager — automatic TLS

cert-manager is a Kubernetes controller that watches Ingress resources and automatically requests TLS certificates from Let's Encrypt. When you annotate an Ingress with `cert-manager.io/cluster-issuer: letsencrypt-prod`, cert-manager handles the ACME challenge, obtains the certificate, stores it in a Secret, and renews it before it expires. You never touch a certificate manually.

## Helm — packaging it all together

Kubernetes resources are defined as YAML files. A real application needs dozens of them: Deployments, Services, ConfigMaps, Secrets, Ingress rules, PodDisruptionBudgets. **Helm** is the package manager for Kubernetes — it bundles all those YAML files into a **chart**, parameterises them with a `values.yaml` file, and installs or upgrades the whole bundle with a single command:

```bash
helm upgrade --install doc-router oci://ghcr.io/analytiq-hub/doc-router \
  --namespace doc-router --set appHost=example.com ...
```

A chart can be published as an OCI artifact to any container registry alongside the Docker images.

If Docker Compose is a `docker run` wrapper, Helm is closer to an apt package: versioned, reproducible, and upgradeable.

### How Helm applies changes

Every time you run `helm upgrade`, Helm compares the new rendered YAML against what it last applied and sends only the diff to the Kubernetes API — resources that haven't changed are left untouched. Helm records each upgrade as a numbered **revision**, stored as a Secret in the cluster:

```bash
$ helm history doc-router -n doc-router
REVISION  STATUS     CHART           APP VERSION  DESCRIPTION
1         superseded doc-router-0.3.5  v27.0.0    Install complete
2         superseded doc-router-0.3.6  v27.0.1    Upgrade complete
3         deployed   doc-router-0.3.7  v27.0.2    Upgrade complete
```

### Rolling back to a known-good state

If an upgrade goes wrong, rolling back to the previous revision is a single command:

```bash
helm rollback doc-router -n doc-router        # rolls back to revision 2
helm rollback doc-router 1 -n doc-router      # rolls back to a specific revision
```

Helm re-applies the exact YAML from that revision — the same image tags, the same config values — so the cluster returns to the state that last worked. Using `--atomic` during an upgrade makes this automatic: if the new Pods don't become healthy within the timeout, Helm rolls back on its own without any manual intervention.

### Zero-downtime rolling updates

When Helm upgrades a Deployment with a new image, Kubernetes does not restart all Pods at once. It uses a **rolling update** strategy controlled by two parameters:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 0   # never take a pod down before a new one is ready
    maxSurge: 1         # allow one extra pod above the desired count during the rollout
```

With `maxUnavailable: 0`, Kubernetes starts a new Pod with the new image first. Only after that Pod passes its readiness probe — meaning it is actually serving traffic — does Kubernetes terminate one of the old Pods. This continues one Pod at a time until all replicas are on the new version. At no point does the number of healthy Pods drop below the desired count.

The result: an upgrade from `v27.0.1` to `v27.0.2` with two replicas proceeds as:

1. Start new Pod (v27.0.2) — 2 old + 1 new running
2. New Pod passes readiness check
3. Terminate one old Pod — 1 old + 1 new running
4. Start second new Pod — 1 old + 2 new running
5. Second new Pod passes readiness — terminate last old Pod
6. Rollout complete — 2 new Pods running, zero downtime

If the new Pod fails its readiness check at step 2, the rollout pauses. No old Pods have been terminated, so the old version continues serving 100% of traffic. With `--atomic`, Helm then rolls the release back automatically.

## Running Kubernetes locally with Kind

Before deploying to a real cluster, it's useful to test locally using **Kind** (Kubernetes in Docker). Kind runs an entire Kubernetes cluster — control plane and worker nodes — as Docker containers on your laptop. There is no cloud provider, no load balancer, and no cloud volumes; Kind uses your local filesystem for storage and `NodePort` services for external access.

```bash
./deploy/scripts/setup-kind.sh   # creates the Kind cluster
./deploy/scripts/deploy-kind.sh  # installs the Helm chart locally
```

The same chart that runs on EKS runs on Kind, with a different `values-kind.yaml` override file. This lets you iterate on chart changes without incurring cloud costs or waiting for node provisioning.

## Summary

| Docker Compose concept | Kubernetes equivalent |
|---|---|
| Container | Pod (usually 1 container, sometimes with sidecars) |
| `service:` block | Deployment + Service |
| Container DNS (service name) | Service DNS (`name.namespace.svc.cluster.local`) |
| Compose project | Namespace |
| `environment:` / `.env` | ConfigMap (non-secret) + Secret (sensitive) |
| Named volume | PersistentVolumeClaim + StorageClass |
| `ports:` expose | Ingress + LoadBalancer Service |
| Manual TLS | cert-manager (automatic Let's Encrypt) |
| `docker-compose.yml` | Helm chart (`values.yaml` + templates) |
| Local Docker | Kind (Kubernetes in Docker) |

**Next:** [Kubernetes Packaging and Deployment: Kustomize, Helm, and GitOps]({% post_url 2026-03-06-kubernetes-packaging-helm-gitops %}) goes deeper into packaging manifests and GitOps with Flux.

---

*Andrei Radulescu-Banu is the founder of [DocRouter.AI](https://docrouter.ai) (document processing with LLMs) and [SigAgent.AI](https://sigagent.ai) (Claude Agent monitoring). His company [AnalytiqHub.com](https://analytiqhub.com) provides consulting services for cloud and AI engineering.*
