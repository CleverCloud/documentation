---
title: Tips & Tricks
shortdesc: Discover some useful tips and tricks to improve your experience with Clever Cloud tools
tags:
- reference
- tips
- tricks
keywords:
- tips
- tricks
type: docs
draft: true
---

Clever Cloud is an easy-to-use platform, designed with developers in mind. Whether you're a beginner or a more experienced user, we try to fit your needs bringing you the best possible experience through our web Console, Clever Tools, API, SDK, integrations.

We like to pay attention to those small details, those features, that make Clever Cloud better to use, unique. Over the time, we've developed them but found out that most of our users or new team members don't know about them. This page exists to help spread the word.

## Web Console

Access Clever Cloud Console to manage your applications, add-ons, organizations and so on: https://console.clever-cloud.com

### Menu advanced filter

The left side menu is a powerful tool with a text field to filter your applications and add-ons. You can type the name of the items you want to find and see results matching your search instantly. But do you know that you can also use specific keywords? Here is the list:

| Keyword        | Description |
| -------        | ----------- |
| `is:addon`     | Filter add-ons |
| `is:app`       | Filter applications |
| `is:[addon]`   | Filter add-ons (for example, `is:kv`, `is:keycloak`, `is:postgresql`) |
| `is:[runtime]` | Filter by runtime name (for example, `is:node`, `is:php`, `is:static-apache`) |

### Environment variables are multi-line

When you edit an environment variable, in simple mode, you see a text input for each variable. But if you press the `Enter` key, the value splits into multiple lines. Thus, you can put the full content of a configuration file in it for example. Of course, you can do the same with expert and JSON modes, through Clever Tools or the API. Environment variables ARE multi-line.

- [Clever Cloud Environment variables reference](/doc/reference/reference-environment-variables)

### Validate new environment variables with ease

When you create a new environment variable in simple mode, add it pressing the `Add` button or the `CTRL+Enter` keys.

{{< callout type="info" >}}
  Don’t forget to press the `UPDATE CHANGES` button at the bottom before leaving the environment variables page
{{< /callout >}}

### Clever Logs come supercharged

The Console provides a powerful logs management interface for applications. You can filter by day, time, text, regular expression, instance per instance. You can apply color themes to it, strip ANSI codes, wrap lines, change date format, time zone, etc. Want to share them? Just select logs lines and copy them in clipboard through keyboard and/or mouse.

Logs are retained for 7 days, they're part of the Clever Cloud all-inclusive experience.

* [Learn more about Logs on Clever Cloud](/doc/administrate/log-management/)

### Universal link

If you need to access an application or an add-on knowing just its ID, use the `goto` link:

```
https://console.clever-cloud.com/goto/id
```

### Universal search

If you need to search an add-on, application, organization by its ID or its name, just press the `/` key and start typing.

### Keyboard shortcuts

When you look at an add-on or an application, press one of the following keys:

| Key | Description |
| --- | ----------- |
| `?` | Show keyboard shortcuts help |
| `a` | Jump to application activity |
| `d` | Jump to application domains |
| `e` | Jump to application environment variables |
| `i` | Jump to application / add-on information |
| `l` | Jump to application / add-on logs |
| `m` | Jump to Application metrics |
| `o` | Jump to application overview |
| `s` | Jump to application scalability |

### Launch applications as one-time tasks

One of our missions is to keep your applications and services up and running, providing logs, metrics, scaling features, and more. But sometimes, you need to launch an application to execute a one-time task. On Clever Cloud, there is an option for that.

Just define an application as a task in its `Information` panel or at creation with Clever Tools (`clever create --type TYPE --task "command to execute"`). The application will start, fetch its dependencies and build as usual, but then just execute the command and stop.

- [Learn more about Clever Tasks](/doc/develop/tasks/)

### Patch update or redeploy a database

When Clever Cloud release a new major/minor version of a database add-on, you can use the migration tool from the Console to upgrade it without downtime. It also allows to move the add-on to another zone. But sometimes, you just need the latest patch version or to redeploy your database. In such case, migrate it to the exact same version, plan, zone and launch the migration process.

- [Learn more about Clever Cloud database add-ons](/doc/addons/)
- [Learn more about Clever Cloud database migration](/doc/administrate/database-migration/)

## Clever Tools

