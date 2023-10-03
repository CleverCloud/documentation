---
type: docs
title: Service Dependencies
position: 6
shortdesc: Materialize the logical dependencies between your applications with service dependencies
tags:
- administrate
keywords:
- application
- dependencies
- services
- configuration
type: docs
---

On Clever Cloud, each application depends on one or more backing addons. Each
addon exposes configuration, which allows the user to choose which addon link
to an application.

In a micro services architecture, backing services can be addons or other
applications. Clever Cloud allows you to declare the dependencies between
applications in the same way you can declare a dependency from an application
to an addon.

Clever Cloud allows to declare the topology of your micro services graph by
letting you link applications in the same way you can link addons.

{{< image "/images/service-dependencies-example.png" "Service dependencies" "width:355px" >}}

To link an application to another, go to the "Service Dependencies" tab and
add the applications you depend on.

## Exposed configuration

Each application can expose configuration to be used by other applications.
For instance an API can expose its URL and credentials to access it. The
exposed configuration will be injected in the dependent applications'
environment.

{{< callout type="warning" >}}
    The configuration exposed by an application is available in the
    environment variables of the <i>dependent</i> applications, but not in
    the environment of the application itself.
{{< /callout >}}


### Redeploy on configuration update

When an application updates its exposed configuration, all applications
depending on it are automatically redeployed.

{{< image "/images/service-dependencies-config-update.png" "Automatic redeployment" "width:100%" >}}
