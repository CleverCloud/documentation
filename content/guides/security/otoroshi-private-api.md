---
type: docs
linkTitle: Private API with Otoroshi
title: Protect a private API with Otoroshi
description: Keep an API private on Clever Cloud with Request Flow and a Network Group, and expose it through Otoroshi with an API key, a quota, and a temporary ban of abusive clients
keywords:
- otoroshi
- api gateway
- api key
- quota
- fail2ban
- network groups
- request flow
- private application
- wireguard
---

{{< hextra/hero-subtitle >}}
  Keep an application out of public reach, and let Otoroshi decide which requests get to it.
{{< /hextra/hero-subtitle >}}

An API gateway sits in front of your services: it receives the requests, checks them, and forwards the valid ones. [Otoroshi](/doc/deploy/services/otoroshi/) is the API gateway that Clever Cloud runs for you, with hundreds of plugins to authenticate, limit, and transform requests. These protections only matter if requests can't bypass the gateway and reach the application directly, through its own domain.

This guide deploys a Node.js API and blocks its public domain with [Request Flow](/doc/manage/request-flow/#block-public-access). Otoroshi then reaches it through a [Network Group](/doc/network/network-groups/), a private WireGuard network. It only forwards `GET` requests that carry a valid API key, within a quota, and bans for a while the clients that fail too often.

## Prepare the application

You need [Git](https://git-scm.com/downloads), [jq](https://jqlang.org/), [OpenSSL](https://openssl-library.org/), [Clever Tools](/doc/tools/cli/), and a [Clever Cloud account](https://console.clever-cloud.com). Create a project and initialize its Git repository:

```bash
mkdir private-api
cd private-api
git init
```

The application answers every request with its path, the address of its client, and the headers it receives, which show where requests come from and what reaches the application. It listens on `0.0.0.0`, so that the Network Group reaches it, and on the port set in `PORT`:

```js {filename="server.js"}
const http = require('node:http');

const port = process.env.PORT || 8080;

http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({ path: req.url, client: req.socket.remoteAddress, headers: req.headers }, null, 2) + '\n');
}).listen(port, '0.0.0.0');
```

The `start` script of `package.json` tells the [Node.js runtime](/doc/deploy/applications/nodejs/) how to run it:

```json {filename="package.json"}
{
  "name": "private-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  }
}
```

## Deploy the private application

Create the application, then show its domain:

```bash
clever create --type node private-api
clever domain
```

Block its public access: with `CC_REQUEST_FLOW` set to `block`, its public domain answers `200 OK` to every request, without reaching the application. The application then listens on port `9000`, set in `PORT`:

```bash
clever env set CC_REQUEST_FLOW block
clever env set PORT 9000
```

Commit the project, then deploy it:

```bash
git add .
git commit -m "Deploy a private API"
clever deploy
```

Once deployed, the domain of the application answers `OK` to any request:

```bash
curl https://app-xxx.cleverapps.io/hello
```

## Create Otoroshi and its Network Group

Create the Otoroshi add-on. It serves routes on its routes domain, by default a `cleverapps.io` domain. To choose it, add the `routes-domain` option at creation, such as `--option routes-domain=my-api.cleverapps.io`, or your own domain, whose [DNS you configure](/doc/manage/domain-names/).

Then enable the Network Group of Otoroshi with the operators commands of Clever Tools. Enabling it restarts Otoroshi:

```bash
clever addon create otoroshi my-otoroshi
clever features enable operators,ng
clever otoroshi enable-ng my-otoroshi
```

Otoroshi now belongs to a Network Group. Get the IDs of the application and of this group, then link the application to it, so that Otoroshi reaches it on port `9000` through the domain name of its member:

```bash
APP_ID=$(jq -r '.apps[0].app_id' .clever.json)
NG_ID=$(clever otoroshi get my-otoroshi -F json | jq -r .features.networkGroup.id)
clever ng link "$APP_ID" "$NG_ID"
BACKEND="$APP_ID.m.$NG_ID.cc-ng.cloud"
```

## Configure the protections

`clever otoroshi get` gives the URL and the credentials of the API of Otoroshi. Otoroshi runs on a Java application, whose `OTOROSHI_ROUTE_BASE_DOMAIN` variable holds the routes domain:

```bash
OTOROSHI=$(clever otoroshi get my-otoroshi -F json)
API_URL=$(echo "$OTOROSHI" | jq -r .api.url)
API_AUTH=$(echo "$OTOROSHI" | jq -r '"\(.api.user):\(.api.secret)"')
OTOROSHI_APP=$(echo "$OTOROSHI" | jq -r .resources.entrypoint)
ROUTES_DOMAIN=$(clever env --app "$OTOROSHI_APP" -F json \
  | jq -r '.env[] | select(.name == "OTOROSHI_ROUTE_BASE_DOMAIN") | .value')
```

This route serves `/api` on the routes domain, and forwards requests to port `9000` of the application, with their full path. The WireGuard tunnel already encrypts this traffic, so the backend doesn't use TLS. Its plugins check each request in turn:

- `Fail2BanPlugin` bans a client for a minute once it sends a wrong secret 3 times within a minute
- `AllowHttpMethods` only accepts `GET` requests
- `ApikeyCalls` rejects requests without a valid API key, or beyond its quota

```bash
curl -u "$API_AUTH" -H "Content-Type: application/json" \
  -X POST "$API_URL/api/routes" --data @- <<EOF
{
  "id": "route_private_api",
  "name": "private-api",
  "frontend": { "domains": ["$ROUTES_DOMAIN/api"], "strip_path": false },
  "backend": { "targets": [{ "hostname": "$BACKEND", "port": 9000, "tls": false }] },
  "plugins": [
    { "plugin": "cp:otoroshi.next.plugins.OverrideHost" },
    { "plugin": "cp:otoroshi.next.plugins.Fail2BanPlugin", "config": {
        "max_retry": 3, "detect_time": 60000, "ban_time": 60000, "status_codes": ["401"] } },
    { "plugin": "cp:otoroshi.next.plugins.AllowHttpMethods", "config": { "allowed": ["GET"] } },
    { "plugin": "cp:otoroshi.next.plugins.ApikeyCalls" }
  ]
}
EOF
```

This API key only works on this route, with a quota of 10 calls every 10 seconds, the default throttling window of Otoroshi. Its secret is random: keep it, as each call to the private API needs it with the client ID:

```bash
API_SECRET=$(openssl rand -base64 32)
curl -u "$API_AUTH" -H "Content-Type: application/json" \
  -X POST "$API_URL/api/apikeys" --data @- <<EOF
{
  "clientId": "private-api-client",
  "clientSecret": "$API_SECRET",
  "clientName": "private-api-client",
  "authorizations": [{ "kind": "route", "id": "route_private_api" }],
  "throttlingQuota": 10
}
EOF
```

You can also manage these settings from the web interface of Otoroshi, opened with `clever otoroshi open webui my-otoroshi`.

## Test the protections

After a few seconds, Otoroshi serves the route. Without an API key, it rejects the request with a `400` status and the `no apikey` error:

```bash
curl "https://$ROUTES_DOMAIN/api/hello"
```

With the API key, the request reaches the application:

```bash
curl -u "private-api-client:$API_SECRET" "https://$ROUTES_DOMAIN/api/hello"
```

```json
{
  "path": "/api/hello",
  "client": "10.113.0.5",
  "headers": {
    "host": "app_xxx.m.ng_xxx.cc-ng.cloud",
    "accept": "*/*",
    "sozu-id": "01M6XZE0PKPGJQM7ZW7NR437M7",
    "forwarded": "proto=https;for=\"203.0.113.10:64057\";by=198.51.100.20",
    "user-agent": "curl/8.7.1",
    "traceparent": "00-84a606f02a267afb013a8094e78a8f74-0febd1452d66a01b-01",
    "x-request-id": "01M6XZE0PKPGJQM7ZW7NR437M7",
    "x-forwarded-port": "443"
  }
}
```

The client of the application is Otoroshi, at its address in the Network Group, and `host` is the domain name of the member, set by the `OverrideHost` plugin. The `forwarded` header keeps the address of the original client. The credentials of the API key don't reach the application: Otoroshi checks them, and doesn't forward the `authorization` header.

Otoroshi only accepts `GET` requests on this route, and rejects the others with a `405` status:

```bash
curl -X POST -u "private-api-client:$API_SECRET" "https://$ROUTES_DOMAIN/api/hello"
```

Beyond the quota, Otoroshi rejects requests with a `429` status until the next window. Send 15 requests in a row: once the quota of the window is reached, the next ones get a `429` status instead of `200`:

```bash
for i in $(seq 1 15); do
  curl -s -o /dev/null -w "%{http_code} " -u "private-api-client:$API_SECRET" "https://$ROUTES_DOMAIN/api/hello"
done
```

Otoroshi identifies a client by its IP address, on every route that uses this plugin. A client that sends a wrong secret 3 times within a minute gets `401` statuses, then a `403` status even with the right secret, until the ban ends:

```bash
for i in $(seq 1 3); do
  curl -s -o /dev/null -w "%{http_code} " -u "private-api-client:wrong-secret" "https://$ROUTES_DOMAIN/api/hello"
done
curl -u "private-api-client:$API_SECRET" "https://$ROUTES_DOMAIN/api/hello"
```

```json
{"error":"temporary_ban","message":"You are temporarily banned due to too many failed requests.","retry_in_seconds":59}
```

To expose the API on another domain later, add it to its Java application and [configure its DNS](/doc/manage/domain-names/), then add it to the frontend of the route.

## Extend your API

The plugins and extensions of Otoroshi cover many other needs, which this guide doesn't set up. Some popular ones:

- [Keycloak](/doc/deploy/services/keycloak/) to log your users in, with an [authentication module](https://maif.github.io/otoroshi/manual/docs/tutorials/secure-app-with-keycloak)
- [JWT tokens](https://maif.github.io/otoroshi/manual/docs/tutorials/secure-an-app-with-jwt-verifiers) issued by your identity provider, checked by Otoroshi
- [OAuth 2.0 client credentials](https://maif.github.io/otoroshi/manual/docs/tutorials/secure-with-oauth2-client-credentials), for calls between services
- [Eclipse Biscuit](https://doc.biscuitsec.org/) tokens, which their holder can restrict, with the [Biscuit Studio](https://cloud-apim.github.io/otoroshi-biscuit-studio/docs/overview) of Cloud APIM
- A [developer portal](https://cloud-apim.github.io/otoroshi-api-portal/) of Cloud APIM, with the documentation of your API and the keys of its users
- [Data exporters](https://maif.github.io/otoroshi/manual/docs/entities/data-exporters), to send the events of the gateway to your analytics tools
- A [mailer endpoint](https://github.com/cloud-apim/otoroshi-plugin-mailer) of Cloud APIM, which turns your SMTP provider into a REST API to send emails
- A static site, such as the documentation of your API, served from a [zip archive](https://maif.github.io/otoroshi/manual/docs/tutorials/zip-backend-plugin)
- [Workflows](https://maif.github.io/otoroshi/manual/docs/topics/workflows), to automate scenarios around your routes, from a visual editor
- [Built-in plugins](https://maif.github.io/otoroshi/manual/docs/plugins/built-in-plugins), such as CORS, a response cache, canary releases, or a Swagger UI

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/deploy/services/otoroshi" title="Otoroshi on Clever Cloud" subtitle="Create Otoroshi, set its domains, and link it to a Network Group" icon="shield-check" >}}
  {{< card link="/developers/doc/network/network-groups" title="Network Groups" subtitle="Link applications, add-ons, and machines in a private network" icon="endpoints" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain middleware in front of your application, or block it" icon="traffic-light" >}}
  {{< card link="https://maif.github.io/otoroshi/manual/docs/index.html" title="Otoroshi manual" subtitle="Routes, plugins, and API keys in the documentation of Otoroshi" icon="book-open" >}}
{{< /cards >}}
