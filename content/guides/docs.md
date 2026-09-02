---
type: docs
linkTitle: Docs
title: Deploy Docs, a collaborative document editor
description: Deploy Docs with a Python backend, a static frontend, collaborative editing, Keycloak authentication and private Cellar storage
keywords:
- cellar
- collaborative editor
- docs
- keycloak
- node.js
- postgresql
- python
- redis
---

{{< hextra/hero-subtitle >}}
  Deploy Docs, an open source collaborative document editor, on Clever Cloud.
{{< /hextra/hero-subtitle >}}

[Docs](https://github.com/suitenumerique/docs) combines a Django API, a Next.js static frontend and a Node.js collaboration server. This guide deploys these components with [PostgreSQL](/developers/doc/addons/postgresql/), [Redis](/developers/doc/addons/redis/), [Cellar S3-compatible object storage](/developers/doc/addons/cellar/) and [Keycloak](/developers/doc/addons/keycloak/).

The deployment uses one custom domain and [path routing](/developers/doc/administrate/domain-names/#path-routing) to expose the following applications:

| Application   | Runtime | Route                                     | Purpose                                         |
| ------------- | ------- | ----------------------------------------- | ----------------------------------------------- |
| Backend       | Python  | `/api/`                                   | API, authentication and database migrations     |
| Collaboration | Node.js | `/collaboration/` and `/api/convert/`     | Live editing and document conversion            |
| Frontend      | Static  | `/`                                       | Browser application                             |
| Media proxy   | Linux   | `/media/`                                 | Authenticated access to private Cellar objects  |

Docs authorizes each media request before signing it for Cellar. The small [Caddy](https://caddyserver.com/) proxy configured below reproduces the authorization flow used by Docs' official ingress without making the bucket public.

## Prepare Docs

You need [Git](https://git-scm.com/downloads), [jq](https://jqlang.org/download/), [OpenSSL](https://openssl-library.org/), [s3cmd](https://s3tools.org/s3cmd) or another S3-compatible client, a custom domain and a [Clever Cloud account](https://console.clever-cloud.com/) to follow this guide.

This guide was tested with Docs `5.5.0`. Set the version to deploy, clone its tag and create a branch for the Clever Cloud configuration:

```bash
export DOCS_VERSION=v5.5.0
git clone --branch "$DOCS_VERSION" https://github.com/suitenumerique/docs.git myDocs
cd myDocs
git switch -c clever-deployment
```

### Configure the backend commands

Create the following helper at the repository root:

```bash {filename="clevercloud.sh"}
#!/usr/bin/env bash
set -eu

export DATABASE_URL="${POSTGRESQL_ADDON_URI}"
export AWS_S3_ENDPOINT_URL="https://${CELLAR_ADDON_HOST}"
export AWS_S3_ACCESS_KEY_ID="${CELLAR_ADDON_KEY_ID}"
export AWS_S3_SECRET_ACCESS_KEY="${CELLAR_ADDON_KEY_SECRET}"

mkdir -p "${DATA_DIR}"

if [[ -d src/backend ]]; then
  cd src/backend
fi

case "${1:-}" in
  migrate)
    uv run python manage.py migrate --no-input
    ;;
  run)
    uv run uvicorn --host 0.0.0.0 --port "${PORT:-8080}" --timeout-graceful-shutdown 300 --limit-max-requests 20000 --lifespan off impress.asgi:application
    ;;
  *)
    printf 'Usage: %s migrate|run\n' "$0" >&2
    exit 1
    ;;
esac
```

Make it executable:

```bash
chmod +x clevercloud.sh
```

The build hook runs migrations after dependencies are installed. The run command starts the ASGI application with Uvicorn. The helper works from both the repository root used by build hooks and `src/backend`, where the Python runtime starts the application.

### Configure the private media proxy

[Mise is available on Clever Cloud](/developers/doc/reference/reference-environment-variables/#install-tools-with-mise-package-manager). Create a dedicated directory and declare Caddy through Mise's GitHub backend:

```bash
mkdir media-proxy
```

```toml {filename="media-proxy/mise.toml"}
[tools]
"github:caddyserver/caddy" = "2.10.2"

[tasks.build]
description = "Install and verify Caddy"
run = "caddy version"

[tasks.run]
description = "Start the authenticated media proxy"
run = "caddy run --config Caddyfile"
```

The `build` and `run` names are significant: the Linux runtime uses these [Mise tasks](https://mise.jdx.dev/tasks/) for its separate build and run phases. Create the proxy configuration:

```caddyfile {filename="media-proxy/Caddyfile"}
:{$PORT:8080} {
  handle /media/* {
    route {
      forward_auth https://{$DOCS_BACKEND_HOST} {
        uri /api/v1.0/documents/media-auth/
        header_up Host {$DOCS_BACKEND_HOST}
        header_up X-Forwarded-Proto https
        header_up X-Original-URL {uri}
        copy_headers Authorization X-Amz-Date X-Amz-Content-SHA256
      }

      uri strip_prefix /media
      rewrite * /{$AWS_STORAGE_BUCKET_NAME}{uri}
      reverse_proxy https://{$CELLAR_HOST} {
        header_up Host {$CELLAR_HOST}
      }
    }
  }

  respond 404
}
```

The [`forward_auth`](https://caddyserver.com/docs/caddyfile/directives/forward_auth) request asks Docs whether the current user can access the object. Docs returns AWS authorization headers for allowed requests, which Caddy forwards to Cellar. The [`route`](https://caddyserver.com/docs/caddyfile/directives/route) block preserves the declared directive order so the `/media` prefix is removed before the bucket name is added to the signed S3 path.

## Create the applications and add-ons

Install [Clever Tools](/developers/doc/cli/), log in and create the four applications with aliases:

```bash
npm i -g clever-tools
clever login

clever create -t python myDocsBackend -a myDocsBackend
clever create -t static myDocsFrontend -a myDocsFrontend
clever create -t node myDocsCollaboration -a myDocsCollaboration
clever create -t linux myDocsMedia -a myDocsMedia
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

Create PostgreSQL, Redis and Cellar add-ons linked to the backend, then create a Keycloak add-on:

```bash
clever addon create postgresql-addon myDocsPostgreSQL -p xxs_sml -l myDocsBackend
clever addon create redis-addon myDocsRedis -p s_mono -l myDocsBackend
clever addon create cellar-addon myDocsCellar -l myDocsBackend
clever addon create keycloak myDocsKeycloak -p base
```

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

## Configure Cellar

Cellar bucket names are global within a cluster. Choose a unique name containing only lowercase letters, numbers, dots and hyphens:

```bash
export DOCS_BUCKET="your-unique-docs-bucket"
```

Read the Cellar configuration, create the private bucket and keep its hostname for the application configuration:

```bash
CELLAR_ENV="$(clever addon env myDocsCellar -F json)"
export CELLAR_HOST="$(jq -er '.CELLAR_ADDON_HOST' <<<"$CELLAR_ENV")"
CELLAR_KEY_ID="$(jq -er '.CELLAR_ADDON_KEY_ID' <<<"$CELLAR_ENV")"
CELLAR_KEY_SECRET="$(jq -er '.CELLAR_ADDON_KEY_SECRET' <<<"$CELLAR_ENV")"

s3cmd --access_key="$CELLAR_KEY_ID" \
  --secret_key="$CELLAR_KEY_SECRET" \
  --host="$CELLAR_HOST" \
  --host-bucket="$CELLAR_HOST" \
  --ssl mb "s3://$DOCS_BUCKET"

unset CELLAR_ENV CELLAR_KEY_ID CELLAR_KEY_SECRET
```

Do not add a public bucket policy. The media proxy uses the current Docs session and short-lived AWS authorization headers to protect uploaded files.

## Configure the shared domain

Store your custom domain and its HTTPS origin, then assign the root and path routes to their applications:

```bash
export DOCS_DOMAIN="docs.your.website.tld"
export DOCS_URL="https://$DOCS_DOMAIN"

clever domain add "$DOCS_DOMAIN" -a myDocsFrontend
clever domain add "$DOCS_DOMAIN/api/" -a myDocsBackend
clever domain add "$DOCS_DOMAIN/collaboration/" -a myDocsCollaboration
clever domain add "$DOCS_DOMAIN/api/convert/" -a myDocsCollaboration
clever domain add "$DOCS_DOMAIN/media/" -a myDocsMedia
```

Configure the required [DNS record](/developers/doc/administrate/domain-names/) for the custom domain. Keep the trailing slash on each path route.

## Configure Keycloak

Wait for the Keycloak add-on to start, then display its URL and open its administration interface:

```bash
export KEYCLOAK_URL="$(clever keycloak get myDocsKeycloak -F json | jq -er '.accessUrl | sub("/admin$"; "")')"
clever keycloak open myDocsKeycloak
```

Use the initial credentials displayed by Clever Cloud. Keycloak asks you to replace the temporary password on first login.

In the Keycloak administration interface:

1. Create a realm named `impress`
2. Create an OpenID Connect client with `impress` as its client ID
3. Enable client authentication and the standard flow
4. Set the root and home URLs to the value of `DOCS_URL`
5. Add `$DOCS_URL/api/v1.0/callback/*` to the valid redirect URIs
6. Add `$DOCS_URL/*` to the valid post-logout redirect URIs
7. Add the value of `DOCS_URL` to the web origins
8. Copy the client secret from the client credentials tab

Create users directly in the realm or configure one of [Keycloak's identity providers](https://www.keycloak.org/docs/latest/server_admin/#_identity_broker). Store the copied client secret in your shell before continuing:

```bash
export OIDC_CLIENT_SECRET="replace-with-the-impress-client-secret"
```

## Configure the applications

Generate independent secrets for Django and the two collaboration authentication mechanisms:

```bash
export DJANGO_SECRET_KEY="$(openssl rand -base64 48)"
export COLLABORATION_SERVER_SECRET="$(openssl rand -base64 48)"
export Y_PROVIDER_API_KEY="$(openssl rand -base64 48)"
```

### Backend

Configure the Python runtime, public URLs, linked services, collaboration server and Keycloak client:

```bash
clever env set APP_FOLDER src/backend -a myDocsBackend
clever env set CC_PYTHON_VERSION 3.14 -a myDocsBackend
clever env set CC_POST_BUILD_HOOK './clevercloud.sh migrate' -a myDocsBackend
clever env set CC_PYTHON_UV_RUN_COMMAND '../../clevercloud.sh run' -a myDocsBackend
clever env set DATA_DIR /tmp/docs -a myDocsBackend

clever env set DJANGO_CONFIGURATION Production -a myDocsBackend
clever env set DJANGO_SETTINGS_MODULE impress.settings -a myDocsBackend
clever env set DJANGO_SECRET_KEY "$DJANGO_SECRET_KEY" -a myDocsBackend
clever env set DJANGO_ALLOWED_HOSTS "$DOCS_DOMAIN" -a myDocsBackend
clever env set DJANGO_CSRF_TRUSTED_ORIGINS "$DOCS_URL" -a myDocsBackend
clever env set CORS_ALLOWED_ORIGINS "$DOCS_URL" -a myDocsBackend
clever env set IMPRESS_BASE_URL "$DOCS_URL" -a myDocsBackend
clever env set LOGIN_REDIRECT_URL "$DOCS_URL" -a myDocsBackend
clever env set LOGIN_REDIRECT_URL_FAILURE "$DOCS_URL" -a myDocsBackend
clever env set LOGOUT_REDIRECT_URL "$DOCS_URL" -a myDocsBackend

clever env set AWS_STORAGE_BUCKET_NAME "$DOCS_BUCKET" -a myDocsBackend
clever env set AWS_S3_REGION_NAME auto -a myDocsBackend
clever env set AWS_REQUEST_CHECKSUM_CALCULATION when_required -a myDocsBackend
clever env set AWS_RESPONSE_CHECKSUM_VALIDATION when_required -a myDocsBackend

clever env set COLLABORATION_API_URL "$DOCS_URL/collaboration/api/" -a myDocsBackend
clever env set COLLABORATION_WS_URL "wss://$DOCS_DOMAIN/collaboration/ws/" -a myDocsBackend
clever env set COLLABORATION_SERVER_SECRET "$COLLABORATION_SERVER_SECRET" -a myDocsBackend
clever env set Y_PROVIDER_API_BASE_URL "$DOCS_URL/" -a myDocsBackend
clever env set Y_PROVIDER_API_KEY "$Y_PROVIDER_API_KEY" -a myDocsBackend

clever env set OIDC_OP_AUTHORIZATION_ENDPOINT "$KEYCLOAK_URL/realms/impress/protocol/openid-connect/auth" -a myDocsBackend
clever env set OIDC_OP_JWKS_ENDPOINT "$KEYCLOAK_URL/realms/impress/protocol/openid-connect/certs" -a myDocsBackend
clever env set OIDC_OP_LOGOUT_ENDPOINT "$KEYCLOAK_URL/realms/impress/protocol/openid-connect/logout" -a myDocsBackend
clever env set OIDC_OP_TOKEN_ENDPOINT "$KEYCLOAK_URL/realms/impress/protocol/openid-connect/token" -a myDocsBackend
clever env set OIDC_OP_USER_ENDPOINT "$KEYCLOAK_URL/realms/impress/protocol/openid-connect/userinfo" -a myDocsBackend
clever env set OIDC_REDIRECT_ALLOWED_HOSTS "$DOCS_DOMAIN" -a myDocsBackend
clever env set OIDC_RP_CLIENT_ID impress -a myDocsBackend
clever env set OIDC_RP_CLIENT_SECRET "$OIDC_CLIENT_SECRET" -a myDocsBackend
clever env set OIDC_RP_SCOPES 'openid email profile' -a myDocsBackend
clever env set OIDC_RP_SIGN_ALGO RS256 -a myDocsBackend
clever env set OIDC_USERINFO_FULLNAME_FIELDS 'given_name,family_name' -a myDocsBackend
clever env set OIDC_USERINFO_SHORTNAME_FIELD preferred_username -a myDocsBackend
```

The helper maps the linked PostgreSQL and Cellar variables to the names expected by Docs. The linked Redis add-on already provides the required `REDIS_URL`.

### Frontend

Docs exports its Next.js frontend as a static site. Configure the Static runtime and use an `L` build instance, which is required by the current frontend build:

```bash
clever env set APP_FOLDER src/frontend -a myDocsFrontend
clever env set CC_NODE_VERSION 22 -a myDocsFrontend
clever env set CC_BUILD_COMMAND '. /home/bas/.nvm/nvm.sh && nvm use "$CC_NODE_VERSION" && yarn install --frozen-lockfile && yarn app:build' -a myDocsFrontend
clever env set CC_WEBROOT /src/frontend/apps/impress/out -a myDocsFrontend
clever env set NEXT_PUBLIC_API_BASE_PATH / -a myDocsFrontend
clever env set NEXT_PUBLIC_API_ORIGIN "$DOCS_URL" -a myDocsFrontend
clever env set NEXT_PUBLIC_PUBLISH_AS_MIT true -a myDocsFrontend
clever env set NEXT_PUBLIC_SW_DEACTIVATED true -a myDocsFrontend
clever env set NODE_OPTIONS --max-old-space-size=4096 -a myDocsFrontend
clever scale --build-flavor L -a myDocsFrontend
```

The explicit `nvm use` keeps the custom Static build command on Node.js 22. The frontend currently rejects the newer system Node.js version otherwise selected before the command starts.

### Collaboration server

Configure the Node.js application from the frontend workspace:

```bash
clever env set APP_FOLDER src/frontend -a myDocsCollaboration
clever env set CC_NODE_VERSION 22 -a myDocsCollaboration
clever env set CC_NODE_BUILD_TOOL yarn -a myDocsCollaboration
clever env set CC_NODE_DEV_DEPENDENCIES true -a myDocsCollaboration
clever env set CC_POST_BUILD_HOOK 'cd src/frontend && yarn COLLABORATION_SERVER build' -a myDocsCollaboration
clever env set CC_RUN_COMMAND 'cd src/frontend && yarn COLLABORATION_SERVER start' -a myDocsCollaboration
clever env set COLLABORATION_BACKEND_BASE_URL "$DOCS_URL" -a myDocsCollaboration
clever env set COLLABORATION_LOGGING true -a myDocsCollaboration
clever env set COLLABORATION_SERVER_ORIGIN "$DOCS_URL" -a myDocsCollaboration
clever env set COLLABORATION_SERVER_SECRET "$COLLABORATION_SERVER_SECRET" -a myDocsCollaboration
clever env set Y_PROVIDER_API_KEY "$Y_PROVIDER_API_KEY" -a myDocsCollaboration
```

Custom build and run hooks start from the repository root, so both commands explicitly enter `src/frontend` despite `APP_FOLDER`.

### Media proxy

Point the Linux runtime to the nested Mise configuration and provide only the non-secret routing values required by Caddy:

```bash
clever env set CC_MISE_FILE_PATH media-proxy/mise.toml -a myDocsMedia
clever env set DOCS_BACKEND_HOST "$DOCS_DOMAIN" -a myDocsMedia
clever env set CELLAR_HOST "$CELLAR_HOST" -a myDocsMedia
clever env set AWS_STORAGE_BUCKET_NAME "$DOCS_BUCKET" -a myDocsMedia
```

The media proxy does not receive Cellar credentials. Docs signs each authorized request and Caddy only forwards the resulting headers.

## Deploy Docs

Commit the Clever Cloud configuration, then deploy the backend, collaboration server, frontend and media proxy from the same repository:

```bash
git add clevercloud.sh media-proxy
git commit -m "Configure Clever Cloud deployment"

clever deploy -a myDocsBackend
clever deploy -a myDocsCollaboration
clever deploy -a myDocsFrontend
clever deploy -a myDocsMedia
```

Open Docs, sign in through Keycloak, create a document and upload an image to verify the complete deployment:

```bash
clever open -a myDocsFrontend
```

You can also check the public configuration endpoint and confirm that an anonymous media request is rejected:

```bash
curl -sS "$DOCS_URL/api/v1.0/config/" | jq .
curl -sS -o /dev/null -w '%{http_code}\n' "$DOCS_URL/media/not-authorized"
```

The second command returns `403`, as expected for a private object without a Docs session.

## Update Docs

Review the [Docs releases](https://github.com/suitenumerique/docs/releases), back up PostgreSQL and replace `vX.Y.Z` below with the selected tag before rebasing the deployment configuration onto it:

```bash
export DOCS_VERSION=vX.Y.Z
git fetch origin --tags
git rebase "$DOCS_VERSION"

clever deploy -a myDocsBackend
clever deploy -a myDocsCollaboration
clever deploy -a myDocsFrontend
clever deploy -a myDocsMedia
```

The backend build hook applies pending migrations. Keep the versions in the runtime configuration aligned with the requirements of the selected Docs release.

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://github.com/suitenumerique/docs" title="Docs source code" subtitle="Review releases, configuration and upstream deployment resources" icon="github" >}}
  {{< card link="/developers/doc/applications/python/" title="Python applications" subtitle="Configure and deploy Python applications" icon="python" >}}
  {{< card link="/developers/doc/applications/static/" title="Static applications" subtitle="Build and deploy static applications" icon="static" >}}
  {{< card link="/developers/doc/applications/nodejs/" title="Node.js applications" subtitle="Configure and deploy Node.js applications" icon="node" >}}
  {{< card link="/developers/doc/applications/linux/" title="Linux applications" subtitle="Configure and deploy any applications" icon="linux" >}}
  {{< card link="/developers/doc/addons/postgresql/" title="PostgreSQL" subtitle="Store persistent application data" icon="circle-stack" >}}
  {{< card link="/developers/doc/addons/redis/" title="Redis" subtitle="Configure the managed in-memory data store" icon="redis" >}}
  {{< card link="/developers/doc/addons/cellar/" title="Cellar" subtitle="Store files in S3-compatible object storage" icon="cellar" >}}
  {{< card link="/developers/doc/addons/keycloak/" title="Keycloak" subtitle="Configure the managed identity and access service" icon="keycloak" >}}
{{< /cards >}}
