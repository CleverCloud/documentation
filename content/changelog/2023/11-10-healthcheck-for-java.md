---
title: Custom healthcheck paths for Java applications
date: 2023-11-10
tags:
  - applications
  - java
authors:
  - name: Julien Durillon
    link: https://github.com/judu
    image: https://github.com/judu.png?size=40
description: Your java applications can now be deployed with one or multiple custom healtchecks
aliases:
- /changelog/2023-11-10-healthcheck-for-java
excludeSearch: true
---

You can now define the paths that the orchestrator will call to validate a deployment for Java applications through one or multiple `CC_HEALTH_CHECK_PATH` environment variables. It works as follows:

* If the application responds on this specified path, and the response code is between `200` and `300`, the orchestrator considers that the deployment has been validated.
* If it responds with another error code outside this interval, the application is considered to have failed its deployment.

Currently, the orchestrator only checks whether the application is listening to TCP port `8080`. It does not always mean that the application has started correctly.

- Read the documentation about [Deployment healthcheck path](/developers/doc/develop/healthcheck/) 📖
