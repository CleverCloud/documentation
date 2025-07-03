---
type: docs
title: Domain names
position: 3
shortdesc: How to setup and configure domains names for your apps
tags:
- dashboard-setup
- apps
keywords:
- DNS
- domain
- URL
type: docs
---

When creating an application, you have two (non-exclusive) choices for domain names:

* Using a personal domain name
* Using a `cleverapps.io` free domain for development and testing purposes, with built-in SSL

Add it in the application configuration: in the console, click **application name** in the first panel, then choose **domain names**. You'll have to choose to add a custom domain name or use a subdomain under `*.cleverapps.io`.

{{< callout type="info" >}}
  You can link one or more domain names to the same application. On the other hand, you can add `mydomain.com/app1` and `mydomain.com/app2` to different Clever Cloud applications at the same time through [path routing](#path-routing).
{{< /callout >}}

## Primary (favourite) domain name

You can set multiple custom or `cleverapps.io` domain names to an application, but only set one of them as the **primary (favourite)**. This is the one that will be used by default when you access your application with the `clever open` command of Clever Tools or through the link in the upper right corner of the Console:

![Primary domain link](/images/doc/primary-domain-link.webp)

To select the primary domain name:
- Click the star icon next to the domain name in the **Domain names** section of your application in the Console
- Use the `clever domain favourite set example.com` command in [Clever Tools](/developers/doc/cli/applications/configuration/#domain)
- Use the dedicated `/vhosts/favourite` endpoint [in the API](/developers/api/v2/#put-/organisations/-id-/applications/-appId-/vhosts/favourite)

## Testing with `cleverapps.io` Domain

{{< callout type="warning" >}}
  Clever Cloud provides `*.cleverapps.io` domains for development and testing purposes. They point to specific reverse proxies and have the following drawbacks: the `.io` TLD isn't made for production, and since we offer the domain, the likelihood of people abusing it can be very high. **It's therefore not possible to guarantee a high level of quality on cleverapps domains**.
{{< /callout >}}

In the console, in the domain name sub menu of your application, there is a default entry configured by default for every new app: `yourAppID.cleverapps.io`, which can be removed.

In your application's domain section, just enter `example.cleverapps.io`. You have to choose a unique one. Trusted SSL is available on every subdomain.

{{< callout emoji="🌐" >}}
`*.cleverapps.io` certificate is only valid for the first subdomain level, it won't work with a domain like `blog.mycompany.cleverapps.io`.
{{< /callout >}}

## Configuring Domain Names by Region

It's possible to point your personalized domain name to Clever Cloud with either a type `A` or `CNAME` record through your registrar.

{{< callout type="warning" >}}
  The use of a CNAME record is **highly** recommended.
{{< /callout >}}

With a `CNAME` record, your DNS configuration is always up-to-date.
Using `A` records requires you to keep the DNS configuration up-to-date manually.

We also support wildcard personal domain names, to do so use the standard pattern to describe it: `*.example.com`

### Europe/Paris (PAR)

Provide the following to your registrar:

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.par.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 91.208.207.214`<br>`@ 10800 IN A 91.208.207.215`<br>`@ 10800 IN A 91.208.207.216`<br>`@ 10800 IN A 91.208.207.217`<br>`@ 10800 IN A 91.208.207.218`<br>`@ 10800 IN A 91.208.207.220`<br>`@ 10800 IN A 91.208.207.221`<br>`@ 10800 IN A 91.208.207.222`<br>`@ 10800 IN A 91.208.207.223`  |

### Europe/Paris HDS (PARHDS)

Provide the following to your registrar:

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.parhds.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 91.208.207.214`<br>`@ 10800 IN A 91.208.207.215`<br>`@ 10800 IN A 91.208.207.220`<br>`@ 10800 IN A 91.208.207.221`<br>`@ 10800 IN A 91.208.207.222`<br>`@ 10800 IN A 91.208.207.223`  |

To benefit from certified hosting for health data, you need to deploy in an HDS zone and to sign up to a specific contract. This begins with [an initial discussion with our team](https://www.clever-cloud.com/fr/hebergement-donnees-de-sante/contact-hds/).

### Europe/Paris onto Scaleway (SCW)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.scw.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 212.129.27.239`<br>`@ 10800 IN A 212.83.186.147`<br>`@ 10800 IN A 212.83.186.216`<br>`@ 10800 IN A 212.129.27.183` |

### Europe/Gravelines HDS (GRAHDS)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.grahds.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 188.165.58.196`<br>`@ 10800 IN A 188.165.58.200` |

To benefit from certified hosting for health data, you need to deploy in an HDS zone and to sign up to a specific contract. This begins with [an initial discussion with our team](https://www.clever-cloud.com/fr/hebergement-donnees-de-sante/contact-hds/).

### Europe/London (LDN)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.ldn.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 77.68.78.36`<br>`@ 10800 IN A 77.68.94.247` |

### Europe/Roubaix (RBX)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.rbx.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 87.98.177.176`<br>`@ 10800 IN A 87.98.177.181`<br>`@ 10800 IN A 87.98.180.173`<br>`@ 10800 IN A 87.98.182.136` |

### Europe/Roubaix HDS (RBXHDS)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.rbxhds.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 135.125.16.47`<br>`@ 10800 IN A 135.125.16.49` |

To benefit from certified hosting for health data, you need to deploy in an HDS zone and to sign up to a specific contract. This begins with [an initial discussion with our team](https://www.clever-cloud.com/fr/hebergement-donnees-de-sante/contact-hds/).

### Europe/Warsaw (WSW)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.wsw.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 145.239.17.127`<br>`@ 10800 IN A 145.239.17.192` |

### North-America/Montreal (MTL)

Provide the following to your registrar:

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.mtl.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 158.69.109.229`<br>`@ 10800 IN A 149.56.117.183` |

### Asia/Singapore (SGP)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.sgp.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 51.79.197.159`<br>`@ 10800 IN A 51.79.197.160` |

### Oceania/Sydney (SYD)

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.syd.clever-cloud.com.` |
| A<br>Only if CNAME is not available  | `@ 10800 IN A 139.99.253.215`<br>`@ 10800 IN A 139.99.253.237` |

{{< callout type="warning" >}}
You cannot use a CNAME on a top-level domain, or on a subdomain which already has DNS records.
{{< /callout >}}

If you want to make your application available from a domain name which doesn't support CNAME records (eg `example.com` in addition to `www.example.com`), check if your registrar provides a web redirection service. This way, you only have to make `www.example.com` point to Clever Cloud. Please note that web redirection provided by registrars only work over HTTP.

Remember that DNS changes may take time to propagate (usually a few hours, sometimes up to a day or more). It depends on the TTL setting of your DNS configuration. For faster changes, you can lower the TTL value in advance, and rise it again afterwards.

{{< callout type="info" >}}
`*.example.com` match for instance `blog.example.com` or `www.example.com`. But for the raw domain `example.com`, you have to add both `*.example.com` and `example.com` to your application.
{{< /callout >}}

### Contextual Example

| Domain Name Use Case        | CNAME config                                    | Record A config                                                | Web redirections                            |
|-----------------------------|-------------------------------------------------|-----------------------------------------------------------------|--------------------------------------------|
| `www.example.com` <br> `example.com` | Point `www.example.com` to `domain.par/mtl.clever-cloud.com.` | No A record needed                                            | Redirect `example.com` to `www.example.com` |
| `www.example.com`           | Point `www.example.com` to `domain.par/mtl.clever-cloud.com.` | No A record needed                                            | No redirect needed                          |
| `example.com`               | No CNAME record needed                           | Point `example.com` to the two IP addresses of the selected region | No redirect needed                          |

## Path routing

Requests are routed to applications based on the domain name, but you can also route depending on its path.

For instance, you can bind `example.com` to an app, and `example.com/api` to another one.
All the HTTP requests on `example.com` where the path starts with `/api` are routed to
the second app. The other requests are routed to the first app.
You can add a path after every domain name you bind in the console (or with [clever tools]({{< ref "doc/cli" >}} "Clever Tools")).

Note that your path-routed application **needs** to have a `/whatever` route.

This will work:

```text
example.com        ->      myfirtapp-main-route

example.com/api    ->      mysecond-app-main-route/api
```

This will NOT work:

```text
example.com        ->      myfirtapp-main-route     (works)

example.com/api    ->      mysecondapp-main-route   (404 response from mysecondapp)
```

### Path routing for static sites

In the case of static files, you usually understand routes as paths in a file tree.

This will work:

```text
example.com/api    ->     my-static-site/api/index.php
```

This will NOT work:

```text
example.com/api    ->     my-static-site/index.php
```

## Gandi CNAME configuration

Here is [an article that demonstrates a simple setup for Gandi CNAMEs](https://www.clever-cloud.com/blog/features/2019/03/05/gandi-domain-on-clever-cloud/).
