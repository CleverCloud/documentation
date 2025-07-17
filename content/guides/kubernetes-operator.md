---
title: Kubernetes Operator
description: Manage your Clever Cloud databases and addons seamlessly from Kubernetes with the Clever Kubernetes Operator
tags:
- guides
keywords:
- Kubernetes
- operator
- databases
- crd
type: "docs"
comments: false
draft: false
aliases:
- /guides/clever-operator
---

## What's the Clever Kubernetes Operator

The [Clever Kubernetes Operator](https://github.com/CleverCloud/clever-kubernetes-operator) is an open source project (MIT licensed) designed to seamlessly integrate [Clever Cloud](https://www.clever-cloud.com/)'s managed services into Kubernetes environments. By leveraging Kubernetes [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions)), the Operator enables developers to manage Clever Cloud resources directly from their Kubernetes clusters, aligning cloud-native practices with Clever Cloud's powerful platform.

Modern applications often require a combination of containerized workloads and managed services, such as databases or caches. Managing these resources separately across platforms can become complex and error-prone. The Clever Kubernetes Operator simplifies this process by acting as a bridge, allowing developers to define and interact with Clever Cloud's resources using familiar Kubernetes paradigms.

### Why Use the Clever Kubernetes Operator?

The Clever Kubernetes Operator was born from a concrete need: to allow users to manage Clever Cloud services directly from a Kubernetes cluster. It reconciles the best of both worlds:

- Keep Kubernetes' flexibility for stateless applications
- Delegate the management of critical databases and services to Clever Cloud

While Kubernetes excels at deploying applications, databases come with operational constraints (backup, replication, restoration, updates…) that make self-management challenging. With the operator, you can maintain the comfort of a managed service while keeping control in your Kubernetes manifests.

### Supported Services

Originally designed for managed databases, the Clever Kubernetes Operator has expanded to support a wide range of Clever Cloud services as native Kubernetes Custom Resources:

- **Databases**:
  - PostgreSQL
  - MySQL
  - MongoDB
- **Key-Value Storage**:
  - Redis
  - Materia KV
- **Object Storage**:
  - Cellar (S3-compatible)
- **Search Engines**:
  - Elasticsearch
- **Message Brokers**:
  - Pulsar
- **Analytics Platforms**:
  - Matomo
  - Metabase
  - Azimutt
- **Authentication Services**:
  - Keycloak
- And more services to come

### Key Features

The Clever Kubernetes Operator provides:

- **Custom Resource Definitions (CRDs):** Extend Kubernetes capabilities to manage Clever Cloud services
- **Declarative Resource Management:** Use YAML manifests to declare and maintain the desired state of your services
- **Seamless Integration:** Interact with Clever Cloud's API securely and efficiently
- **Automatic Secret Injection:** Connection details are automatically injected as Kubernetes Secrets
- **Prometheus Integration:** Metrics are exposed for monitoring
- **Operator Lifecycle Manager (OLM) Compatibility:** Works with standard Kubernetes operator frameworks

This documentation guides you through:

- Installing and configuring the Clever Kubernetes Operator in your cluster.
- Managing Clever Cloud resources such as PostgreSQL and Redis through examples.


## Prerequisites

Before you begin, ensure that you have the following tools and resources based on your intended actions:

### To Build the Operator

- **Git:** Clone the Clever K8S Operator repository to access the source code.
- **Rust toolchain:** Install the Rust programming language and its toolchain to compile the operator from source. Follow the installation guide at [https://rustup.rs/](https://rustup.rs/).
- **Docker:** Build container images for deploying the operator in Kubernetes.

### To Deploy the Operator

- **Kubernetes Cluster:** Ensure you have access to a running Kubernetes cluster.
- **Kubectl:** Install Kubernetes command-line tool for managing cluster resources Installation guide available at https://kubernetes.io/docs/tasks/tools/.
- **Clever Cloud Account Credentials:** [Obtain API tokens and secrets from your Clever Cloud](/developers/api/howto) account to configure the operator.

These prerequisites are essential for getting started with the Clever Kubernetes Operator, whether you're contributing to its development or deploying it in production.

## Authentication

The Clever Kubernetes Operator requires configuration to connect to Clever Cloud's API and manage resources within your cluster. Three authentication methods are supported:

### 1. Full OAuth1 Authentication (4 parameters)

This is the most complete authentication method, requiring all four OAuth1 parameters:

- _Consumer key_
- _Consumer Secret_
- _Token_
- _Secret_

To obtain these credentials, you need to connect to the Clever Cloud API, which uses OAuth1-based authentication. As explained in the [Clever Cloud API Overview](/developers/api/howto), you need to create an OAuth consumer token in the Clever Cloud console, use it to obtain the _Consumer key_ and the _Consumer Secret_, and complete the OAuth authentication process to get the _Token_ and _Secret_.

Configuration example:

```toml
[api]
token = "your-token"
secret = "your-secret"
consumer-key = "your-consumer-key"
consumer-secret = "your-consumer-secret"
```

**Best for:**
- Production environments
- Full control over permissions
- Fine-grained access scope configuration


> #### Need an easier way to get these credentials?
>
> Yes, the OAuth dance can be complex. For a simpler setup, there is a small application that you can deploy on Clever Cloud that automates most of the process for you.
>
> The code and tutorial are available at [https://github.com/CleverCloud/oauth-consumer-server](https://github.com/CleverCloud/oauth-consumer-server).

### 2. Simplified OAuth1 Authentication (token + secret)

This method uses only the token and secret, automatically using the public client credentials (like those from Clever Tools):

```toml
[api]
token = "your-token"
secret = "your-secret"
```

If you already use the Clever Cloud CLI (clever-tools), you can extract these credentials from its configuration file, typically located at `$HOME/.config/clever-cloud/clever-tools.json`. The token and secret values can be found in this file and reused for the operator configuration.

**Best for:**
- Standard usage scenarios
- Development, testing, or demos
- Users already using Clever Cloud CLI

This is the recommended approach for most users.

### 3. Bearer Token Authentication ("oauthless" mode)

The simplest method: a single token for direct use, without consumer or secret:

```toml
[api]
token = "your-bearer-token"
```

**Best for:**
- Simple integrations
- Quick scripts or automation
- Environments using the "oauthless" backend authentication


## Installation

The Clever Kubernetes Operator can be deployed in several ways depending on your needs.

### Quick Deployment from DockerHub

The simplest method is to apply the published manifests directly:

{{% steps %}}

#### Apply the CRDs and deployment manifests

```bash
kubectl apply -f https://raw.githubusercontent.com/CleverCloud/clever-kubernetes-operator/main/deployments/kubernetes/v1.30.0/10-custom-resource-definition.yaml
kubectl apply -f https://raw.githubusercontent.com/CleverCloud/clever-kubernetes-operator/main/deployments/kubernetes/v1.30.0/20-deployment.yaml
```

This installs the CRDs and the operator deployment using the official image.

#### Configure your credentials

After deployment, you'll need to update the ConfigMap with your authentication credentials:

```bash
kubectl edit configmap clever-kubernetes-operator-configuration -n clever-kubernetes-operator-system
```

Modify the ConfigMap to include your credentials:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: clever-kubernetes-operator-configuration
  namespace: clever-kubernetes-operator-system
data:
  config.toml: |
    [api]
    endpoint = "https://api.clever-cloud.com/v2"
    token = "<your_token>"
    secret = "<your_secret>"
    consumerKey = "<your_consumer_key>"
    consumerSecret = "<your_consumer_secret>"
```

Replace `<your_token>`, `<your_secret>`, `<your_consumer_key>`, and `<your_consumer_secret>` with the credentials obtained using one of the authentication methods described earlier.

{{% /steps %}}

### Manual Deployment from Repository

{{% steps %}}

#### Clone the repository

```bash
git clone https://github.com/CleverCloud/clever-kubernetes-operator/
cd clever-kubernetes-operator
```

#### Insert your credentials into the manifests

The manifests are in the folder `/deployments/kubernetes/v1.30.0/`. Modify the `ConfigMap` object in the file `/deployments/kubernetes/v1.30.0/20-deployment.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: clever-kubernetes-operator-configuration
  namespace: clever-kubernetes-operator-system
data:
  config.toml: |
    [api]
    endpoint = "https://api.clever-cloud.com/v2"
    token = "<your_token>"
    secret = "<your_secret>"
    consumerKey = "<your_consumer_key>"
    consumerSecret = "<your_consumer_secret>"
```

Replace `<your_token>`, `<your_secret>`, `<your_consumer_key>`, and `<your_consumer_secret>` with your credentials.

#### Apply the manifests to deploy the operator

```bash
kubectl apply -f deployments/kubernetes/v1.30.0/10-custom-resource-definition.yaml
kubectl apply -f deployments/kubernetes/v1.30.0/20-deployment.yaml
```

{{% /steps %}}

### Installing via Helm Chart

For more flexibility and customization options, you can use the Helm chart provided with the operator.

{{% steps %}}

#### Clone the repository

```bash
git clone https://github.com/CleverCloud/clever-kubernetes-operator/
cd clever-kubernetes-operator/deployments/kubernetes/helm
```

#### Configure your credentials in the `values.yaml` file

Edit the `values.yaml` file to include your authentication credentials in the `config` section:

```yaml
config:
  endpoint: "https://api.clever-cloud.com/v2"
  token: "<your_token>"
  secret: "<your_secret>"
  consumerKey: "<your_consumer_key>"
  consumerSecret: "<your_consumer_secret>"
```

Replace `<your_token>`, `<your_secret>`, `<your_consumer_key>`, and `<your_consumer_secret>` with the credentials obtained using one of the authentication methods described earlier.

#### Customize other Helm chart values (optional)

The `values.yaml` file allows you to customize various aspects of the deployment, such as:

- Resource limits and requests
- Node selector, tolerations, and affinity
- Service account configuration
- Image repository and tag
- Namespace configuration

#### Install the chart

```bash
helm install clever-kubernetes-operator . -n clever-kubernetes-operator --create-namespace -f values.yaml
```

#### Verify the installation

```bash
kubectl get pods -n clever-kubernetes-operator
```

You should see the operator pod running in the specified namespace.

{{% /steps %}}

### Building from Source

{{% steps %}}

#### Clone the repository

```bash
git clone https://github.com/CleverCloud/clever-kubernetes-operator.git
cd clever-kubernetes-operator
```

#### Build the binary

The operator is written in Rust. Make sure you have the Rust toolchain installed (follow the installation guide at [https://rustup.rs/](https://rustup.rs/) if needed).

```bash
make build
```

#### Configure the operator

Create a configuration file (e.g., `config.toml`) with your credentials:

```toml
[api]
endpoint = "https://api.clever-cloud.com/v2"
token = "<your_token>"
secret = "<your_secret>"
consumerKey = "<your_consumer_key>"
consumerSecret = "<your_consumer_secret>"
```

Replace `<your_token>`, `<your_secret>`, `<your_consumer_key>`, and `<your_consumer_secret>` with your credentials.

#### Run the operator

```bash
target/release/clever-kubernetes-operator --config config.toml
```

{{% /steps %}}

## Deployment Options

The Clever Kubernetes Operator offers flexible deployment options to suit different operational needs:

### In-Cluster Deployment

This is the standard deployment model where the operator runs as a pod within your Kubernetes cluster:

- **Advantages**:
  - Direct access to Kubernetes API without additional configuration
  - Standard Kubernetes RBAC controls
  - Follows the typical operator pattern

- **Best for**:
  - Standard Kubernetes environments
  - When you want to keep all components within the cluster

### Remote Deployment from Clever Cloud

An alternative approach is to run the operator as a Clever Cloud application that connects to your Kubernetes cluster remotely:

- **Advantages**:
  - Reduces resource consumption on your Kubernetes cluster
  - Centralizes control when managing multiple clusters
  - Leverages Clever Cloud's managed platform for the operator itself

- **Best for**:
  - Managing multiple Kubernetes clusters
  - Reducing cluster resource usage
  - Centralizing operator management

#### Setting up Remote Deployment

1. Create a new application on Clever Cloud
2. Configure the application with:
   - The operator binary or Docker image
   - A valid `kubeconfig` file with appropriate permissions
   - Your Clever Cloud API credentials
3. Deploy the application

The operator will connect to your Kubernetes cluster using the provided `kubeconfig` and manage resources as if it were running inside the cluster.

## Configuration

Configuration options are available at two levels: global (applies to all namespaces) and namespace-specific.

### Global Configuration

Global configuration settings apply across all namespaces. Global configuration can be provided through a `ConfigMap`, a `Secret` or by the environment.

- **Environment Variables:**

    - `CLEVER_OPERATOR_API_ENDPOINT`: The endpoint for the Clever Cloud API.
    - `CLEVER_OPERATOR_API_TOKEN`: Your Clever Cloud API token.
    - `CLEVER_OPERATOR_API_SECRET`: The secret associated with your API token.
    - `CLEVER_OPERATOR_API_CONSUMER_KEY`: Your Clever Cloud consumer key
    - `CLEVER_OPERATOR_API_CONSUMER_SECRET`: Your Clever Cloud consumer secret.

- **Configuration Files:** By default, if the `--config` flag isn't provided to the binary, the operator looks at the following locations to retrieve its configuration (in order of priority):

    1. `/usr/share/clever-kubernetes-operator/config.{toml,yaml,json}`
    2. `/etc/clever-kubernetes-operator/config.{toml,yaml,json}`
    3. `$HOME/.config/clever-kubernetes-operator/config.{toml,yaml,json}`
    4. `$HOME/.local/share/clever-kubernetes-operator/config.{toml,yaml,json}`
    5. `config.{toml,yaml,json}` (in the current working directory)


### Namespace-Level Configuration

Namespace-level configurations override the global settings for specific namespaces. They're defined using a Kubernetes Secret resource named `clever-kubernetes-operator` with the `config` key.

- **Creating a Namespace-Level Configuration:** Create a Kubernetes Secret with the necessary configuration keys:

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: clever-secret
      namespace: <your_namespace>
    stringData:
      config: |
        [api]
        endpoint = "https://api.clever-cloud.com/v2"
        token = <your_token>
        secret = <your_secret>
        consumerKey = <your_consumer_key>
        consumerSecret = <your_consumer_secret>
    ```

- **Applying the Configuration:** Apply the Secret to your namespace:

    ```bash
    kubectl apply -f namespace-config.yaml
    ```


The operator automatically detects and applies namespace-specific configurations when interacting with resources in that namespace.

### Validating Configuration

To ensure your configuration applies correctly, look at the operator logs for any errors or warnings:

```bash
kubectl logs -n clever-kubernetes-operator <operator-pod-name>
```

## Usage Examples

The Clever Kubernetes Operator enables you to manage Clever Cloud resources directly from your cluster using custom resources. Below are examples for various supported services.

### How the Operator Works

The Clever Kubernetes Operator acts as a bridge between your Kubernetes cluster and Clever Cloud. When you create a custom resource in your cluster:

1. The operator detects the new resource
2. It calls the Clever Cloud API to create the corresponding service
3. Once the service is created, the operator automatically injects a Kubernetes Secret containing connection details
4. Your applications can then use these secrets to connect to the service

### Managing PostgreSQL Resources

- **Creating a PostgreSQL Instance:** Define a YAML manifest for the PostgreSQL resource:

    ```yaml
    apiVersion: api.clever-cloud.com/v1
    kind: PostgreSQL
    metadata:
      name: my-postgresql
      namespace: default
    spec:
      version: "14"
      plan: "S"
      region: "par"
      encryption: true
    ```

    Apply the manifest to your cluster:

    ```bash
    kubectl apply -f postgresql.yaml
    ```

- **Verifying the Deployment:** Check the status of the PostgreSQL resource:

    ```bash
    kubectl get postgresql my-postgresql -o yaml
    ```

- **Accessing PostgreSQL:** The operator automatically creates a Secret with the same name as your resource containing connection details:

    ```bash
    kubectl get secret my-postgresql -o yaml
    ```

### Managing Redis Resources

- **Creating a Redis Instance:** Define a YAML manifest for the Redis resource:

    ```yaml
    apiVersion: clever-cloud.com/v1
    kind: Redis
    metadata:
      name: my-redis
      namespace: default
    spec:
      version: "704"
      plan: "dev"
      region: "par"
    ```

    Apply the manifest to your cluster:

    ```bash
    kubectl apply -f redis.yaml
    ```

- **Verifying the Deployment:** Check the status of the Redis resource:

    ```bash
    kubectl get redis my-redis -o yaml
    ```

- **Accessing Redis:** Retrieve the connection details from the Clever Cloud dashboard or the resource's status field.

### Additional Supported Resources

The Clever Kubernetes Operator supports many other Clever Cloud services, including:

- Elasticsearch
- MongoDB
- MySQL
- Cellar (S3-compatible object storage)
- Pulsar (message broker)
- Matomo (analytics)
- Metabase (business intelligence)
- Azimutt (database visualization)
- Keycloak (authentication)

For examples of how to configure these resources, refer to the `examples/kubernetes` directory in the [Clever Kubernetes Operator repository](https://github.com/CleverCloud/clever-kubernetes-operator). These examples provide YAML manifests for all supported resources with their available configuration options.

## Troubleshooting

If you encounter issues with the Clever Kubernetes Operator, here are some common problems and their solutions:

### Operator Pod Not Starting

**Symptoms:** The operator pod stays in `Pending` or `CrashLoopBackOff` state.

**Possible Solutions:**

1. Check pod events and logs:
   ```bash
   kubectl describe pod -n clever-kubernetes-operator <pod-name>
   kubectl logs -n clever-kubernetes-operator <pod-name>
   ```

2. Verify resource constraints:
   - Ensure your cluster has sufficient resources
   - Check if there are any node selectors or taints preventing scheduling

### Authentication Errors

**Symptoms:** The operator logs show authentication or authorization errors when trying to connect to the Clever Cloud API.

**Possible Solutions:**

1. Verify your credentials are correct in the ConfigMap or Secret
2. Ensure you're using the right authentication method for your use case
3. Check if your API tokens have expired or been revoked
4. Verify network connectivity to the Clever Cloud API

### Custom Resources Not Being Processed

**Symptoms:** You create a custom resource, but nothing happens and no corresponding service appears in Clever Cloud.

**Possible Solutions:**

1. Check the operator logs for errors:
   ```bash
   kubectl logs -n clever-kubernetes-operator <pod-name>
   ```

2. Verify the custom resource is valid:
   ```bash
   kubectl get <resource-type> <resource-name> -o yaml
   ```

3. Ensure the CRDs are properly installed:
   ```bash
   kubectl get crds | grep clevercloud
   ```

### Connection Secrets Not Created

**Symptoms:** The service is created in Clever Cloud, but no Kubernetes Secret is created with connection details.

**Possible Solutions:**

1. Check the operator logs for errors related to secret creation
2. Verify the operator has permissions to create secrets in the target namespace
3. Check if there's a naming conflict with an existing secret

### Version or Plan Not Available

**Symptoms:** You get an error indicating that the specified version or plan is not available.

**Possible Solutions:**

1. Check the available versions and plans for the service in the Clever Cloud console
2. Update your custom resource to use a valid version and plan combination
3. Verify the region you selected supports the requested service

### Getting Help

If you continue to experience issues:

1. Check the [GitHub repository](https://github.com/CleverCloud/clever-kubernetes-operator) for known issues or to report a new one
2. Contact Clever Cloud support for assistance with API or service-specific problems
3. Join the Clever Cloud community channels for peer support
