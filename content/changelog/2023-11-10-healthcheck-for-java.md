---
title: Custom healthcheck path for Java
date: 2023-11-10
tags:
  - java
excludeSearch: true
description: Define custom healthcheck variables for java
---

This allows you to define variables in `CC_HEALTH_CHECK_PATH` format which define the paths that the orchestrator will call to validate a deployment, for Java appliactions.

* If the application responds on this specified path, and the response code is between `200` and `300`, the orchestrator considers that the deployment has been validated.
* If it responds with another error code outside this interval, the application is considered to have failed its deployment.

Currently, the orchestrator only checks whether the application is listening to TCP port 8080. This does not always mean that the application has started correctly.

The documentation is here: [Deployment healthcheck path](https://developers.clever-cloud.com/doc/develop/healthcheck/).
