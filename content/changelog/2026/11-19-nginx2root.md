---
title: "NGINX2Root: Clever Cloud runtimes don't enable the affected features (Security update)"
description: The NGINX configuration of Clever Cloud Python and Ruby runtimes doesn't enable the features affected by the NGINX2Root vulnerabilities, and our images will shortly include NGINX 1.30.7 which fixes them
date: 2026-11-19
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [NGINX security advisories](https://nginx.org/en/security_advisories.html) describe five vulnerabilities fixed in NGINX 1.30.7 and 1.31.9, known as [NGINX2Root](https://nginx2root.com/). Some of them can allow unauthenticated remote code execution with the privileges of the NGINX worker process. Each one requires a specific feature to be enabled:

- [CVE-2026-123007](https://www.cve.org/CVERecord?id=CVE-2026-123007) and [CVE-2026-123633](https://www.cve.org/CVERecord?id=CVE-2026-123633): HTTP/2
- [CVE-2026-121810](https://www.cve.org/CVERecord?id=CVE-2026-121810): HTTP/3
- [CVE-2026-123634](https://www.cve.org/CVERecord?id=CVE-2026-123634): `resolver` with a `proxy_pass` destination built from the request, and `mirror`
- [CVE-2026-113425](https://www.cve.org/CVERecord?id=CVE-2026-113425): mail proxy with `auth_http`

## Clever Cloud runtimes

[Python](/doc/deploy/applications/python/) and [Ruby](/doc/deploy/applications/ruby/) runtimes use NGINX in front of your application. Their configuration enables none of these features: you have nothing to do. We will nevertheless update NGINX in our images shortly to 1.30.7, the latest stable release, which includes these fixes.

The custom services we provide to some customers that could be affected have all been updated already.

## Your own NGINX

If you run your own NGINX, in a [Docker](/doc/deploy/applications/docker/) or [Linux](/doc/deploy/applications/linux/) application for example, our load balancers forward requests to it in HTTP/1.1: an attacker can't reach the HTTP/2 and HTTP/3 vulnerabilities through them. Your application can still be exposed if its configuration combines `resolver`, a `proxy_pass` destination built from the request and `mirror`, or if a [TCP redirection](/doc/manage/tcp-redirections/) gives direct access to NGINX.

Update it to 1.30.7 or 1.31.9 anyway. Until then, disable the affected features you don't need, as described in the [researchers' write-up](https://xint.io/blog/nginx2root-remote-code-execution).

If you have any questions or need help, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).
