---
type: docs
title: FAQ
position: 3
tags:
- help
keywords:
- faq
- scaler
- languages
- kubernetes
- firewall
- scp
- ssh
- on premises
- pdf
- timezone
type: docs
---

## What is a Scaler?

A _scaler_ is an individual instance hosting your app. You can attribute one or more scalers to your apps. scalers come in many sizes based on each language requirements from pico to XL.

A fixed set of resources supports each scaler.

When enabling auto-scalability, you have to set a minimum and a maximum of active scalers in your apps settings. This way you can precisely control your monthly fee.

{{< callout type="warning" >}}
  Nano and pico instances operate with **reduced CPU priority** on the host system. As a result, during periods of high load on the hypervisor, these instances may experience performance degradation (since they yield processing power to higher-priority workloads).
{{< /callout >}}

## What languages and frameworks are supported by Clever Cloud?
Currently Clever Cloud supports:

* Java (Play Framework 1 & 2, Maven, War files… )
* Node.js
* PHP ([see frameworks and CMS]({{< ref "/guides" >}}))
* Python (Django)
* Ruby
* Go
* Haskell
* Scala
* Rust
* Docker

## How many applications can I create?
As many as you want. We've not set a limited number of apps by developer.

## How to setup domain names I own?

You can bind custom domain names to your applications. Please have a look at [Custom Domain Names](../../administrate/domain-names).

## How can I disable one of my existing applications?

