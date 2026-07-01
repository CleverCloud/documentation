---
type: docs
draft: false
linkTitle: SvelteKit
title: SvelteKit
description: Deploy SvelteKit as a static site, single-page application, or with server-side rendering on Clever Cloud with step-by-step configuration guide
keywords:
- sveltekit
- svelte
- static site generator
- single page application
- Node.js
- javascript framework
- ssr
- ssg
- spa
aliases:
- /doc/sveltekit
- /sveltekit
---

{{< hextra/hero-subtitle >}}
  SvelteKit is a full-stack web framework for Svelte, with support for static site generation, single-page applications, and server-side rendering on Clever Cloud.
{{< /hextra/hero-subtitle >}}

Clever Cloud supports all three SvelteKit rendering modes. SSG (static site generation) and SPA (single-page application) both use [`@sveltejs/adapter-static`](https://svelte.dev/docs/kit/adapter-static) and deploy to the [Static runtime](/developers/doc/applications/static/). SSR (server-side rendering) uses [`@sveltejs/adapter-node`](https://svelte.dev/docs/kit/adapter-node) and deploys to the [Node.js runtime](/developers/doc/applications/nodejs/).

SSG is the right choice for content-oriented sites where pages don't change per visitor. SPA works well for dashboards and interactive tools where SEO is not a priority. SSR is best when pages must reflect real-time data or per-user state.

To follow this guide with a fresh project, scaffold a new SvelteKit application using the official CLI (you'll need [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):

{{< tabs >}}
  {{< tab name="npm" icon="npm" >}}
    ```bash
    npx sv create mySvelteApp
    cd mySvelteApp
    npm install
    ```
  {{< /tab >}}
  {{< tab name="pnpm" icon="pnpm" >}}
    ```bash
    npx sv create mySvelteApp
    cd mySvelteApp
    pnpm install
    ```
  {{< /tab >}}
{{< /tabs >}}

## Deploy as a static site

Both SSG and SPA modes use `@sveltejs/adapter-static` and deploy to the Clever Cloud Static runtime. SSG prebuilds every route as a separate HTML file at build time. SPA ships a single HTML shell and handles all routing in the browser.

### Static Site Generation

Install the adapter, then configure it in `vite.config.ts`:

```bash
npm i -D @sveltejs/adapter-static
```

```typescript
// vite.config.ts
import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit({
      adapter: adapter()
    })
  ]
});
```

Enable prerendering in your root layout so SvelteKit generates static HTML for every route at build time:

```javascript
// src/routes/+layout.js
export const prerender = true;
```

### Single-Page Application

For a SPA, disable server-side rendering in the root layout and configure a fallback page. The fallback is an HTML file the static server returns for any path that has no matching file, allowing SvelteKit's client-side router to take over:

```javascript
// src/routes/+layout.js
export const ssr = false;
```

```typescript
// vite.config.ts
import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit({
      adapter: adapter({ fallback: '200.html' })
    })
  ]
});
```

{{< callout type="tip" >}}
The following steps use `myStaticApp` as an example folder name. Replace it with your actual project folder (`mySvelteApp` if you followed the scaffold above).
{{< /callout >}}

{{% content "static-create" %}}

### Environment variables

Clever Cloud's static runtime does not auto-detect SvelteKit, so you need to configure the output directory and build command explicitly. `CC_WEBROOT` points to the `build/` directory that the adapter generates. Clever Cloud installs dependencies automatically, but does not run the build. `CC_PRE_BUILD_HOOK` is what triggers `npm run build` and produces the output directory:

{{< tabs >}}
  {{< tab name="npm" icon="npm" >}}
    ```bash
    clever env set CC_WEBROOT "build"
    clever env set CC_PRE_BUILD_HOOK "npm install && npm run build"
    ```
  {{< /tab >}}
  {{< tab name="pnpm" icon="pnpm" >}}
    ```bash
    clever env set CC_NODE_BUILD_TOOL "pnpm"  # optional if pnpm-lock.yaml is committed
    clever env set CC_WEBROOT "build"
    clever env set CC_PRE_BUILD_HOOK "pnpm install && pnpm run build"
    ```
  {{< /tab >}}
{{< /tabs >}}

### Scale your application

A pico instance is sufficient to serve a static site. Use a medium build instance (`M`) to provide enough memory for compiling your project:

```bash
clever scale --flavor pico
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## Deploy with server-side rendering

SSR renders pages on each request using a Node.js server. Use `@sveltejs/adapter-node`, which outputs a self-contained server bundle to the `build/` directory.

### Configure the adapter

Install the adapter and update `vite.config.ts`:

```bash
npm i -D @sveltejs/adapter-node
```

```typescript
// vite.config.ts
import adapter from '@sveltejs/adapter-node';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit({
      adapter: adapter()
    })
  ]
});
```

### Create a Node.js application

Install [Clever Tools](/developers/doc/cli/) and create a Node.js application linked to your project folder:

```bash
npm i -g clever-tools
clever login

