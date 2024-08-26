---
type: docs
title: TCP redirections
shortdesc: TCP redirections to port 4040 of your instance
tags:
- administrate
keywords:
- tcp
- cli-setup
- redirection
type: docs
---
{{< callout type="warning" >}}
TCP redirections are currently available free of charge as long as the feature is in BETA stage.
Once the feature leaves the BETA stage, it won't be free anymore.
{{< /callout >}}

## What is a TCP redirection?

Every application hosted Clever Cloud must listen on port 8080 and answer to HTTP traffic.
This is useful for both routing requests and monitoring purposes.

However, some applications might additionally require binary protocol, with raw TCP interactions.
In that case, you can use a TCP redirection to route TCP traffic, through Clever Cloud reverse proxies, to your application.

Every application can be configured to receive TCP traffic on the port 4040.
Clever Cloud then assigns a specific port to your application to expose it to TCP traffic. This port is chosen at random above 5000.

Use this specific port to send and receive TCP traffic.

{{< callout type="warning" >}}
The application must still be listening to the 8080 port, regardless of TCP configuration.
{{< /callout >}}

## What is a namespace?

Clever cloud manages a fleet of reverse proxies that fulfill different purposes, depending on their type and region.
A namespace is a group of reverse proxies. You may encounter:

- `default`: the stable public group of your region
- `cleverapps`: the group behind all the `cleverapps.io` domains
- dedicated name: if you are a premium customer with dedicated reverse proxies

Use `default` or dedicated namespace for applications with a custom domain name.  
Use `cleverapps` for applications under the `cleverapps.io` domain.
If your application has both a custom domain name and a `cleverapps.io` one, you may activate TCP redirections on both of them.
Note that this generates two different ports, one for each domain.  
You should use one or the other depending on the domain name you use in your request.

To list the possible redirections available to your application, you can use the following:

```bash
clever tcp-redirs list-namespaces
```

## Creating a new TCP redirection

### With the console

From your console, select your application. In the secondary menu, go to **TCP redirections**.
From there, you can create a TCP redirection for a specific namespace (see [namespaces doc](#what-is-a-namespace?))

The creation is instantaneous. Find the TCP redirection port on this page.

![Redirection console](/images/doc/TCP_redirection_console.png)

### With the Clever CLI

You can use the following command to create a TCP redirection from the CLI:

```bash
clever tcp-redirs add --namespace default
```

Depending on your situation, you should replace `default` with the appropriate namespace.

The port assigned to your application displays right after the TCP redirection creation.
You can then contact your application over TCP using `tcp://your-domain-name:the-port/`.

## Managing redirections

### Listing active redirections

To visualize your application's redirections:

- from your console, an active redirection has a green tick next to it
- from the Clever CLI, you can use:

```bash
clever tcp-redirs
```

### Deleting redirections

To delete a redirection on an application:

- from your console, use the `delete` button next to the redirection
- from the Clever CLI, use:

```bash
clever tcp-redirs remove (port) --namespace (namespace)
```

Example: if your redirection is on port **5500** and the **default** namespace, the command would be

```bash
clever tcp-redirs remove 5500 --namespace default
```