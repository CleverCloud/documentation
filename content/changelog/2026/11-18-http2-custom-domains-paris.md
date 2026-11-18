---
title: Try HTTP/2 on your custom domains in the Paris region
description: After cleverapps.io domains, point your custom domains to a new CNAME record to test HTTP/2 in the Paris region, before we enable it for all of them
date: 2026-11-18
tags:
  - sozu
  - domain
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We enabled the [HTTP/2 support of Sōzu 2](/changelog/2026/06-05-sozu-2.1.0/) on `cleverapps.io` domains in June, to check that it behaves as expected at scale. You can now test it on your custom domains in the Paris region (`par`), before we enable it for all of them later in 2027.

To do so, point your domain to this `CNAME` record, which leads to load balancers we deploy next to the existing ones:

```text
domain.par.h2.services.clever-cloud.com.
```

These load balancers serve the Let's Encrypt certificate of your domain, and still answer clients that only support HTTP/1.1. `clever domain diag` doesn't know this record, and reports it as one to replace: ignore this suggestion.

Your application keeps receiving HTTP/1.1 requests, with the `X-Request-Id` and `traceparent` headers these load balancers add. HTTP/2 stops at the load balancers for now: an option will later let you use it all the way to your application.

- Learn more about [HTTP/2 on custom domains](/doc/manage/domain-names/#http2-in-the-paris-region)
- Learn more about [load balancers and their request headers](/doc/network/load-balancers/)
- [Share your feedback on HTTP/2](https://github.com/CleverCloud/Community/discussions/categories/general)
