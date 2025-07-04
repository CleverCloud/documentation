---
title: Identify VM Tasks through the API
date: 2023-11-29
tags:
  - api
  - applications
authors:
  - name: Alexandre Duval
    link: https://github.com/kannarfr
    image: https://github.com/kannarfr.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: You can now check if an application is a task via the Clever Cloud API
aliases:
- /changelog/2023-11-29-api-update
excludeSearch: true
---
For years, you can deploy applications on Clever Cloud as a `Task` with the API or more recently the `CC_TASK=true` environment variable. As this feature will be widely available and used, the API has been updated to return such a state in the `instance.lifetime` object:

```json{filename="GET https://api.clever-cloud.com/v2/self/applications/<appId>",linenos=table,hl_lines=[17]}
{
  "id": "string",
  "name": "string",
  "description": "string",
  "zone": "string",
  "zoneId": "string",
  "instance": {
    "type": "string",
    "version": "string",
    "variant": {},
    "minInstances": int,
    "maxInstances": int,
    "maxAllowedInstances": int,
    "minFlavor": {},
    "maxFlavor": {},
    "flavors": [],
    "lifetime": "string",  //Allowed: REGULAR ┃ MIGRATION ┃ TASK
    "instanceAndVersion": "string"
  },
  …
}
```

- [Read the full APIv2 documentation](/developers/api/v2)
