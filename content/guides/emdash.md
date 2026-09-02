---
type: docs
linkTitle: EmDash
title: Deploy a website with EmDash CMS
description: Deploy an EmDash CMS website on Clever Cloud with PostgreSQL and Cellar object storage
keywords:
- emdash
- cms
- astro
- node.js
- postgresql
- cellar
- s3 storage
---

{{< hextra/hero-subtitle >}}
  Deploy an EmDash CMS website with persistent content and media storage on Clever Cloud.
{{< /hextra/hero-subtitle >}}

[EmDash](https://emdashcms.com/) is an open source, Astro-based content management system. This guide deploys its Node.js version with [PostgreSQL](/developers/doc/addons/postgresql/) for content and configuration, and [Cellar](/developers/doc/addons/cellar/) for uploaded media.

## Create an EmDash project

You need [Git](https://git-scm.com/downloads), Node.js 22.12 or later, [jq](https://jqlang.org/download/), [s3cmd](https://s3tools.org/s3cmd) or another S3-compatible client, and a [Clever Cloud account](https://console.clever-cloud.com) to follow this guide.

Use the [official project generator](https://docs.emdashcms.com/getting-started/) to create a Node.js blog with npm:

```bash
npm create emdash@latest my-emdash -- --template node:blog --pm npm --yes
cd my-emdash
```

The generator also provides `starter`, `marketing`, and `portfolio` templates. Replace `blog` in the command to use one of them.

Replace the local SQLite dependency with the PostgreSQL driver, update EmDash to its current release, and install the AWS SDK packages required by its S3 adapter:

```bash
npm uninstall better-sqlite3
npm install emdash@latest pg @aws-sdk/client-s3 @aws-sdk/s3-request-presigner
```

Replace `astro.config.mjs` with the following configuration. It preserves the generated blog settings while reading the linked PostgreSQL and Cellar add-on variables at run time:

```javascript {filename="astro.config.mjs"}
import node from "@astrojs/node";
import react from "@astrojs/react";
import auditLog from "@emdash-cms/plugin-audit-log";
import { defineConfig, fontProviders } from "astro/config";
import emdash, { s3 } from "emdash/astro";
import { postgres } from "emdash/db";

export default defineConfig({
  output: "server",
  adapter: node({
    mode: "standalone",
  }),
  image: {
    layout: "constrained",
    responsiveStyles: true,
  },
  integrations: [
    react(),
    emdash({
      database: postgres({
        connectionString: process.env.POSTGRESQL_ADDON_URI,
      }),
      storage: s3({
        endpoint: `https://${process.env.CELLAR_ADDON_HOST}`,
        bucket: process.env.EMDASH_BUCKET,
        accessKeyId: process.env.CELLAR_ADDON_KEY_ID,
        secretAccessKey: process.env.CELLAR_ADDON_KEY_SECRET,
        region: "default",
      }),
      plugins: [auditLog],
    }),
  ],
  fonts: [
    {
      provider: fontProviders.google(),
      name: "Inter",
      cssVariable: "--font-body",
      weights: [400, 500, 600, 700],
      fallbacks: ["sans-serif"],
    },
    {
      provider: fontProviders.google(),
      name: "JetBrains Mono",
      cssVariable: "--font-mono",
      weights: [400, 500],
      fallbacks: ["monospace"],
    },
  ],
  devToolbar: { enabled: false },
});
```

EmDash [supports PostgreSQL for production Node.js deployments](https://docs.emdashcms.com/deployment/database/#postgresql). Its S3 adapter uses path-style addressing, signed uploads, and an application media endpoint, which are compatible with Cellar.

Initialize the Git repository:

```bash
git init
```

## Create the Clever Cloud resources

Install [Clever Tools](/developers/doc/cli/), log in, and create a Node.js application with an alias:

```bash
npm i -g clever-tools
clever login

clever create -t node -a myEmDash
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

You can display your application’s URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

Create and link a PostgreSQL add-on. Then create a Cellar add-on and keep its ID for the bucket configuration:

```bash
clever addon create postgresql-addon myEmDashPg -p xxs_sml -l myEmDash

CELLAR_ADDON_ID="$(
  clever addon create cellar-addon myEmDashCellar -l myEmDash -F json |
    jq --exit-status --raw-output '.id'
)"
```

