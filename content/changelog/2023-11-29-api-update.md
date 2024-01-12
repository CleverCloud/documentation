---
title: API update for tasks VM
date: 2023-11-29
tags:
  - api
excludeSearch: true
description: You can now check if an application is a task via the API
---
The API has been updated to return a "TASK" state in the `instance.lifetime` object on the path `https://api.clever-cloud.com/v2/self/applications/{appId}`.  
It is now easier to know whether an instance is of type "TASK" or not.

```json{filename="GET https://api.clever-cloud.com/v2/self/applications/<appId>",linenos=table,hl_lines=[10]}
{
  "id": "string",
  "name": "string",
  "description": "string",
  "zone": "string",
  "zoneId": "string",
  "instance": {
    …
    "defaultEnv": {},
    "lifetime": "REGULAR",    //Allowed: REGULAR┃MIGRATION┃TASK
    "instanceAndVersion": "string"
  },
  …
}
```

You can find the full API [documentation here](http://developers.clever-cloud.com/openapi/#get-/self/applications/-appId-).
