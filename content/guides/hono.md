---
type: docs
draft: false
linkTitle: Hono
title: Hono
description: Deploy a Hono application on Clever Cloud with the Node.js runtime and a step-by-step configuration guide
keywords:
- hono
- node.js
- javascript framework
- typescript
- api
- web framework
---

{{< hextra/hero-subtitle >}}
  Deploy Hono, a lightweight web framework built on Web Standards, with the Node.js runtime on Clever Cloud.
{{< /hextra/hero-subtitle >}}

Hono supports multiple JavaScript runtimes. This guide uses the [Clever Cloud Node.js runtime](/developers/doc/applications/nodejs/) with the [@hono/node-server adapter](https://hono.dev/docs/getting-started/nodejs).

To follow this guide with a fresh project, scaffold a new Hono application using the official CLI (you'll need [Node.js](https://nodejs.org/en/download) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)). Pass `-t nodejs` to select the Node.js template directly. When prompted, confirm the dependency installation and select `npm` as package manager:

```bash
npm create hono@latest myHonoApp -- -t nodejs
cd myHonoApp
git init
```

## Deploy Hono with Node.js

To deploy your Hono project to Clever Cloud, adapt its entry point, then create and configure the application.

### Adapt the entry point

The `nodejs` template's `src/index.ts` starts a server on port 3000 and has no shutdown handling. Adapt both behaviours before deploying. 

Clever Cloud sets `PORT` environment variable to `8080` by default and expects the application to listen on every network interface. Read it rather than hardcoding this value to remain compatible with [Request Flow port allocation](/developers/doc/develop/request-flow/#port-management), keep port 3000 as a local fallback, and set the hostname to `0.0.0.0`. Also close the server on `SIGINT` and `SIGTERM` so in-flight requests can finish during a restart or zero-downtime deployment:

```typescript
// src/index.ts
import { serve } from '@hono/node-server'
import { Hono } from 'hono'

const app = new Hono()

app.get('/', (c) => {
  return c.text('Hello Hono!')
})

const server = serve({
  fetch: app.fetch,
  hostname: '0.0.0.0',
  port: Number(process.env.PORT) || 3000
}, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})

const shutdown = () => {
  server.close((err) => {
    if (err) {
      console.error(err)
      process.exit(1)
    }
    process.exit(0)
  })
}

process.on('SIGINT', shutdown)
process.on('SIGTERM', shutdown)
```

The generated `package.json` defines three scripts: `dev` runs the server with live reload, `build` compiles TypeScript to `dist/` with `tsc`, and `start` runs the compiled output with `node dist/index.js`.

### Create a Node.js application

Install [Clever Tools](/developers/doc/cli/) and create a Node.js application linked to your project folder:

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

By default, Clever Cloud only installs production dependencies, so `typescript` would be missing when `tsc` runs. `CC_NODE_DEV_DEPENDENCIES` includes development dependencies, and `CC_POST_BUILD_HOOK` builds `dist/` before the generated `start` script runs. No `PORT` variable needs to be set for this deployment because Clever Cloud injects it automatically. If your project grows, you can [increase the build or runtime instance size](/developers/doc/administrate/scalability/).

### Deploy your code

The Hono template does not ignore its generated `dist/` directory. Add it to `.gitignore`:

```gitignore {filename=".gitignore"}
dist/
```

Then commit and deploy the project:

```bash
git add .
git commit -m "First deploy"

clever deploy
clever open
```

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application" icon="node" >}}
  {{< card link="https://hono.dev/docs" title="Hono documentation" subtitle="Learn more about the Hono framework" icon="hono" >}}
{{< /cards >}}
