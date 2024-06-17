---
title: Marketplace APIs & Tools
shortdesc: How to integrate your own service as an add-on on Clever Cloud's Marketplace
keywords:
- Add-on
- API
- Marketplace
- Partners
aliases:
- /doc/extend/addon-api/
type: docs
comments: false
weight: 13

---

Clever Cloud allows its Marketplace partners to provide services as add-ons with revenue sharing. Thus, they can be available to purchase and provision from the [Console](https://console.clever-cloud.com), [Clever Tools](https://github.com/CleverCloud/clever-tools), the [API](/api) or other integrations such as the [Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/).

You want to help us to offer more services to our users? Just reach us: [partnership@clever-cloud.com](mailto:partnership@clever-cloud.com?subject=I%20want%20to%20become%20a%20Clever%20Cloud%20Marketplace%20partner). Then, you will be able to use our dedicated tools and APIs to provide your service as an add-on, whether they're hosted on Clever Cloud or not.

* [Add-on Manifest](#add-on-manifest): to provide your service as an add-on
* [Add-on provider requests](#add-on-provider-requests): to provision, modify or delete add-ons
* [Add-on infos API](#add-on-infos-api): to list provisioned add-ons and get detailed information about them

## Add-on Manifest

First, provide a JSON manifest file that describes your add-on:

```json
{
  "id": "addon-name",
  "name": "Addon Name",
  "api": {
    "config_vars": [ "ADDON_NAME_MY_VAR" ],
    "regions": [ "eu" ],
    "password": "44ca82ddf8d4e74d52494ce2895152ee",
    "sso_salt": "fcb5b3add85d65e1dddda87a115b429f",
    "production": {
      "base_url": "https://yourservice.com/clevercloud/resources",
      "sso_url": "https://yourservice.com/clevercloud/sso/login"
    },
    "test": {
      "base_url": "http://localhost:9000/clevercloud/resources",
      "sso_url": "http://localhost:9000/clevercloud/sso/login"
    }
  }
}
```

Fields

* `id` - An ID for your add-on. All lower case, no spaces or punctuation. Underscores and dashes are allowed. This can’t be changed after the first push. It is also used for HTTP basic auth when making provisioning calls.

* `name` (Optional) - A human-readable name for your add-on. You will be able to change it later in the dashboard, so you don't even have to provide it right now.

* `api/config_vars` - A list of configuration variables that will be returned on provisioning calls. Each `config_var` name must start with the capitalized, add-on id with underscores, as in the example.

* `api/password` - Password that Clever Cloud will send in HTTP basic auth when making provisioning calls. You should generate a long random string for that field.

* `api/sso_salt` - Shared secret used in single sign-on between the Clever Cloud admin panel and your service’s admin panel. You should generate a long random string for that field.

* `api/regions` - The list of geographical zones supported by your add-on. It cannot be empty. As for now, it *MUST* contain the element "eu". More will be supported.

* `api/production/base_url` - The production endpoint on which Clever Cloud sends actions requests (provision, deprovision, and plan change).

* `api/production/sso_url` - The production endpoint for single sign-on.

* `api/test/base_url` - The test endpoint on which Clever Cloud sends actions requests. Used to test your service when you create an add-on provider. After the add-on creation,`api/production/base_url` is used.

* `api/test/sso_url` - The test endpoint for single sign-on. Used to test your service when you create an add-on provider. After that, the `api/production/sso_url` is used.

## Add-on Provider requests

When a Clever Cloud's customer interacts with your add-on, you'll receive requests on your `base_url` API endpoint. The following sections describe the requests you'll receive and the responses you should send.

### Provisioning

When a customer installs your add-on, Clever Cloud issues a POST request to your service to provision a resource for his app.

The request will be the following:

```json
Request: POST {base_url}
Request Body: {
  "addon_id": "addon_xxx",
  "owner_id": "orga_xxx",
  "owner_name": "My Company",
  "user_id": "user_yyy",
  "plan": "basic",
  "region": "EU",
  "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx",
  "logplex_token": "logtoken_yyy",
  "options": {}
}
Response Body: {
  "id": "myaddon_id",
  "config": {
    "ADDON_NAME_MY_VAR": "some value"
  },
  "message": "Some provisioning message"
}
```

The request body contains the following fields:

* `addon_id` - The id we give to your add-on to identify it on our side.

* `owner_id` - The id of the customer this add-on will belong to.

* `owner_name` - The name of the customer. (Actually, the name of the organisation)

* `user_id` - The id of the user that is performing the action of provisioning this
  add-on. (The user will do it for the account of `owner_id`).

* `plan` - The slug field for the plan the user chose. You can create
plans in the dashboard once your add-on manifest has been uploaded to
the Clever Cloud platform. We send you the slug of the given plan,
not its name.

* `region` - The region to provision the add-on. As for now, only "EU" will be sent.

* `callback_url` - The URL you can use to get informations about the add-on and the user. This URL is available as soon as the provisioning is done. You can't use this URL during the POST call.

* `logplex_token` - Deprecated, don't use it.

* `options` - String -> String map with options.

The response body contains the following fields:

* `id` - The add-on id as seen from your side. It *MUST* be a String.

* `config` (Optional) - A String -> String map with value for each config\_var defined in your manifest. A key that is not in your config\_vars will be ignored.

* `message` (Optional) - A creation message we will display in the dashboard.

### Deprovisioning

When a customer deletes your add-on, Clever Cloud issues a DELETE request to your service to deprovision a ressource for his app.

The request will be the following:

```json
Request: DELETE {base_url}/{addon_id}
Request Body: none
Response Status: 200
```

* `addon_id` - This is the same as the `id` field set in the response to the provisioning call.

### Plan change

When a customer wants to change its add-on's plan, Clever Cloud issues a PUT request to your service.

The request will be the following:

```json
Request: PUT {base_url}/{addon_id}
Request Body: {
  "addon_id": "addon_xxx",
  "plan": "premium"
}
Response Body: {
  "config": { ... },
  "message": "your message here"
}
```

* `addon_id` - This is the same as the `id` field set in the response to the provisioning call.

The request body contains:

* `addon_id` - The add-on's id as seen from our side.

* `plan` - The name of the new plan.

The response body contains:

* `config` - The value for the new config map. Same constraints as in the provisioning response.

* `message` - A message displayed in our dashboard.

### Examples

You can find templates for add-on providers in various languages on GitHub:

* [https://github.com/Redsmin/passport-clevercloud](Node.js)
* [https://github.com/CleverCloud/addon-provider-template](Scala with Play! Framework 2)

## Add-on Infos API

This is the API Clever Cloud provides to allow you to list provisioned add-ons and get detailed information about them.

```bash
curl -XGET https://api.clever-cloud.com/v2/vendor/apps -u addon-name:44ca82ddf8d4e74d52494ce2895152ee
```

### List all add-ons provided by you

```json
GET /vendor/apps
Response Body: [
  {
    "provider_id": "addon-name",
    "addon_id": "addon_xxx",
    "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx",
    "plan": "test",
    "owner_id": "user_foobar"
  }, {
    "provider_id": "addon-name",
    "addon_id": "addon_yyy",
    "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_yyy",
    "plan": "premium",
    "owner_id": "orga_baz"
  }
]
```

* `provider_id` - Should be the same as the "id" field of your uploaded manifest.

* `addon_id` - The add-on's id from Clever Cloud's POV.

* `callback_url` - URL to call to get more informations about this add-on.

* `plan` - The current plan of this add-on.

* `owner_id` - The id of the owner that provisioned the add-on. This should never change.

### Get information about a specific add-on

**Caution**: this endpoint is **not** available during the provisioning call. If you want
information, you need to reply to the provisioning call, **then** you can call this
endpoint.

```json
GET /vendor/apps/{addonId}
Response Body: {
  "id": "addon_xxx",
  "name": "My addon-name instance",
  "config": {"MYADDON_URL": "http://myaddon.com/52e82f5d73"},
  "callback_url": "https://api.clever-cloud.com/v2/vendor/apps/addon_xxx",
  "owner_email": "user@example.com",
  "owner_id": "orga_baz",
  "owner_emails": ["user@example.com", "foobar@baz.com"],
  "region": "eu",
  "domains": []
}
```

This endpoint gives you more information about a provisioned add-on.

* `id` - The add-on id from Clever Cloud's POV.

* `name` - The name the user gave to this add-on in the Clever Cloud dashboard.

* `config` - Config vars as you defined during the provision call.

* `callback_url` - The URL you just called.

* `owner_email` - One of the owner's email address.

* `owner_emails` - All the owner's email addresses.

* `owner_id` - The id of the owner that provisioned the add-on. This should never change.

* `region` - The region this add-on is located in. As for now, we only support "eu".

* `domains` - Originally the domains names for the application owning the add-on. We return an empty list.

### Update the configuration variables for an add-on

```json
PUT /vendor/apps/{addonId}
Request Body: {
  "config": {
    "ADDON_NAME_URL": "http://myaddon.com/ABC123"
  }
}
Response Status: 200 OK
```

The object should only contain the `config` object your API returned
during the provisioning.

{{< callout type="info" >}}
This endpoint is **not** available during the provisioning call. You need to reply to the provisioning call, **then** you can call this endpoint.
{{< /callout >}}

### Sample code

```python
#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
api.py
"""
from flask import Flask, redirect, Response, jsonify, request
import auth
import provision

app = Flask(__name__)

@app.route('/')
def index():
  """
  Render the home template
  """
  return redirect("https://google.com/")

@app.route('/clevercloud/resources', methods=['POST'])
@auth.requires_auth
def clevercloud_create_resource():
  data = request.json
  msg = provision.add(**data)
  return jsonify(msg)

@app.route('/clevercloud/resources/<string:id>', methods=['DELETE','PUT'])
@auth.requires_auth
def clevercloud_action_resource(id):
  data = request.json
  if request.method == 'POST':
    msg = provision.del(id,**data)

  if request.method == 'PUT':
    msg = provision.update(id,**data)

  return jsonify(msg)

@app.route('/clevercloud/sso/login')
def clevercloud_sso_login():
  return Response(status=200)

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=9000,debug=True)
```

## Authentication

To secure the calls to the API, please provide a HTTPS connection and use a Basic authentication. The username must be your provider ID (`addon-name` in our example). The password must be the `password` value set in your manifest.

Your provider API must check that all calls to it are authenticated with this user/password combination. If the authentication fails, you should return a 401 HTTP status code.

### Sample with Flask in Python

```python
from functools import wraps
from flask import request, Response


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return password == '44ca82ddf8d4e74d52494ce2895152ee'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Poney required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
```

## SSO

Your service probably has a web UI admin panel that your users log into to manage and view their resources. Clever Cloud customers will be able to access the admin panel for their resource if you implement single sign-on (SSO).

Clever Cloud will generate a single sign-on token by combining the salt (a shared secret), timestamp, and resource ID. The user’s browser will be redirected to your site with this token. Your site can confirm the authenticity of the token, then set a cookie for the user session and redirect them to the admin panel for their resource.

When the user clicks your add-on in their add-on menu, they will be directed via HTTP POST to a URL defined in your manifest.

```http
POST <production/sso_url>
Request Body: id=<id>&token=<token>&timestamp=<timestamp>&nav-data=<nav-data>&email=<email>
```

* The hostname or `sso_url` comes from your add-on manifest
* The `id` is the ID for the previously provisioned resource
* The `timestamp` is a millisecond timestamp. You *SHOULD* verify that it's not older than 15 minutes
* The `token` is computed using the formula below
* The `nav-data` contains information like the current app name and installed add-ons for Clever Cloud's Console.

### Token

The token field in the SSO call, is created as follows:

```javascript
sha1sum(id + ':' + sso_salt + ':' + timestamp)
```

Where:

* `id` - The id of the connecting add-on. This is the id you returned on
the provision call.

* `sso_salt` - The sso_salt field defined in your manifest.

* `timestamp` - The timestamp field of the sso request.

### Sample in Python

```python
from hashlib import sha1
import time

id = "1234"
salt = "fcb5b3add85d65e1dddda87a115b429f"
timestamp = str(time.time())
token = sha1(id + ':' + salt + ':' + timestamp).hexdigest()
print token
```

This will return:

```text
'aca601ba464437cbaa12b2fedd7db755c32ddb5e'
```