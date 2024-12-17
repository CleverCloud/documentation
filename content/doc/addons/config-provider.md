---
type: docs
title: Configuration provider
shortdesc: Share configuration between apps
tags:
- addons
keywords:
- configuration
- environment variables
aliases:
- /doc/deploy/addon/config-provider
type: docs
---

The configuration provider add-on helps you to create groups of environment variables that you can share with multiple applications.

## Example

Let's take an example with 2 Node.js applications exposing some REST APIs: `shipping-api` and `payment-api`.

The `shipping-api` application needs the following environment variables:

* `PULSAR_TOPIC=order`
* `USER_API_HOST=https://user.example.com/api`
* `ENABLE_PARTNERS=true`

The `payment-api` application needs the following environment variables:

* `PULSAR_TOPIC=order`
* `USER_API_HOST=https://user.example.com/api`
* `ENABLE_SEPA=false`

![Two Node.js applications with their own environment variables](/images/doc/schema-config-provider-01.svg "Two Node.js applications with their own environment variables")

As you can see, we had to define `PULSAR_TOPIC` and `USER_API_HOST` in both applications with the same value.
If we ever need to change these values, we'll have to apply the updates in both apps and restart them.

NOTE: This is a simple example, but we could have more than just 2 microservices and more than just 2 common variables.

To simplify this process, we will create a configuration provider add-on.
It will allow us to define those common variables in one place and inject them in our 2 applications.

![Two Node.js applications with their own environment variables](/images/doc/schema-config-provider-02.svg "Two Node.js applications with their own environment variables")

Think of a configuration provider as a way to group a set of environment variables and share them with any application.

![One application overriding the environment variable value for PULSAR_TOPIC](/images/doc/schema-config-provider-03.svg "One application overriding the environment variable value for PULSAR_TOPIC")

If a variable is defined in a configuration provider **and** also in the application, the value defined in the application wins.

## How to create a config provider

In the console, go to the organisation where you have your applications.

1. Click on **Create** and then on **an add-on**
2. You will see a list of add-ons, select **Configuration provider**
3. Select the first plan and click on **Next**
4. Toggle the **Link** for each application you need and then on **Next**
5. Define a name and click on **Next**

Once you have your configuration provider, you can set the variables in the form.
You can find out more about rules and format in [this page]({{< ref "doc/develop/env-variables.md#environment-variables-rules-and-formats" >}}).

{{< callout type="info" >}}
At any point, you can link/unlink an application from the configuration provider by going to the app's _"Service dependencies"_ page.
{{< /callout >}}

## Details and behaviour

* As with any other add-on, you can only link a configuration provider to applications that are in the same organisation.
* Variables defined directly in the application override the ones injected from the configuration provider.
* When you update the variables of a configuration provider, all applications linked to it will be automatically restarted.
* You can create multiple configuration providers in your organisation and link them to different applications.

## Pricing

This add-on is completely free.
No fee will be invoiced to you while using this kind of add-on.
