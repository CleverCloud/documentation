---
type: docs
linkTitle: Ghost
title: Deploy a self-hosted Ghost 6 publication
description: Deploy Ghost on Clever Cloud with MySQL, Cellar object storage and an FS Bucket
keywords:
- blogging
- cellar
- ghost
- linux
- mise
- mysql
- publishing
- s3 storage
---

{{< hextra/hero-subtitle >}}
  Deploy Ghost, an open source publishing platform, on Clever Cloud.
{{< /hextra/hero-subtitle >}}

[Ghost](https://ghost.org/) is a publishing platform for websites, memberships and newsletters. This guide deploys Ghost on the [Linux runtime](/developers/doc/applications/linux/) with [Mise](https://mise.jdx.dev/), [MySQL](/developers/doc/addons/mysql/), [Cellar S3-compatible object storage](/developers/doc/addons/cellar/) and an [FS Bucket](/developers/doc/addons/fs-bucket/).

MySQL stores publications, users and settings. Cellar stores uploaded images, media and files through Ghost's built-in S3 storage adapter. The FS Bucket persists themes and routing configuration uploaded from Ghost Admin.

## Prepare the application

You need [Git](https://git-scm.com/downloads), [jq](https://jqlang.org/download/), [s3cmd](https://s3tools.org/s3cmd) or any other S3-compatible client, and a [Clever Cloud account](https://console.clever-cloud.com/) to follow this guide.

Create a directory and initialize its Git repository:

```bash
mkdir myGhost
cd myGhost
git init
```

This guide targets Ghost `6.60.0`. To deploy another release, adapt `GHOST_VERSION` and use a Node.js version accepted by that release as described in the update section.

[Mise is available on Clever Cloud](/developers/doc/reference/reference-environment-variables/#install-tools-with-mise-package-manager). Create the following `mise.toml` file to download the selected Ghost release, install its production dependencies and define the commands used by the Linux runtime:

```toml {filename="mise.toml"}
[tools]
node = "{{ env.CC_NODE_VERSION }}"

[tools."http:ghost"]
version = "{{ get_env(name='GHOST_VERSION', default='6.60.0') }}"
url = "https://registry.npmjs.org/ghost/-/ghost-{{ version }}.tgz"
strip_components = 1

[env]
database__client = "mysql"
database__connection__host = "{{ env.MYSQL_ADDON_HOST }}"
database__connection__port = "{{ env.MYSQL_ADDON_PORT }}"
database__connection__user = "{{ env.MYSQL_ADDON_USER }}"
database__connection__password = "{{ env.MYSQL_ADDON_PASSWORD }}"
database__connection__database = "{{ env.MYSQL_ADDON_DB }}"
logging__transports = '["stdout"]'
paths__contentPath = "{{ env.APP_HOME }}/content"
server__host = "0.0.0.0"
server__port = "{{ env.PORT }}"
storage__active = "S3Storage"
storage__S3Storage__bucket = "{{ env.GHOST_BUCKET }}"
storage__S3Storage__staticFileURLPrefix = "content/images"
storage__S3Storage__cdnUrl = "https://{{ env.CELLAR_ADDON_HOST }}/{{ env.GHOST_BUCKET }}"
storage__S3Storage__region = "default"
storage__S3Storage__endpoint = "https://{{ env.CELLAR_ADDON_HOST }}"
storage__S3Storage__forcePathStyle = "true"
storage__S3Storage__accessKeyId = "{{ env.CELLAR_ADDON_KEY_ID }}"
storage__S3Storage__secretAccessKey = "{{ env.CELLAR_ADDON_KEY_SECRET }}"

# Multipart uploads start at 10 MiB; this threshold can be increased up to 5 GiB
# Chunks can be increased from 5 MiB up to 5 GiB, with at most 10,000 per upload
storage__S3Storage__multipartUploadThresholdBytes = "10485760"
storage__S3Storage__multipartChunkSizeBytes = "5242880"
storage__media__adapter = "S3Storage"
storage__media__staticFileURLPrefix = "content/media"
storage__files__adapter = "S3Storage"
storage__files__staticFileURLPrefix = "content/files"

[tasks.build]
description = "Install Ghost and seed default content"
run = '''
set -euo pipefail
mkdir ghost
cp -a '{{ tools["http:ghost"].path }}/.' ghost/
mv ghost/content ghost-default-content
cd ghost
corepack enable pnpm
pnpm install --prod --frozen-lockfile
mkdir -p "$APP_HOME/content"
cp -a -n "$APP_HOME/ghost-default-content/." "$APP_HOME/content/"
'''

[tasks.run]
description = "Start Ghost"
dir = "ghost"
run = "node index.js"
```

The [HTTP backend](https://mise.jdx.dev/dev-tools/backends/http.html) downloads and extracts the official npm package for the selected Ghost release. The `build` and `run` names are significant: the Linux runtime automatically uses these [Mise tasks](https://mise.jdx.dev/tasks/) for its separate build and run phases. At the end of a successful build, the build task copies only missing default content to persistent storage. Ghost logs to standard output so they are available through Clever Cloud's application logs.

## Create the application and add-ons

Install [Clever Tools](/developers/doc/cli/), log in and create a Linux application with an alias used to link the add-ons:

```bash
npm i -g clever-tools
clever login

clever create -t linux -a myGhost
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

Create and link MySQL 8.4, Cellar and FS Bucket add-ons:

```bash
clever addon create mysql-addon myGhostMySQL -p xxs_sml --addon-version 8.4 -l myGhost
clever addon create cellar-addon myGhostCellar -l myGhost
clever addon create fs-bucket myGhostContent -l myGhost
```

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

Mount the linked FS Bucket on the `content` directory. This path corresponds to `$APP_HOME/content` in the Mise configuration:

```bash
FS_BUCKET_HOST="$(clever env -F json | jq -er 'first(.fromAddons[] | select(.addonName == "myGhostContent") | .env[] | select(.name == "BUCKET_HOST") | .value)')"
clever env set CC_FS_BUCKET "/content:${FS_BUCKET_HOST}"
unset FS_BUCKET_HOST
```

This name-based lookup is unambiguous only if the add-on name is unique. If several linked add-ons use the same name, it selects the first one found. To target the resource explicitly, replace the first command with the add-on ID returned by `clever addon create`:

```bash
FS_BUCKET_HOST="$(clever addon env ADDON_ID -F json | jq -er '.BUCKET_HOST')"
```

## Configure Cellar

Cellar bucket names are global within a cluster. Choose a unique name containing only lowercase letters, numbers, dots and hyphens:

```bash
export GHOST_BUCKET="your-unique-ghost-bucket"
```

Export only the linked Cellar variables to your current shell, then create the bucket:

```bash
source <(clever env -F shell | grep '^export CELLAR_ADDON_')

s3cmd --access_key="$CELLAR_ADDON_KEY_ID" \
  --secret_key="$CELLAR_ADDON_KEY_SECRET" \
  --host="$CELLAR_ADDON_HOST" \
  --host-bucket="$CELLAR_ADDON_HOST" \
  --ssl mb "s3://$GHOST_BUCKET"
```

Ghost returns direct URLs for uploaded assets, so visitors need public read access to bucket objects. Create a policy that allows reads without allowing public writes or bucket listing:

```bash
jq --null-input --arg bucket "$GHOST_BUCKET" '{
  Version: "2012-10-17",
  Statement: [{
    Sid: "PublicRead",
    Effect: "Allow",
    Principal: "*",
    Action: "s3:GetObject",
    Resource: "arn:aws:s3:::\($bucket)/*"
  }]
}' > ghost-bucket-policy.json

s3cmd --access_key="$CELLAR_ADDON_KEY_ID" \
  --secret_key="$CELLAR_ADDON_KEY_SECRET" \
  --host="$CELLAR_ADDON_HOST" \
  --host-bucket="$CELLAR_ADDON_HOST" \
  --ssl setpolicy ghost-bucket-policy.json "s3://$GHOST_BUCKET"

rm ghost-bucket-policy.json
unset CELLAR_ADDON_KEY_ID CELLAR_ADDON_KEY_SECRET CELLAR_ADDON_HOST
```

Keep `GHOST_BUCKET` exported for the next section.

## Configure Ghost

Store the application domain in a shell variable, using either its `.cleverapps.io` domain or your custom domain:

```bash
export GHOST_URL="https://your-ghost-domain.example.com"
```

Configure the Ghost and Node.js versions, public URL and bucket name:

```bash
clever env set GHOST_VERSION 6.60.0
clever env set CC_NODE_VERSION 22.23.1

clever env set GHOST_BUCKET "$GHOST_BUCKET"
clever env set NODE_ENV production
clever env set url "$GHOST_URL"
```

The linked add-ons provide their credentials to the application. The `mise.toml` file maps them to Ghost's nested configuration and sets the server address and port.

### Configure email

Ghost requires transactional email for invitations, password resets, member sign-ins and Admin verification on new devices. Configure the SMTP service of your choice and replace every example value with your provider's settings:

```bash
clever env set mail__transport SMTP
clever env set mail__from "Ghost <ghost@your.website.tld>"
clever env set mail__options__host smtp.example.com
clever env set mail__options__port 465
clever env set mail__options__secure true
clever env set mail__options__auth__user SMTP_USERNAME
clever env set mail__options__auth__pass A_STRONG_SMTP_PASSWORD
```

See the [Ghost mail configuration](https://docs.ghost.org/config/#mail) for provider-specific options. Transactional email works with standard SMTP services, but Ghost's built-in bulk newsletter delivery [requires Mailgun](https://docs.ghost.org/newsletters/#bulk-email-configuration).

If an SMTP service is not yet available during the initial configuration, you can temporarily disable Admin verification on new devices:

```bash
clever env set security__staffDeviceVerification false
```

Only use this setting while configuring the application. Before using Ghost in production, configure SMTP and re-enable device verification:

```bash
clever env set security__staffDeviceVerification true
clever restart
```

## Deploy Ghost

Commit the deployment configuration and deploy the application:

```bash
git add mise.toml
git commit -m "First deploy"

clever deploy
```

Open the application and append `/ghost` to its URL to create the publication owner account:

```bash
clever open
```

The public publication is available from the application URL, while Admin is available at `https://your-ghost-domain.example.com/ghost`.

## Update Ghost

Export your content from Ghost Admin and make sure you have a recent [MySQL backup](/developers/doc/cli/addons/#database-backups) before updating. Check the [`engines.node` requirement](https://github.com/TryGhost/Ghost/blob/v6.60.0/ghost/core/package.json) of the Ghost release you want to use, then update both version variables when necessary. For example:

```bash
clever env set GHOST_VERSION 6.60.0
clever env set CC_NODE_VERSION 22.23.1
clever restart --without-cache
```

The rebuild downloads the selected release and installs dependencies for the configured Node.js version. Ghost applies pending MySQL migrations when the new version starts.

## Learn more

{{< cards >}}
  {{< card link="https://docs.ghost.org/" title="Ghost documentation" subtitle="Configure and manage a Ghost publication" icon="ghost" >}}
  {{< card link="/developers/doc/applications/linux" title="Linux application runtime" subtitle="Configure and deploy any application" icon="linux" >}}
  {{< card link="/developers/doc/addons/mysql" title="MySQL" subtitle="Explore managed MySQL databases" icon="mysql" >}}
  {{< card link="/developers/doc/addons/cellar" title="Cellar" subtitle="Explore S3-compatible object storage" icon="cellar" >}}
  {{< card link="/developers/doc/addons/fs-bucket" title="FS Bucket" subtitle="Persist files across deployments" icon="fsbucket" >}}
{{< /cards >}}
