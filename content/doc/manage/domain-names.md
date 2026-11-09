---
type: docs
linkTitle: Domain Names
title: Domain Names
description: Serve your application on cleverapps.io or on your own domains, point their DNS records to its region, and share a domain between applications with path routing
keywords:
- domain names
- dns configuration
- custom domains
- cname
- cleverapps.io
- path routing
- favorite domain
aliases:
- /doc/develop/common-configuration/domain-names
- /doc/admin-console/custom-domain-names
- /doc/administrate/domain-names
- /guides/domain-names
- /doc/common-configuration/domain-names
---

Each application gets a `cleverapps.io` domain at creation, such as `app-<uuid>.cleverapps.io`. Add your own domains to serve it in production: point their DNS records to the region of the application, and Clever Cloud generates their [TLS certificates](/doc/security/ssl/) with Let's Encrypt.

## Add a domain

In the Console, open the application, then its **Domain names** menu. With Clever Tools, list, add, or remove the domains of an application:

```bash
clever domain
clever domain add www.example.com
clever domain rm www.example.com
```

A domain can only serve one application, unless you split it with [path routing](#path-routing). Clever Cloud refuses a domain already bound to another application. It also refuses a domain when another organisation already uses its parent domain or one of its subdomains, unless you're an administrator of this organisation. If you own such a domain, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

[`clever domain overview`](/doc/tools/cli/applications/configuration/#domain) lists the domains of all your applications.

## cleverapps.io domains

You can remove the default `cleverapps.io` domain of an application, or add another one, such as `my-shop.cleverapps.io`, if no other application uses it. Clever Cloud manages their DNS and their certificate, so they work once you add them.

Use them for development and testing: they go through reverse proxies shared by all applications, and Clever Cloud doesn't guarantee their quality of service. Their certificate only covers one level, such as `my-shop.cleverapps.io`: a name such as `blog.my-shop.cleverapps.io` only works over HTTP. A wildcard such as `*.my-shop.cleverapps.io` isn't allowed.

## Configure the DNS records

Point your domain to the load balancers of the region of your application, in the DNS zone of your domain provider. Prefer a `CNAME` record: Clever Cloud keeps the addresses behind it up to date. Use `A` records only where a `CNAME` record isn't allowed, such as on the root of a domain like `example.com`, or on a name which already has other records.

The **Domain names** menu of the application shows the records of its region. The health data hosting (HDS) regions require a [specific contract](/doc/manage/regions/#health-data-hosting).

| Region                     | `CNAME` record                    | `A` records                                                                                                                                                                      |
| -------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Paris (`par`)              | `domain.par.clever-cloud.com.`    | `91.208.207.214`<br>`91.208.207.215`<br>`91.208.207.216`<br>`91.208.207.217`<br>`91.208.207.218`<br>`91.208.207.220`<br>`91.208.207.221`<br>`91.208.207.222`<br>`91.208.207.223` |
| Paris HDS (`parhds`)       | `domain.parhds.clever-cloud.com.` | `91.208.207.214`<br>`91.208.207.215`<br>`91.208.207.220`<br>`91.208.207.221`<br>`91.208.207.222`<br>`91.208.207.223`                                                             |
| Paris, on Scaleway (`scw`) | `domain.scw.clever-cloud.com.`    | `212.83.186.147`<br>`212.83.186.216`<br>`212.129.27.183`<br>`212.129.27.239`                                                                                                     |
| Gravelines HDS (`grahds`)  | `domain.grahds.clever-cloud.com.` | `188.165.58.196`<br>`188.165.58.200`                                                                                                                                             |
| Roubaix (`rbx`)            | `domain.rbx.clever-cloud.com.`    | `87.98.177.181`<br>`87.98.180.173`<br>`87.98.182.136`                                                                                                                            |
| Roubaix HDS (`rbxhds`)     | `domain.rbxhds.clever-cloud.com.` | `135.125.16.47`<br>`135.125.16.49`                                                                                                                                               |
| London (`ldn`)             | `domain.ldn.clever-cloud.com.`    | `77.68.78.36`<br>`77.68.94.247`                                                                                                                                                  |
| Warsaw (`wsw`)             | `domain.wsw.clever-cloud.com.`    | `145.239.17.127`<br>`145.239.17.192`                                                                                                                                             |
| Montreal (`mtl`)           | `domain.mtl.clever-cloud.com.`    | `149.56.117.183`<br>`158.69.109.229`                                                                                                                                             |
| Singapore (`sgp`)          | `domain.sgp.clever-cloud.com.`    | `51.79.197.159`<br>`51.79.197.160`                                                                                                                                               |
| Sydney (`syd`)             | `domain.syd.clever-cloud.com.`    | `139.99.253.215`<br>`139.99.253.237`                                                                                                                                             |

Check your domains with Clever Tools: it compares their records with the expected ones, and suggests the records to add.

```bash
clever domain diag
```

This command only checks the DNS records. It checks neither the certificates nor the HTTP responses.

### Root domain and `www` subdomain

To serve both `example.com` and `www.example.com`, add both to your application. Point `www.example.com` to the region with a `CNAME` record, and `example.com` with `A` records. If you'd rather not maintain `A` records, many domain providers can redirect `example.com` to `www.example.com`, often over HTTP only: then only add `www.example.com` to your application.

### Wildcard domains

A wildcard domain, such as `*.example.com`, serves the names one level under it, such as `blog.example.com` or `shop.example.com`. It doesn't serve `example.com` itself, nor deeper names such as `api.blog.example.com`: add them to your application too. Point the wildcard with a `CNAME` record named `*`. Clever Cloud doesn't generate wildcard certificates: [upload your own](/doc/security/ssl/).

### Change the DNS records of a domain

DNS resolvers keep a record for the duration of its time to live (TTL), so a change can take this long to reach all the visitors. Before you change the records of a domain, for instance to move it to another region, lower their TTL, such as to 60 seconds. Then, wait for the duration of the previous TTL. After the change, set the TTL back to its previous value.

## Favorite domain

The favorite domain of an application is the one that `clever open` and the link at the top of its Console page open. Set it among the domains of the application, with the star next to it in the **Domain names** menu, or with Clever Tools:

```bash
clever domain favourite set www.example.com
```

The favorite domain doesn't redirect the other domains of the application to it.

## Path routing

Several applications can share a domain, each one on its own path. For instance, bind `example.com` to a first application, and `example.com/api/` to a second one: the requests whose path starts with `/api/` go to the second application, and the other ones to the first.

```bash
clever domain add example.com --app "<firstAppID>"
clever domain add example.com/api/ --app "<secondAppID>"
```

The path matches the start of the request path, as text: a route on `/api`, without the final slash, also catches `/apiv2`. End the path with a slash to only match this folder: a request on `/api` itself then goes to the first application.

The second application receives the full path, prefix included: it must serve its routes under `/api/`, such as from an `api/` folder for a static site.
