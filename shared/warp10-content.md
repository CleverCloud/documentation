### Time and duration in Warp 10

The platform's time unit is in **microsecond**.

* [Learn more about date functions](https://www.warp10.io/tags/date)
* [Learn more about time functions](https://www.warp10.io/tags/time)

#### Duration is set by the followings symbols

- `d`: day
- `h`: Hour
- `ms`: millisecond
- `ns`: nanosecond
- `ps`: picosecond
- `s`: second
- `us`: microsecond
- `w`: week

#### Date

Allowed format:

- ISO8601
- Timestamp in microsecond

Builtin function:

- `NOW`: get the current timestamp
- `ISO8601`: Convert a string or a timestamp to a ISO8601 date format

## Technical constraints

The followings limits are defined in Warp 10. The **soft** limit can be passed over by an [`AUTHENTICATE`](https://www.warp10.io/doc/AUTHENTICATE) operation. Operations over **soft limits** may be intensive. The **hard** limit is unsurpassable.

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

## Classes Reference

In Warp 10, classes organize metrics from various sources, like applications or add-ons, into specific categories (CPU usage, memory statistics, etc.). This structure makes the data easy to retrieve and analyze with WarpScript.

For a complete list of Telegraf classes and their descriptions, see [the classes list](/doc/metrics/#classes).

## Macro

Warp 10 provide a server side macro manager. It is a way to release some ready to use WarpScript. Hence, Clever Cloud provides some macros as helpers to avoid redundant and often need code.

* [Warp 10' macros documentations](https://www.warp10.io/content/03_Documentation/07_Extending_Warp_10/01_Server_side_macros)

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
