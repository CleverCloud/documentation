---
type: docs
linkTitle: Outline
title: Deploy self-hosted Outline
description: Deploy the Outline knowledge base on Clever Cloud with PostgreSQL, Redis, and Cellar object storage
keywords:
- outline
- knowledge base
- wiki
- node.js
- postgresql
- redis
- cellar
---

{{< hextra/hero-subtitle >}}
  Deploy Outline, an open source knowledge base for teams, on Clever Cloud.
{{< /hextra/hero-subtitle >}}

[Outline](https://www.getoutline.com/) is a collaborative knowledge base and wiki. This guide deploys it on the [Linux runtime](/developers/doc/applications/linux/) with [Mise](https://mise.jdx.dev/), [PostgreSQL](/developers/doc/addons/postgresql/), [Redis](/developers/doc/addons/redis/), and [Cellar S3-compatible object storage](/developers/doc/addons/cellar/). Outline recommends Docker for self-hosted installations, but it also [documents installation from source](https://docs.getoutline.com/s/hosting/doc/from-source-BlBxrNzMIP).

## Prepare the application

You need [Git](https://git-scm.com/downloads), [OpenSSL](https://openssl-library.org/), and an S3-compatible client to follow this guide. The commands below use [s3cmd](https://s3tools.org/s3cmd), but you can adapt them to another S3-compatible client.

Create a directory for the deployment configuration:

```bash
mkdir myOutline
cd myOutline
git init
```

This guide targets Outline `v1.9.2`. To deploy another Outline release, adjust `OUTLINE_VERSION` and `CC_NODE_VERSION` as described below.

[Mise is available on Clever Cloud](/developers/doc/reference/reference-environment-variables/#install-tools-with-mise-package-manager). Create the following `mise.toml` file to download the selected Outline release during the build phase, install its dependencies, and define the commands used by the Linux runtime:

```toml {filename="mise.toml"}
[tools."http:outline"]
version = "{{ get_env(name='OUTLINE_VERSION', default='v1.9.2') }}"
url = "https://github.com/outline/outline/archive/refs/tags/{{ version }}.tar.gz"
strip_components = 1

[tasks.build]
description = "Build the selected Outline release"
run = '''
set -euo pipefail
mkdir outline
cp -a '{{ tools["http:outline"].path }}/.' outline/
cd outline
corepack enable
yarn install --immutable
yarn build
yarn workspaces focus --production
yarn cache clean
'''

[tasks.run]
description = "Start Outline"
run = "bash run.sh"
```

The [HTTP backend](https://mise.jdx.dev/dev-tools/backends/http.html) downloads and extracts the source archive. The `build` and `run` names are significant: the Linux runtime automatically uses these [Mise tasks](https://mise.jdx.dev/tasks/) for its separate build and run phases.

Create a startup script that maps the variables injected by linked Clever Cloud add-ons to the names expected by Outline:

```bash {filename="run.sh"}
#!/usr/bin/env bash
set -euo pipefail

export DATABASE_URL="${POSTGRESQL_ADDON_URI}"
export REDIS_COLLABORATION_URL="${REDIS_URL}"
export AWS_ACCESS_KEY_ID="${CELLAR_ADDON_KEY_ID}"
export AWS_SECRET_ACCESS_KEY="${CELLAR_ADDON_KEY_SECRET}"
export AWS_S3_UPLOAD_BUCKET_URL="https://${CELLAR_ADDON_HOST}"

cd outline
node build/server/index.js
```

The linked Redis add-on provides `REDIS_URL`, which the script also maps to `REDIS_COLLABORATION_URL` to synchronize collaborative editing between Outline processes and application instances. Outline automatically applies pending database migrations when it starts, so no separate migration command is needed.

## Create the application and add-ons

Install [Clever Tools](/developers/doc/cli/), log in, and create a Linux application with an alias used to link the add-ons:

```bash
npm i -g clever-tools
clever login

clever create -t linux -a myOutline
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

Create PostgreSQL, Redis, and Cellar add-ons, then link them to the application:

```bash
clever addon create postgresql-addon myOutlinePostgreSQL -p xxs_sml --link myOutline
clever addon create redis-addon myOutlineRedis -p s_mono --link myOutline
clever addon create cellar-addon myOutlineCellar --link myOutline
```

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

## Configure Cellar

Outline stores uploaded files in a private S3 bucket and gives authenticated users temporary download URLs. Bucket names are global within a Cellar cluster, so choose a unique name containing only lowercase letters, numbers, dots, and hyphens:

```bash
export OUTLINE_BUCKET="your-unique-outline-bucket"
```

Export only the linked Cellar add-on variables to your current shell, then create the bucket:

```bash
source <(clever env -F shell | grep '^export CELLAR_ADDON_')

s3cmd --access_key="$CELLAR_ADDON_KEY_ID" \
  --secret_key="$CELLAR_ADDON_KEY_SECRET" \
  --host="$CELLAR_ADDON_HOST" \
  --host-bucket="$CELLAR_ADDON_HOST" \
  --ssl mb "s3://$OUTLINE_BUCKET"
```

Direct uploads from the browser require a [CORS policy](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing). Display the application domain to get the exact HTTPS origin:

```bash
clever domain
```

Create the following file and replace `https://your-outline-domain.example.com` with that origin. Browser write requests are allowed from your Outline application's origin, while downloads can use the temporary URLs generated by Outline:

```xml {filename="cors.xml"}
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>https://your-outline-domain.example.com</AllowedOrigin>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
  </CORSRule>
  <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
  </CORSRule>
</CORSConfiguration>
```

Apply the policy, then remove the credentials from your shell. Keep the `OUTLINE_BUCKET` value exported for use in the next section:

```bash
s3cmd --access_key="$CELLAR_ADDON_KEY_ID" \
  --secret_key="$CELLAR_ADDON_KEY_SECRET" \
  --host="$CELLAR_ADDON_HOST" \
  --host-bucket="$CELLAR_ADDON_HOST" \
  --ssl setcors cors.xml "s3://$OUTLINE_BUCKET"

rm cors.xml
unset CELLAR_ADDON_KEY_ID CELLAR_ADDON_KEY_SECRET CELLAR_ADDON_HOST
```

The bucket remains private: Outline signs file downloads, so it does not need a public-read bucket policy.

## Configure Outline

Store the application domain in a shell variable (`app-id.cleverapps.io` or your custom domain):

```bash
export OUTLINE_URL="https://your-outline-domain.example.com"
```

Generate two independent secrets and configure the Outline release, Node.js, public URL, and object storage. The `CC_NODE_VERSION` value must match one of the ranges accepted by `engines.node` in the `package.json` of the selected Outline release:

```bash
# Use a value accepted by engines.node for the selected Outline release:
# https://github.com/outline/outline/blob/v1.9.2/package.json#L44-L46
clever env set OUTLINE_VERSION v1.9.2
clever env set CC_NODE_VERSION 26.3.0
clever env set CC_NODE_BUILD_TOOL yarn-berry

clever env set SECRET_KEY "$(openssl rand -hex 32)"
clever env set UTILS_SECRET "$(openssl rand -base64 32)"
clever env set NODE_ENV production
clever env set WEB_CONCURRENCY 1
clever env set DEFAULT_LANGUAGE en_US
clever env set URL "$OUTLINE_URL"
clever env set FILE_STORAGE s3
clever env set FILE_STORAGE_UPLOAD_MAX_SIZE 262144000
clever env set AWS_REGION default
clever env set AWS_S3_UPLOAD_BUCKET_NAME "$OUTLINE_BUCKET"
```

Outline requires `SECRET_KEY` to contain exactly 64 hexadecimal characters, while `UTILS_SECRET` accepts the Base64 value. Clever Cloud provides the application `PORT`. The linked add-ons provide their credentials, so they do not need to be copied into the application environment.

`WEB_CONCURRENCY` controls the number of Outline processes started inside each application instance. Outline recommends roughly one process per 512 MB of available memory, so this guide keeps the value at `1` for the default `XS` run instance. Increase it only on a larger instance and after monitoring the application's memory and CPU usage. The `REDIS_COLLABORATION_URL` mapping in the startup script follows Outline's [horizontal scaling documentation](https://docs.getoutline.com/s/hosting/doc/horizontal-scaling-hkfU5Stao7), so collaborative editing remains synchronized if you later run several processes or application instances.

`DEFAULT_LANGUAGE` controls the default interface language; replace `en_US` with another [Outline language code](https://translate.getoutline.com/) if needed. `FILE_STORAGE_UPLOAD_MAX_SIZE` is expressed in bytes: `262144000` sets a 250 MiB attachment limit and matches Outline's [versioned environment sample](https://github.com/outline/outline/blob/v1.9.2/.env.sample). You can configure a larger value, but Outline applies it to the [`content-length-range` condition of each presigned S3 upload](https://github.com/outline/outline/blob/v1.9.2/server/storage/files/S3Storage.ts#L44-L67), so test the intended size with your network and storage service before increasing it. Document and workspace imports can use separate limits; see Outline's [file storage documentation](https://docs.getoutline.com/s/hosting/doc/file-storage-N4M0T6Ypu7).

Outline's dependency installation and client build need more memory than the default build instance provides. Use an `M` instance for the build phase; the application keeps the default `XS` instance for its runtime:

```bash
clever scale --build-flavor M
```

### Configure authentication

Outline needs at least one authentication method before users can sign in and supports the following methods:

| Authentication method | Required variables | Callback URL |
| --- | --- | --- |
| Discord | `DISCORD_CLIENT_ID`, `DISCORD_CLIENT_SECRET` | `$URL/auth/discord.callback` |
| Email magic links | `SMTP_HOST` or `SMTP_SERVICE`, `SMTP_FROM_EMAIL` | — |
| Google | `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | `$URL/auth/google.callback` |
| Microsoft Entra ID | `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` | `$URL/auth/azure.callback` |
| OpenID Connect | `OIDC_CLIENT_ID`, `OIDC_CLIENT_SECRET`, `OIDC_ISSUER_URL` | `$URL/auth/oidc.callback` |
| Slack | `SLACK_CLIENT_ID`, `SLACK_CLIENT_SECRET` | `$URL/auth/slack.callback` |

Email magic links require a complete [SMTP configuration](https://docs.getoutline.com/s/hosting/doc/smtp-cqCJyZGMIB), including the credentials and connection settings required by your email provider. Configure the matching callback URL in your provider, then set its variables. For OpenID Connect, also allow the application URL (`$URL`) as a post-logout redirect URI if the provider exposes a logout endpoint. For example:

```bash
clever env set OIDC_CLIENT_ID "YOUR_CLIENT_ID"
clever env set OIDC_CLIENT_SECRET "A_STRONG_CLIENT_SECRET"
clever env set OIDC_ISSUER_URL "https://your-provider.example.com"
clever env set OIDC_DISPLAY_NAME "Company SSO"
```

Once signed in, users can also register passkeys for subsequent authentication. The first user to create an Outline workspace becomes its administrator. SAML authentication is only available in licensed editions.

## Deploy Outline

Commit the deployment configuration and deploy the application:

```bash
git add mise.toml run.sh
git commit -m "First deploy"

clever deploy
```

Outline builds its client and server during the build phase, then starts and applies pending PostgreSQL migrations during the run phase. Check that PostgreSQL and Redis are reachable with its health endpoint:

```bash
curl "$OUTLINE_URL/_health"
```

It returns `OK` when both dependencies are available. You can then open Outline and sign in with the authentication provider you configured:

```bash
clever open
```

## Update Outline

Make sure you have a recent [PostgreSQL backup](/developers/doc/addons/postgresql/#database-daily-backup-and-retention) before updating. Check the `engines.node` requirements in the `package.json` of the Outline release you want to deploy, such as the [file for v1.9.2](https://github.com/outline/outline/blob/v1.9.2/package.json#L44-L46). Update both version variables when necessary, then rebuild the current commit so Mise downloads and builds the new release. For example, these commands update an older deployment to Outline v1.9.2:

```bash
clever env set OUTLINE_VERSION v1.9.2
clever env set CC_NODE_VERSION 26.3.0
clever restart --without-cache
```

Replace the example values with the versions you selected. Outline applies pending database migrations when the new version starts.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/linux" title="Linux application runtime" subtitle="Configure and deploy any application" icon="linux" >}}
  {{< card link="/developers/doc/addons/postgresql" title="PostgreSQL" subtitle="Explore managed PostgreSQL databases" icon="pg" >}}
  {{< card link="/developers/doc/addons/redis" title="Redis" subtitle="Explore managed Redis databases" icon="redis" >}}
  {{< card link="/developers/doc/addons/cellar" title="Cellar" subtitle="Explore S3-compatible object storage" icon="fsbucket" >}}
  {{< card link="https://docs.getoutline.com/s/hosting" title="Outline hosting documentation" subtitle="Learn more about self-hosting Outline" icon="outline" >}}
{{< /cards >}}
