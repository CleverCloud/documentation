---
title: "API: set environment variables at application creation"
date: 2024-03-07
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
description: A game changer for some features coming soon
aliases:
- /changelog/2024-03-07-env-vars-app-creation-api
excludeSearch: true
---

When you create an application with the Clever Cloud API, you can now set environment variables directly. This feature is available in the `POST v2/organisations/{id}/applications` endpoint, with an object to set:

```json
"env": {
    "ENV_VAR": "value",
    "ANOTHER_ENV_VAR": "another value"
}
```

The response will contain an `env` object, with the environment variables set:

```json
"env": [
{
  "name": "ENV_VAR",
  "value": "value"
},
{
  "name": "ANOTHER_ENV_VAR",
  "value": "another value"
}]
```

You can get this object from the applications endpoints, such as `GET v2/organisations/{id}/applications/{appId}`.
