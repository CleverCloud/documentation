---
type: docs
weight: 3
linkTitle: Kubernetes
title: Clever Kubernetes Engine (CKE)
description: Create and manage Kubernetes clusters using Clever Cloud Kubernetes Engine with Materia etcd
keywords:
- kubernetes
- cke
- materia
- etcd
- k8s
- cluster
- csi
- persistent storage
- kubeconfig
- load balancers
---

Clever Kubernetes Engine (CKE) allows you to create and manage Kubernetes clusters with ease on Clever Cloud infrastructure. It uses Materia etcd, our implementation of etcd built on top of FoundationDB, as the backing store for your cluster's state. It ensures reliability at scale.

Our approach remains the same as with our other products: our Kubernetes offer is based on open-source technologies, we create value and enhance your developer/user experience through some parts of the stack created and maintained by our engineering team, but we provide a "vanilla" Kubernetes experience to our customers, with no lock-in. It's easy to migrate your workloads to and from Clever Kubernetes.

We operate the Kubernetes control plane for you: upgrades, availability, and patching are our responsibility. You manage your own node pools — scaling them up or down manually as needed — while we ensure the control plane remains stable. Access is straightforward: we provide a kubeconfig file so you can use `kubectl` or any other Kubernetes compatible tool with the same workflow you already know.

> [!NOTE] Clever Kubernetes is in private access
> Ask for activation to your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice)

## Prerequisites

To use Clever Kubernetes you'll need :
- An authorized access for your organisation
- Clever Tools 4.3.0 or later installed
- kubectl installed

To check if you have access to Clever Kubernetes for your organisation, run the following command in your terminal:

```bash
clever features enable k8s
clever k8s list --org <your_org_id>
```

If you get an error or if you miss anything, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

- [kubectl installation guide](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [Learn more about Clever Tools k8s command](/doc/cli/kubernetes/)

>[!NOTE] Kubernetes clusters quotas
> During the private access phase, each organization can deploy a limited number of Kubernetes clusters.\
> If you need more clusters, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

## Create a Kubernetes cluster

To create a Kubernetes cluster, use the following command:

```bash
clever k8s create clusterName --org <your_org_id>
```

Cluster is immediately created and starts its deployment. It takes approximately 1 minute to deploy and configure all the underlying infrastructure. If you want to monitor the progress after creation, use the `--watch` option:

```bash
clever k8s create clusterNameOrId --org <your_org_id> --watch
```

You can list all your clusters at any time using:

```bash
clever k8s list --org <your_org_id>
```

> [!TIP]
> In [Clever Cloud Console](https://console.clever-cloud.com), you can filter Kubernetes clusters in the left menu by searching for `is:k8s`, `is:kube` or `is:kubernetes`

## Supported versions

Clever Cloud follows [the official Kubernetes version support policy](https://kubernetes.io/releases/), which maintains support for the most recent three minor versions (n-2). At any given time, the Kubernetes project maintains release branches for the latest three minor releases.

For example, if the latest release, used as default, is v1.34:

* v1.34 (current)
* v1.33 (supported)
* v1.32 (supported)
* v1.31 (unsupported)

Each supported Kubernetes minor version typically receives patch releases for approximately 12 months after its initial release. It's a good practice to maintain your clusters on a supported version to benefit from the latest security patches, bug fixes, and features. For clusters running unsupported versions, Clever Cloud reserves the right to initiate automatic upgrades to ensure platform security and stability.

## Add persistent storage (CSI)

You can use Clever Cloud block storage to attach a persistent volume to a cluster through a  CSI (Container Storage Interface). Once its status is `ACTIVE`, use the following command:

```bash
clever k8s add-persistent-storage clusterNameOrId --org <your_org_id>
```

## Get the kubeconfig file

Get the kubeconfig file to interact with your cluster:

```bash
clever k8s get-kubeconfig clusterNameOrId --org <your_org_id>
```

You can directly save it as your local kubeconfig file:

```bash
clever k8s get-kubeconfig clusterNameOrId --org <your_org_id> > ~/.kube/config
```

Check everything is working by listing the nodes of your cluster (it should be empty at this point):

```bash
# With the default kubeconfig file:
kubectl get nodes

# To target a specific kubeconfig file:
kubectl get nodes --kubeconfig=kubeconfig.yaml
```

## Clever Kubernetes operator

Clever Cloud's Kubernetes clusters are designed to work seamlessly with the rest of the platform. A good example is our [open-source Kubernetes Operator](https://github.com/CleverCloud/clever-kubernetes-operator), which allows you to easily provision and use Clever Cloud resources directly from inside your cluster and combine Kubernetes workloads with the services you already trust on Clever Cloud.

- [Learn more about the Clever Cloud Kubernetes Operator](/doc/kubernetes/operator/)

## Create a node group

A node group is a collection of Kubernetes nodes that function as the compute resources for your cluster. Each node group consists of virtual machines of the same flavor, meaning they have identical characteristics: vCPU, RAM and location (Paris region only for now). Node groups simplify management by letting you scale or upgrade similar nodes together as a unit rather than individually managing each node.

Once your cluster deployed and configured you can create a node group using `kubectl` from a YAML file that defines the `NodeGroup` resource.

For example, create a file named `example-nodegroup.yaml` with the following content:

```yaml{filename="example-nodegroup.yaml"}
apiVersion: api.clever-cloud.com/v1
kind: NodeGroup
metadata:
  name: example-nodegroup
spec:
  flavor: m
  nodeCount: 2
```

Then, apply this configuration to your cluster using `kubectl create`:

```bash
kubectl create -f example-nodegroup.yaml
```

The node group creation process takes approximately 60 to 90 seconds to complete. Once created, the new nodes will automatically join your cluster and become available for scheduling workloads.

You can list the node groups of your cluster using `kubectl`:

```bash
kubectl get nodegroups

NAME      DESIREDNODECOUNT   CURRENTNODECOUNT   FLAVOR   AGE
default   2                  2                  m        2m
```

The `DESIREDNODECOUNT` is the number of nodes that you asked for, the `CURRENTNODECOUNT` is the number of nodes currently in the node group. When creating a node group, the `CURRENTNODECOUNT` is `0` and increases until it reaches the `DESIREDNODECOUNT`.

You can also list the nodes of your cluster using `kubectl`:

```bash
kubectl get nodes

NAME            STATUS   ROLES    AGE     VERSION
default-node0   Ready    <none>   6d17h   v1.34.1
default-node1   Ready    <none>   3d18h   v1.34.1
```

## Scaling a node group

To scale up or down a node group, use the `kubectl scale` command. For example, to scale the `example-nodegroup` to 4 nodes, run:

```bash
kubectl scale nodegroup example-nodegroup --replicas=4
```

## Deployment with a load balancer service

Here is an example of a simple NGINX deployment with a load balancer service:

```bash
kubectl create deployment nginx --image=nginx:alpine --replicas=2
kubectl expose deployment/nginx --type=LoadBalancer --port 80
```

Alternatively, you can create a YAML file named `deployment-demo.yaml` with the following content and apply it using `kubectl apply -f deployment-demo.yaml`:

```yaml{filename="deployment-demo.yaml"}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  labels:
    app: nginx
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80        # Port accessible from outside the cluster
      targetPort: 80  # Port on which the container is listening
```
