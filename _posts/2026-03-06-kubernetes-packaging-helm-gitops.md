---
layout: post
title: "Kubernetes Packaging and Deployment: Kustomize, Helm, and GitOps"
date: 2026-03-06 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/kubernetes-packaging-helm-gitops-splash.png
categories: [tech, kubernetes, devops]
description: "The second part of the Kubernetes primer series: Kustomize, Helm, and GitOps with Flux — packaging manifests and letting the cluster manage itself."
---

This is the second part of the Kubernetes primer series. The [first part]({% post_url 2026-03-05-kubernetes-for-docker-users-primer %}) covered the core building blocks — Pods, Deployments, Services, Secrets, PVCs, and Helm basics. This part goes deeper into the two dominant approaches to packaging Kubernetes manifests, and then introduces GitOps as an alternative to running deploy scripts manually.

---

## The manifest problem

A real Kubernetes application needs dozens of YAML files: Deployments, Services, ConfigMaps, Secrets, Ingress rules, HorizontalPodAutoscalers, PodDisruptionBudgets. Writing them by hand is feasible once, but the moment you need the same app running in three environments — local, staging, production — you face a choice:

- **Copy the files for each environment** and keep them in sync manually (fragile)
- **Use a tool that handles the variation** for you

Two tools dominate: **Kustomize** and **Helm**. They solve the same problem differently, and many projects use both — Helm for third-party software, Kustomize for their own app.

---

## Kustomize — layered YAML patches

Kustomize ships with `kubectl` (no install needed) and works with plain YAML. The idea is a **base + overlays** structure:

```
manifests/
  base/
    deployment.yaml      # canonical deployment
    service.yaml
    kustomization.yaml   # lists the resources
  overlays/
    dev/
      kustomization.yaml # patches for dev
      patch-replicas.yaml
    prod/
      kustomization.yaml # patches for prod
      patch-replicas.yaml
      patch-resources.yaml
```

The base defines the resource once. Each overlay patches only what differs. A typical patch looks like:

```yaml
# overlays/prod/patch-replicas.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 4       # override base value of 2
```

To deploy the prod overlay:

```bash
kubectl apply -k overlays/prod/
```

Kustomize merges the base YAML with all patches before sending anything to the API server. You always see plain, readable YAML — there is no templating language to learn, and the output is predictable.

### Variable substitution

For values that vary by environment (hostnames, image tags, resource sizes), Kustomize offers `substituteFrom`: it reads variables from a ConfigMap or Secret and injects them into the manifests at apply time:

```yaml
# kustomization.yaml
configurations:
  - var-references.yaml
vars:
  - name: APP_DOMAIN
    objref:
      kind: ConfigMap
      name: project-values
      apiVersion: v1
    fieldref:
      fieldpath: data.domain
```

This is less flexible than Helm's full templating but keeps the YAML closer to what Kubernetes actually receives.

### What Kustomize does not do

Kustomize has no concept of a release, no revision history, and no built-in rollback. If you apply a broken overlay, you must fix it and reapply, or manually apply a previous version. For the same reason, there is no `--atomic` safety net — if a deployment fails mid-rollout, you notice from `kubectl` output, not from the packaging tool.

---

## Helm — templated packages

Helm wraps Kubernetes YAML in a full templating engine (Go templates) and adds lifecycle management on top. A chart is a directory:

```
doc-router/
  Chart.yaml          # name, version, appVersion
  values.yaml         # default values
  templates/
    deployment.yaml   # Go template
    service.yaml
    ingress.yaml
    _helpers.tpl      # reusable template fragments
```

A template looks like:

```yaml
# templates/deployment.yaml
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: backend
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          resources:
            requests:
              cpu: {{ .Values.resources.requests.cpu }}
```

To install with custom values:

```bash
helm upgrade --install doc-router ./doc-router \
  --set replicaCount=4 \
  --set image.tag=v1.2.3
```

Or via an override file:

```bash
helm upgrade --install doc-router ./doc-router -f values-prod.yaml
```

### Release history and rollback

Helm records every install and upgrade as a numbered revision in the cluster. You can inspect history and roll back:

```bash
helm history doc-router -n doc-router
helm rollback doc-router 2 -n doc-router   # back to revision 2
```

With `--atomic`, a failed upgrade automatically triggers a rollback — the old version keeps running uninterrupted.

### Publishing charts as OCI artifacts

A packaged chart can be pushed to any OCI-compatible registry (ghcr.io, ECR, Docker Hub) and pulled from anywhere:

```bash
helm push doc-router-0.3.7.tgz oci://ghcr.io/analytiq-hub
helm upgrade --install doc-router oci://ghcr.io/analytiq-hub/doc-router --version 0.3.7
```

This means a customer cluster can install your app with a single command, pulling both the chart and images from the same registry, with no Git access required.

---

## Kustomize vs Helm — when to use each

| | Kustomize | Helm |
|---|---|---|
| Learning curve | Low — just YAML | Higher — Go templates + chart structure |
| Flexibility | Patches and substitutions | Full templating, conditionals, loops |
| Release history | None | Built-in, per-revision |
| Rollback | Manual | `helm rollback` |
| Failure safety | None | `--atomic` auto-rollback |
| Publishing | OCI artifact via Flux | `helm push` to any OCI registry |
| Best for | Your own first-party manifests | Distributable packages, third-party software |

