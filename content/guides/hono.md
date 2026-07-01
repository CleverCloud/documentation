---
type: docs
draft: false
linkTitle: Hono
title: Hono
description: Deploy a Hono application on the Node.js runtime on Clever Cloud with step-by-step configuration guide
keywords:
- hono
- node.js
- javascript framework
- typescript
- api
- web framework
aliases:
- /doc/hono
- /hono
---

{{< hextra/hero-subtitle >}}
  Hono is a small, fast web framework built on Web Standards, running across many JavaScript runtimes, on Clever Cloud.
{{< /hextra/hero-subtitle >}}

Hono supports many runtimes, including Cloudflare Workers, Deno, Bun, Vercel, Netlify, AWS Lambda, and Node.js. Clever Cloud runs Hono applications on the [Node.js runtime](/developers/doc/applications/nodejs/) through the [`@hono/node-server`](https://github.com/honojs/node-server) adapter.

To follow this guide with a fresh project, scaffold a new Hono application using the official CLI (you'll need [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)). Pass `-t nodejs` to select the Node.js template directly, since the interactive picker lists 13 runtimes and does not display them all at once:

```bash
npm create hono@latest myHonoApp -- -t nodejs
cd myHonoApp
```

Answer "yes" when prompted to install dependencies.

## Deploy a Node.js application

To deploy your Hono project to Clever Cloud, adapt its entry point, then create and configure the application.

### Adapt the entry point

The `nodejs` template's `src/index.ts` starts a server on port 3000 and has no shutdown handling. Both need adjusting before deploying to Clever Cloud.

Clever Cloud automatically injects a `PORT` environment variable set to `8080`, and requires every application to listen on `0.0.0.0:8080`. Read `process.env.PORT` instead of the hardcoded port, with a fallback for local development. Clever Cloud also terminates the previous instance during a restart or a redeploy with zero-downtime deployment enabled, so keep a reference to the returned server and close it on `SIGINT`/`SIGTERM` to let in-flight requests finish before the process exits:

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
  port: Number(process.env.PORT) || 3000
}, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})

process.on('SIGINT', () => {
  server.close()
  process.exit(0)
})
process.on('SIGTERM', () => {
  server.close((err) => {
    if (err) {
      console.error(err)
      process.exit(1)
    }
    process.exit(0)
  })
})
```

The generated `package.json` defines three scripts: `dev` runs the server with live reload, `build` compiles TypeScript to `dist/` with `tsc`, and `start` runs the compiled output with `node dist/index.js`.

### Create a Node.js application

Install [Clever Tools](/developers/doc/cli/) and create a Node.js application linked to your project folder:

```bash
npm i -g clever-tools
clever login

cd myHonoApp
clever create -t node

# Or link an existing Clever Cloud application:
clever link your_app_name_or_ID
```

### Environment variables

Configure instance sizing, then set the build hook. A medium build instance (`M`) provides enough memory to compile the project; an XS instance is sufficient to run the server:

```bash
clever scale --build-flavor M
clever scale --flavor XS

clever env set CC_NODE_DEV_DEPENDENCIES install
clever env set CC_POST_BUILD_HOOK "npm run build"
```

By default, Clever Cloud only installs production dependencies, so `typescript` would be missing when `tsc` runs. `CC_NODE_DEV_DEPENDENCIES` tells it to install development dependencies too, and `CC_POST_BUILD_HOOK` runs the `build` script once they're installed, which produces `dist/` for `start` to run automatically afterwards. No `PORT` variable needs to be set: Clever Cloud injects it automatically, and the application already reads it from `process.env.PORT`.

{{< callout type="warning" >}}
A new application defaults to a `pico` build instance. If your deployment logs repeat the same lines without progressing past `tsc`, the build ran out of memory before scaling took effect. Run the `clever scale --build-flavor M` command above, then `clever restart --without-cache` to retry the build.
{{< /callout >}}

### Push your code

Once you complete these steps, commit your project and deploy it:

```bash
git add .
git commit -m "First deploy"
clever deploy  # or: git push clever main:master (find the git URL in your app's Information tab)
clever open
```

You can display your application's URL or add a custom domain (DNS configuration required):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application" icon="node" >}}
  {{< card link="https://hono.dev/docs" title="Hono documentation" subtitle="Official documentation for the Hono framework" icon="code-bracket" >}}
{{< /cards >}}
