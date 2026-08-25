---
type: docs
weight: 2
linkTitle: Service tokens
title: Service tokens
description: Create and use Clever Cloud organisation service tokens, machine-to-machine credentials for CI/CD pipelines, monitoring tools and scripts.
keywords:
- service tokens
- biscuit
- machine to machine
- automation
- ci/cd
- api
---

Organisation service tokens are machine-to-machine credentials based on [Biscuit](https://www.biscuitsec.org/). They allow automated systems such as CI/CD pipelines, monitoring tools or deployment scripts to interact with the Clever Cloud API without tying access to a personal user account.

Unlike [API tokens](/developers/api/howto/#api-tokens), which authenticate requests on behalf of a specific user, a service token belongs to an organisation and carries its own role. Access no longer disappears when a team member leaves, and each automated system gets its own revocable credential, scoped to what it actually needs.

## Scope and limitations

A service token grants access to a single organisation. A token created for organisation A can't read or modify anything in organisation B, whatever role it carries.

Service tokens are only implemented under `/v2/organisations/{id}` paths. Endpoints outside this prefix reject them, so `GET /v2/organisations` returns an error even with a valid token: always target the organisation the token belongs to.

## Manage service tokens

Manage service tokens through four endpoints under `/v2/organisations/{id}/service-tokens`:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v2/organisations/{id}/service-tokens` | Create a token |
| `GET` | `/v2/organisations/{id}/service-tokens` | List tokens, supports `?limit=` and `?offset=` |
| `GET` | `/v2/organisations/{id}/service-tokens/{tokenId}` | Get a token |
| `DELETE` | `/v2/organisations/{id}/service-tokens/{tokenId}` | Revoke a token |

These endpoints require your own credentials: create and revoke service tokens with the authentication method you already use, such as [`clever curl`](/developers/api/howto/#clever-curl), an API token through the API bridge, or OAuth 1.

### Create a token

Create a service token with a name, a role, an optional application scope and an optional lifetime:

```bash
clever curl -X POST https://api.clever-cloud.com/v2/organisations/<ORGANISATION_ID>/service-tokens \
  -H "Content-Type: application/json" \
  -d '{
    "name": "ci-deploy-token",
    "role": "DEVELOPER",
    "app_id": "app_xxx",
    "ttl_seconds": 2592000
  }'
```

| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Name identifying the token in the organisation |
| `role` | Yes | One of `ADMIN`, `MANAGER`, `DEVELOPER`, `ACCOUNTING` |
| `app_id` | No | Restricts the token to a single application or add-on |
| `ttl_seconds` | No | Token lifetime, from 1 second to 1 year. Defaults to 90 days |

You can only assign a role equal to or lower than your own, so only organisation admins create `ADMIN` or `ACCOUNTING` tokens. Refer to [roles and privileges](/developers/doc/account/organisations/#roles-and-privileges) to pick the role matching what your automated system needs.

Setting `app_id` restricts the token to a single application or add-on: the API rejects any request targeting another resource. Omit it to give the token organisation-wide access for its role.

### List and revoke tokens

List the tokens of an organisation, paginating with `limit` and `offset`:

```bash
clever curl "https://api.clever-cloud.com/v2/organisations/<ORGANISATION_ID>/service-tokens?limit=20&offset=0"
```

Deleting a token revokes it immediately, and the API rejects every subsequent request using it:

```bash
clever curl -X DELETE https://api.clever-cloud.com/v2/organisations/<ORGANISATION_ID>/service-tokens/<TOKEN_ID>
```

## Authenticate with a service token

Send the biscuit as a bearer token in the `Authorization` header:

```bash
curl https://api.clever-cloud.com/v2/organisations/<ORGANISATION_ID>/applications \
  -H "Authorization: Bearer <BISCUIT>"
```

### Deploy over HTTP

Service tokens also work for `git push` over HTTP, which makes them convenient for CI/CD pipelines where no SSH key is available. Git uses Basic authentication here, and the biscuit goes in the username field, with an unused password:

```text
Authorization: Basic base64(<BISCUIT>:<not-used>)
```

Get the HTTP deployment URL of your application from the Clever Cloud Console, in **Information** > **Deployment URL**, then pass the token inline in the remote URL:

```bash
git remote add clever https://<BISCUIT>@<DEPLOYMENT_HOST>/<APP_ID>.git
git push clever main
```

Writing the token in the remote URL stores it in `.git/config` and exposes it in process listings. To keep it out of both, provide it through `GIT_ASKPASS` instead:

```bash
cat > /tmp/askpass.sh <<'EOF'
#!/bin/sh
echo "$SERVICE_TOKEN"
EOF
chmod +x /tmp/askpass.sh

GIT_ASKPASS=/tmp/askpass.sh SERVICE_TOKEN="<BISCUIT>" \
  git push https://<DEPLOYMENT_HOST>/<APP_ID>.git main
```

## Security boundaries

Service tokens enforce the same permission model as user roles, plus additional scoping. Each token belongs to one organisation, optionally to one application or add-on, and its role determines which operations it can perform: an `ACCOUNTING` token can't read application details, for example.

Tokens are also time-limited and revocable. Once their lifetime has elapsed, the API rejects them. Deleting a token revokes it immediately, so rotating a compromised credential takes a single `DELETE` request. The audit trail records every request authenticated with a biscuit, which lets you trace what each automated system did.

> [!WARNING]
> A service token is a credential granting access to your organisation's resources. Store it in the secret manager of your CI/CD platform, never in your repository, and give each automated system its own token with the narrowest role and application scope it can work with.
