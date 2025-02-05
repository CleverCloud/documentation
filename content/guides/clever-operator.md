---
title: Clever Operator
description: Manage your Clever Cloud databases and addons seamlessly from Kubernetes with Clever Operator.
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
---

## What's the Clever Operator

The [Clever Operator](https://github.com/CleverCloud/clever-operator) is an open source project designed to seamlessly integrate [Clever Cloud](https://www.clever-cloud.com/)’s managed services into Kubernetes environments. By leveraging Kubernetes [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions)), the Clever Operator enables developers to manage Clever Cloud resources directly from their Kubernetes clusters, aligning cloud-native practices with Clever Cloud’s powerful platform.

Modern applications often require a combination of containerized workloads and managed services, such as databases or caches. Managing these resources separately across platforms can become complex and error-prone. The Clever Operator simplifies this process by acting as a bridge, allowing developers to define and interact with Clever Cloud’s resources using familiar Kubernetes paradigms.

Key features of the Clever Operator include:

- **Custom Resource Definitions (CRDs):** Extend Kubernetes capabilities to manage Clever Cloud services like PostgreSQL, Redis, and more.
- **Declarative Resource Management:** Use YAML manifests to declare and maintain the desired state of your services.
- **Seamless Integration:** Interact with Clever Cloud’s API securely and efficiently.
- **Scalability and Flexibility:** Manage resources across multiple namespaces with consistent configurations.

This documentation guide you through:

- Installing and configuring the Clever Operator in your Kubernetes cluster.
- Managing Clever Cloud resources such as PostgreSQL and Redis through examples.


## Prerequisites

Before you begin, ensure that you have the following tools and resources based on your intended actions:

### To Build the Operator

- **Git:** Clone the Clever Operator repository to access the source code.
- **Rust toolchain:** Install the Rust programming language and its toolchain to compile the operator from source. Follow the installation guide at [https://rustup.rs/](https://rustup.rs/).
- **Docker:** Build container images for deploying the operator in Kubernetes.

### To Deploy the Operator

- **Kubernetes Cluster:** Ensure you have access to a running Kubernetes cluster.
- **Kubectl:** Install Kubernetes command-line tool for managing cluster resources Installation guide available at https://kubernetes.io/docs/tasks/tools/.
- **Clever Cloud Account Credentials:** Obtain API tokens and secrets from your Clever Cloud account to configure the operator.

These prerequisites are essential for getting started with the Clever Operator, whether you're contributing to its development or deploying it in production.

## Installation

The simplest ways to deploy the Clever Operator are either directly from Docker Hub or using the Helm chart.

### Deploying from DockerHub

Applying the deployment scripts:

```bash
kubectl apply -f https://raw.githubusercontent.com/CleverCloud/clever-operator/main/deployments/kubernetes/v1.24.0/10-custom-resource-definition.yaml 
kubectl apply -f https://raw.githubusercontent.com/CleverCloud/clever-operator/main/deployments/kubernetes/v1.24.0/20-deployment.yaml
```


### Installing via Helm Chart

1. Configuring `values.yaml` in `deployments/kubernetes/helm` with your values.

2. Installing the chart:
	```bash
    helm install clever-operator -n clever-operator --create-namespace -f values.yaml .
    ```


### Building from Source

1. Cloning the repository:

```bash
git clone https://github.com/CleverCloud/clever-operator.git
cd clever-operator
```

2. Building the binary:

```bash
make build
```

 3. Running the operator:

```bash
target/release/clever-operator
```

### Building and Deploying the Docker Image

1. Building the Docker image:

	```bash
	DOCKER_IMG=<your-registry>/<your-namespace>/clever-operator:latest make docker-build
	```

1. Pushing the image to your registry:

	```bash
	DOCKER_IMG=<your-registry>/<your-namespace>/clever-operator:latest make docker-push
	```

3. Updating the Kubernetes deployment script: 
	
	Modify `deployments/kubernetes/v1.24.0/20-deployment.yaml` to use your Docker image.

4. Deploying to Kubernetes:
	```bash
	make deploy-kubernetes
	```


## Configuration

The Clever Operator requires configuration to connect to Clever Cloud's API and manage resources within your Kubernetes cluster. Configuration options are available at two levels: global (applies to all namespaces) and namespace-specific.

For details on how to obtain these credentials, follow the instructions on the [How to obtain the credentials for the Clever Operator](./credentials.md) document.

### Global Configuration

Global configuration settings apply across all namespaces and are defined via environment variables or configuration files.

- **Environment Variables:**
    
    - `CLEVER_OPERATOR_API_ENDPOINT`: The endpoint for the Clever Cloud API.
    - `CLEVER_OPERATOR_API_TOKEN`: Your Clever Cloud API token.
    - `CLEVER_OPERATOR_API_SECRET`: The secret associated with your API token.
    - `CLEVER_OPERATOR_API_CONSUMER_KEY`: Your Clever Cloud consumer key
    - `CLEVER_OPERATOR_API_CONSUMER_SECRET`: Your Clever Cloud consumer secret.

- **Configuration Files:** By default, if the `--config` flag isn't provided to the binary, the operator looks at the following locations to retrieve its configuration (in order of priority):
    
    1. `/usr/share/clever-operator/config.{toml,yaml,json}`
    2. `/etc/clever-operator/config.{toml,yaml,json}`
    3. `$HOME/.config/clever-operator/config.{toml,yaml,json}`
    4. `$HOME/.local/share/clever-operator/config.{toml,yaml,json}`
    5. `config.{toml,yaml,json}` (in the current working directory)


### Namespace-Level Configuration

Namespace-level configurations override the global settings for specific namespaces. They're defined using a Kubernetes Secret resource named `clever-operator` with the `config` key.

- **Creating a Namespace-Level Configuration:** Create a Kubernetes Secret with the necessary configuration keys:
    
    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: clever-operator
      namespace: my-namespace
    data:
      config: |-
        api:
          endpoint: "https://api.clever-cloud.com/v2"
          token: "<your-api-token>"
          secret: "<your-api-secret>"
          consumerKey: "<your-consumer-key>"
          consumerSecret: "<your-consumer-secret>"
        proxy:
          host: "proxy.example.com"
          port: 8080
    ```
    
- **Applying the Configuration:** Apply the Secret to your namespace:
    
    ```bash
    kubectl apply -f namespace-config.yaml
    ```
    

The operator automatically detects and applies namespace-specific configurations when interacting with resources in that namespace.

### Validating Configuration

To ensure your configuration is applied correctly, look at the operator logs for any errors or warnings:

```bash
kubectl logs -n clever-operator <operator-pod-name>
```

## Usage Examples

The Clever Operator enables you to manage Clever Cloud resources directly from your Kubernetes cluster using custom resources. Below are examples for PostgreSQL and Redis.

### Managing PostgreSQL Resources

- **Creating a PostgreSQL Instance:** Define a YAML manifest for the PostgreSQL resource:
    
    ```yaml
    apiVersion: clever-cloud.com/v1
    kind: PostgreSQL
    metadata:
      name: my-postgresql
      namespace: default
    spec:
      version: "14"
      plan: "dev"
      region: "par"
    ```
    
    Apply the manifest to your cluster:
    
    ```bash
    kubectl apply -f postgresql.yaml
    ```
    
- **Verifying the Deployment:** Check the status of the PostgreSQL resource:
    
    ```bash
    kubectl get postgresql my-postgresql -o yaml
    ```
    
- **Accessing PostgreSQL:** Retrieve the connection details from the Clever Cloud dashboard or the resource’s status field.


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
    
- **Accessing Redis:** Retrieve the connection details from the Clever Cloud dashboard or the resource’s status field.

These examples demonstrate the simplicity and power of using the Clever Operator to manage cloud resources in a declarative way in Kubernetes.

