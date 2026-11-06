---
type: docs
linkTitle: TCP Redirections
title: TCP redirections
description: Expose a raw TCP port of your Clever Cloud application through the load balancers, for protocols other than HTTP, from the Console, Clever Tools or Terraform
keywords:
- tcp redirections
- tcp port
- port forwarding
- namespace
- raw tcp
- non-http protocol
aliases:
- /doc/administrate/tcp-redirections
- /doc/common-configuration/tcp-redirections
---

A TCP redirection opens a public port on the Clever Cloud load balancers and forwards its raw TCP traffic to port `4040` of your application. Use it for protocols other than HTTP, such as SFTP, MQTT, or a game server. TCP redirections are free.

## How it works

- Your application listens on port `4040`. A [Docker container](/doc/deploy/applications/docker/#ports-mapping-and-network-groups) can use another port through `CC_DOCKER_EXPOSED_TCP_PORT`
- Clever Cloud chooses the public port. It stays the same while the redirection exists, even when the application redeploys
- Deployments still wait for the HTTP [health check](/doc/develop/common-configuration/healthcheck/) of your application on port `8080`: a TCP redirection doesn't replace it
- The load balancers forward the bytes unchanged: your application handles TLS itself, with its own certificate
- Your application sees the address of the load balancer, not the one of the client
- With several instances, the load balancers spread new connections across them

## Choose a namespace

A namespace is a group of load balancers. Each application can have one TCP redirection per namespace:

- `default`: the load balancers of your custom domains
- `cleverapps`: the load balancers of the `cleverapps.io` domains
- A private namespace, for organisations with dedicated load balancers

Use the namespace of the domain your clients connect to. List the namespaces available with [Clever Tools](/doc/tools/cli/):

```bash
clever tcp-redirs list-namespaces
```

## Create a TCP redirection

In the [Console](https://console.clever-cloud.com), open the **TCP redirections** page of your application, then click **Create** next to the namespace.

With Clever Tools, set the namespace with `--namespace`:

```bash
clever tcp-redirs add --namespace cleverapps
```

The command displays the public port, such as `Successfully added tcp redirection on port: 24950`. Clients then connect to this port on a domain of your application, here its `cleverapps.io` domain:

```bash
nc my-app.cleverapps.io 24950
```

Replace the domain and the port with those of your application.

With [Terraform](/doc/tools/terraform/), set `namespace` in the `redirection` attribute of the application: its read-only `port` holds the public port.

## List and remove TCP redirections

The **TCP redirections** page of the Console shows each redirection and its port. With Clever Tools, list them in human or JSON format:

```bash
clever tcp-redirs
clever tcp-redirs --format json
```

To remove a redirection, click **Delete** next to it in the Console. With Clever Tools, set its port and its namespace:

```bash
clever tcp-redirs remove 24950 --namespace cleverapps
```

Removing the redirection stops new connections through its port. A new redirection in this namespace can get a different port.

## Examples

- [Mosquitto](https://github.com/CleverCloud/mosquitto-example): an MQTT broker built on the Linux runtime
- [Node.js TCP chat](https://github.com/CleverCloud/nodejs-tcp-chat-example): a chat room to join with `nc`
- [SFTPGo](/guides/sftpgo/): an SFTP server exposed through a TCP redirection, with a web interface
