---
title: Configuration provider
shortdesc: Share configuration between apps
tags:
- addons
keywords:
- configuration
- environment variables
---

Expose configuration to your applications (via environment variables).
If you have multiple applications which need the same configuration items
(for instance credentials for an external service), you can create an
addon dedicated to expose configuration to these applications.

In addition to not copying configuration in each application, every modification
of your environment variables triggers automatic deployment of the linked applications.

## Create the addon

Click on "Add an add-on", then choose "Configuration provider" and select the applications
you want to link. On the dashboard, click on "edit" and input the environment variables.
The syntax is `NAME=value`, like in the "expert mode" of the environment variables panel of any application.
Once you click "Save", all the linked applications will be restarted.

## Pricing

This add-on is completely free. No fee will be invoiced to you while using this kind of add-on.