[Installing our CLI](https://github.com/CleverCloud/clever-tools/blob/58032c8c3ffdd56eb9da3a847d1fd2485eb489b9/docs/setup-systems.md#how-to-install-clever-tools) is as easy as `npm i -g clever-tools`. Then, just run `clever login`, you're ready to go.

### SSH in any application without effort

Clever Cloud Platform-as-a-Service (PaaS) provides immutable infrastructure. While SSH access isn't necessary nor recommended, Clever Tools provides a `clever ssh` command to SSH into instances, helpful for debugging purposes. You can pass a key to it:

```bash
clever ssh
clever ssh --app app_id_or_name
clever ssh -a app_id_or_name -i ~/.ssh/id_ed25519
```

If you need to diagnose a problem, you can set the `CC_TROUBLESHOOT` environment variable to `true`. Once started, the application will stay up even if there is an error (up to 1 hour).

- [Lean more about SSH on Clever Cloud](/doc/account/ssh-keys-management/)

### Diagnose domains DNS configuration of your applications

Clever Tools provides a `domain diag` command to check the DNS configuration of domains linked to your applications. It doesn't cover cases such as when you use a CDN or private load balancers, but it will tell you if everything is OK or if you need to fix something.

```bash
clever domain diag
clever domain diag -a app_id_or_name
clever domain diag --app app_id_or_name --filter text_to_filter
```

### Get the full list of your applications

You can get the full list of your applications, grouped by organization, with `clever applications list`.

### Get anything in JSON format

(Almost) all Clever Tools commands can be used with the `--format json` or `-f json` option to get the result in JSON format. It makes it easier to use for scripts or CI/CD, or with tools such as `jq`, `jless` or `jql` for example.

### The amazing power of `clever curl`

You want to query our API or use it in scripts, CI/CD, etc. But you don't want to manage authentication and tokens? There is a Clever Tools feature for that: `clever curl`. It's just a `curl` wrapper, executed with your credentials and token automatically. For example, just run:

```bash
clever curl https://api.clever-cloud.com/v2/self
```

You'll get all the details of your account. Use it with `jq` or `jless` to make it more powerful:

```bash
clever curl https://api.clever-cloud.com/v2/summary | jless
```

You'll get a JSON object and could navigate in every resource accessible to your account: applications, add-ons, organizations, etc.

* [Learn more about Clever Cloud API](/api/)

### Open the Console or an application in your browser

Clever Tools provides commands to access an application in your browser through its favorite domain or to open it in the Clever Cloud Console:

```bash
clever open
clever open --app app_id_or_name

clever console
clever console --app app_id_or_name
```

### Pass your authentication to Clever Tools

To use Clever Tools with your account, you need to use the `clever login` command. But you can also login with your credentials and token directly or pass them as environment variables for a one-time use:

```bash
# Login with credentials as environment variables
export CLEVER_TOKEN=TOKEN
export CLEVER_SECRET=SECRET
clever login

# Pass your token and secret directly to the login command
clever login --token TOKEN --secret SECRET

# Use your credentials and token for a one-time use
CLEVER_TOKEN=TOKEN CLEVER_SECRET=SECRET clever profile
```

### Need something? Ask (or contribute)!

Clever Tools is an open source project, build with Node.js. It's easy to use and extend. Multiple members of our team are working on it, but we're happy to receive ideas, issues, pull requests. Want to be part of it? [Join us!](https://github.com/CleverCloud/clever-tools)

- [Learn more about Clever Tools](https://github.com/CleverCloud/clever-tools/tree/master/docs#readme)

## Did you know?

### Learn what's new on Clever Cloud

We're constantly improving our platform. You can follow our [blog](https://www.clever-cloud.com/blog/) to learn more about Clever Cloud's journey. But if you want technical updates about our services, read our public Changelog or subscribe to its RSS feed.

- [Clever Cloud Changelog](/changelog/)
- [Clever Cloud Changelog RSS feed](/changelog/index.xml)

### Our runtimes come batteries included

In each runtime, we provide a set of tools you can directly use for your applications and scripts. For example, if you need Node.js in a specific version in another runtime than `node`, just declare `CC_NODE_VERSION`. But you'll also find Python, Ruby, tools such as Clever Tools, `jq`, `tmux`. If you need a local in-memory Redis instance, you can use `redis-server`, and so on. One day, we'll provide a maintained public list of them.

### One domain, multiple applications: discover Path routing

You can easily link a (sub-)domain to an application on Clever Cloud. We generate a TLS certificate for you and apply it instantly, thanks to our [open source load balancer Sõzu](https://github.com/sozu-proxy/sozu). But you can also use the same (sub-)domain for multiple applications with different paths. For example, you can have an application for your blog linked to `mydomain.com/blog` and another one for your API linked to `mydomain.com/api`.

- [Learn more about Path routing](/doc/administrate/domain-names/#path-routing)

### Create and distribute your own add-ons for you, your customers or Clever Cloud's

If you provide a service, you can distribute it on Clever Cloud through an add-on provider. Thus, it can be available as an add-on, to link it to applications for you and across your organizations. It can also join Clever Cloud's Marketplace and become available to our customers.

- [Learn more about Add-on Provider and Marketplace API](/doc/marketplace/)

### Use the `cleverapps.io` you want with your applications

Clever Cloud provides a free domain `cleverapps.io` for your applications. It's not intended to be used for production, as we sometimes make changes to it, but it's enough for demo and testing environments. Once created, we provide a `app_id.cleverapps.io` domain for each application. But you can set any subdomain you want. Have fun with it! (But don't abuse it, it's a shared resource).

And if you use your own custom domain, just remove the `cleverapps.io` one.

### Clever Cloud is built on top of its own public API

How do we ensure that our API is great to use, and how do we push ourselves to make it better every day? We use it. Everything you can do with our Console, Clever Tools, SDK and integrations, you can build the same with our public API.

- [Learn more about Clever Cloud API](/api)

### Use our Web Components and make your own Clever Cloud interface

All our new Console features are built with open source Web Components and accessibility. You don't need a specific framework to use them, just those good old standards. They're available [as a npm package](https://www.npmjs.com/package/@clevercloud/components). Our team work on them [on a public repository](https://github.com/CleverCloud/clever-components), detailing its choices through Architecture Decision Records (ADRs). Want to now more or to contribute? Just take a look at our [Storybook](/doc/clever-components/?path=/docs/readme--docs).

### You need anything? Ask us!

Our main mission is to help our customers. We do it providing the Clever Cloud platform as a public cloud on our or partners infrastructure, on-premise or on edge devices in specific cases, all with the same Control Plane. But we also provide a lot of dedicated, off catalogue, services to help users to get the best out of Clever Cloud. You need anything special? [Ask us!](https://www.clever-cloud.com/contact/) Our sales team will be happy to help.