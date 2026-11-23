---
type: docs
linkTitle: Bun
title: Bun application runtime
description: Deploy Bun applications on Clever Cloud, which install their dependencies and start with Bun, with its native clients for PostgreSQL, MySQL, Cellar, Redis, and Materia KV
keywords:
- bun
- bun app hosting
- bun cloud
- bun.lock
- hono
- javascript
- typescript
---

## Overview

[Bun](https://bun.com) is a JavaScript runtime and a package manager, which runs TypeScript without a build. On a [Node.js application](/doc/deploy/applications/nodejs/), Clever Cloud installs your dependencies and starts your project with Bun when it finds a `bun.lock` file. Bun includes clients for SQL databases, S3, and Redis, which work with several [add-ons](#built-in-clients-for-clever-cloud-add-ons) of Clever Cloud, without any dependency to add.

## Create your Bun application

A Bun application is a Node.js application. To create it, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type node
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Bun application

### Mandatory needs

A Bun application needs:

- A `bun.lock` file, or `CC_NODE_BUILD_TOOL=bun`, so that Clever Cloud uses Bun
- A `package.json` file, with a start script or a `main` field, to [start your application](#start-command)
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

`bun install` writes the `bun.lock` file, which sets the exact version of each dependency: commit it. Clever Cloud checks the `yarn.lock` and `pnpm-lock.yaml` files first, so remove them from a project that moves to Bun.

Clever Cloud doesn't detect the binary `bun.lockb` file of Bun releases before 1.2, and then installs your dependencies with npm. Convert it with `bun install --save-text-lockfile`, or set `CC_NODE_BUILD_TOOL=bun` to use Bun anyway.

For instance, a minimal [Hono](https://hono.dev) application, in TypeScript:

```json {filename="package.json"}
{
  "name": "hello-bun",
  "type": "module",
  "scripts": {
    "start": "bun server.ts"
  },
  "dependencies": {
    "hono": "^4.13.20"
  },
  "devDependencies": {
    "@types/bun": "^1.4.5"
  }
}
```

```ts {filename="server.ts"}
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => c.text('Hello from Bun on Clever Cloud'));

Bun.serve({
  hostname: '0.0.0.0',
  port: Number(Bun.env.PORT ?? 8080),
  fetch: app.fetch,
});
```

To try it locally, run `bun install`, then `bun start`: it listens on port 8080.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then installs the dependencies of your project, without its `devDependencies`:

```bash
bun install --omit dev --no-progress
```

Clever Cloud skips them whatever the value of `NODE_ENV`, unlike npm. To install them, such as for a build tool, set `CC_NODE_DEV_DEPENDENCIES=install`: Clever Cloud then runs `bun install --no-progress`.

Bun runs TypeScript files directly. To build your application, such as to bundle a frontend, run your `build` script in the post-build hook:

```bash
clever env set CC_POST_BUILD_HOOK "bun run build"
```

A hook runs from the root of your repository: with `CC_APP_FOLDER`, start it with `cd` to this folder.

### Bun version

Clever Cloud uses Bun {{< runtime_version bun >}} by default, the version of its images. To set another one, add Bun to a `mise.toml` file in your project:

```toml {filename="mise.toml"}
[tools]
bun = "1.4.4"
```

[Mise](/doc/manage/mise/) installs this version before the build: it then installs your dependencies and runs your application.

### Start command

Clever Cloud starts your application from the folder of your project, with the first of these commands that applies:

1. `CC_RUN_COMMAND`, when you set it
2. `bun start`, which runs the start script of your `package.json` file
3. `bun` and the file of the `main` field, such as `bun server.ts`

### Built-in clients for Clever Cloud add-ons

These clients of Bun connect to add-ons from the variables that they set:

- [`redis`](https://bun.com/docs/runtime/redis): [Redis](/doc/deploy/databases/redis/) and [Materia KV](/doc/deploy/databases/materia-kv/), with `REDIS_URL`, which it reads by default
- [`S3Client`](https://bun.com/docs/runtime/s3): [Cellar](/doc/deploy/storage/cellar/), with `CELLAR_ADDON_*` and an existing bucket
- [`SQL`](https://bun.com/docs/runtime/sql): [MySQL](/doc/deploy/databases/mysql/) and [PostgreSQL](/doc/deploy/databases/postgresql/), with `MYSQL_ADDON_URI` or `POSTGRESQL_ADDON_URI`

For instance, with a Redis, a PostgreSQL, and a Cellar add-on linked to your application:

```ts {filename="server.ts"}
import { redis, S3Client, SQL } from 'bun';

const db = new SQL(Bun.env.POSTGRESQL_ADDON_URI);
const cellar = new S3Client({
  accessKeyId: Bun.env.CELLAR_ADDON_KEY_ID,
  secretAccessKey: Bun.env.CELLAR_ADDON_KEY_SECRET,
  endpoint: `https://${Bun.env.CELLAR_ADDON_HOST}`,
  bucket: 'my-bucket',
});

const visits = await redis.incr('visits');
const [{ now }] = await db`SELECT now()`;
await cellar.file('hello.txt').write(`Visit number ${visits}, at ${now}`);
```

The [Bun add-ons examples](https://github.com/CleverCloud/bun-addons-examples) show how to use other Clever Cloud add-ons with Bun.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the packages that Bun downloads between commits, in `~/.bun/install/cache`. If you move this folder with the `BUN_INSTALL_CACHE_DIR` variable of Bun, Clever Cloud keeps this folder instead.

## Bun applications as Clever Tasks

A Bun application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud installs its dependencies with Bun, then runs `CC_RUN_COMMAND` from the folder of your project, instead of starting a web server. The task stops when this command ends.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks):

```bash
clever create --type node --task "bun migrate.ts"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Node.js" subtitle="Deploy Node.js applications with npm, pnpm, or Yarn" icon="simple:nodedotjs" >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
