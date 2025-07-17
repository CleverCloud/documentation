---
title: Custom healthcheck paths for all applications
date: 2024-02-26
tags:
  - applications
authors:
  - name: Julien Durillon
    link: https://github.com/judu
    image: https://github.com/judu.png?size=40
description: Your applications can now be deployed with one or multiple custom healtchecks
aliases:
- /changelog/2024-02-26-healthcheck-for-everyone
excludeSearch: true
---

Up until now, the deployment process only checked whether the application is listening to TCP port `8080`. That doesn't always mean that the application has started correctly.

You can now define the paths that the orchestrator will call to validate a deployment for applications through one or multiple `CC_HEALTH_CHECK_PATH` environment variables. It works as follows:

* If the application responds on this specified path, and the response code is between `200` and `300`, the orchestrator considers that the deployment has been validated.
* If it responds with a code outside this interval, the application is considered to have failed its deployment.

- Read the documentation about [Deployment healthcheck path](/developers/doc/develop/healthcheck/) 📖

