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

When creating an application, you have two (non exclusive) choices for domain names:

* Using a personal domain name
* Using a **\*.cleverapps.io** free domain for dev purposes, with built-in SSL

Add it in the application configuration: in the console, click on your **application name** in the first panel, then choose **domain names**. You'll have to choose to add a custom domain name or use a sub-domain under `*.cleverapps.io`.

{{< callout type="info" >}}
  You can link one or more domain names to the same application. On the other hand, you can add `mydomain.com/app1` and `mydomain.com/app2` to different Clever Cloud applications at the same time through [prefix routing](#prefix-routing).
{{< /callout >}}

## Using a **\*.cleverapps.io** free domain, with built-in SSL

{{< callout type="warning" >}}
  `*.cleverapps.io` domains are given for development and tests purpose. They point to
  specific reverse proxies and have the following weaknesses: .io TLD is not a stable one, and since we offer the domain, the probability that people will abuse it is high. Thus, we do not garantee the same QoS on the cleverapps reverse proxies.
{{< /callout >}}

In the console, in the domain name sub menu of your application, there is a default entry configured by default for every new app: `yourAppID.cleverapps.io`, which can be removed.

In your application's domain section, just enter `example.cleverapps.io`. You have to choose a unique one. Trusted SSL is available on every sub-domain.

{{< callout type="warning" >}}
`*.cleverapps.io` certificate is only valid for the first sub-domain level, it won't work with a domain like `blog.mycompany.cleverapps.io`.
{{< /callout >}}

## Using Personal Domain Names

You can point your domain name to Clever Cloud either with a CNAME record or with A records.

**The use of a CNAME record is highly recommended.**

With a CNAME record, your DNS configuration is always up-to-date.
Using A records will require you to keep the DNS configuration up-to-date manually.

Domain names linked to Clever Cloud applications are monitored, so we will send you an email if your DNS configuration is obsolete or incorrect.

We also support wildcard personal domain names, to do so use the standard pattern to describe it: `*.example.com`

### Your Application Runs in the Europe/Paris ('PAR') Zone

Provide the following to your registrar:

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.par.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 185.42.117.108`<br>`@ 10800 IN A 185.42.117.109`<br>`@ 10800 IN A 46.252.181.103`<br>`@ 10800 IN A 46.252.181.104`<br>`@ 10800 IN A 91.208.207.214`<br>`@ 10800 IN A 91.208.207.215`<br>`@ 10800 IN A 91.208.207.216`<br>`@ 10800 IN A 91.208.207.217`<br>`@ 10800 IN A 91.208.207.218`  |

### Your Application Runs in the Europe/Paris onto Scaleway ('SCW') Zone

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.scw.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 212.129.27.239`<br>`@ 10800 IN A 212.83.186.147`<br>`@ 10800 IN A 212.83.186.216`<br>`@ 10800 IN A 212.129.27.183` |

### Your Application Runs in the Europe/Roubaix ('RBX') Zone

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.rbx.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 87.98.180.173`<br>`@ 10800 IN A 87.98.182.176`<br>`@ 10800 IN A 87.98.180.181`<br>`@ 10800 IN A 87.98.182.136` |

### Your Application Runs in the Europe/Roubaix HDS ('RBXHDS') Zone

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.rbxhds.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 135.125.16.47`<br>`@ 10800 IN A 135.125.16.49` |

### Your Application Runs in the Europe/Warsaw ('WSW') Zone

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.wsw.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 145.239.17.127`<br>`@ 10800 IN A 145.239.17.192` |

### Your Application Runs in the Europe/Gravelines ('GRAHDS') Zone

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.grahds.clever-cloud.com.` |
| A<br>Only if CNAME is not available | @ 10800 IN A 188.165.58.196<br>@ 10800 IN A 188.165.58.200 |

### Your Application Runs in the North-America/Montreal ('MTL') Zone

Provide the following to your registrar:

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.mtl.clever-cloud.com.` |
| A<br>Only if CNAME is not available | @ 10800 IN A 149.56.147.232<br>@ 10800 IN A 149.56.126.234 |

### Your Application Runs in the Asia/Singapore ('SGP') Zone

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.sgp.clever-cloud.com.` |
| A<br>Only if CNAME is not available | @ 10800 IN A 51.79.197.159<br>@ 10800 IN A 51.79.197.160 |

### Your Application Runs in the Oceania/Sydney ('SYD') Zone

| Record Type                                   | Value                                                                             |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| CNAME<br>Recommended</span></sub></sup> | `{yoursubdomain} 10800 IN CNAME domain.syd.clever-cloud.com.`                   |
| A<br>Only if CNAME is not available                         | Two records: <br> `@ 10800 IN A 139.99.253.215` <br> `@ 10800 IN A 139.99.253.237` |

### Your Application Runs in the Jeddah ('JED') Zone

| Record Type         | Value                                                        |
|---------------------|--------------------------------------------------------------|
| CNAME               | `{yoursubdomain} 10800 IN CNAME domain.jed.clever-cloud.com.` |
| A<br>Only if CNAME is not available | Two records: <br> `@ 10800 IN A 158.101.226.110` <br> `@ 10800 IN A 150.230.50.217` |

{{< callout type="warning" >}}
You cannot use a CNAME  on a top-level domain, or on a subdomain which already has DNS records.
{{< /callout >}}

If you want to make your application available from a domain name which does not support CNAME records (eg `example.com` in addition to `www.example.com`), check if your registrar provides a web redirection service. This way, you only have to make `www.example.com` point to Clever Cloud. Please note that web redirection provided by registrars only work over HTTP.

Remember that DNS changes may take time to propagate (usually a few hours, sometimes up to a day or more). It depends on the TTL setting of your DNS configuration. For faster changes, you can lower the TTL value in advance, and rise it again afterwards.

{{< callout type="info" >}}
`*.example.com` will match e.g. `blog.example.com` or `www.example.com`. But for the raw domain `example.com`, you will have to add both `*.example.com` and `example.com` to your application.
{{< /callout >}}

### Contextual Example

| Domain Name Use Case        | CNAME config                                    | Record A config                                                | Web redirections                            |
|-----------------------------|-------------------------------------------------|-----------------------------------------------------------------|--------------------------------------------|
| `www.example.com` <br> `example.com` | Point `www.example.com` to `domain.par/mtl.clever-cloud.com.` | No A record needed                                            | Redirect `example.com` to `www.example.com` |
| `www.example.com`           | Point `www.example.com` to `domain.par/mtl.clever-cloud.com.` | No A record needed                                            | No redirect needed                          |
| `example.com`               | No CNAME record needed                           | Point `example.com` to the two IP addresses of the selected region | No redirect needed                          |

## Prefix routing

Requests are routed to applications based on the domain name, but you can also route based
on a path prefix.

For instance, you can bind `example.com` to an app, and `example.com/api` to another one.
All the HTTP requests on `example.com` where the path starts with `/api` will be routed to
the second app. The other requests will be routed to the first app.
You can add a path after every domain name you bind in the console (or with [clever tools]({{< ref "/doc/CLI" >}})).

Note that your prefix-routed application **needs** to have a `/prefix` route.

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

### Prefix routing for static sites

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
