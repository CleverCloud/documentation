---
type: docs
linkTitle: Marketplace
title: Marketplace API
description: Provide your service as an add-on on Clever Cloud, with a manifest, provisioning requests, the vendor API, and single sign-on to your dashboard
keywords:
- Add-on
- API
- Marketplace
- Partners
- integration
- manifest
- sso
- provisioning
- vendor api
aliases:
- /doc/extend/add-ons-api/
- /doc/extend/addon-api/
- /doc/marketplace
- /marketplace
---

Marketplace partners provide their services as add-ons on Clever Cloud, with revenue sharing. Customers create these add-ons from the [Console](https://console.clever-cloud.com), [Clever Tools](/doc/tools/cli/), the [API](/api), or other integrations such as the [Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/), and get their credentials as environment variables.

To offer your service on Clever Cloud, [contact the partners team](https://partners.clever-cloud.com). Your service can run on Clever Cloud or elsewhere: it only needs an HTTPS API that Clever Cloud calls, and a dashboard that customers open from the Console.

## How it works

An add-on provider describes your service with a manifest. Once you register it, Clever Cloud calls your API:

- When a customer creates an add-on, to [provision](#provisioning) a resource and get its credentials
- When a customer deletes an add-on, to [deprovision](#deprovisioning) the resource
- When a customer changes the plan of an add-on, if your provider supports it, to [migrate](#plan-changes) the resource

When a customer opens the add-on from the Console, Clever Cloud signs them in to your dashboard with [single sign-on](#single-sign-on). Your service calls the [vendor API](#vendor-api) to list the add-ons, read their details, and update their configuration.

## Create an add-on provider

### Write the manifest

The manifest is a JSON file that describes your add-on provider:

```json {filename="manifest.json"}
{
  "id": "my-service",
  "name": "My Service",
  "api": {
    "config_vars": ["MY_SERVICE_URL", "MY_SERVICE_TOKEN"],
    "password": "<a long random string>",
    "sso_salt": "<another long random string>",
    "production": {
      "base_url": "https://my-service.example.com/clevercloud/resources",
      "sso_url": "https://my-service.example.com/clevercloud/sso/login"
    },
    "test": {
      "base_url": "https://staging.my-service.example.com/clevercloud/resources",
      "sso_url": "https://staging.my-service.example.com/clevercloud/sso/login"
    }
  }
}
```

| Field                 | Description                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `id`                  | ID of the provider, also its user name for the authentication of requests. It can't change after the registration |
| `name`                | Name of the provider shown to customers, which you can change later                                               |
| `api.config_vars`     | Environment variables that the add-on provides, each starting with the `id`, in capitals, `-` replaced by `_`     |
| `api.password`        | Password of the authentication of requests, from 12 to 4096 characters, without `:`                               |
| `api.sso_salt`        | Shared secret of the single sign-on signatures, from 12 to 4096 characters                                        |
| `api.production`      | `base_url` and `sso_url` used once Clever Cloud opens the provider in private access, or to all its customers     |
| `api.test`            | `base_url` of your API and `sso_url` of your dashboard, used for the providers of your organisation               |

Clever Cloud calls the `base_url` from its servers, and the customer's browser opens the `sso_url`: both must be public and use HTTPS. Over HTTP, the requests would expose the credentials of the provider, and the Console couldn't show your dashboard.

### Register the provider

As an administrator or a manager of an organisation, register the manifest from the **Create an add-on provider** page of the Console, at `https://console.clever-cloud.com/organisations/<orgID>/providers/new`, or with the API:

```bash
clever curl -s -X POST -H "Content-Type: application/json" -d @manifest.json \
  "https://api.clever-cloud.com/v2/organisations/<orgID>/addonproviders"
```

Then, create the plans of the provider from the Console, or with the API. Clever Cloud sends the slug of the chosen plan in its requests:

```bash
clever curl -s -X POST -H "Content-Type: application/json" \
  -d '{"name":"Basic","slug":"basic","price":0,"features":[]}' \
  "https://api.clever-cloud.com/v2/organisations/<orgID>/addonproviders/my-service/plans"
```

The `…/features` route of the provider describes the features that the plans compare.

### Use your provider

A provider you register is only visible to the members of its organisation, who create its add-ons, even in their personal spaces. Clever Cloud then uses the `test.base_url` and the `test.sso_url` of the manifest: set both.

Clever Cloud only uses the `production` URLs for the providers it opens in private access, or to all its customers. To offer your service to Clever Cloud customers this way, [contact the partners team](https://partners.clever-cloud.com).

## Requests from Clever Cloud

Clever Cloud authenticates each request with HTTP basic authentication: the `id` of the provider as user name, and the `password` of the manifest. Check them before you process any request.

Clever Cloud waits up to 20 seconds for the connection, and 120 seconds for the answer. Answer with a `2xx` status to succeed. With a `4xx` status, the customer gets an error that includes the body of your answer; with a `5xx` status, a service error with this body.

### Provisioning

When a customer creates an add-on, Clever Cloud sends a `POST` request to the `base_url`:

```json
{
  "addon_id": "addon_xxx",
  "heroku_id": "addon_xxx",
  "addon_name": "my-addon",
  "owner_id": "orga_xxx",
  "owner_name": "My organisation",
  "user_id": "user_xxx",
  "plan": "basic",
  "region": "par",
  "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx",
  "logplex_token": "log_xxxxxxxxxx",
  "options": {},
  "tags": []
}
```

| Field          | Description                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| `addon_id`     | ID of the add-on on Clever Cloud; `heroku_id` holds the same value                       |
| `addon_name`   | Name that the customer gave to the add-on                                                |
| `owner_id`     | ID of the organisation or the user that owns the add-on, with `owner_name` its name      |
| `user_id`      | ID of the user who creates the add-on                                                    |
| `plan`         | Slug of the chosen plan                                                                  |
| `region`       | Region of the add-on, such as `par` or `mtl`                                             |
| `callback_url` | URL of the add-on in the [vendor API](#vendor-api), available once the provisioning ends |
| `options`      | Options the customer set at creation, as strings                                         |
| `tags`         | Tags of the owner                                                                        |

Answer with the ID of the resource in your service, and the environment variables of the add-on:

```json
{
  "id": "my-resource-id",
  "config": {
    "MY_SERVICE_URL": "https://my-service.example.com/r/my-resource-id",
    "MY_SERVICE_TOKEN": "xxx"
  },
  "message": "Your add-on is ready"
}
```

Clever Cloud stores `id` as the real ID of the add-on, and uses it in the next requests. It injects every key of `config` in the applications linked to the add-on, even the ones not listed in `config_vars`. It doesn't display `message`.

The provisioning is synchronous: Clever Cloud only creates the add-on once you answer, so the `callback_url` doesn't work during this request. To prepare a resource that takes longer, answer first, then send its configuration later with the [vendor API](#update-the-configuration).

### Deprovisioning

When a customer deletes an add-on, Clever Cloud sends a `DELETE` request to `{base_url}/{id}`, with the `id` you returned at provisioning, and no body. Answer with a `2xx` status: otherwise, Clever Cloud doesn't delete the add-on. Answer `2xx` too if the resource doesn't exist anymore.

### Plan changes

Customers can change the plan or the region of an add-on only when Clever Cloud has enabled it for your provider. Clever Cloud then sends a `POST` request to `{base_url}/{id}/migrations`, with the target plan and region:

```json
{
  "addon_id": "addon_xxx",
  "heroku_id": "addon_xxx",
  "owner_id": "orga_xxx",
  "plan": "premium",
  "region": "par",
  "version": null,
  "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx/migration_callback?plan_id=plan_xxx&region=par",
  "tags": []
}
```

Clever Cloud forwards your answer to the customer. Once the resource uses its new plan, call its `callback_url` with a `PUT` request, as for an [update of the configuration](#update-the-configuration): Clever Cloud then records the new plan and region, and applies the configuration you send.

## Vendor API

The vendor API lets your service read and update its add-ons. Authenticate with the `id` of the provider and the `password` of the manifest:

```bash
curl -u "my-service:<password>" https://api.clever-cloud.com/v2/vendor/apps
```

A request without authentication gets a `400` status, and wrong credentials a `401` one.

### List the add-ons

`GET /v2/vendor/apps` lists the add-ons of your provider:

```json
[
  {
    "provider_id": "my-resource-id",
    "addon_id": "addon_xxx",
    "heroku_id": "addon_xxx",
    "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx",
    "plan": "Basic",
    "owner_id": "orga_xxx"
  }
]
```

`provider_id` is the ID you returned at provisioning, and `plan` the name of the plan. The list returns 4,000 add-ons at most: request the first page with `?offset=0`, then increase `offset` by 4,000 for each next page. It omits the add-ons without an owner.

### Get an add-on

`GET /v2/vendor/apps/{id}` returns an add-on, from its `addon_xxx` ID or the ID you returned:

```json
{
  "id": "addon_xxx",
  "name": "my-addon",
  "config": { "MY_SERVICE_URL": "https://my-service.example.com/r/my-resource-id" },
  "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx",
  "owner_email": "user@example.com",
  "owner_emails": ["user@example.com"],
  "owner_id": "orga_xxx",
  "owner_name": "My organisation",
  "region": "par",
  "domains": ["my-app.example.com"]
}
```

`owner_email` is the first member of the owner with a valid email, and `owner_emails` the emails of its active members. `domains` lists the domains of the applications linked to the add-on. An add-on of another provider gets a `403` status, and an unknown one a `404` status.

### Update the configuration

`PUT /v2/vendor/apps/{id}` replaces the environment variables of an add-on:

```json
{
  "config": {
    "MY_SERVICE_URL": "https://my-service.example.com/r/my-resource-id",
    "MY_SERVICE_TOKEN": "yyy"
  }
}
```

The new `config` replaces the whole previous one: send every variable, as a missing one is deleted. Clever Cloud then redeploys the running applications linked to the add-on, so they get the new values.

## Single sign-on

When a customer opens your add-on from the Console, the Console sends a form with a `POST` request to the `sso_url` of the manifest, and shows its result in a frame. The form holds the following fields:

| Field              | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `id`               | ID of the resource, returned at provisioning                  |
| `timestamp`        | Time of the request, in seconds since the Unix epoch          |
| `token`            | `sha1(id + ':' + sso_salt + ':' + timestamp)`, in hexadecimal |
| `signature`        | Signature of the user information, described below            |
| `email`, `user_id` | Email and ID of the Clever Cloud user                         |
| `nav-data`         | Always empty                                                  |

The `signature` is the SHA-512 hash, in hexadecimal, of these values separated by `:`:

```text
id:user_id:email:nav-data:sso_salt:timestamp
```

Compute the signature with your `sso_salt`, and reject the request if it differs, or if the timestamp is older than a few minutes. Then, sign the user in to your service, and show the dashboard of this resource.

The Console shows your dashboard in a frame: allow it to frame your pages with the `frame-ancestors` directive of your Content Security Policy, and set your session cookies with `SameSite=None` and `Secure`.

## Example

This [Flask](https://flask.palletsprojects.com/) application checks the requests of Clever Cloud, answers provisioning and deprovisioning, and checks single sign-on:

```python {filename="app.py"}
import hashlib, hmac, os, secrets, time
from flask import Flask, abort, jsonify, request

app = Flask(__name__)
PROVIDER_ID = os.environ["PROVIDER_ID"]
PASSWORD = os.environ["PROVIDER_PASSWORD"]
SSO_SALT = os.environ["PROVIDER_SSO_SALT"]


def same(a, b):
    return hmac.compare_digest((a or "").encode(), b.encode())


def check_auth():
    auth = request.authorization
    if not auth or auth.username != PROVIDER_ID or not same(auth.password, PASSWORD):
        abort(401)


@app.post("/clevercloud/resources")
def provision():
    check_auth()
    data = request.get_json()
    resource_id = secrets.token_hex(8)
    # Create the resource of data["addon_id"] with the data["plan"] plan
    return jsonify(id=resource_id, config={"MY_SERVICE_TOKEN": secrets.token_urlsafe(24)})


@app.delete("/clevercloud/resources/<resource_id>")
def deprovision(resource_id):
    check_auth()
    # Delete the resource, and succeed if it doesn't exist anymore
    return "", 204


@app.post("/clevercloud/sso/login")
def sso():
    form = request.form
    try:
        timestamp = int(form["timestamp"])
        parts = [form["id"], form["user_id"], form["email"], form.get("nav-data", ""), SSO_SALT, str(timestamp)]
    except (KeyError, ValueError):
        abort(400)
    expected = hashlib.sha512(":".join(parts).encode()).hexdigest()
    if not same(form.get("signature"), expected) or abs(time.time() - timestamp) > 300:
        abort(403)
    # Sign the user in, then redirect them to the dashboard of the resource
    return "Signed in", 200, {"Content-Type": "text/plain"}
```

The application reads the values of your manifest from its environment: `PROVIDER_ID` holds its `id`, `PROVIDER_PASSWORD` its `api.password`, and `PROVIDER_SSO_SALT` its `api.sso_salt`. It needs Flask:

```text {filename="requirements.txt"}
flask
```

To try it locally, install Flask, then start the application with these values:

```bash
pip install flask
PROVIDER_ID=my-service PROVIDER_PASSWORD=local-password-123 PROVIDER_SSO_SALT=local-salt-456 flask --app app run --port 8000
```

To deploy it on Clever Cloud as a [Python application](/doc/deploy/applications/python/), commit `app.py` and `requirements.txt` in a Git repository, then create the application, set its variables and the module to start, with the values of your manifest:

```bash
clever create --type python my-service-provider
clever env set PROVIDER_ID my-service
clever env set PROVIDER_PASSWORD "<api.password>"
clever env set PROVIDER_SSO_SALT "<api.sso_salt>"
clever env set CC_PYTHON_MODULE app:app
clever deploy
```

The `base_url` of the manifest is then `https://<domain>/clevercloud/resources`, and its `sso_url` `https://<domain>/clevercloud/sso/login`, with the domain of the application.
