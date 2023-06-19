---
title: Blackfire
position: 2
shortdesc: Configuring Blackfire on Clever Cloud
tags:
- apps
keywords:
- blackfire
- metrics
- monitoring
---


## Overview

Blackfire can be used on Clever Cloud with **PHP** applications.

[Blackfire](https://www.blackfire.io/) helps to improve web applications, performance at each step of its lifecycle: from development to test, staging and production.


## Blackfire configuration

### Necessary information

Before setting up your app, be sure to have a [Blackfire Account](https://www.blackfire.io/).


### Configuration

To configure Blackfire, you need to set the environment variables `CC_BLACKFIRE_SERVER_TOKEN` and `CC_BLACKFIRE_SERVER_ID`.


### Optional configuration

If you need to fine-tune agent settings, you can use the following environment variables:

```bash
CC_BLACKFIRE_LOG_LEVEL
CC_BLACKFIRE_MEMORY_LIMIT
CC_BLACKFIRE_COLLECTOR
CC_BLACKFIRE_TIMEOUT
CC_BLACKFIRE_STATSD
CC_BLACKFIRE_STATSD_PREFIX
```

### Usage

Just redeploy your application on Clever Cloud for the changes to take effect. A few minutes later, your application will begin sending data to Blackfire. Once Blackfire receives the data, your application will be listed in the dashboard.

