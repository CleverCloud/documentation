---
title: 'Docs'
description: 
tags:
- guides
keywords:
- 

draft: false
type: docs
---

{{< hextra/hero-subtitle >}}
  The open source document editor where your notes can become knowledge through live collaboration.
{{< /hextra/hero-subtitle >}}

## Docs architecture overview



## How to Configure Docs

Docs depends on some services that needs configuration before it can function. Use the **Create > an add-on** fonction to create each dependency on Clever Cloud.

### Keycloak

Docs uses Keycloak as an authentification provider. Configure it by follwoing these steps:

{{% steps %}}

#### Create a Keycloak add-on

If you don't have a Keycloak instance, create one on Clever Cloud. If you already have one, skip this step. For the sake of demonstration, this guide follows [the example values provided by Docs](https://github.com/suitenumerique/docs/blob/main/docs/examples/impress.values.yaml). You can rename them as you see fit.

#### Create a new realm

Name it `impress`.

#### Create a new client

Name it `impress` as well.

#### Client settings

##### General settings

- Client ID: impress
- Client name: impress
- Always Display in UI: ON

##### Access settings

- Root URL: `https://<docs-base-domain>`
- Home URL: `https://<docs-base-domain>`
- Valid redirect URIs: `https://<docs-base-domain>/api/v1.0/callback/*`
- Valid post logout redirect URIs: `https://<docs-base-domain>/*`
- Web origins: `https://<docs-base-domain>`

##### Capability config

- Client authentication: ON
- Authorization: OFF
- Authentication flow: Standard flow

##### Find the Client Secret

Find it in **Clients > impress > credentials**, named **Client secret*.

##### Optional : Add an identity provider

You can choose among different identity providers : GitHub, Google, etc, and even Clever Cloud.

#### Inject the variables in the **backend** application

```env
OIDC_OP_AUTHORIZATION_ENDPOINT="https://<cc_keycloak_hostname_value>/realms/impress/protocol/openid-connect/auth"
OIDC_OP_JWKS_ENDPOINT="https://<cc_keycloak_hostname_value>/realms/impress/protocol/openid-connect/certs"
OIDC_OP_LOGOUT_ENDPOINT="https://<cc_keycloak_hostname_value>/realms/impress/protocol/openid-connect/session/end"
OIDC_OP_TOKEN_ENDPOINT="https://<cc_keycloak_hostname_value>/realms/impress/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT="https://<cc_keycloak_hostname_value>/realms/impress/protocol/openid-connect/userinfo"
OIDC_RP_CLIENT_ID="impress"
OIDC_RP_CLIENT_SECRET="<client-secret>"
OIDC_RP_SCOPES="openid email"
OIDC_RP_SIGN_ALGO="RS256"
```

{{% /steps %}}

### Redis

Create a Redis add-on, but don't connect it to the application, since Docs requires an URI format that differs from the one provided by Clever Cloud. Instead, inject the variable in the **backend** application, using this format: `REDIS_URL="redis://default:<redis_password>:<redis_host>:<redis_port>"`

### Cellar

Docs uses s3 compatible storage to store uploaded files by users.

{{% steps %}}

#### Create a Cellar add-on

#### Create a bucket

#### Inject the variables in the **backend** application

```env
AWS_S3_ACCESS_KEY_ID="<cellar-addon_key_id_value>"
AWS_S3_ENDPOINT_URL="<cellar-addon_host_value>"
AWS_S3_REGION_NAME="auto"
AWS_S3_SECRET_ACCESS_KEY="<cellar-addon_key_secret_value>"
AWS_STORAGE_BUCKET_NAME="<name-of-your-bucket>"
```

{{% /steps %}}

## 🎓 Further Help

{{< cards >}}
  {{< card link="" title="Card title" subtitle="Card subtiltle" icon="adjustments-horizontal" >}}
{{< /cards >}}