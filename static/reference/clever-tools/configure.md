---
type: docs
title: Application configuration with Clever Tools
shortdesc: Configure an application using the Clever Cloud CLI tool
tags:
- cli
- reference
keywords:
- apps
- configuration
---

## Inspect the current configuration

`clever config` will list you all available configuration for your application.

```shell
$ clever config
Name: phpinfo
Description: phpinfo
Zero-downtime deployment: enabled
Sticky sessions: disabled
Cancel current deployment on push: disabled
Force redirection of HTTP to HTTPS: disabled
```

You can also get a single configuration using `clever config get {name}`

```shell
$ clever config get cancel-on-push
Cancel current deployment on push: disabled
```

## Update your configuration

You can update a single configuration using `clever config set {name} {value}`

```shell
$ clever config set sticky-sessions true
Sticky sessions: enabled
```

You can also update all of the configuration at once using `clever config update [options]`

```shell
$ clever config update --description="Displays phpinfo()" --disable-sticky-sessions --enable-force-https
Description: Displays phpinfo()
Sticky sessions: disabled
Force redirection of HTTP to HTTPS: enabled
```
