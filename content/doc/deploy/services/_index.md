---
type: docs
linkTitle: Services
title: Services
description: Add identity, analytics, business intelligence, transactional email, API management, and CI/CD services next to your applications on Clever Cloud, then create and delete them
keywords:
- services
- managed services
- identity
- analytics
- automation
aliases:
- /doc/services
---

These services cover what your team needs around its own code, without installing it yourself. Clever Cloud or a partner operates them: Keycloak, Matomo, Metabase, and Otoroshi Gateway run on applications and add-ons of your organisation, which you see and resize like your own.

## Identity and API management

Keycloak signs your users in, and gives them single sign-on across all your applications. Otoroshi Gateway routes, authenticates, and rate limits the calls to your APIs, and acts as a gateway to LLM providers.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/services/keycloak" title="Keycloak" subtitle="Identity and access management with single sign-on" icon="simple:keycloak" >}}
  {{< card link="/developers/doc/deploy/services/otoroshi" title="Otoroshi Gateway" subtitle="API gateway with preconfigured plugins, including an LLM gateway" icon="endpoints" >}}
{{< /cards >}}

## Analytics and business intelligence

Matomo measures the audience of your websites while you keep its data. Metabase turns the data of your databases into charts and dashboards.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/services/matomo" title="Matomo" subtitle="Privacy-focused web analytics platform" icon="simple:matomo" >}}
  {{< card link="/developers/doc/deploy/services/metabase" title="Metabase" subtitle="Business intelligence and data visualization platform" icon="simple:metabase" >}}
{{< /cards >}}

## Code hosting and CI/CD

Heptapod Cloud hosts your Git and Mercurial repositories: it isn't an add-on, and you [open it](/doc/deploy/services/heptapod/#accessing-heptapod-cloud) with your Clever Cloud account. Jenkins runs your pipelines on runners that Clever Cloud starts on demand.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/services/heptapod" title="Heptapod" subtitle="Fork of GitLab Community Edition with Mercurial support" icon="git" >}}
  {{< card link="/developers/doc/deploy/services/jenkins" title="Jenkins" subtitle="Open source automation server" icon="simple:jenkins" >}}
{{< /cards >}}

## Email and configuration

MailPace sends the transactional emails of your applications. A configuration provider shares environment variables between several applications.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/services/mailpace" title="MailPace" subtitle="Fast and reliable transactional email" icon="mail" >}}
  {{< card link="/developers/doc/deploy/services/config-provider" title="Config Provider" subtitle="Manage, import and inject configuration and credentials" icon="creds" >}}
{{< /cards >}}

## Create a service

In the [Console](https://console.clever-cloud.com/), select **Create** at the top of the sidebar, then **Add-on**, and pick a service, except Heptapod. Choose its plan, region, and name. With [Clever Tools](/doc/tools/cli/addons/), `clever addon providers` lists the services, and `clever addon providers show keycloak` the plans of one. Then create it:

```bash
clever addon create keycloak my-keycloak
```

The page of each service details its options, and what to configure next. Clever Tools also manages Keycloak, Matomo, Metabase, and Otoroshi Gateway with their own [operator commands](/doc/tools/cli/operators/). A service that provides environment variables, such as MailPace or a configuration provider, gives them to the applications you [link it to](/doc/manage/service-dependencies/#link-a-service): restart them to read the variables.

## Delete a service

Select **Delete the add-on** in the danger zone of the **Dashboard** of the add-on, or **Remove add-on** in its **Information** menu. With Clever Tools:

```bash
clever addon delete my-keycloak
```

Deleting Keycloak, Matomo, Metabase, or Otoroshi Gateway also deletes the applications and add-ons it created: export your data first.
