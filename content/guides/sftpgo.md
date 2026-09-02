---
type: docs
linkTitle: SFTPGo
title: Deploy an SFTP server with SFTPGo
description: Deploy SFTPGo on Clever Cloud with the Linux runtime, PostgreSQL and Cellar object storage
keywords:
- sftpgo
- sftp
- file transfer
- linux
- mise
- postgresql
- cellar
- s3 storage
- file management
---

{{< hextra/hero-subtitle >}}
  SFTPGo is an open-source SFTP server with multi-user management, a web interface and support for S3-compatible storage backends such as Cellar.
{{< /hextra/hero-subtitle >}}

Clever Cloud provides built-in SFTP access to [FS Buckets](/developers/doc/addons/fs-bucket/). Deploy SFTPGo when you need advanced user management or fine-grained access control, or when you want to expose files stored in [Cellar](/developers/doc/addons/cellar/) over SFTP. This guide uses the [Linux runtime](/developers/doc/applications/linux/) and [Mise](https://mise.jdx.dev/) to install SFTPGo, PostgreSQL to persist its configuration, and Cellar for object storage.

This guide only covers SFTP. FTP requires a dedicated TCP port range. Contact [Clever Cloud support](https://console.clever-cloud.com/ticket/center) if you need it.

## Prepare the SFTPGo project

You need [Git](https://git-scm.com/downloads), [OpenSSL](https://openssl-library.org/) and a [Clever Cloud account](https://console.clever-cloud.com) to follow this guide. Create a project and initialize its Git repository:

```bash
mkdir mySftpGo
cd mySftpGo
git init
```

[Mise](https://mise.jdx.dev/) is available on Clever Cloud. Declare dependencies, environment variables and tasks in a `mise.toml` file. Here, use it to install the latest stable SFTPGo release from GitHub and define its run task:

```toml {filename="mise.toml"}
[settings.github]
github_attestations = false

[tools]
# Replace "latest" with a specific release such as "2.7.5" to pin SFTPGo.
"github:drakkan/sftpgo" = "latest"

[env]
SFTPGO_DATA_PROVIDER__DRIVER = "postgresql"
SFTPGO_DATA_PROVIDER__CONNECTION_STRING = "{{ env.POSTGRESQL_ADDON_URI }}"
SFTPGO_HTTPD__TEMPLATES_PATH = { value = "{{ tools['github:drakkan/sftpgo'].path }}/templates", tools = true }
SFTPGO_HTTPD__STATIC_FILES_PATH = { value = "{{ tools['github:drakkan/sftpgo'].path }}/static", tools = true }
SFTPGO_HTTPD__OPENAPI_PATH = { value = "{{ tools['github:drakkan/sftpgo'].path }}/openapi", tools = true }
SFTPGO_SMTP__TEMPLATES_PATH = { value = "{{ tools['github:drakkan/sftpgo'].path }}/templates", tools = true }
SFTPGO_SFTPD__BINDINGS__0__PORT = "4040"
SFTPGO_RUNTIME_DIR = "/tmp/sftpgo"
SFTPGO_SFTPD__HOST_KEYS = "{{ env.SFTPGO_RUNTIME_DIR }}/id_ed25519"
SFTPGO_LOG_FILE_PATH = ""
SFTPGO_LOG_LEVEL = "info"

[tasks.run]
run = '''
#!/usr/bin/env bash

set -euo pipefail

: "${SFTPGO_SSH_HOST_KEY_B64:?Configure the persistent SFTP host key before deploying}"
mkdir -p "$SFTPGO_RUNTIME_DIR"
chmod 700 "$SFTPGO_RUNTIME_DIR"
printf '%s' "${SFTPGO_SSH_HOST_KEY_B64}" | openssl base64 -d -A > "$SFTPGO_SFTPD__HOST_KEYS"
chmod 600 "$SFTPGO_SFTPD__HOST_KEYS"

sftpgo serve
'''
```

The project-level `github_attestations` setting works around an incompatibility between the GitHub attestation currently published for SFTPGo and the version of Mise available on Clever Cloud. Mise still verifies the downloaded asset checksum.

The name `run` is significant: unless you define `CC_RUN_COMMAND`, the Linux runtime [detects and executes](/developers/doc/applications/linux/#build-and-run-commands) the [Mise task](https://mise.jdx.dev/tasks/) as the application run command. It restores the persistent SFTP host key, prepares the temporary directory and starts the SFTPGo server. The environment maps the PostgreSQL add-on URI injected by Clever Cloud to SFTPGo and points to the web resources installed by Mise.

SFTPGo listens on port `8080` for its web interface by default. The configuration binds its SFTP server to port `4040`, used by Clever Cloud TCP redirections. It sends logs to the standard output with `info` level because SFTPGo's default `debug` logs can include the PostgreSQL URI.

## Create and configure the Clever Cloud resources

Install [Clever Tools](/developers/doc/cli/), log in and create a Linux application with an alias:

```bash
npm i -g clever-tools
clever login

clever create -t linux -a mySftpGo
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

Use the application alias to create and link a PostgreSQL add-on and a Cellar add-on. The native links automatically inject the PostgreSQL and Cellar environment variables into the application:

```bash
clever addon create postgresql-addon mySftpGoPg -p xxs_sml -l mySftpGo
clever addon create cellar-addon mySftpGoCellar -l mySftpGo
```

You can alternatively create the application and add-ons, and link the add-ons to the application, from the [Clever Cloud Console](https://console.clever-cloud.com/).

Finally, create the TCP redirection used for SFTP connections:

```bash
clever tcp-redirs add --namespace cleverapps
```

The command returns the public TCP port to use with your application's `.cleverapps.io` domain. To use a custom SFTP hostname, follow the [TCP redirection documentation](/developers/doc/administrate/tcp-redirections/) and create the redirection in the appropriate namespace.

## Deploy SFTPGo

Commit the project:

```bash
git add .
git commit -m "First deploy"
```

SFTPGo exposes its setup page publicly until the first administrator exists. Generate its password once, store it in your password manager, then create the account securely from environment variables during the first deployment:

```bash
SFTPGO_ADMIN_USERNAME="admin"
SFTPGO_ADMIN_PASSWORD="$(openssl rand -base64 32)"

clever env set SFTPGO_DEFAULT_ADMIN_USERNAME "$SFTPGO_ADMIN_USERNAME"
clever env set SFTPGO_DEFAULT_ADMIN_PASSWORD "$SFTPGO_ADMIN_PASSWORD"
clever env set SFTPGO_DATA_PROVIDER__CREATE_DEFAULT_ADMIN true

# Prints the generated configuration
clever env
```

You can replace `admin` with any administrator username.

Generate an Ed25519 SSH host key and store it in the application environment. The startup task restores the same key on every application instance and rebuild, keeping the SFTP server fingerprint stable:

```bash
clever env set SFTPGO_SSH_HOST_KEY_B64 "$(openssl genpkey -algorithm ED25519 | openssl base64 -A)"
```

SFTPGo supports multiple [host keys](https://docs.sftpgo.com/2.7/config-file/#sshsftp-server), but one Ed25519 key provides a secure default for modern SFTP clients. Keep this private environment variable defined: removing or replacing it changes the server fingerprint after the next restart. Deploy the application:

```bash
clever deploy
```

Once SFTPGo has started, the administrator remains stored in PostgreSQL. Remove the bootstrap variables from the application environment and restart the application so they are no longer available to the running process. Then open the web administration interface:

```bash
clever env rm SFTPGO_DEFAULT_ADMIN_USERNAME
clever env rm SFTPGO_DEFAULT_ADMIN_PASSWORD
clever env rm SFTPGO_DATA_PROVIDER__CREATE_DEFAULT_ADMIN

clever restart
clever open
```

## Use Cellar as a storage backend

A new Cellar add-on does not contain a bucket. Create one with Cellar Explorer in the [Clever Cloud Console](https://console.clever-cloud.com/), or with an [S3-compatible client](/developers/doc/addons/cellar/#managing-your-buckets).

### Configure Cellar through the SFTPGo web interface

Create a user in the SFTPGo web administration interface and select **S3-compatible** as its storage provider:

| Setting                   | Value                                                |
| ------------------------- | ---------------------------------------------------- |
| Bucket                    | Your Cellar bucket name                              |
| Home Dir                  | `/tmp/sftpgo`                                        |
| Region                    | `default`                                            |
| Access Key                | The `CELLAR_ADDON_KEY_ID` value                      |
| Access Secret             | The `CELLAR_ADDON_KEY_SECRET` value                  |
| Endpoint                  | `https://` followed by the `CELLAR_ADDON_HOST` value |
| Use path-style addressing | Enabled                                              |

SFTPGo requires a local home directory for temporary files when using S3-compatible storage. The startup task creates `/tmp/sftpgo` on every application instance. The open-source edition [uses unlinked local files for transfers to and from object storage](https://github.com/drakkan/sftpgo/discussions/1968), so a transfer can temporarily consume its full size on the instance disk. Account for the largest expected files and simultaneous transfers when choosing the run instance; completed files remain stored in Cellar, but in-progress transfers can fail if local disk is exhausted.

Force path-style addressing to support every valid Cellar bucket name, including names containing dots. The linked Cellar add-on makes the other values available in the application environment variables in the Clever Cloud Console.

### Configure Cellar through the REST API

You can also create the SFTPGo user with the [SFTPGo REST API](https://docs.sftpgo.com/latest/rest-api/) without opening the web interface. This example requires `curl` and `jq`. Display the application's domains and choose the one you want to use for the web API:

```bash
clever domain
```

Set a variable with this domain, then retrieve the linked Cellar add-on ID with Clever Tools. Set the bucket name and new SFTP username. OpenSSL generates the user's password once, so the following commands can reuse it:

```bash
SFTPGO_URL="https://your-sftpgo-domain.example.com"
CELLAR_ADDON_ID="$(
  clever service -F json --only-addons |
    jq --exit-status --raw-output \
      'first(.addons[] | select(.realId | startswith("cellar_")) | .id)'
)"
SFTPGO_BUCKET="your-cellar-bucket"
SFTPGO_USERNAME="myUser"
SFTPGO_PASSWORD="$(openssl rand -base64 32)"
```

You can replace `myUser` with any username. Store `SFTPGO_PASSWORD` in your password manager before unsetting it at the end of this procedure.

Request an API token with the administrator credentials defined before the first deployment:

```bash
SFTPGO_TOKEN="$(
  curl --fail --silent --show-error \
    --user "${SFTPGO_ADMIN_USERNAME}:${SFTPGO_ADMIN_PASSWORD}" \
    "${SFTPGO_URL}/api/v2/token" |
    jq --exit-status --raw-output '.access_token'
)"
```

The `shell` output format returns the linked Cellar add-on variables as export statements. Load them directly into the current shell, then use them to build the SFTPGo user configuration:

```bash
source <(clever addon env "$CELLAR_ADDON_ID" -F shell)

jq --null-input \
  --arg username "$SFTPGO_USERNAME" \
  --arg password "$SFTPGO_PASSWORD" \
  --arg bucket "$SFTPGO_BUCKET" \
  --arg access_key "$CELLAR_ADDON_KEY_ID" \
  --arg access_secret "$CELLAR_ADDON_KEY_SECRET" \
  --arg endpoint "https://$CELLAR_ADDON_HOST" \
  '{
    status: 1,
    username: $username,
    password: $password,
    home_dir: "/tmp/sftpgo",
    permissions: {"/": ["*"]},
    filesystem: {
      provider: 1,
      s3config: {
        bucket: $bucket,
        region: "default",
        access_key: $access_key,
        access_secret: {status: "Plain", payload: $access_secret},
        endpoint: $endpoint,
        force_path_style: true
      }
    }
  }' | curl --fail --silent --show-error \
    --request POST \
    --header "Authorization: Bearer ${SFTPGO_TOKEN}" \
    --header "Content-Type: application/json" \
    --data-binary @- \
    "${SFTPGO_URL}/api/v2/users"
```

Once the user exists, remove its password, the API token and the Cellar credentials from your shell:

```bash
unset SFTPGO_ADMIN_USERNAME SFTPGO_ADMIN_PASSWORD SFTPGO_PASSWORD SFTPGO_TOKEN
unset CELLAR_ADDON_KEY_ID CELLAR_ADDON_KEY_SECRET CELLAR_ADDON_HOST
```

## Connect with an SFTP client

Use any SFTP client with the following settings:

- **Host**: your application's `.cleverapps.io` domain for the `cleverapps` redirection created above
- **Port**: the port returned by `clever tcp-redirs add`
- **Username and credentials**: those of the SFTPGo user you created, not the administrator account

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/linux" title="Linux applications" subtitle="Deploy any application" icon="linux" >}}
  {{< card link="/developers/doc/addons/cellar" title="Cellar object storage" subtitle="Store files with an S3 API" icon="database" >}}
  {{< card link="/developers/doc/addons/fs-bucket" title="FS Buckets" subtitle="Store files with SFTP access" icon="fsbucket" >}}
  {{< card link="https://docs.sftpgo.com/latest/" title="SFTPGo documentation" subtitle="Configure users and storage" icon="book-open" >}}
{{< /cards >}}
