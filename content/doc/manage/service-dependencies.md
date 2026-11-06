---
type: docs
linkTitle: Service Dependencies
title: Link applications to add-ons and other applications
description: Link an application to add-ons and to other applications of its organisation to receive their environment variables, and publish the configuration of an application for the applications that depend on it
keywords:
- service dependencies
- exposed configuration
- published configuration
- linked add-ons
- linked applications
- environment variables
- microservices
aliases:
- /doc/admin-console/service-dependencies
- /doc/administrate/service-dependencies
- /doc/databases-and-services/add-service
- /doc/service-dependencies
- /doc/services-dependencies
---

The service dependencies of an application are the add-ons and the other applications it uses. When you link a service to an application, the application receives the environment variables this service provides:

| Linked service                                                    | Variables the application receives                                                |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| A database or another add-on                                      | Its connection details and credentials, listed in the add-on's information panel  |
| A [configuration provider](/doc/deploy/services/config-provider/) | The variables you store in it, to share them with several applications            |
| Another application                                               | The variables it publishes in its [exposed configuration](#exposed-configuration) |

You link a service from the application that uses it, and the service must belong to the same organisation.

## Link a service

In the [Console](https://console.clever-cloud.com), open the application that uses the service, then its **Service dependencies** tab. Select an add-on in **Link add-ons**, or an application in **Link applications**, then click **Add**. To remove a link, click the remove button next to the linked service: the service itself stays.

With [Clever Tools](/doc/tools/cli/service-dependencies/), from a folder linked to the application:

```bash
clever service link-addon orders-db
clever service link-app payments-api
clever service
```

Adding or removing a link doesn't redeploy the application: the variables change on its next deployment. Restart it to apply them:

```bash
clever restart
```

The **Environment variables** tab of the application lists its own variables, then the variables of each linked add-on and application.

## Exposed configuration

An application doesn't share its environment variables with the applications that depend on it. It shares only the variables you add to its exposed configuration, such as its URL or the credentials to call it.

For example, to let a `storefront` application call a `payments-api` application, open `payments-api` in the Console, then its **Exposed configuration** tab. Add `PAYMENTS_API_URL` with the value `https://payments-api.example.com`, then click **Update changes**. Then link `payments-api` to `storefront` from its **Service dependencies** tab, and restart `storefront`. With Clever Tools:

```bash
clever published-config set PAYMENTS_API_URL https://payments-api.example.com --app payments-api
clever service link-app payments-api --app storefront
clever restart --app storefront
```

Once restarted, `storefront` reads `PAYMENTS_API_URL` from its environment.

> [!NOTE] Not available in the application itself
> The exposed configuration of an application goes to the applications that depend on it, not to the application itself. Set the variables it needs in its own environment variables.

An application receives only the exposed configuration of the applications it links to. It doesn't receive the one of their own dependencies.

### Redeploy on configuration update

Each time you save the exposed configuration of an application, Clever Cloud redeploys the applications that depend on it, except the ones you stopped. Stopped applications receive the new values when they start.

Each `clever published-config set`, `rm`, or `import` command saves the exposed configuration, even when its values don't change. To change several variables with one redeployment, save them at once in the Console, or with `clever published-config import`, which replaces the whole exposed configuration.

## Conflicting variable names

When several sources define the same variable, the application receives one value, in this order of precedence:

1. The environment variables of the application itself
2. The exposed configuration of the linked applications
3. The variables of the linked add-ons, including configuration providers

To override a value of a linked service, set the same variable in the application. When two linked applications, or two linked add-ons, define the same variable, the value the application receives isn't defined. Give exposed variables a name specific to their application, such as `PAYMENTS_API_URL` rather than `API_URL`.