Log in with your account to [console.clever-cloud.com](https://console.clever-cloud.com), and select the appropriate organisation and app in the left column. Then click on the application name and select **Overview**. Click on the **Stop** button to stop your app.

## What type of content can I deploy?

Please refer to the Acceptable Use Policy, article 2, [_Reasonable use of the Platform_](https://www.clever-cloud.com/acceptable-use-policy/).

## How do I add or remove members in my organisations?

Log in with your account to [console.clever-cloud.com](https://console.clever-cloud.com), and select the appropriate organisation in the left panel. Then click on **Members** in the mid pane. You'll see a list of the organisation's members. If your are an admin, you can revoke or grant permissions.

## How do I report an application that infringes your Terms and Conditions?

To report an application that infringes Clever Cloud's Terms and Conditions, please contact the legal team at <abuse@clever-cloud.com>.

We will investigate and contact the application's owner over the violation if needed.

## Does Clever Cloud support TLS/SSL (HTTPS)?

Yes. For testing purposes, `cleverapps.io` domains support TLS out of the box. For custom SSL certificates, you can either generate one automatically with Let's Encrypt while adding a domain, or [use an existing one]{{< ref "doc/administrate/ssl/#uploading-my-own-certificates" >}}).
Have a look at [installing TLS certificates](/developers/doc/administrate/ssl), and feel free to contact the support team in the [Ticket Center](https://console.clever-cloud.com/ticket-center-choice) if you have questions.

## What are the supported ciphers ?

As this information can change over time with security updates, here's the nmap command to look up SSL/TLS ciphers on a Clever Cloud configured domain:

```shell
nmap --script ssl-enum-ciphers -p 443 example.com
```

## I'd like to have two applications available on the same domain name

Refer to [prefix routing]({{< ref "doc/administrate/domain-names/#prefix-routing" >}}) to learn how to have two applications share a domain name.

## How do I define cron jobs for my application?

See [Cron Configuration File](../../administrate/cron) for more information.

## How to know if a user comes from a secure connection?

Load-balancers handles all connections ahead of your applications and forward them in plain HTTP, you can't rely on the server port to know the scheme used by the user.

Instead, you can use the `X-Forwarded-Proto` HTTP header to get the information, it's set to either '_http_' or '_https_'.

{{< callout type="info" >}}
In order to use `request.secure` instead of using the header, you must add `XForwardedSupport=all` in your `application.conf`.
{{< /callout >}}

{{< callout type="warning" >}}
In order to use `request.secure` instead of accessing the header, you must add `trustxforwarded=true` in your `application.conf`.
{{< /callout >}}

## PHP: `$_SERVER` auth variables are always empty, how do I make this work?

- [Lean more about the $_SERVER variable on Clever Cloud](../../applications/php/#using-http-authentication)

## How to get the user's IP address?

Load-balancers ahead of your applications handle all connections and forward them in plain HTTP.
So if you get the `REMOTE_ADDR` or `Client-IP` header, you get only the IP of the load balancer that forwarded the user request.

To get the original client's IP address, use the `X-Forwarded-For` HTTP header. The load balancer automatically adds this header to each request.

The `X-Forwarded-For` header contains a comma-separated list of IP addresses. The first address in this list is your end user's original IP address. Any subsequent addresses represent the proxies that the request passed through before reaching your application.
[Read the Wikipedia page for more details](https://en.wikipedia.org/wiki/X-Forwarded-For).

## How do I identify different instances of my application?

If your application needs to differentiate all the running nodes internally, you can use the `INSTANCE_NUMBER` environment variable.

For example, if 3 instances are running for your application, this environment variable will contain `0` on the first, `1` on the second and `2` on the third.

## I need a private ssh key to fetch my private dependencies. How do I do that?

If your company manages its own artifacts in a private repository (like, you can only
access them via git+ssh or sFTP), and you need a private key to connect to the server, you
can commit them in your application's Clever Cloud repository and then add a
`clevercloud/ssh.json` file.

- [Learn more about ssh.json](../../reference/common-configuration/#private-ssh-key)

## I get a `java.lang.UnsupportedClassVersionError: Unsupported major.minor version` error. How can I fix it?

If you get this error on a Java (or any JVM language) application, it means that your application was compiled with a newer Java version than the one used to run it.

As an example, if a Spring Boot application was compiled with Java `17` and run with Java `11`, the following error occurs:

```bash
java.lang.UnsupportedClassVersionError: org/springframework/boot/loader/JarLauncher has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0
```

By default, Java apps on Clever Cloud use Java `11`, but you can change it. Please head [over here]({{< ref "doc/applications/java/java-jar/#available-java-versions" >}} "Java versions") for more information.

For reference, the table below lists the class file version for each major Java version ([official doc](https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html)) :

| Java version | Class file version |
| ------------ | ------------------ |
| 7            | 51.0               |
| 8            | 52.0               |
| 11           | 55.0               |
| 17           | 61.0               |
| 21           | 65.0               |

## I want SSH access to my server

Clever Cloud does not give you access to a server or a VPS, it makes your application run. Each instance is started and configured automatically, and can be stopped at any moment.

If however, you still need SSH access for debugging purposes, please have a look at [SSH access](/developers/doc/cli/applications/deployment-lifecycle/#ssh), but keep in mind that changes made on an instance are not persistent across deployments.

## I want to user Clever Cloud on my own premises, is that possible?

Yes, since 2016 Clever Cloud is packaged for private data center. This offer called "Clever Cloud On Premises" is available upon request: you can send a mail to [sales@clever-cloud.com](mailto:sales@clever-cloud.com) or visit [https://www.clever-cloud.com/on-premises](https://www.clever-cloud.com/on-premises) for more info.

## Where are my applications and add-ons located?

Applications and add-ons are located in either _Paris, France_ or _Montreal, Canada_. You can choose where you want it to be when you create an application
and a Clever Cloud add-on.

Clever Cloud is based in Nantes, France.

## I want to run Kubernetes on top of Clever CLoud, is that possible?

It's currently not possible to use Kubernetes on our platform. It is however on our Roadmap.

## How to setup a firewall on Clever Cloud?

Specific firewall rules can be enabled on demand to the support or in case of attack.

## Can I `scp` something in a VM

You cannot `scp` something to the VM, you can however easily `scp` something from the VM to the outside.

## I need to convert something to PDF with `wkhtmltopdf`

`wkhtmltopdf` is available and fully functional but we deeply recommend to use `chromium headless` instead.

## What is the timezone used by my application/add-on?

All instances on Clever Cloud run on the UTC timezone. We recommend to handle all your dates in UTC internally, and only handle timezones when reading or displaying dates.

## I received an email saying "Add-on [my add-on] disk is nearly full". What do I do?

A full disk can cause your database to crash or become unresponsive.
Consider upgrading your add-on plan.
You might want to do one of the following:

### Remove data from your database

You can take a snapshot of your database and export the obsolete data to a cold storage.
Then you can remove records from your database, re-index your tables and try to perform a VACUUM operation if the database software allows it.

### Migrate your add-on to a bigger plan

… or to the same plan.

You can buy more disk space by migrating your add-on to a higher plan.
If a VACUUM operation needs more disk that there is remaining, migrating to the same plan cleans up the file on disk and regains space.

## Where are the backups stored?

Clever Cloud stores all backups on [Cellar](https://www.clever-cloud.com/product/cellar-object-storage/), a replicated object storage service with three copies distributed across datacenters in the PAR region to ensure durability. Even if one datacenter fails, your backups remain safe.

For custom configurations (for example, multiple retention policies), contact Support. To locate backups not visible in the Console, use [Clever Tools](https://github.com/CleverCloud/clever-tools) with: `clever database backups DATABASE-ID [--format, -F] FORMAT`.  Find more [documentation on restoring backups with the CLI](/developers/doc/cli/addons/#database-backups).


## I can't create my add-on

To create add-ons, you need to complete your account information, including your city and ZIP code.
For instance, you cannot create a Matomo add-on until you provide these details.

## I get unknown regular requests, is there a problem ?

The platform performs routine health checks to applications every 2 minutes. You may notice these periodic HTTP requests in your logs, with `X-Clevercloud-Monitoring` header. They're part of Clever Cloud's standard monitoring process.

## What is a DEV plan ?

DEV plan is a free-tier plan available for some databases, designed to let customers explore and test these products. They operate on shared clusters, which may result in variable performance; they also have no SLA guarantees.

Some features such as simultaneous connections numbers, functions… might be reduced or unavailable.

Support is not able to provide help in case of DEV plan.

