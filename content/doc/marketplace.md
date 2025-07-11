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
- /doc/extend/add-ons-api/
type: docs
comments: false
weight: 13

---

Clever Cloud allows its Marketplace partners to provide services as add-ons with revenue sharing. Thus, they can be available to purchase and provision from the [Console](https://console.clever-cloud.com), [Clever Tools](https://github.com/CleverCloud/clever-tools), the [API](/developers/api) or other integrations such as the [Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/).

You want to help us to offer more services to our users? [Contact us](https://partners.clever-cloud.com). Then, you will be able to use our dedicated tools and APIs to provide your service as an add-on, whether they're hosted on Clever Cloud or not.

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
    "password": "<YOUR BEST RANDOM 35+ CHARS>",
    "sso_salt": "<YOUR VERY BEST RANDOM 35+ CHARS>",
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

### Available fields

* `id` - An ID for your add-on. All lower case, no spaces or punctuation. Underscores and dashes are allowed. This can’t be changed after the first push. It is also used for HTTP basic auth when making provisioning calls.
* `name` (Optional) - A human-readable name for your add-on. You will be able to change it later in the dashboard, so you don't even have to provide it right now.
* `api/config_vars` - A list of configuration variables that will be returned on provisioning calls. Each `config_var` name must start with the capitalized, add-on id with underscores, as in the example.
* `api/password` - Password that Clever Cloud will send in HTTP basic auth when making provisioning calls. You should generate a long random string for that field.
* `api/sso_salt` - Shared secret used in single sign-on between the Clever Cloud admin panel and your service’s admin panel. You should generate a long random string for that field.
* `api/regions` - The list of geographical zones supported by your add-on. It cannot be empty. As for now, it *MUST* contain the element "eu". More will be supported.
* `api/production/base_url` - The production endpoint on which Clever Cloud sends actions requests (provision and deprovision).
* `api/production/sso_url` - The production endpoint for single sign-on.
* `api/test/base_url` - The test endpoint on which Clever Cloud sends actions requests. Used to test your service when you create an add-on provider. After the add-on creation,`api/production/base_url` is used.
* `api/test/sso_url` - The test endpoint for single sign-on. Used to test your service when you create an add-on provider. After that, the `api/production/sso_url` is used.

## Add-on Provider requests

When a Clever Cloud's customer interacts with your add-on, you'll receive requests on your `base_url` API endpoint. The following sections describe the requests you'll receive and the responses you should send.

### Provisioning

When a customer installs your add-on, Clever Cloud issues a POST request to your service to provision a resource for his app.

Clever Cloud will send the following request:

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
* `callback_url` - The URL you can use to get details about the add-on and the user. This URL is available as soon as the provisioning is done. You can't use this URL during the POST call.
* `options` - String -> String map with options.
The response body contains the following fields:
* `id` - The add-on id as seen from your side. It *MUST* be a String.
* `config` (Optional) - A String -> String map with value for each config\_var defined in your manifest. A key that is not in your config\_vars will be ignored.
* `message` (Optional) - A creation message we will display in the dashboard.

### De-provisioning

When a customer deletes your add-on, Clever Cloud issues a DELETE request to your service to de-provision a resource for his app.

The request will be the following:

```json
Request: DELETE {base_url}/{addon_id}
Request Body: none
Response Status: 200
```

* `addon_id` - This is the same as the `id` field set in the response to the provisioning call.

### Examples

You can find templates for add-on providers in various languages on GitHub:

* [Node.js](https://github.com/Redsmin/passport-clevercloud)
* [Scala with Play! Framework 2](https://github.com/CleverCloud/addon-provider-template)

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

* `callback_url` - URL to call to get more details about this add-on.

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

* `config` - Configuration variables as you defined during the provision call.

* `callback_url` - The URL you just called.

* `owner_email` - One of the owner's email address.

* `owner_emails` - All the owner's email addresses.

* `owner_id` - The id of the owner that provisioned the add-on. This should never change.

* `region` - The region this add-on is located in. As for now, only "eu" is supported.

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
    return password == '<THE PASSWORD>'

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

Your service probably has a web UI admin panel that your users log into to manage and view their resources.
Clever Cloud customers will be able to access the admin panel for their resource if you implement single sign-on (SSO).

Clever Cloud will generate a single sign-on signature by combining the salt (a shared secret you defined in your manifest) with the rest of the body (see below).
Clever Cloud redirects the user’s browser to your SSO URL with this signature.
Your site can confirm the authenticity of the signature, then set a cookie for the user session and redirect them to the admin panel for their resource.

When the user opens your add-on dashboard in their add-on menu, they will be directed via HTTP POST to the SSO URL defined in your manifest.

```http
POST <production/sso_url>
Content-Type: application/x-www-form-urlencoded

id=<id>&timestamp=<timestamp>&nav-data=<nav-data>&email=<email>&user_id=<user_id>&signature=<signature>
```

* The hostname or `sso_url` comes from your add-on manifest
* The `id` is the ID for the previously provisioned resource
* The `timestamp` is a millisecond timestamp. You *SHOULD* verify that it's not older than a few minutes (like 5)
* The `user_id` is a unique string identifying the current user on the Clever Cloud platform
* The `email` is the current primary email of the current user on the Clever Cloud platform
* The `nav-data` contains information like the current app name and installed add-ons for Clever Cloud's Console. At the time of writing this doc, this field is always empty
* The `signature` is computed using the formula below

### Token

The `signature` field in the SSO call is created as follows:

```javascript
sha512sum(id + ':' + user_id + ':' + email + ':' + nav-data + ':' + sso_salt + ':' + timestamp)
```

Where `sso_salt` is the shared secret you defined while registering in the marketplace.
The other fields are the url-decoded fields previously enumerated.

### Sample in Python

```python
from hashlib import sha512
import time

id = "1234"
salt = "<SOME RANDOM STRING>"
user_id = "user_cccdddee-efff-4445-5566-6777888999aa"
email = "me@my.self"
nav_data = ""
timestamp = str(time.time())
sig = sha512((id + ':' + user_id + ':' + email + ':' + nav_data + ':' + sso_salt + ':' + timestamp).encode("utf-8")).hexdigest()
print sig
```

This code returns:

```python
'2a79420ccb4dccb2f18985da60393d1383d4ef4ac02cef3274a543bb3fe82d15e5dee19cbca753e8eac24e6383d332ef258daea6ea3340c3526af175329e7dd8'
```
