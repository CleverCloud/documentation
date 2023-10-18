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

You can link one or several domain names in the console.

Add it in the application configuration: in the console, click on your **application name** in the first panel, then choose **domain names**. You'll have to choose to add a custom domain name or use a sub-domain under <code>*.cleverapps.io</code>.

## Using a **\*.cleverapps.io** free domain, with built-in SSL

{{< callout type="warning" >}}
  `*.cleverapps.io` domains are given for development and tests purpose. They point to
  specific reverse proxies and have the following weaknesses:
  - .io TLD is not a stable one
  - since we offer the domain, the probability that people will abuse it is high. Thus, we
    do not garantee the same QoS on the cleverapps reverse proxies.
{{< /callout >}}

In the console, in the domain name sub menu of your application, there is a default entry configured by default for every new app: <code>yourAppID.cleverapps.io</code>, which can be removed.

In your application's domain section, just enter <code>example.cleverapps.io</code>. You have to choose a unique one. Trusted SSL is available on every sub-domain.

{{< callout type="warning" >}}
  `*.cleverapps.io` certificate is only valid for the first sub-domain level, it won't work with a domain like `blog.mycompany.cleverapps.io`.
{{< /callout >}}

## Using Personal Domain Names

You can point your domain name to Clever Cloud either with a CNAME record or with A records.

**The use of a CNAME record is highly recommended.**

With a CNAME record, your DNS configuration is always up-to-date.
Using A records will require you to keep the DNS configuration up-to-date manually.

Domain names linked to Clever Cloud applications are monitored, so we will send you an email if your DNS configuration is obsolete or incorrect.

We also support wildcard personal domain names, to do so use the standard pattern to describe it: <code>*.example.com</code>


### Your Application Runs in the Europe/Paris ('PAR') Zone

Provide the following to your registrar:

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.par.clever-cloud.com. </code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Four records:<br>
    <code>@ 10800 IN A 185.42.117.108</code><br>
    <code>@ 10800 IN A 185.42.117.109</code><br>
    <code>@ 10800 IN A 46.252.181.103</code><br>
    <code>@ 10800 IN A 46.252.181.104</code>
    </td>
  </tr>
</table>


### Your Application Runs in the Europe/Paris onto Scaleway ('SCW') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.scw.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Four records:<br>
    <code>@ 10800 IN A 212.129.27.239</code><br>
    <code>@ 10800 IN A 212.83.186.147</code>
    <code>@ 10800 IN A 212.83.186.216</code>
    <code>@ 10800 IN A 212.129.27.183</code>
    </td>
  </tr>
</table>

### Your Application Runs in the Europe/Roubaix ('RBX') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.rbx.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Four records:<br>
    <code>@ 10800 IN A 87.98.180.173</code><br>
    <code>@ 10800 IN A 87.98.182.176</code><br>
    <code>@ 10800 IN A 87.98.180.181</code><br>
    <code>@ 10800 IN A 87.98.182.136</code>
    </td>
  </tr>
</table>

### Your Application Runs in the Europe/Roubaix HDS ('RBXHDS') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.rbxhds.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 135.125.16.47</code><br>
    <code>@ 10800 IN A 135.125.16.49</code>
    </td>
  </tr>
</table>

### Your Application Runs in the Europe/Warsaw ('WSW') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.wsw.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 145.239.17.127</code><br>
    <code>@ 10800 IN A 145.239.17.192</code>
    </td>
  </tr>
</table>

### Your Application Runs in the Europe/Gravelines ('GRAHDS') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.grahds.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 188.165.58.196</code><br>
    <code>@ 10800 IN A 188.165.58.200</code>
    </td>
  </tr>
</table>

### Your Application Runs in the North-America/Montreal ('MTL') Zone

Provide the following to your registrar:

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.mtl.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 149.56.147.232</code><br>
    <code>@ 10800 IN A 149.56.126.234</code><br>
    </td>
  </tr>
</table>

### Your Application Runs in the Asia/Singapore ('SGP') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.sgp.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 51.79.197.159</code><br>
    <code>@ 10800 IN A 51.79.197.160</code>
    </td>
  </tr>
</table>

