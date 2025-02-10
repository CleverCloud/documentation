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
- **Clever Cloud Account Credentials:** [Obtain API tokens and secrets from your Clever Cloud]({{< ref "/api/howto" >}} "API Overview") account to configure the operator.

These prerequisites are essential for getting started with the Clever Operator, whether you're contributing to its development or deploying it in production.

## Getting the credentials

The Clever Operator requires configuration to connect to Clever Cloud's API and manage resources within your Kubernetes cluster. This configuration requires four credentials:

- _Consumer key_
- _Consumer Secret_
- _Token_
- _Secret_

To obtain them, you need to connect to the Clever Cloud API, that has an OAuth1 based authentication. As explained in the [Clever Cloud API Overview](/api/howto), you need to create an OAuth consumer token in the Clever Cloud console, use it to obtain the _Consumer key_ and the _Consumer Secret_, and do the OAuth authentication dance to get the _Token_ and _Secret_.


> #### This seems cumbersome, is there an easier way?
>
> Yes the OAuth dance is complex. If you want a simpler setup, there is a small application that you can deploy on Clever Cloud and that automates most of the pain away from you.
>
> The code and tutorial are on [https://github.com/CleverCloud/oauth-consumer-server](https://github.com/CleverCloud/oauth-consumer-server).

## Installation

The simplest ways to deploy the Clever Operator are either directly from Docker Hub or using the Helm chart.

### Deploying from DockerHub

1. Clone the repository:

    ```bash
    git clone https://github.com/CleverCloud/clever-operator/
    ```

1. Insert your credentials into the manifests.

    The manifests are on folder `/deployments/kubernetes/v1.24.0/`. Modify the `ConfigMap` object in file `/deployments/kubernetes/v1.24.0/:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: clever-operator-configuration
      namespace: clever-operator-system
    data:
      config.toml: |
        [api]
        endpoint = "https://api.clever-cloud.com/v2"
        token = "<your_token>"
        secret = "<your_secret>"
        consumerKey = "<your_consumer_key>"
        consumerSecret = "<your_consumer_secret>"
    ```

    Replacing `<your_token>`, `<your_secret>`, `<your_consumer_key>` and `<your_consumer_secret>` by the credentials obtained in the precedent section.

1. Apply the manifests to deploy the operator.


    ```bash
    kubectl apply -f /deployments/kubernetes/v1.24.0/10-custom-resource-definition.yaml 
    kubectl apply -f /deployments/kubernetes/v1.24.0/20-deployment.yaml
    ```

### Installing via Helm Chart

1. Clone the repository:

    ```bash
    git clone https://github.com/CleverCloud/clever-operator/
    ```

1. Configure your credentials in the `config` section of the file `values.yaml` in `deployments/kubernetes/helm`.

    ```yaml
    config:
      token: "<your_token>"
      secret: "<your_secret>"
      consumerKey: "<your_consumer_key>"
      consumerSecret: "<your_consumer_secret>"
    ```
    Replacing `<your_token>`, `<your_secret>`, `<your_consumer_key>` and `<your_consumer_secret>` by the credentials obtained in the precedent section.

1. Install the chart:

    ```bash
      helm install clever-operator -n clever-operator --create-namespace -f values.yaml .
    ```

### Building from Source

1. Clone the repository:

  ```bash
  git clone https://github.com/CleverCloud/clever-operator.git
  cd clever-operator
  ```

1. Insert your credentials into the manifests.

    The manifests are on folder `/deployments/kubernetes/v1.24.0/`. Modify the `ConfigMap` object in file `/deployments/kubernetes/v1.24.0/:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: clever-operator-configuration
      namespace: clever-operator-system
    data:
      config.toml: |
        [api]
        endpoint = "https://api.clever-cloud.com/v2"
        token = "<your_token>"
        secret = "<your_secret>"
        consumerKey = "<your_consumer_key>"
        consumerSecret = "<your_consumer_secret>"
    ```

    Replacing `<your_token>`, `<your_secret>`, `<your_consumer_key>` and `<your_consumer_secret>` by the credentials obtained in the precedent section.

1. Build the binary:

    ```bash
    make build
    ```

1. Running the operator:

    ```bash
    target/release/clever-operator
    ```

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

