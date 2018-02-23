---
title: Service Dependencies
position: 6
shortdesc: Materialize the logical dependencies between your applications with service dependencies
tags:
- dependencies
keywords:
- application
- configuration
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

<figure class="cc-content-img" style="width:355px">
  ><img src="/doc/assets/images/service-dependencies-example.png" data-action="zoom">
  <figcaption>Service dependencies</figcaption>
</figure>

To link an application to another, go to the "Service Dependencies" tab and
add the applications you depend on.

## Exposed configuration

Each application can expose configuration to be used by other applications.
For instance an API can expose its URL and credentials to access it. The
exposed configuration will be injected in the dependent applications'
environment.

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Note:</h4>
  </div>
  <div class="panel-body">
    The configuration exposed by an application is available in the
    environment variables of the <i>dependent</i> applications, but not in
    the environment of the application itself.
  </div>
</div>

### Redeploy on configuration update

When an application updates its exposed configuration, all applications
depending on it are automatically redeployed.

<figure class="cc-content-img" style="width:100%">
  <img src="/doc/assets/images/service-dependencies-config-update.png" data-action="zoom">
  <figcaption>Automatic redeployment</figcaption>
</figure>