### Your Application Runs in the Oceania/Sydney ('SYD') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.syd.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 139.99.253.215</code><br>
    <code>@ 10800 IN A 139.99.253.237</code>
    </td>
  </tr>
</table>

### Your Application Runs in the Jeddah ('JED') Zone

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Record Type</center></th>
    <th><center>Value</center></th>
  </tr>
  <tr>
    <td>CNAME <div><span class="label label-success">Recommended</span></div></td>
    <td>
    <code>{yoursubdomain} 10800 IN CNAME domain.jed.clever-cloud.com.</code>
    </td>
  </tr>
  <tr>
    <td>A<div><small>Only if CNAME is not available</small></div></td>
    <td>Two records:<br>
    <code>@ 10800 IN A 158.101.226.110</code><br>
    <code>@ 10800 IN A 150.230.50.217</code>
    </td>
  </tr>
</table>

{{< callout type="warning" >}}
    You cannot use a CNAME  on a top-level domain, or on a subdomain which already has DNS records.
{{< /callout >}}

If you want to make your application available from a domain name which does not support CNAME records (eg <code>example.com</code> in addition to <code>www.example.com</code>), check if your registrar provides a web redirection service. This way, you only have to make <code>www.example.com</code> point to Clever Cloud. Please note that web redirection provided by registrars only work over HTTP.

Remember that DNS changes may take time to propagate (usually a few hours, sometimes up to a day or more). It depends on the TTL setting of your DNS configuration. For faster changes, you can lower the TTL value in advance, and rise it again afterwards.

{{< callout type="info" >}}
    <div>
      <code>*.example.com</code> will match e.g. <code>blog.example.com</code> or <code>www.example.com</code>.
    </div>
    <div> But for the raw domain <code>example.com</code>, you will have to add both <code>*.example.com</code> and <code>example.com</code> to your application.</div>
{{< /callout >}}
<br>

### Contextual Example

<table class="table table-striped">
  <thead>
    <tr>
      <th>Domain Name Use Case</th> <th>CNAME config</th> <th>record A config</th> <th>Web redirections</th>
    </tr>
  </thead>
  <tboby>
    <tr>
      <td><code>www.example.com</code> <br> <code>example.com</code></td>
      <td> point <code>www.example.com</code> to <code>domain.par/mtl.clever-cloud.com.</code></td>
      <td>No A record needed</td>
      <td>Redirect <code>example.com</code> to <code>www.example.com</code> </td>
    </tr>
    <tr>
      <td><code>www.example.com</code></td>
      <td> point <code>www.example.com</code> to <code>domain.par/mtl.clever-cloud.com.</code></td>
      <td>No A record needed</td>
      <td>No redirect needed</td>
    </tr>
    <tr>
      <td><code>example.com<code></td>
      <td>No CNAME record needed</td>
      <td>point <code>example.com</code> to the two IP addresses of the selected region</td>
      <td>No redirect needed</td>
    </tr>
  </tboby>
</table>

## Prefix routing

Requests are routed to applications based on the domain name, but you can also route based
on a path prefix.

For instance, you can bind `example.com` to an app, and `example.com/api` to another one.
All the HTTP requests on `example.com` where the path starts with `/api` will be routed to
the second app. The other requests will be routed to the first app.
You can add a path after every domain name you bind in the console (or with [clever tools]({{< ref "/doc/CLI" >}})).

Note that your prefix-routed application **needs** to have a `/prefix` route.

This will work:

```
example.com        ->      myfirtapp-main-route

example.com/api    ->      mysecond-app-main-route/api
```

This will NOT work:

```
example.com        ->      myfirtapp-main-route     (works)

example.com/api    ->      mysecondapp-main-route   (404 response from mysecondapp)
```

### Prefix routing for static sites

In the case of static files, you usually understand routes as paths in a file tree.

This will work:

```
example.com/api    ->     my-static-site/api/index.php
```

This will NOT work:

```
example.com/api    ->     my-static-site/index.php
```

## Gandi CNAME configuration

Here is <a href="https://blog.clever-cloud.com/blog/features/2019/03/05/gandi-domain-on-clever-cloud/" target="_blank">an article that demonstrates a simple setup for Gandi CNAMEs</a>.
