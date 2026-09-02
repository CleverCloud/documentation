---
type: docs
weight: 10
linkTitle: Access Logs
title: Access Logs
description: Read the HTTP requests reaching your applications on Clever Cloud, with their status, latency and origin
keywords:
- access logs
- http requests
- traffic
- latency
- monitoring
aliases:
- /doc/observability/access-logs
---

Access logs contain all incoming HTTP requests to your application. For the output of the application itself, see [Logs](/doc/develop/observability/logs).

It contains all incoming HTTP requests to your application. You can see access logs with the following command:

```bash
clever accesslogs
```

As with the `logs` command, you can specify `--before` and `--after` flags.
If you don't specify any options, the logs display continuously.

To change the output, specify the `--format` (`-F`) flag with one of these values:

- `human` (default): a human-readable, colored table

  ```txt
  2026-06-24T08:05:43.880Z   255.255.255.255   FR/Nantes   200   GET  /
  ```

- `clf`: [Common Log Format](https://en.wikipedia.org/wiki/Common_Log_Format)

  ```txt
  255.255.255.255 - - [24/Jun/2026:08:05:43 +0000] "GET /" 200 562
  ```

  The HTTP protocol version isn't part of the access log payload, so the request line is limited to `method path` (no `HTTP/x.y` token).

- `json`: a JSON array of log objects (requires a bounding flag such as `--before`)
- `json-stream`: a stream of JSON log objects

  Both JSON formats share the same object shape:

  ```json
  {
    "id": "01F91AEG8Z9RJKYB7JY7H56FNB",
    "date": "2026-06-24T08:05:43.880Z",
    "applicationId": "app_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "instanceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "region": "par",
    "zone": "par",
    "requestId": "01F91AEG8Z9RJKYB7JY7H56FNB",
    "bytesIn": 658,
    "bytesOut": 562,
    "source": {
      "ip": "255.255.255.255",
      "port": 58477,
      "city": "Nantes",
      "countryCode": "FR",
      "geoLocation": { "latitude": 50.624, "longitude": 3.0511 }
    },
    "destination": {
      "ip": "46.252.181.17",
      "port": 14001,
      "city": "Chaponost",
      "countryCode": "FR",
      "geoLocation": { "latitude": 45.7059, "longitude": 4.7444 }
    },
    "http": {
      "request": {
        "method": "GET",
        "path": "/",
        "host": "www.clever-cloud.com",
        "scheme": "https"
      },
      "response": {
        "statusCode": 200,
        "serviceTime": null,
        "time": 31
      }
    },
    "tls": null
  }
  ```
