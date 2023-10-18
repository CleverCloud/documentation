---
type: docs
title: Warp 10
shortdesc: Warp 10. Geo Time series database. Presentations, concepts and examples
tags:
  - metrics
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

A GTS is a GeoTime Serie defined by a `class` and somes `labels`. They are indexed and used to quickly retrieved the data.

`labels` is a kind of dictionnary. That is called a **map** under the warp10 terminology.

A GTS may contain some values which have the following models : `[ timestamp longitude latitude altitude value ]`

Warp 10 uses [Warp Script](https://www.warp10.io/content/03_Documentation/04_WarpScript). It's a **stack** based **language using reverse polish notation**.

> The metrics ovh team built an other way to request Warp 10: https://github.com/ovh/tsl/

> [Warp 1O documentation is availlable on their website](https://www.warp10.io/doc/reference)

### Time and duration in Warp 10

> More information about [date functions here](https://www.warp10.io/tags/date), and [time functions here](https://www.warp10.io/tags/time).

<div class=“panel panel-warning”>
  <div class=“panel-heading”>
    <h4>Note:</h4>
  </div>
  <div class=“panel-body”>
  The plateform's time unit is in <b>microsecond.</b>
  </div>
</div>

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
- `ISO8601` : Convert a string or a timstamp to a iso8601 date format

## Endpoint

The Clever Cloud Warp 10 endpoint is:

```
https://c1-warp10-clevercloud-customers.services.clever-cloud.com/api/v0
```

You can find documentation about endpoint gateway [here](https://www.warp10.io/content/03_Documentation/03_Interacting_with_Warp_10/01_Introduction).

> You can find the endpoint and an available token under the `metric` tab of your application

You can query our Warp 10 platform with your own script. Here's a curl example :

```bash
  curl -T <Path/to/a/warpscript_file> https://c1-warp10-clevercloud-customers.services.clever-cloud.com/api/v0/exec
```

> Do not forget the endpoint. `exec` in the previous exemple.

## Token

Tokens are based on your application with the notion of producer and owner. Hence, only the data owner can see it.

You can find a 5 days available token in the `metric` tab of your application.

## Technical constraints

The followings limits are defined in Warp 10. The **soft** one can be passed over by an [`AUTHENTICATE`](https://www.warp10.io/doc/AUTHENTICATE) operation. The **hard** one is unsurpassable.

<table class="table table-bordered">
<thead>
<tr>
<th style="text-align:center">WarpScript Operator</th>
<th style="text-align:center">Warp 10 limit description</th>
<th style="text-align:center">soft limit</th>
<th style="text-align:center">hard limit</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXGTS">MAXGTS</a></td>
<td style="text-align:center">Maximum number of GTS which can be fetched</td>
<td style="text-align:center">10e5</td>
<td style="text-align:center">5e7</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/LIMIT">LIMIT</a></td>
<td style="text-align:center">maximum number of datapoints which can be fetched during a script execution</td>
<td style="text-align:center">10e6</td>
<td style="text-align:center">10e7</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXBUCKETS">MAXBUCKETS</a></td>
<td style="text-align:center">maximum number of buckets which can be created by a call to BUCKETIZE</td>
<td style="text-align:center">10e5</td>
<td style="text-align:center">50e5</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXDEPTH">MAXDEPTH</a></td>
<td style="text-align:center">maximum depth (number of levels) of the execution stack</td>
<td style="text-align:center">5e3</td>
<td style="text-align:center">5e3</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXLOOP">MAXLOOP</a></td>
<td style="text-align:center">maximum number of <strong>milliseconds</strong> which can be spent in a loop</td>
<td style="text-align:center">5e3</td>
<td style="text-align:center">10e3</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXOPS">MAXOPS</a></td>
<td style="text-align:center">maximum number of operations which can be performed during a single WarpScript execution</td>
<td style="text-align:center">5e6</td>
<td style="text-align:center">5e7</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXSYMBOLS">MAXSYMBOLS</a></td>
<td style="text-align:center">maximum number of simultaneous symbols which can be defined on the stack during a single WarpScript execution</td>
<td style="text-align:center">64</td>
<td style="text-align:center">256</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXGEOCELLS">MAXGEOCELLS</a></td>
<td style="text-align:center">maximum number of cells a GEOSHAPE</td>
<td style="text-align:center">10e3</td>
<td style="text-align:center">10e4</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXPIXELS">MAXPIXELS</a></td>
<td style="text-align:center">maximum size (in pixels) of images which can be created by PGraphics</td>
<td style="text-align:center">10e5</td>
<td style="text-align:center">10e5</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://www.warp10.io/doc/MAXRECURSION">MAXRECURSION</a></td>
<td style="text-align:center">maximum nesting depth of macro calls</td>
<td style="text-align:center">16</td>
<td style="text-align:center">32</td>
</tr>
</tbody>
</table>

<div class=“panel panel-warning”>
  <div class=“panel-heading”>
    <h4>Warning:</h4>
  </div>
  <div class=“panel-body”>
    operation over <i> soft limts </i> may be really intensives.
  </div>
</div>

### Usage:

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

It provide the path to the Clever Cloud Warp 10 gateway and let you explore your data.

## Macro

Warp 10 provide a server side macro manager. It is a way to release some ready to use WarpScript. Hence, Clever Cloud provides some macros as helpers to avoid redondant and often need code.

<div class=“panel panel-warning”>
  <div class=“panel-heading”>
    <h4>Note:</h4>
  </div>
  <div class=“panel-body”>
  More information on the <a href="https://www.warp10.io/content/03_Documentation/07_Extending_Warp_10/01_Server_side_macros">Warp 10' macros documentations</a>.
  </div>
</div>

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

### AccessLogs

- `fetch_accessLogs_key_v0`

We provide the following macro to easily and quickly deep dive into access logs data. As we store access log as a Json value in a geotime series ([metrics documentation here]({{< ref "doc/metrics/overview.md#access-logs-metrics" >}})), this macro can be useful for straightforward access to a specific key. it allows you to fetch the `accessLogs` class and get only wanted value instead of the whole Json.

```bash
  '<READ TOKEN>' { 'app_id'  'id' } '<1stLevelKey>' NOW 1 h  @clevercloud/fetch_accessLogs_key_v0
```

```bash
  '<READ TOKEN>' { 'app_id'  'id' } '<1stLevelKey>.<2ndLevelKey>' NOW 10 m  @clevercloud/fetch_accessLogs_key_v0
```

> More example in the [metrics part of this documenation]({{< ref "doc/metrics/overview.md#access-logs-metrics" >}}).

**Nested keys** can be reached using a dot (`.`) to represent the depth.

```bash
'<READ TOKEN>' '<LABELS>' '<KEY>' '<START>' '<END>' @clevercloud/fetch_accessLogs_key_v0
```
