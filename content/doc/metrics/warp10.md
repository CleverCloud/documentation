---
type: docs
linkTitle: Warp 10
title: Warp 10
description: Use Warp 10 Geo Time series database on Clever Cloud with presentations, concepts, and implementation examples
keywords:
  - GTS
  - warp 10
  - Quantum
  - visualization
  - time series
  - database
aliases:
- /doc/administrate/metrics/warp10/
---

{{% content "warp10-concepts" %}}

## Endpoint

The Clever Cloud Warp 10 endpoint is:

```html
https://c2-warp10-clevercloud-customers.services.clever-cloud.com/api/v0
```

* Learn more about [endpoint gateway on warp10.io](https://www.warp10.io/content/03_Documentation/03_Interacting_with_Warp_10/01_Introduction)

You can find the endpoint and an available token under the `metric` tab of your application. You can query our Warp 10 platform with your own script. Here's an example with `curl`:

```bash
  curl -T <Path/to/a/warpscript_file> https://c2-warp10-clevercloud-customers.services.clever-cloud.com/api/v0/exec
```
## Token

Tokens are based on your application with the notion of producer and owner. Hence, only the data owner can see it.

You can find a 5 days available token in the `metric` tab of your application.

{{% content "warp10-content" %}}
