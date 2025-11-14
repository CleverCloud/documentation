---
title: Otoroshi 17.8.1 is available, with HTTP Security Headers and Time Restriction plugins
description: Small bump, but great new possibilities for your APIs and applications
date: 2025-11-14
tags:
  - addons
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v17.8.1](https://github.com/MAIF/otoroshi/releases/tag/v17.8.1) is available with multiple improvements and bug fixes. It brings two new plugins to inject common HTTP security headers (HSTS, CSP, XFO, X-XSS-Protection, X-Content-Type-Options) on responses or restrict when a route is accessible (days range, time range): `HTTP Security Headers` and `Time Restriction`.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.8.1_1763110173` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.8.1_1763110173
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
