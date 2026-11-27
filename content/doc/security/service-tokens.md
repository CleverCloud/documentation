---
type: docs
linkTitle: Service tokens
title: Create and manage service tokens
description: Give CI/CD pipelines, monitoring tools, and scripts an organisation-scoped credential for the Clever Cloud API
keywords:
- service token
- biscuit
- api
- ci/cd
- automation
- credentials
---

A service token is a machine-to-machine credential for the Clever Cloud API. It belongs to an organisation and carries a role. A pipeline, a monitoring tool, or a script uses it to act on the resources of the organisation, without a personal account.

The value of a service token is a [Biscuit](https://doc.biscuitsec.org/) token: a compact, signed credential that the API checks on each request. The API returns it only once, when you create it.

Because it's a Biscuit token, its holder can attenuate it to derive a token with fewer rights or a shorter lifetime. The operation needs no call to the API, and the [Biscuit documentation](https://doc.biscuitsec.org/) describes it.

## Prerequisites

To create a service token, you need:

- A Clever Cloud account, and `clever login` run on your computer
- The identifier of the organisation, such as `orga_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- The `manage_organisations_services` permission on this organisation
- A role at least as high as the role of the token you create

Set the identifiers in your shell:

```bash
ORG=orga_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
API="https://api.clever-cloud.com/v2/organisations/$ORG"
```

`clever curl` wraps `curl` and adds the credentials of your current login, so you don't have to sign each request yourself.

## Create an organisation-wide token

This token covers every application and add-on of the organisation:

```bash
clever curl -X POST "$API/service-tokens" \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "ci-deploy-token",
    "description": "Deployment pipeline",
    "role": "DEVELOPER",
    "ttl_seconds": 2592000
  }' > token.json

TOKEN=$(jq -r .token token.json)
```

The response holds the token in the `token` field, and the description of the token in the `metadata` field. Its `refreshToken` field stays `null`, because a service token expires without a refresh.

The request body holds these fields:

| Field         | Description                                                         |
| ------------- | ------------------------------------------------------------------- |
| `name`        | Name of the token, shown in the list of the tokens                  |
| `description` | Description of the token, optional                                  |
| `role`        | `ADMIN`, `MANAGER`, `DEVELOPER`, or `ACCOUNTING`                    |
| `resources`   | Identifiers of the resources the token applies to, optional         |
| `ttl_seconds` | Lifetime of the token in seconds, from `1` to `31536000` (one year) |

The `role` of a token never exceeds the role of the member who creates it. The [roles and their privileges](/doc/security/iam-roles/#roles-and-privileges) tell what each role allows. The `ttl_seconds` field defaults to `7776000` seconds, which is 90 days.

> [!WARNING] The token appears only in the creation response
> The API never returns it again. Store it in your secret manager before you close the response.

## Restrict a token to specific resources

The `resources` field lists the resources the token applies to, with `app_…` or `addon_…` identifiers:

```bash
APP=app_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

clever curl -X POST "$API/service-tokens" \
  -H 'Content-Type: application/json' \
  -d "{
    \"name\": \"ci-deploy-myapp\",
    \"role\": \"DEVELOPER\",
    \"resources\": [\"$APP\"],
    \"ttl_seconds\": 604800
  }" > token.json

TOKEN=$(jq -r .token token.json)
```

Every identifier must belong to the organisation, otherwise the API returns a `404`. Without `resources`, or with an empty list, the token covers the whole organisation for its role.

## Use the token

Send the token as a bearer token. Use `curl` rather than `clever curl`, so the credentials of your login don't mix with the token:

```bash
# The application in the scope of the token
curl -H "Authorization: Bearer $TOKEN" "$API/applications/$APP"

# Another application: the API returns a 403
curl -H "Authorization: Bearer $TOKEN" "$API/applications/app_9d1f4c2e-8b3a-4f5d-9c2b-1e6f7a8b9c0d"

# The list of the applications: the API returns a 403
curl -H "Authorization: Bearer $TOKEN" "$API/applications"
```

A token restricted to one application can't read the list of the applications, nor reach any other application.

## Deploy over HTTPS

The API returns the HTTP git URL of an application in `deployment.httpUrl`:

```bash
clever curl "$API/applications/$APP" | jq -r .deployment.httpUrl
```

Git sends the token as the username of the Basic authentication, and ignores the password. Git stores a token placed in the remote URL in clear text in `.git/config`, so prefer `GIT_ASKPASS` to keep it out of the disk:

```bash
cat > /tmp/askpass.sh <<'EOF'
#!/bin/sh
case "$1" in
  Username*) printf '%s\n' "$TOKEN" ;;
  *)         printf 'unused\n' ;;
esac
EOF
chmod +x /tmp/askpass.sh

export TOKEN
GIT_ASKPASS=/tmp/askpass.sh git push \
  "$(clever curl "$API/applications/$APP" | jq -r .deployment.httpUrl)" HEAD:master
```

The token needs a role that allows deploying, `DEVELOPER` at least. When you restrict a token to specific resources, list the application you push.

## List, inspect, and revoke tokens

```bash
clever curl "$API/service-tokens"
clever curl "$API/service-tokens/$TOKEN_ID"
clever curl -X DELETE "$API/service-tokens/$TOKEN_ID"
```

The list shows the identifier of each token, which the other two endpoints take as `TOKEN_ID`. It accepts `?limit=` and `?offset=` parameters. They also accept the revocation identifier of the token. A revocation applies immediately.

## Limits

- The role of the token bounds what it can do: an `ACCOUNTING` token can't read the applications
- For an add-on, the identifier in the URL must match the one in `resources`: `addon_…` in `resources` needs `addon_…` in the URL, and a `real_id` needs that `real_id`
- The creation of tokens is rate-limited per organisation
- The expiry of a token applies immediately
