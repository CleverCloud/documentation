---
type: docs
linkTitle: SvelteKit
title: Deploy a SvelteKit application
description: Deploy a SvelteKit application as a static site, a single-page application, or a Node.js server on Clever Cloud
keywords:
- sveltekit
- svelte
- static site generation
- single-page application
- Node.js
- JavaScript framework
- server-side rendering
---

{{< hextra/hero-subtitle >}}
  SvelteKit is a full-stack web framework for Svelte, with support for static site generation, single-page applications, and server-side rendering.
{{< /hextra/hero-subtitle >}}

Clever Cloud supports all three SvelteKit rendering modes. Static site generation (SSG) and single-page applications (SPA) use [@sveltejs/adapter-static](https://svelte.dev/docs/kit/adapter-static) and the [Static runtime](/developers/doc/applications/static/). Server-side rendering (SSR) uses [@sveltejs/adapter-node](https://svelte.dev/docs/kit/adapter-node) and the [Node.js runtime](/developers/doc/applications/nodejs/).

SSG is well suited to content-oriented sites whose pages do not change for each visitor. SPA works well for interactive applications where search engine indexing is not a priority. Use SSR when pages depend on real-time data or user-specific state.

## Create a SvelteKit project

You need [Git](https://git-scm.com/downloads) and [Node.js](https://nodejs.org/en/download) to follow this guide. Create a minimal TypeScript project:

```bash
npx sv create --template minimal --types ts --no-add-ons --install npm mySvelteApp
cd mySvelteApp
```

If you already have a SvelteKit project, run the following commands from its root directory.

## Deploy as a static site

Both SSG and SPA modes use `@sveltejs/adapter-static` and the Clever Cloud Static runtime. SSG generates an HTML file for each route at build time. SPA generates a single HTML shell and handles routing in the browser.

Install the Static adapter:

```bash
npm install --save-dev @sveltejs/adapter-static
```

Then choose one of the following rendering modes.

### Static site generation

Configure the adapter in `vite.config.ts`:

```typescript {filename="vite.config.ts"}
import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit({
      compilerOptions: {
        // Force runes mode for the project, except for libraries. Can be removed in Svelte 6.
        runes: ({ filename }) =>
          filename.split(/[/\\]/).includes('node_modules') ? undefined : true
      },
      adapter: adapter()
    })
  ]
});
```

Enable prerendering in the root layout so SvelteKit generates static HTML for every route:

```typescript {filename="src/routes/+layout.ts"}
export const prerender = true;
```

### Single-page application

SPA mode has performance and search engine optimization drawbacks. Prefer SSG or SSR unless your application specifically needs client-only rendering.

Disable server-side rendering in the root layout:

```typescript {filename="src/routes/+layout.ts"}
export const ssr = false;
```

Then configure a fallback page in `vite.config.ts`:

```typescript {filename="vite.config.ts"}
import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit({
      compilerOptions: {
        // Force runes mode for the project, except for libraries. Can be removed in Svelte 6.
        runes: ({ filename }) =>
          filename.split(/[/\\]/).includes('node_modules') ? undefined : true
      },
      adapter: adapter({ fallback: '200.html' })
    })
  ]
});
```

### Create a Static application

Install [Clever Tools](/developers/doc/cli/), log in, initialize the Git repository, and create a Static application:

```bash
npm i -g clever-tools
clever login

git init
clever create -t static
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

To use an existing application instead, link it to the current repository:

```bash
clever link your_app_name_or_ID
```

### Configure the build

Set the output directory and the command Clever Cloud runs during the build phase:

```bash
clever env set CC_WEBROOT "/build"
clever env set CC_BUILD_COMMAND "npm install && npm run build"
```

For SPA mode, also tell the default [Static Web Server](https://static-web-server.net/v2/features/error-pages/#fallback-page-for-use-with-client-routers) to serve the generated fallback for routes that do not match a file:

```bash
clever env set SERVER_FALLBACK_PAGE "./build/200.html"
```

Your Static application is ready. Continue to [deploy the application](#deploy-the-application).

## Deploy with server-side rendering

SSR renders pages on each request using a Node.js server. Install `@sveltejs/adapter-node`, which generates a standalone server in the `build/` directory:

```bash
npm install --save-dev @sveltejs/adapter-node
```

Configure the adapter in `vite.config.ts`:

```typescript {filename="vite.config.ts"}
import adapter from '@sveltejs/adapter-node';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit({
      compilerOptions: {
        // Force runes mode for the project, except for libraries. Can be removed in Svelte 6.
        runes: ({ filename }) =>
          filename.split(/[/\\]/).includes('node_modules') ? undefined : true
      },
      adapter: adapter()
    })
  ]
});
```

### Create a Node.js application

Install [Clever Tools](/developers/doc/cli/), log in, initialize the Git repository, and create a Node.js application:

```bash
npm i -g clever-tools
clever login

git init
clever create -t node
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

To use an existing application instead, link it to the current repository:

```bash
clever link your_app_name_or_ID
```

### Configure the application

Configure Clever Cloud to install the development dependencies needed by the build, run that build, and start the generated Node.js server:

```bash
clever env set CC_NODE_DEV_DEPENDENCIES install
clever env set CC_POST_BUILD_HOOK "npm run build"
clever env set CC_RUN_COMMAND "node build"
clever env set PROTOCOL_HEADER "x-forwarded-proto"
clever env set HOST_HEADER "host"
```

Clever Cloud provides the `PORT` environment variable expected by `adapter-node`. `PROTOCOL_HEADER` and `HOST_HEADER` let SvelteKit reconstruct the public URL from requests forwarded by Clever Cloud, including requests made through a [custom domain](/developers/doc/administrate/domain-names/).

## Deploy the application

Commit the project and deploy it:

```bash
git add .
git commit -m "First deploy"

clever deploy
clever open
```

You can display the application's domains or add a [custom domain](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/nodejs/" title="Node.js applications" subtitle="Configure and deploy Node.js applications" icon="node" >}}
  {{< card link="/developers/doc/applications/static/" title="Static applications" subtitle="Configure and deploy static applications" icon="static" >}}
  {{< card link="<https://svelte.dev/docs/kit/adapters>" title="SvelteKit adapters" subtitle="Choose and configure a SvelteKit adapter" icon="svelte" >}}
{{< /cards >}}