cd mySvelteApp
clever create -t node

# Or link an existing Clever Cloud application:
clever link your_app_name_or_ID
```

### Environment variables

Configure instance sizing, then set the required variables. A medium build instance (`M`) provides enough memory to compile the project; an XS instance is sufficient to run the server:

```bash
clever scale --build-flavor M
clever scale --flavor XS
```

{{< tabs >}}
  {{< tab name="npm" icon="npm" >}}
    ```bash
    clever env set PORT 8080
    clever env set PROTOCOL_HEADER "X-Forwarded-Proto"
    clever env set HOST_HEADER "Host"
    clever env set CC_NODE_DEV_DEPENDENCIES install
    clever env set CC_POST_BUILD_HOOK "npm run build"
    clever env set CC_RUN_COMMAND "node build"
    ```
  {{< /tab >}}
  {{< tab name="pnpm" icon="pnpm" >}}
    ```bash
    clever env set PORT 8080
    clever env set PROTOCOL_HEADER "X-Forwarded-Proto"
    clever env set HOST_HEADER "Host"
    clever env set CC_NODE_BUILD_TOOL "pnpm"  # optional if pnpm-lock.yaml is committed
    clever env set CC_NODE_DEV_DEPENDENCIES install
    clever env set CC_POST_BUILD_HOOK "pnpm run build"
    clever env set CC_RUN_COMMAND "node build"
    ```
  {{< /tab >}}
{{< /tabs >}}

By default, Clever Cloud only installs production dependencies, so `vite` and `@sveltejs/kit` would be missing when the build runs (they're dev dependencies). `CC_NODE_DEV_DEPENDENCIES` tells it to install development dependencies too, and `CC_POST_BUILD_HOOK` runs `vite build` once they're installed, producing the `build/` directory that `node build` requires.

`PORT` must be set to `8080`. SvelteKit's built server listens on port 3000 by default, but Clever Cloud requires all applications to be exposed on port 8080.

`PROTOCOL_HEADER` and `HOST_HEADER` tell SvelteKit which headers to read the request protocol and hostname from. Clever Cloud routes all traffic through a reverse proxy and forwards the original protocol via `X-Forwarded-Proto`. The origin is then reconstructed from each incoming request. This means the configuration works with the default `cleverapps.io` domain and with any custom domain you add later.

{{< callout type="info" >}}
If you prefer a fixed origin, set `ORIGIN` to your application's public URL (for example `https://your-app.cleverapps.io`) instead of `PROTOCOL_HEADER` and `HOST_HEADER`. Do not set both approaches at the same time.
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
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application" icon="static" >}}
  {{< card link="https://svelte.dev/docs/kit/adapters" title="SvelteKit Adapters" subtitle="Official documentation for SvelteKit adapters" icon="code-bracket" >}}
{{< /cards >}}
