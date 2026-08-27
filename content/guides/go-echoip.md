---
type: docs
linkTitle: EchoIP
title: Deploy EchoIP with Go
description: Build and deploy the EchoIP IP address lookup service with the Go runtime
keywords:
- go
- echoip
- golang
- IP service
- web service
---

{{< hextra/hero-subtitle >}}
  Deploy EchoIP from source with the Go runtime and expose the client IP received through Clever Cloud’s reverse proxy
{{< /hextra/hero-subtitle >}}

[EchoIP](https://github.com/mpolden/echoip) is a service that returns information about the client IP address in plain text, JSON or HTML.

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com)
- [Git](https://git-scm.com/downloads)
- [Clever Tools](/doc/cli), installed and connected to your account

## Clone EchoIP

Clone the upstream repository and move into its directory:

```bash
git clone https://github.com/mpolden/echoip.git
cd echoip
```

## Create the application

Create a Go application with the `myEchoIp` alias:

```bash
clever create -t go -a myEchoIp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application’s URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

## Configure EchoIP

The upstream repository contains several Go packages. Select the EchoIP command package, then start its compiled binary with `X-Forwarded-For` as a trusted header:

```bash
clever env set CC_GO_PKG ./cmd/echoip
clever env set CC_RUN_COMMAND "~/go_home/bin/echoip -H X-Forwarded-For"
```

Clever Cloud terminates HTTP connections at its reverse proxy and forwards the original client address in this header. Without the `-H` option, EchoIP would return the proxy address.

## Deploy EchoIP

Deploy the current Git commit and open the application:

```bash
clever deploy
clever open
```

The root path returns the client IP address for command-line clients and an HTML page for browsers. Use `/json` for a JSON response:

```bash
curl https://your-echoip-domain.example/json
```

Country, city and autonomous system information require the optional [GeoLite2 databases documented by EchoIP](https://github.com/mpolden/echoip#geoip-databases). The IP lookup works without them.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/golang" title="Go applications" subtitle="Configure and deploy Go applications" icon="go" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://github.com/mpolden/echoip" title="EchoIP repository" subtitle="Explore EchoIP features and configuration" icon="github" >}}
{{< /cards >}}
