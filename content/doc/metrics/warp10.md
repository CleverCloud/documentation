---
type: docs
title: Warp 10
shortdesc: Warp 10. Geo Time series database. Presentations, concepts and examples
tags:
  - metrics
aliases:
- /doc/administrate/metrics/warp10/
keywords:
  - GTS
  - warp 10
  - Quantum
  - visualization
  - time series
  - database
---

## Main concepts

Warp 10 is a time series database. The notion of `class`, `labels`, `longitude`, `latitude`, `altitude` and `value` are used.

A GTS is a GeoTime Serie defined by a `class` and some `labels`. They're indexed and used to quickly retrieved the data.

`labels` is a kind of dictionary. That's called a **map** under the warp10 terminology.

A GTS may contain some values which have the following models : `[ timestamp longitude latitude altitude value ]`

Warp 10 uses [Warp Script](https://www.warp10.io/content/03_Documentation/04_WarpScript). It's a **stack** based **language using reverse polish notation**.

> The metrics OVHcloud team built an other way to request Warp 10: <https://github.com/ovh/tsl/>
> Warp 1O documentation [is available on their website](https://www.warp10.io/doc/reference)

### Time and duration in Warp 10

> More information about [date functions here](https://www.warp10.io/tags/date), and [time functions here](https://www.warp10.io/tags/time).

{{< callout type="info" >}}
The platform's time unit is in **microsecond**.
{{< /callout >}}

#### Duration is set by the followings symbols

- `d` : day
- `h` : Hour
- `ms` : millisecond
- `ns` : nanosecond
- `ps` : picosecond
- `s` : second
- `us` : microsecond
- `w` : week

#### Date

Allowed format :

- ISO8601
- Timestamp in microsecond

Builtin function :

- `NOW` : get the current timestamp
- `ISO8601` : Convert a string or a timestamp to a ISO8601 date format

## Endpoint

The Clever Cloud Warp 10 endpoint is:

```html
https://c2-warp10-clevercloud-customers.services.clever-cloud.com/api/v0
```

- Learn more about [endpoint gateway on warp10.io](https://www.warp10.io/content/03_Documentation/03_Interacting_with_Warp_10/01_Introduction)

You can find the endpoint and an available token under the `metric` tab of your application. You can query our Warp 10 platform with your own script. Here's an example with `curl`:

```bash
  curl -T <Path/to/a/warpscript_file> https://c2-warp10-clevercloud-customers.services.clever-cloud.com/api/v0/exec
```

{{< callout type="warning" >}}
Do not forget the endpoint. `exec` in the previous example.
{{< /callout >}}

## Token

Tokens are based on your application with the notion of producer and owner. Hence, only the data owner can see it.

You can find a 5 days available token in the `metric` tab of your application.

## Technical constraints

The followings limits are defined in Warp 10. The **soft** one can be passed over by an [`AUTHENTICATE`](https://www.warp10.io/doc/AUTHENTICATE) operation. The **hard** one is unsurpassable.

| WarpScript Operator | Warp 10 limit description | soft limit | hard limit |
| ------------------- | ------------------------------------------------------------- | ---------- | ---------- |
| MAXGTS | Maximum number of GTS which can be fetched | 10e5 | 5e7 |
| LIMIT | Maximum number of datapoints which can be fetched during a script execution | 10e6 | 10e7 |
| MAXBUCKETS | Maximum number of buckets which can be created by a call to BUCKETIZE | 10e5 | 50e5 |
| MAXDEPTH | Maximum depth (number of levels) of the execution stack | 5e3 | 5e3 |
| MAXLOOP | Maximum number of milliseconds which can be spent in a loop | 5e3 | 10e3 |
| MAXOPS | Maximum number of operations which can be performed during a single WarpScript execution | 5e6 | 5e7 |
| MAXSYMBOLS | Maximum number of simultaneous symbols which can be defined on the stack during a single WarpScript execution | 64 | 256 |
| MAXGEOCELLS | Maximum number of cells a GEOSHAPE | 10e3 | 10e4 |
| MAXPIXELS | Maximum size (in pixels) of images which can be created by PGraphics | 10e5 | 10e5 |
| MAXRECURSION | Maximum nesting depth of macro calls | 16 | 32 |

{{< callout type="warning" >}}
Operation over **soft limits** may be intensives.
{{< /callout >}}

### Usage

An example where it is needed to increase the fetch limit by the `LIMIT` function

```warpscript
'<READTOKEN>' AUTHENTICATE
50e6 TOLONG LIMIT
// Fetch on the 'accessLogs' class for your application id as labels
[ '<READTOKEN>' 'accessLogs' { 'app_id' '<APP_ID>'  } NOW 1 w ] FETCH
```

## Visualization and exploration

### Quantum

Quantum is a web tool used to run some WarpScript. You can access to it from your metrics interface.

It provides the path to the Clever Cloud Warp 10 gateway and let you explore your data.

## Macro

Warp 10 provide a server side macro manager. It is a way to release some ready to use WarpScript. Hence, Clever Cloud provides some macros as helpers to avoid redundant and often need code.

{{< callout type="info" >}}
More information on the [Warp 10' macros documentations](https://www.warp10.io/content/03_Documentation/07_Extending_Warp_10/01_Server_side_macros).
{{< /callout >}}

### Consumption

The following macros are helpers to compute consumption in seconds

- `app_consumption`

Return the consumption in **second** by **applications** for a specific **organisation**.
`Start` and `End` parameters can be either a timestamp in microseconds or an iso8601 date format.

```bash
'<READ TOKEN>' '<ORGANISATION ID>' '<START>' '<END>' @clevercloud/app_consumption
```

- `orga_consumption`

Return **all** the consumption in **second** for a specific **organisation**. `Start` and `End` parameters
can be either a timestamp in microseconds or an iso8601 date format.

```bash
'<READ TOKEN>' '<ORGANISATION ID>' '<START>' '<END>' @clevercloud/app_consumption
```

### Access Logs

- `fetch_accessLogs_key_v0`

We provide the following macro to easily and quickly deep dive into access logs data. As we store access log as a JSON value in a geotime series ([metrics documentation here]({{< ref "doc/metrics#access-logs-metrics" >}})), this macro can be useful for straightforward access to a specific key. It allows you to fetch the `accessLogs` class and get only wanted value instead of the whole JSON.

```bash
  '<READ TOKEN>' { 'app_id'  'id' } '<1stLevelKey>' NOW 1 h  @clevercloud/fetch_accessLogs_key_v0
```

```bash
  '<READ TOKEN>' { 'app_id'  'id' } '<1stLevelKey>.<2ndLevelKey>' NOW 10 m  @clevercloud/fetch_accessLogs_key_v0
```

> More example in the [metrics part of this documentation]({{< ref "doc/metrics#access-logs-metrics" >}}).

**Nested keys** can be reached using a dot (`.`) to represent the depth.

```bash
'<READ TOKEN>' '<LABELS>' '<KEY>' '<START>' '<END>' @clevercloud/fetch_accessLogs_key_v0
```
