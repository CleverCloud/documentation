---
type: docs
linkTitle: Farm.js
title: Deploy a Farm.js application
description: Deploy a Farm.js full-stack application on Clever Cloud with the Node.js runtime and a step-by-step configuration guide
keywords:
- farm.js
- farmjs
- node.js
- javascript framework
- typescript
- server-side rendering
---

{{< hextra/hero-subtitle >}}
  Deploy Farm.js, a full-stack framework with typed file routing, server actions and streaming server-side rendering, with the Node.js runtime on Clever Cloud.
{{< /hextra/hero-subtitle >}}

Farm.js builds an application into a self-contained Node.js server. This guide uses the [Clever Cloud Node.js runtime](/developers/doc/deploy/applications/nodejs/) to build and run that server.

To follow this guide with a fresh project, scaffold a new Farm.js application with the official CLI (you'll need [Node.js](https://nodejs.org/en/download) 22.13 or later and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)). Follow the prompts, then initialize a Git repository:

```bash
npx @farm.js/create-app@latest myFarmApp
cd myFarmApp
git init
```

## Deploy Farm.js with Node.js

### Check the start script

The Node.js runtime starts the application with the `start` script from `package.json`. New Farm.js applications run the server that `farm build` writes to `.farm/.output`:

```json {filename="package.json"}
{
  "scripts": {
    "build": "farm build",
    "start": "node .farm/.output/server/index.mjs"
  }
}
```

If `farm.config.ts` sets `deploy.target` to another platform, such as `vercel`, remove it or set it to `node`. A platform target builds output that only that platform can serve.

### Create a Node.js application

Install [Clever Tools](/developers/doc/manage/cli/), log in and create a Node.js application:

```bash
npm i -g clever-tools
clever login

clever create -t node

# Or link an existing Clever Cloud application:
clever link your_app_name_or_ID
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

### Configure the application

```bash
clever env set CC_NODE_DEV_DEPENDENCIES install
clever env set CC_POST_BUILD_HOOK "npm run build"
```

By default, Clever Cloud only installs production dependencies, but `farm build` runs the Farm.js CLI, which is a development dependency. `CC_NODE_DEV_DEPENDENCIES` includes development dependencies, and `CC_POST_BUILD_HOOK` builds the server before the `start` script runs. The Farm.js server reads the `PORT` variable that Clever Cloud injects, so you don't need to set it.

### Deploy your code

New Farm.js applications already ignore the generated `.farm/` directory. Commit and deploy the project:

```bash
git add .
git commit -m "First deploy"

clever deploy
clever open
```

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/develop/common-configuration/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application" icon="simple:nodedotjs" >}}
  {{< card link="https://farmjs.dev/docs/deployment" title="Farm.js deployment" subtitle="Learn more about building and deploying Farm.js" icon="farmjs" >}}
{{< /cards >}}
