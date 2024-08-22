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

Most of Clever Cloud's applications must listen on port 8080 and answer to HTTP traffic.
This serves requests routing as well as monitoring purposes.

However, some applications might require binary protocol, with raw TCP interactions.
In that case, you can use a TCP redirection to route TCP traffic from reverse proxies to your application.

The IN port on reverse proxies (public side) is the usual 4040.
The TCP redirection assigns a random OUT port specifically to your application (starting from port 5000)
Configure the application to listen to this provided port.

Once done, your application can now send and receive TCP traffic.


Our reverse proxies then make your application available using HTTP(s) using your domain name.

Some applications might additionally want to use a binary protocol, with raw TCP interactions.
For this scenario, your application will have to listen for TCP traffic on port 4040.
Once this is done, all you need to do is add a TCP redirection to your application. A port will be


## What is a namespace?

A namespace is a group of reverse proxies: either the default public ones, cleverapps.io, or dedicated ones
A TCP redirection is associated with one of those 3 groups.

- If you are  a regular customer and want to use a custom domain name, you have to use the
"default" namespace.
- If you are a premium customer with dedicated reverse proxies, you have your own namespace.
- If you want to use a cleverapps.io domain, you can use the "cleverapps" namespace.

If you aren't sure what are the possible namespaces for your application, you can use `clever tcp-redirs list-namespaces`.
This command lists all the possible namespaces current application.

## Creating a new TCP redirection

### With the console

From your console, select your application. In the secondary menu, go to **TCP redirections**.
From there, you can create a `default` or `cleverapps` TCP redirection ( see [namespaces doc](#what-is-a-namespace?))

The creation is instantaneous. Find the application assigned port on this page. 

![Redirection console](/images/doc/TCP_redirection_console.png)

### With the Clever CLI

You can use the `clever tcp-redirs add --namespace default` command to create a TCP redirection from the CLI.
Depending on your situation, you should replace `default` with the appropriate namespace.

The port assigned to your application is displayed right after the TCP redirection creation.
You can then contact your application's TCP listener using `tcp://your-domain-name:the-port/`.

you can obviously replace "default" by the namespace of your choice. You will be prompted with
the port that has been assigned to you and you will be able to contact your application's TCP

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
`clever tcp-redirs remove 5500 --namespace default`

## Listing active TCP redirections

You can list active TCP redirections for the current application using `clever tcp-redirs`

## Deleting a TCP redirection

First, you need to know which port was allocated to you, and in which namespace. You can list
the active TCP redirections to make sure you have the proper data.

We'll use namespace "default" and port "42" for this example.

