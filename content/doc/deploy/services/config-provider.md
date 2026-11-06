---
type: docs
linkTitle: Configuration provider
title: Share environment variables between applications
description: Store environment variables once in a configuration provider add-on, link it to several applications of your organisation, and update them all from one place
keywords:
- configuration provider
- config provider
- shared environment variables
- configuration
- addon
- microservices
aliases:
- /addons/config-provider
- /deploy/addon/config-provider
- /doc/addons/config-provider
- /doc/deploy/addon/config-provider
- /doc/deploy/services/configuration-provider
- /doc/services/config-provider
- /doc/services/configuration-provider
---

A configuration provider is an add-on that holds environment variables for several applications. Instead of setting the same variables in each application, you set them once in the configuration provider, then [link it](/doc/manage/service-dependencies/) to the applications that need them. When you update a variable, the linked applications receive the new value. This add-on is free.

For example, a `shipping-api` and a `payment-api` application both need `PULSAR_TOPIC=order` and `USER_API_HOST=https://user.example.com/api`. A configuration provider holds these two variables, and each application keeps its own variables, such as `ENABLE_PARTNERS` or `ENABLE_SEPA`.

A configuration provider holds variables that don't belong to a single application. To share the URL or the credentials of an application with the applications that call it, use its [exposed configuration](/doc/manage/service-dependencies/#exposed-configuration) instead.

## Create a configuration provider

In the [Console](https://console.clever-cloud.com), open the organisation of your applications, then:

1. Click **Create**, then **Add-on**, and select **Configuration provider**
2. Select the plan, then click **Next**
3. If the organisation has applications, toggle **Link** for each one that needs the variables, then click **Next**
4. Enter a name, select a region, then click **Next**

The Console then opens the **Dashboard** of the add-on. Set the variables in its **Variables** form, then click **Update changes**. The variables follow the same [rules and formats](/doc/develop/common-configuration/environment-variables/#environment-variables-rules-and-formats) as the ones of an application.

With [Clever Tools](/doc/tools/cli/addons/#config-provider), create it in the organisation of your applications, replacing `my-team` with its name or ID, then set its variables:

```bash
clever addon create config-provider shared-config --org my-team
clever config-provider set shared-config PULSAR_TOPIC order
clever config-provider set shared-config USER_API_HOST https://user.example.com/api
```

Then, from a folder linked to each application, link it and restart the application:

```bash
clever service link-addon shared-config
clever restart
```

An application receives the variables of a configuration provider on its next deployment. Adding or removing the link doesn't redeploy the application: restart it to apply the change. To link or unlink a configuration provider later, open the **Service dependencies** tab of the application.

## Update the variables

Each time you save the variables of a configuration provider, Clever Cloud redeploys the applications linked to it, except the ones you stopped. Stopped applications receive the new values when they start.

Each `clever config-provider set`, `rm`, or `import` command saves the variables, even when their values don't change, and redeploys these applications. To change several variables with one redeployment, save them at once in the Console, or with `clever config-provider import`. It replaces all the variables of the configuration provider, so write the complete list, one `NAME=value` entry per line:

```bash
cat > shared.env <<'EOF'
PULSAR_TOPIC=order
USER_API_HOST=https://user.example.com/api
EOF
clever config-provider import shared-config < shared.env
```

## Override a shared value

A variable set in the application itself takes precedence over the same variable in a configuration provider. For example, set `PULSAR_TOPIC=payment` in `payment-api` to override `order` for this application only. The [order of precedence](/doc/manage/service-dependencies/#conflicting-variable-names) lists all the sources of variables.

When you move variables from your applications to a configuration provider, remove the copies you want to share from each application, or they keep overriding the shared values. Then redeploy each application, as for any change to its own variables.

You can create several configuration providers, for example one per environment or per team, and link an application to more than one. Don't define the same variable in two configuration providers linked to the same application: the value it receives isn't defined.
