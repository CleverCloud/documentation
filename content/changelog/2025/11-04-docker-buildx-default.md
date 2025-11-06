---
title: Buildx used by default in Docker runtime from January 12th, 2026
description: It's never too late to update, prepare your applications right now
date: 2025-11-04
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[In June](/changelog/2025/06-17-images-update/), we introduced the `CC_DOCKER_BUILDX` environment variable to let users migrate to Docker Buildx progressively. Starting January 12th, 2026, Docker Buildx will be used as the default builder for all Docker-based applications. If you need to continue using the classic Docker builder, you must set `CC_DOCKER_BUILDX=false` in your application settings.
