---
title: "Node.js image update, with Mise package manager and Redirection.io easy setup"
date: 2025-01-15
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Ease your life on Clever Cloud
excludeSearch: true
---

We deployed an updated Node.js image with no impact for our users. It uses `22.13 LTS` release by default and Linux Kernel `6.12.9`.

## Mise package manager

It's the first image to include the [Mise package manager](https://mise.jdx.dev/), allowing you to install and manage many developer tools, environment variables, secrets, aliases, tasks, hooks through commands or a configuration file. It's compatible with [asdf ecosystem](https://mise.jdx.dev/dev-tools/comparison-to-asdf.html).

* Learn more about [Mise](https://mise.jdx.dev/)

## Redirection.io easy setup

This image is also the first to include [Redirection.io](https://redirection.io/) easy setup. To configure the agent as a proxy, you just need to create an app listening on the port of your choice, get a project key from Redirection.io and set these environment variables:

- `CC_ENABLE_REDIRECTIONIO=true`
- `CC_REDIRECTIONIO_PROJECT_KEY=""`: The Redirection.io project key
- `CC_REDIRECTIONIO_FORWARD_PORT=""`: The listening port of your application

The Redirection.io agent will start as a service, listen to `8080` port and forward the traffic to your application. An optional `CC_REDIRECTIONIO_INSTANCE_NAME` is also available. It's the name of your application by default.

These environment variables will progressively be available on all our compatible images.

- [Clever Cloud Environment Variables Reference](/developers/doc/reference/reference-environment-variables/)