In practice many projects use both: Helm for installing third-party dependencies (ingress-nginx, cert-manager, MongoDB operator), and Kustomize for their own application manifests. The two are compatible — a Kustomize overlay can reference a Helm chart as a generator.

---

## GitOps — the cluster manages itself

Both Kustomize and Helm, as described so far, are **imperative**: a human (or a CI job) runs a command that pushes changes into the cluster. GitOps flips this model.

In GitOps, the desired cluster state is declared in a Git repository (or an OCI artifact registry). A controller running *inside* the cluster continuously watches that source and reconciles actual state to match it. No one runs `helm upgrade` — the cluster pulls its own updates.

```
Developer pushes to Git / CI pushes OCI artifact
         ↓
  Source of truth updated
         ↓
  In-cluster controller detects drift
         ↓
  Controller applies the diff
         ↓
  Cluster matches desired state
```

The key property: **the cluster self-heals**. If someone manually deletes a Deployment or edits a ConfigMap, the controller notices the drift and reverts it within seconds. The Git repo (or OCI artifact) is always the authoritative source.

---

## Flux — a GitOps controller

**Flux** is one of the two dominant GitOps controllers (the other is Argo CD). It runs as a set of controllers in the cluster and watches sources:

### Sources

Flux can watch:
- **Git repositories** — on every push, Flux reconciles the cluster
- **OCI artifact registries** — on every `flux push artifact`, Flux pulls and applies
- **Helm repositories** — for managing Helm releases declaratively

### Core resources

**GitRepository / OCIRepository** — defines where Flux watches:
```yaml
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: OCIRepository
metadata:
  name: my-app
  namespace: flux-system
spec:
  interval: 1m
  url: oci://123456789.dkr.ecr.us-east-1.amazonaws.com/my-app-manifests
  ref:
    tag: latest
```

**Kustomization** — tells Flux what to apply from the source:
```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: my-app
  namespace: flux-system
spec:
  interval: 5m
  sourceRef:
    kind: OCIRepository
    name: my-app
  path: ./manifests/kubernetes/overlays/prod
  prune: true      # delete resources removed from source
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: backend
      namespace: my-app
```

**HelmRelease** — manages a Helm release declaratively:
```yaml
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: ingress-nginx
  namespace: flux-system
spec:
  interval: 1h
  chart:
    spec:
      chart: ingress-nginx
      version: "4.11.3"
      sourceRef:
        kind: HelmRepository
        name: ingress-nginx
  values:
    controller:
      replicaCount: 2
```

### CI/CD with Flux

A typical Flux-based pipeline looks like:

```
1. Developer opens a PR
2. CI runs tests
3. PR merged to main
4. CI builds Docker image → pushes to ECR
5. CI packages Kustomize manifests as OCI artifact → flux push artifact → ECR
6. Flux detects new artifact version
7. Flux applies manifests to cluster
8. Cluster rolls out new Deployment
```

Steps 6–8 happen automatically, inside the cluster, with no deploy script and no human intervention.

### Flux vs running deploy scripts

| | Shell script (`helm upgrade`) | Flux GitOps |
|---|---|---|
| Who initiates deploy | Human or CI job | Cluster controller |
| Drift detection | None — manual kubectl needed | Continuous — auto-reverts |
| Audit trail | CI logs | Git history + Flux events |
| Rollback | `helm rollback` | Revert commit, Flux reconciles |
| Complexity | Low — just a shell script | Higher — Flux controllers + CRDs |
| Air-gapped / on-prem | Simple | Requires Flux + registry access |

GitOps is the right choice for teams with multiple people deploying to shared clusters, or for production environments where drift must be detected and prevented. For a small team or a self-hosted product where simplicity matters, shell scripts with `helm upgrade --install` are easier to understand, debug, and hand off to a customer.

---

## Summary

| Tool | Role | Key strength |
|---|---|---|
| **Kustomize** | Overlay-based YAML patching | Plain YAML, no templates, built into kubectl |
| **Helm** | Templated package manager | Release history, rollback, publishable charts |
| **Flux** | GitOps controller | Self-healing cluster, drift detection, no manual deploys |
| **Argo CD** | GitOps controller (alternative to Flux) | Web UI, application health visualisation |

A mature production setup typically uses all three: Kustomize or Helm for defining manifests, Flux or Argo CD for reconciling them, and a CI pipeline that produces the artifacts both consume.

**Next:** [Deploying Doc Router on Kubernetes]({% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}) walks through a real application deployment (Helm chart, workers, CI/CD, EKS and Digital Ocean). If you need in-cluster MongoDB with vector search, see [Self-Hosted MongoDB on Kubernetes with Atlas Search]({% post_url 2026-03-08-self-hosted-mongodb-kubernetes-atlas-search %}).

---

*Andrei Radulescu-Banu is the founder of [DocRouter.AI](https://docrouter.ai) (document processing with LLMs) and [SigAgent.AI](https://sigagent.ai) (Claude Agent monitoring). His company [AnalytiqHub.com](https://analytiqhub.com) provides consulting services for cloud and AI engineering.*
