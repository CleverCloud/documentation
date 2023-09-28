---
title: TCP redirections with Clever Tools
shortdesc: TCP redirections to port 4040 of your instance
tags:
- administrate
keywords:
- tcp
- cli-setup
- redirection
---
{{< alert "warning" "TCP redirections are a BETA feature" >}}
    <p>
    TCP redirections are currently available free of charge as long as the feature is still considered in a BETA stage.
    Once the feature leaves the BETA stage, it won't be free anymore.
    </p>
{{< /alert >}}


## What is a TCP redirection?

A regular application on Clever Cloud needs to listen on port 8080 and answer to HTTP traffic.
Our reverse proxies then make your application available using HTTP(s) using your domain name.

Some applications might additionally want to use a binary protocol, with raw TCP interactions.
For this scenario, your application will have to listen for TCP traffic on port 4040.
Once this is done, all you need to do is add a TCP redirection to your application. A port will be
provided to you, and your TCP listener will be available on your domain name using the provided port.

## What is a namespace?

When creating a TCP redirection, you will need to choose in which namespace you want to create it.
If you are a Premium customer with dedicated reverse proxies, you will have your own namespace.
If you are not a Premium customer and want to use a custom domain name, you will have to use the
"default" namespace.
If you want to use a cleverapps domain, you will have to use the "cleverapps" namespace.

`clever tcp-redirs list-namespaces` will provide you with a list of namespaces that you are allowed
to use for the current application.

## Creating a new TCP redirection

Creating a new TCP redirection is as simple as `clever tcp-redirs add --namespace default` where
you can obviously replace "default" by the namespace of your choice. You will be prompted with
the port that has been assigned to you and you will be able to contact your application's TCP
listener using `tcp://your-domain-name:the-port/`

## Listing active TCP redirections

You can list active TCP redirections for the current application using `clever tcp-redirs`

## Deleting a TCP redirection

First, you need to know which port was allocated to you, and in which namespace. You can list
the active TCP redirections to make sure you have the proper data.

We'll use namespace "default" and port "42" for this example.

You can now remove your TCP redirection using `clever tcp-redirs remove 42 --namespace default`.
