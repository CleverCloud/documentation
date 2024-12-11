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

aliases:
- /doc/admin-console/service-dependencies
---

On Clever Cloud, each application depends on one or more backing add-ons. Each
add-on exposes configuration, which allows the user to choose which add-on link
to an application.

In a micro services architecture, backing services can be add-ons or other
applications. Clever Cloud allows you to declare the dependencies between
applications in the same way you can declare a dependency from an application
to an add-on.

Clever Cloud allows to declare the topology of your micro services graph by
letting you link applications in the same way you can link add-ons.

![Service dependencies](/images/doc/service-dependencies-example.png "Service dependencies")

To link an application to another, go to the "Service Dependencies" tab and
add the applications you depend on.

## Exposed configuration

Each application can expose configuration to be used by other applications.
For instance an API can expose its URL and credentials to access it. The
exposed configuration will be injected in the dependent applications'
environment.

{{< callout type="warning" >}}
The configuration exposed by an application is available in the environment variables of the **dependent** applications, but not in the environment of the application itself.
{{< /callout >}}

### Redeploy on configuration update

When an application updates its exposed configuration, all applications
depending on it are automatically redeployed.

![Automatic redeployment](/images/doc/service-dependencies-config-update.png "Automatic redeployment")
