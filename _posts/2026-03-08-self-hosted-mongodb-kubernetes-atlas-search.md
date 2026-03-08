---
layout: post
title: "Self-Hosted MongoDB on Kubernetes with Atlas Search (mongot)"
date: 2026-03-08 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/self-hosted-mongodb-kubernetes-atlas-search-splash.png
categories: [tech, kubernetes, devops, mongodb]
description: "Run a production-grade MongoDB replica set with optional Atlas Search (vector and full-text) inside Kubernetes — for air-gapped, on-prem, or any environment where Atlas isn't an option."
---

For air-gapped environments, on-premises clusters, or any deployment where MongoDB Atlas is not an option, you can run a production-grade MongoDB replica set with optional **Atlas Search** (full-text and vector indexes) entirely inside Kubernetes. This post describes the [`mongodb-atlas-local`](https://github.com/analytiq-hub/analytiq-charts) Helm chart and the operational details we learned running it on EKS and elsewhere.

If you're new to Kubernetes, the [Kubernetes for Docker Users primer]({% post_url 2026-03-05-kubernetes-for-docker-users-primer %}) covers Pods, Deployments, Services, PVCs, and Helm basics. For packaging and GitOps, see [Kubernetes Packaging and Deployment]({% post_url 2026-03-06-kubernetes-packaging-helm-gitops %}).

## Why not Bitnami?

The obvious choice for an in-cluster MongoDB is the Bitnami chart, which is widely used and simple to install. The problem is **vector search**. Applications that need semantic search or Atlas-style indexes require the `mongot` process — a sidecar that runs alongside `mongod` and handles full-text and vector indexes. Bitnami deploys a plain community MongoDB without `mongot`, so Atlas Search is simply not available.

The only supported path to `mongot` in a self-hosted environment is the [MongoDB Kubernetes Operator](https://github.com/mongodb/mongodb-kubernetes-operator), which introduces the `MongoDBCommunity` and `MongoDBSearch` custom resources. The operator manages the StatefulSet, replica set initialization, user creation, and TLS — and, when `MongoDBSearch` is enabled, injects the `mongot` sidecar with the right configuration.

Our chart wraps the operator's CRDs with sensible defaults and a single `helm upgrade --install` interface, so operators don't need to understand the operator's internals to get a working cluster. You can run MongoDB with or without search; if you don't need vector or full-text search, you can disable the `mongot` sidecar and save resources.

## Two-phase install

`mongot` requires a running, authenticated replica set to connect to — it cannot start on a fresh cluster. The install therefore happens in two phases:

```bash
# Phase 1: bring up the replica set without search
helm upgrade --install mongodb oci://ghcr.io/analytiq-hub/mongodb-atlas-local \
  --version 2.0.1 --namespace mongodb \
  --set mongodb.adminPassword="..." \
  --set mongodb.appUser.password="..." \
  --set search.enabled=false

# Wait for replica set Ready
kubectl wait --for=condition=ready pod -l app=mongodb-mongodb-atlas-local \
  -n mongodb --timeout=300s

# Phase 2: enable search
helm upgrade mongodb oci://ghcr.io/analytiq-hub/mongodb-atlas-local \
  --version 2.0.1 --namespace mongodb --reuse-values \
  --set search.enabled=true
```

Attempting a single-phase install with `search.enabled=true` results in `mongot` crash-looping because the replica set isn't ready to accept its connection.

## Node sizing for stateful workloads

Adding MongoDB changes the cluster sizing arithmetic considerably. Each replica pod runs two containers: `mongod` (500m CPU, 400Mi) and `mongodb-agent` (500m CPU, 400Mi), plus a `mongot` sidecar (250m CPU, 250Mi) when search is enabled. A 3-replica set therefore requests ~2.25 vCPU and ~3.15 Gi of memory, on top of whatever other workloads you run.

The scheduler must fit the entire pod on one node. On a cluster with two `t3.medium` nodes (2 vCPU / 4 Gi each), if existing workloads already consume ~1.7 vCPU in requests, there may be ~2.2 vCPU free across both nodes — but never more than ~740m on a single node. A MongoDB pod that needs ~750m CPU cannot be scheduled. Adding a third node (or sizing nodes with enough headroom) resolves it.

The practical lesson: **account for stateful pods when sizing the initial node group**, or ensure the autoscaler can provision new nodes quickly enough not to block workloads.

## EBS CSI Driver and the gp2 trap (EKS)

When we added MongoDB to an EKS cluster, PVCs sat in `Pending` indefinitely with the error:

```
no persistent volumes available for this claim and no storage class is set
```

EKS creates a `gp2` StorageClass by default, but it has two problems. First, it is not marked as the default class — PVCs with an empty `storageClassName` get no provisioner assigned. Second, and more importantly, `gp2` uses the legacy in-tree `kubernetes.io/aws-ebs` provisioner, which was removed in Kubernetes 1.27. On EKS 1.35, it is simply gone.

The fix is to create a `gp3` StorageClass backed by the EBS CSI driver (`ebs.csi.aws.com`) and mark it as the cluster default:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  type: gp3
  encrypted: "true"
```

`WaitForFirstConsumer` is important — it delays EBS volume creation until the pod is actually scheduled to a node, which ensures the volume is created in the correct availability zone. `allowVolumeExpansion: true` enables online resizing without pod restarts.

Provision this StorageClass (and the EBS CSI driver) via Terraform or your preferred IaC so new clusters get it automatically.

## Summary

| Topic | Takeaway |
|-------|----------|
| **Chart** | `mongodb-atlas-local` on [analytiq-charts](https://github.com/analytiq-hub/analytiq-charts) — replica set + optional `mongot` for Atlas Search |
| **Install** | Two-phase: bring up replica set with `search.enabled=false`, then enable search |
| **Sizing** | Reserve enough CPU/memory per node for the full MongoDB pod; scheduler places whole pod on one node |
| **EKS storage** | Use a `gp3` StorageClass with `ebs.csi.aws.com`; don't rely on the default `gp2` |

We use this chart for [Doc Router](https://docrouter.ai) and other applications that need MongoDB with vector search. For the full Doc Router deployment story (Helm chart, workers, CI/CD, multi-cloud), see [Deploying Doc Router on Kubernetes]({% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}).

---

*Andrei Radulescu-Banu is the founder of [DocRouter.AI](https://docrouter.ai) (document processing with LLMs) and [SigAgent.AI](https://sigagent.ai) (Claude Agent monitoring). His company [AnalytiqHub.com](https://analytiqhub.com) provides consulting services for cloud and AI engineering.*
