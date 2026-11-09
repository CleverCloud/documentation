---
type: docs
linkTitle: Getting started
weight: 10
title: Deploy Your First Application
description: In about ten minutes, deploy a Node.js application on Clever Cloud with Clever Tools, link a PostgreSQL database to it, update it, and learn where to go next
keywords:
- quickstart
- getting started
- first deployment
- tutorial
- clever tools
- deploy
- add-on
aliases:
- /deploy
- /doc/clever-cloud-overview/add-application
- /doc/deploy/git-deployment
- /doc/getting-started/quickstart
- /doc/quickstart
- /getting-started/authentication
- /getting-started/quickstart
- /quickstart
---

In about ten minutes, you deploy a small Node.js application on Clever Cloud, link a PostgreSQL database to it, ship a change, and clean up. Along the way, you see how Clever Cloud builds your code, runs it, and gives it the credentials of its services.

You need:

- A [Clever Cloud account](/doc/account-billing/user/#create-an-account), created with your email or GitHub, with a confirmed email address
- [Git](https://git-scm.com/), to send your code to Clever Cloud
- Node.js 24 or later, to install Clever Tools with npm, or one of the [other installation methods](/doc/tools/cli/install/)

To protect your account, enable [two-factor authentication](/doc/account-billing/user/#two-factor-authentication-2fa) before you start: enabling it later signs Clever Tools out by default.

## Install Clever Tools

Install Clever Tools, the command line interface of Clever Cloud, then sign in: `clever login` opens the Console in your browser to authorize it.

```bash
npm install -g clever-tools
clever login
```

## Write the application

Create a folder for the application, and move into it:

```bash
mkdir hello-clever
cd hello-clever
```

Add two files to it. The application answers each request with a greeting, and tells whether a database is linked:

```json {filename="package.json"}
{
  "name": "hello-clever",
  "scripts": {
    "start": "node server.js"
  }
}
```

```javascript {filename="server.js"}
const http = require("node:http");

const database = process.env.POSTGRESQL_ADDON_HOST ? "linked" : "not linked yet";

http
  .createServer((req, res) => res.end(`Hello from Clever Cloud! Database: ${database}\n`))
  .listen(process.env.PORT || 8080);
```

Clever Cloud deploys what Git tracks: from this folder, turn it into a Git repository, and commit the files.

```bash
git init
git add .
git commit -m "First version"
```

## Deploy it

Create a Node.js application on Clever Cloud, then deploy your code. The application [consumes credits](/doc/account-billing/consumption/) while it runs, until you [clean up](#clean-up):

```bash
clever create --type node hello-clever
clever deploy
```

`clever create` links the folder to the new application, in the [Paris region](/doc/manage/regions/) by default. `clever deploy` pushes your commit, then shows the logs of the deployment: Clever Cloud starts a new instance, installs the dependencies, runs `npm start`, and checks that the application listens on port `8080`. Once it's up, the command ends with the URL of the application, such as `https://app-<uuid>.cleverapps.io/`. Open it:

```bash
clever open
```

The page shows `Hello from Clever Cloud! Database: not linked yet`. [How Clever Cloud works](/doc/how-it-works/) details each step. If the deployment fails, its logs tell why: the [troubleshooting page](/doc/find-help/troubleshooting/) covers the most common causes, such as an application that doesn't listen on port `8080`.

`clever deploy` relies on Git: you can also deploy with a plain `git push`. Add your [SSH key](/doc/account-billing/ssh-keys/) to your profile, copy the **Deployment URL** from the **Information** menu of the application in the Console, then push your commit to `master`, the branch that Clever Cloud deploys:

```bash
git remote add clever "<deployment-url>"
git push clever HEAD:master
```

## Add a database

Databases, storage, and other services are add-ons. Create a [PostgreSQL](/doc/deploy/databases/postgresql/) add-on, and link it to the application. The free `dev` plan runs on [shared resources](/doc/deploy/databases/postgresql/#note-on-shared-databases): use it to test, and choose a dedicated plan for production.

```bash
clever addon create postgresql-addon hello-db --plan dev --link hello-clever
```

Linking an add-on gives its credentials to the application as environment variables, such as `POSTGRESQL_ADDON_HOST` or `POSTGRESQL_ADDON_URI`. List them, then restart the application so that it reads them:

```bash
clever env
clever restart
```

Once the restart ends, reload the page: it shows `Database: linked`, as the application now finds the credentials of the database. Your code never holds a password, and the same code runs with another database in another environment, such as a staging one.

## Ship a change

Each deployment starts from a new instance, built from your last commit. Change the greeting in `server.js`, then commit and deploy:

```bash
git commit -am "Change the greeting"
clever deploy
```

Reload the page to see the change. To follow what your application prints, stream its logs, and stop with `Ctrl+C`:

```bash
clever logs
```

## Clean up

The application consumes resources as long as it runs. [Delete the add-on](/doc/deploy/databases/#delete-a-database), then [the application](/doc/manage/#archive-and-delete):

```bash
clever addon delete hello-db --yes
clever delete --yes
```

## Prefer the Console

Everything you did with Clever Tools, you can do in the [Console](https://console.clever-cloud.com/): [create and deploy an application](/doc/deploy/applications/#create-and-deploy-an-application), with Git or from a GitHub repository, then [create a database](/doc/deploy/databases/#create-a-database), or any other add-on, and link it to your application.

## Go further

You deployed, configured, and updated an application in a few commands. From here, bring your own project, or fork one of the [examples and demos](https://github.com/CleverCloud/examples-and-demos) of your runtime, then prepare it for production.

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications" title="Deploy your stack" subtitle="Configure the build and the run of Node.js, Python, PHP, Java, Go, Docker, and more" icon="rocket-launch" >}}
  {{< card link="/developers/guides" title="Follow a guide" subtitle="Deploy a framework, such as Laravel, Django, or Nuxt, or self-host a tool such as WordPress" icon="book-open" >}}
  {{< card link="/developers/doc/manage/domain-names" title="Add your domain" subtitle="Serve your application on your own domain, with a free TLS certificate" icon="globe-alt" >}}
  {{< card link="/developers/doc/manage/scaling" title="Scale it" subtitle="Set the size and number of instances, or let them grow with the load" icon="arrows-expand" >}}
  {{< card link="/developers/doc/observability" title="Monitor it" subtitle="Logs, metrics, and access logs of your applications and add-ons" icon="chart-bar" >}}
  {{< card link="/developers/doc/ai-llms" title="Deploy with your AI assistant" subtitle="Drive Clever Cloud from Claude Code, Cursor, Codex, or any agent" icon="sparkles" >}}
{{< /cards >}}

To learn the platform step by step, [Clever Cloud Academy](https://academy.clever.cloud/?lang=en) offers courses with hands-on exercises, from Cloud Concepts 101 to Advanced Deployment Recipes, and certifications to validate your skills. Sign in with your Clever Cloud account.