The native links inject both add-ons’ variables into the application. You can alternatively create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

## Create the media bucket

Choose a globally unique bucket name and set the public application URL. Use the `.cleverapps.io` domain returned by `clever domain` or your custom domain:

```bash
EMDASH_BUCKET="your-unique-emdash-bucket"
EMDASH_URL="https://your-emdash-domain.example.com"
```

Load the Cellar credentials into the current shell without displaying them, then create the private bucket:

```bash
source <(clever addon env "$CELLAR_ADDON_ID" -F shell)

s3cmd --access_key="$CELLAR_ADDON_KEY_ID" \
  --secret_key="$CELLAR_ADDON_KEY_SECRET" \
  --host="$CELLAR_ADDON_HOST" \
  --host-bucket="$CELLAR_ADDON_HOST" \
  --ssl mb "s3://$EMDASH_BUCKET"
```

The EmDash administration interface uploads media directly to Cellar with signed URLs. Add an origin-specific [CORS policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) to allow these `PUT` requests from your application:

```bash
cat > emdash-cors.xml <<EOF
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>${EMDASH_URL}</AllowedOrigin>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
    <ExposeHeader>ETag</ExposeHeader>
    <MaxAgeSeconds>3600</MaxAgeSeconds>
  </CORSRule>
</CORSConfiguration>
EOF

s3cmd --access_key="$CELLAR_ADDON_KEY_ID" \
  --secret_key="$CELLAR_ADDON_KEY_SECRET" \
  --host="$CELLAR_ADDON_HOST" \
  --host-bucket="$CELLAR_ADDON_HOST" \
  --ssl setcors emdash-cors.xml "s3://$EMDASH_BUCKET"

rm emdash-cors.xml
unset CELLAR_ADDON_KEY_ID CELLAR_ADDON_KEY_SECRET CELLAR_ADDON_HOST
```

The bucket remains private. EmDash serves stored media through its application endpoint and only uses signed Cellar URLs for direct uploads.

## Configure and deploy EmDash

The project generator writes an `EMDASH_ENCRYPTION_KEY` to the ignored `.env` file. EmDash uses this key to [encrypt plugin secrets](https://docs.emdashcms.com/deployment/nodejs/#recommended-encryption-key). Back it up in a password manager or secret store, then add it and the public values to the application environment:

```bash
source .env

clever env set EMDASH_ENCRYPTION_KEY "$EMDASH_ENCRYPTION_KEY"
clever env set EMDASH_BUCKET "$EMDASH_BUCKET"
clever env set EMDASH_SITE_URL "$EMDASH_URL"
clever env set HOST 0.0.0.0
clever env set CC_POST_BUILD_HOOK "npm run build"

unset EMDASH_ENCRYPTION_KEY EMDASH_BUCKET EMDASH_URL CELLAR_ADDON_ID
```

`EMDASH_SITE_URL` defines the canonical origin used for passkeys, redirects, cross-site request forgery checks and other browser-facing features. `HOST` exposes Astro to Clever Cloud’s Request Flow, while the post-build hook generates the standalone server before the `start` script runs.

The EmDash build exceeds the memory available on the default XS build environment. Use a dedicated S build instance while keeping the run instance at its default XS size:

```bash
clever scale --build-flavor S
```

Commit the project and deploy it:

```bash
git add .
git commit -m "First deploy"

clever deploy
```

Open the administration interface and follow the setup wizard. The first administrator uses a passkey, so complete this step from a browser and device that support [WebAuthn](https://www.w3.org/TR/webauthn-3/):

```bash
clever open
```

The wizard configures the site and creates the first administrator. PostgreSQL preserves this configuration and your content across rebuilds, while Cellar stores uploaded media.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/addons/cellar/" title="Cellar" subtitle="Manage S3-compatible object storage" icon="cellar" >}}
  {{< card link="/developers/doc/applications/nodejs/" title="Node.js" subtitle="Configure and deploy Node.js applications" icon="node" >}}
  {{< card link="/developers/doc/addons/postgresql/" title="PostgreSQL" subtitle="Manage PostgreSQL databases" icon="pg" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://docs.emdashcms.com/" title="EmDash documentation" subtitle="Configure and use EmDash" icon="emdash" >}}
{{< /cards >}}
