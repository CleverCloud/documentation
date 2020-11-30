---
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
---

## What is a Scaler?

A <dfn id="def-scaler">scaler</dfn> is an individual instance hosting your app. You can attribute one or more Scalers to your apps. Scalers come in many sizes based on each language requirements from Pico to XL.

Each [scaler](#def-scaler) is given a fixed set of resources.
When enabling auto-scalability, you have to set a minimum and a maximum of active [scalers](#def-scaler) in your apps settings. This way you can precisely control your monthly fee.

## What languages and frameworks are supported by Clever Cloud?

Currently Clever Cloud supports:

* Java (Play Framework 1 & 2, Maven, War files… )
* Node.js
* PHP ([see frameworks and CMS]({{< ref "deploy/application/php/tutorials/" >}}))
* Python (Django)
* Ruby
* Go
* Haskell
* Scala
* Rust
* Docker

## How many applications can I create with Clever Cloud?

As many as you want. We've not set a limited number of apps by developer.

## How to setup domain names I own?

You can bind custom domain names to your applications. Please have a look at [Custom Domain Names]({{< ref "administrate/domain-names.md" >}}).

## How can I disable one of my existing applications?

Log in with your account to [console.clever-cloud.com](https://console.clever-cloud.com), and select the appropriate organization and app in the left column. Then click on the application name and select **Overview**. Click on the **Stop** button to stop your app.

## What type of content is allowed on Clever Cloud?

Please refer to our Terms and Conditions, article 6, *Obligations and responsibilities of the client*.

## How do I add or remove members in my organizations?

Log in with your account to [console.clever-cloud.com](https://console.clever-cloud.com), and select the appropriate organization in the left panel. Then click on **Members** in the mid pane. You'll see a list of the organization's members. If your are an admin, you can revoke or grant permissions.

## How do I report an application that is in violation of your Terms and Conditions?

To report an application that is in violation of Clever Cloud's Terms and Conditions, please contact us at <abuse@clever-cloud.com>.

We will investigate and contact the application's owner over the violation if needed.

## Does Clever Cloud support TLS/SSL (HTTPS)?

Absolutely! For testing purposes, `cleverapps.io` domains support TLS out of the box. For custom SSL certificates, you can either order one from us or use an existing one.
Have a look at [installing SSL certificates]({{< ref "administrate/ssl.md" >}}), and feel free to contact us at <contact@clever-cloud.com> if you have questions.

## I'd like to have two applications available on the same domain name

Please refer to [prefix routing]({{< ref "administrate/domain-names.md#prefix-routing" >}}) to learn how to have two applications share a domain name.

## How do I define cron jobs for my application?

See [Cron Configuration File]({{< ref "administrate/cron.md" >}}) for more information.

## How to know if a user comes from a secure connection?

All connections are handled by load-balancers ahead of your applications and forwarded in plain http, you cannot rely on the server port to know the scheme used by the user.

Instead, you can use the `X-Forwarded-Proto` HTTP header to get the information, it is set to either '*http*' or '*https*'.

{{< alert "warning" "Note for Play Framework! 1.2.x users" >}}
    In order to use `request.secure` instead of using the header, you must add `XForwardedSupport=all` in your *application.conf*.
{{< /alert >}}

{{< alert "warning" "Note for Play Framework! 2.3+ users" >}}
    In order to use `request.secure` instead of accessing the header, you must add `trustxforwarded=true` in your *application.conf*.
{{< /alert >}}


## PHP: `$_SERVER` auth variables are always empty, how do I make this work?

It's explained [here]({{< ref "deploy/application/php/php-apps.md#using-http-authentication" >}}).

## How to get the user's IP address?

All connections are handled by load-balancers ahead of your applications
and forwarded in plain http.

So if you get the `REMOTE_ADDR` or `Client-IP` header, you will only
get the IP of the front load balancer that forwarded the user request.

Instead of these headers you need to use the `X-Forwarded-For` HTTP
header, which is set by our load balancer to the client's address. Please
remember that it is a list, containing the address of each proxy the request
has been through, if the said proxy has modified the `X-Forwarded-For`
header: [Read the Wikipedia page for more informations](https://en.wikipedia.org/wiki/X-Forwarded-For)

## When my application runs on multiple instances, how can I differentiate them?

If your application needs to differentiate all the running nodes internally,
you can use the `INSTANCE_NUMBER` environment variable.

For example, if 3 instances are running for your application, this environment variable will
contain `0` on the first, `1` on the second and `2` on the third.

## I need a private ssh key to fetch my private dependencies. How do I do that?

If your company manages its own artifacts in a private repository (like, you can only
access them via git+ssh or sftp), and you need a private key to connect to the server, you
can commit them in your application's Clever Cloud repository and then add a
`clevercloud/ssh.json` file.

The ssh.json file is documented [here]({{< ref "reference/common-configuration.md#private-ssh-key" >}}).

## I get a `Unsupported major.minor version` error. How can I fix it?

If you get this error on a Java (or any JVM language) application, it means that your application requires a specific version of Java.
By default, Java 8 is used; but you can change it. Please head [over here]({{< ref "deploy/application/java/java-gradle.md#available-java-versions" >}})
for more information.

## I want SSH access to my server

Clever Cloud does not give you access to a server or a VPS, it makes your application run. Each instance is started and configured automatically, and can be stopped at any moment. If however, you still need SSH access for debugging purposes, please have a look at [SSH access]({{< ref "reference/clever-tools/ssh-access.md" >}}), but keep in mind that changes made on an instance are not persistent across deployments.

## I want to user Clever Cloud on my own premises, is that possible?

Yes, since 2016 Clever Cloud is packaged for private datacenter. This offer called "Clever Cloud On Premises" is avaialble upon request: you can send a mail to <sales@clever-cloud.com> or visit [https://www.clever-cloud.com/on-premises](https://www.clever-cloud.com/on-premises) for more infos.

## Where are my applications and add-ons located?

Applications and add-ons are located in either *Paris, France* or *Montreal,
Canada*. You can choose where you want it to be when you create an application
and a Clever Cloud add-on.

Clever Cloud is based in Nantes, France.

## I want to run Kubernetes on top of Clever CLoud, is that possible?

It's currently not possible to use Kubernetes on our platform. It is however on our Roadmap.

## How to setup a firewall on Clever Cloud?

Specific firewall rules can be enabled on demand to the support or in case of attack.

## Can I `scp` something in a VM

You cannot `scp` something to the VM, you can however easily `scp` something from the VM to the outside.

## I need to convert something to PDF with `wkhtmltopdf`

Sadly `wkhtmltopdf`needs an X server to run, which is not available on our image. You should use `chromium headless` instead.
