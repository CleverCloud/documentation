---
type: docs
title: Metrics Overview
shortdesc: Gather metrics on your applications
weight: 1
tags:
  - metrics
keywords:
  - metrics
  - accesslogs
  - Warp10
  - prometheus
  - stasd
---

{{< callout type="warning" >}}
Clever Cloud Metrics is still in beta.
{{< /callout >}}

In addition to logs, you can have access to metrics to know how your application behaves.
By default, system metrics like CPU and RAM use are available, as well as application-level metrics when available (apache or nginx status for instance).

## Display metrics

For each application, there is a `Metrics` tab in the console.

### Overview pane

To get a quick overview of the current state of your scalers, the overview pane
displays the current CPU, RAM, Disk and Network activity. On supported platforms,
you can also have access to requests / second, and GC statistics.

{{< image "/images/grafana-from-oveview-pane.png" "Direct link from Overview pane to app dashboard in Grafana"  >}}

### Advanced pane

Advanced metrics allow you to access all gathered metrics,
on a specified time range.

### Custom queries

All metrics are stored in [Warp 10]({{< ref "doc/administrate/metrics/warp10.md" >}}), so you can explore data directly with the [quantum]({{< ref "doc/administrate/metrics/warp10.md" >}}) interface, with [WarpScript](https://www.warp10.io/doc/reference).

For instance, you can derive metrics over time, do custom aggregations or combine metrics.

### Get alerts

You can set up alerts in Grafana to be notified on your apps and add-ons consumption. This can be useful to monitor databases capacity or latency.

{{< image "/images/grafana-alerts.png" "Alert option from the general menu in Grafana"  >}}

For example, check [this tutorial on how to create Slack alerts with Grafana](https://www.clever-cloud.com/blog/features/2021/12/03/slack-alerts-for-grafana/).

## Access Logs metrics

All your applications access logs are pushed to [Warp 10]({{< ref "doc/administrate/metrics/warp10.md" >}}). You are now able to process them directly in the console in the Metrics tab of your applications.

### Request rate

We provide a request rate metric. It is an average of the access logs request count over 1 minute. It is updated every 30 second.

This can be reached using the Warp 10 class: `request_rate`.

> There are the same labels than for others metrics ([see monitoring-metrics](https://www.clever-cloud.com/doc/administrate/metrics/overview/#monitoring-metrics))

### Access Log data model

Access logs are defined in the `'accessLogs'` Warp 10 class and there are three Warp 10 labels available:

- `owner_id`: Organisation ID
- `app_id` : Application ID (ex: `app_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx` ) or Addon ID (ex: `postgresql_xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx`)
- `adc` or `sdc`
  - `adc` (Application Delivery Controller) are used for HTTP connections
  - `sdc` (Service Delivery Controller) are used for TCP connections

> Available addons for the field `addon_id` are mysql, redis, mongodb and postgresql addons.

{{< callout type="warning" >}}
- Add-ons on shared plans (usually DEV plans) do not provide access logs
- There are no recorded access logs in case of a direct access to an add-on
{{< /callout >}}

To reduce space used to store access logs, we defined the following key-value models.

#### Key-Value model for applications

AccessLogs data models for application. Using HTTP protocol.

```txt
t -> timestamp
a -> appId or addonId
o -> ownerId
i -> instanceId
ipS -> ipSource
pS -> portSource # 0 if undefined
s -> source
  lt -> latitude
  lg -> longitude
  ct -> city
  co -> country
ipD -> ipDestination
pD -> portDestination # 0 if undefined
d -> destination
  lt -> latitude
  lg -> longitude
  ct -> city
  co -> country
vb -> verb
path -> path
bIn -> bytesInt
bOut -> bytesOut
h -> hostname
rTime -> responseTime
sTime -> serviceTime
scheme -> scheme
sC -> statusCode
sT -> statusText
tS -> Haproxy termination_state
adc -> Reverse proxy hostname
w -> workerId (Sozu)
r -> requestId (Sozu)
tlsV -> tlsVersion (Sozu)
```

#### Key-Value model for addons

AccessLogs data models for addons. Using TCP protocol.

```txt
t -> timestamp
a -> appId or addonId
o -> ownerId
i -> instanceId
ipS -> ipSource
pS -> portSource # 0 if undefined
s -> source
  lt -> latitude
  lg -> longitude
  ct -> city
  co -> country
ipD -> ipDestination
pD -> portDestination # 0 if undefined
d -> destination
  lt -> latitude
  lg -> longitude
  ct -> city
  co -> country
tS -> Haproxy termination_state
sdc -> Reverse proxy hostname
sDuration -> total session duration time in millis
```

### Queries examples:

The main ways to use `accessLogs` data is to `FETCH` over it and get interesting values by a JSON processing.

{{< callout type="info" >}}
Look at *fetch_accessLogs_key_v0* macro to have a convenient way to explore access log data, see [Warp 10 documentation]({{< ref "doc/administrate/metrics/warp10.md" >}}).
{{< /callout >}}

<script src="https://gist.github.com/cnivolle/4a9b20254131c0256cd7e4246d3070a7.js"></script>

A convenient way to integrate the intercepted data in a workflow is to use [WarpScript](https://www.warp10.io/content/03_Documentation/04_WarpScript/). It is a good idea to use the GTS format to be able to apply all GTS transformation on the output.

In the following example, we get the `accessLogs` status codes and create a GTS as an output to be able to use FILTER or any other transformation on it a second time.

<script src="https://gist.github.com/cnivolle/2ee8607d995daa1316e17ffc3874d047.js"></script>

An example using the provided Clever Cloud macro to straightforward access to the access logs input byte :

```txt
'<READ TOKEN>' { 'app_id'  'id' } 'bIn' NOW 1 h  @clevercloud/fetch_accessLogs_key_v0
```

or to get the latitude of the destination, which is a nested data:

```txt
'<READ TOKEN>' { 'app_id'  'id' } 'd.lt' NOW 1 h  @clevercloud/fetch_accessLogs_key_v0
```

## Monitoring' metrics

All applications and VMs instances behind are monitored. Data is sent to [Warp 10]({{< ref "doc/administrate/metrics/warp10.md" >}}), a Geotimes series database.
All metrics can be processed directly in the console in the Metrics tab of your applications or by the Clever Cloud Warp 10 endpoint.

### Monitoring data model

All metrics data follow the same schema in warp 10.
Each class represents a specific metric. The context is provided by the Warp 10 labels.

#### Class values and Labels

##### Overview

A telegraf daemon supplies most metrics.

Each metric is recorded as a Warp 10 class.
Labels provide additional information about the VMs like instances id, organisation id, reverse proxy used.

##### Labels

In metrics' data, mains labels would be :

- `owner_id` : A unique ID by organisation
- `app_id` : A unique ID of application
- `host` : HV id hosting the VM instance
- `adc` : Reverse proxy ID for http connexion (ie: applications)
- `sdc` : Reverse proxy ID for tcp connexion (ie: addons)
- `vm_type` : `volatile` or `persistent`. Is it a stateless application or a stateful add-on
- `deployment_id` : ID of the deployment

{{< callout type="warning" >}}
For some specific metrics. Some labels could miss.
{{< /callout >}}

##### Classes

Telegraf provide lots of metrics described in their [documentation](https://github.com/influxdata/telegraf/tree/master/plugins/inputs).

Below, the list of all Warp 10 classes representing Telegraf metrics :

<table align="center" class="table table-bordered" >
  <tbody>
    <tr>
      <td align="center">conntrack.ip_conntrack_count</td>
      <td align="center">mem.swap_free</td>
    </tr>
    <tr>
      <td align="center">conntrack.ip_conntrack_max</td>
      <td align="center">mem.swap_total</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_guest</td>
      <td align="center">mem.total</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_guest_nice</td>
      <td align="center">mem.used</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_idle</td>
      <td align="center">mem.used_percent</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_iowait</td>
      <td align="center">mem.vmalloc_chunk</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_irq</td>
      <td align="center">mem.vmalloc_total</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_nice</td>
      <td align="center">mem.vmalloc_used</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_softirq</td>
      <td align="center">mem.wired</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_steal</td>
      <td align="center">mem.write_back</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_system</td>
      <td align="center">mem.write_back_tmp</td>
    </tr>
    <tr>
      <td align="center">cpu.usage_user</td>
      <td align="center">net.bytes_recv</td>
    </tr>
    <tr>
      <td align="center">disk.free</td>
      <td align="center">net.bytes_sent</td>
    </tr>
    <tr>
      <td align="center">disk.inodes_free</td>
      <td align="center">net.drop_in</td>
    </tr>
    <tr>
      <td align="center">disk.inodes_total</td>
      <td align="center">net.drop_out</td>
    </tr>
    <tr>
      <td align="center">disk.inodes_used</td>
      <td align="center">net.err_in</td>
    </tr>
    <tr>
      <td align="center">disk.total</td>
      <td align="center">net.err_out</td>
    </tr>
    <tr>
      <td align="center">disk.used</td>
      <td align="center">net.packets_recv</td>
    </tr>
    <tr>
      <td align="center">disk.used_percent</td>
      <td align="center">net.packets_sent</td>
    </tr>
    <tr>
      <td align="center">http_response.http_response_code</td>
      <td align="center">net_response.response_time</td>
    </tr>
    <tr>
      <td align="center">http_response.response_time</td>
      <td align="center">net_response.result_code</td>
    </tr>
    <tr>
      <td align="center">http_response.result_code</td>
      <td align="center">net_response.result_type</td>
    </tr>
    <tr>
      <td align="center">http_response.result_type</td>
      <td align="center">netstat.tcp_close</td>
    </tr>
    <tr>
      <td align="center">kernel.boot_time</td>
      <td align="center">netstat.tcp_close_wait</td>
    </tr>
    <tr>
      <td align="center">kernel.context_switches</td>
      <td align="center">netstat.tcp_closing</td>
    </tr>
    <tr>
      <td align="center">kernel.entropy_avail</td>
      <td align="center">netstat.tcp_established</td>
    </tr>
    <tr>
      <td align="center">kernel.interrupts</td>
      <td align="center">netstat.tcp_fin_wait1</td>
    </tr>
    <tr>
      <td align="center">kernel.processes_forked</td>
      <td align="center">netstat.tcp_fin_wait2</td>
    </tr>
    <tr>
      <td align="center">mem.active</td>
      <td align="center">netstat.tcp_last_ack</td>
    </tr>
    <tr>
      <td align="center">mem.available</td>
      <td align="center">netstat.tcp_listen</td>
    </tr>
    <tr>
      <td align="center">mem.available_percent</td>
      <td align="center">netstat.tcp_none</td>
    </tr>
    <tr>
      <td align="center">mem.buffered</td>
      <td align="center">netstat.tcp_syn_recv</td>
    </tr>
    <tr>
      <td align="center">mem.cached</td>
      <td align="center">netstat.tcp_syn_sent</td>
    </tr>
    <tr>
      <td align="center">mem.commit_limit</td>
      <td align="center">netstat.tcp_time_wait</td>
    </tr>
    <tr>
      <td align="center">mem.committed_as</td>
      <td align="center">netstat.udp_socket</td>
    </tr>
    <tr>
      <td align="center">mem.dirty</td>
      <td align="center">processes.blocked</td>
    </tr>
    <tr>
      <td align="center">mem.free</td>
      <td align="center">processes.dead</td>
    </tr>
    <tr>
      <td align="center">mem.high_free</td>
      <td align="center">processes.idle</td>
    </tr>
    <tr>
      <td align="center">mem.high_total</td>
      <td align="center">processes.paging</td>
    </tr>
    <tr>
      <td align="center">mem.huge_page_size</td>
      <td align="center">processes.running</td>
    </tr>
    <tr>
      <td align="center">mem.huge_pages_free</td>
      <td align="center">processes.sleeping</td>
    </tr>
    <tr>
      <td align="center">mem.huge_pages_total</td>
      <td align="center">processes.stopped</td>
    </tr>
    <tr>
      <td align="center">mem.inactive</td>
      <td align="center">processes.total</td>
    </tr>
    <tr>
      <td align="center">mem.low_free</td>
      <td align="center">processes.total_threads</td>
    </tr>
    <tr>
      <td align="center">mem.low_total</td>
      <td align="center">processes.unknown</td>
    </tr>
    <tr>
      <td align="center">mem.mapped</td>
      <td align="center">processes.zombies</td>
    </tr>
    <tr>
      <td align="center">mem.page_tables</td>
      <td align="center">procstat_lookup.pid_count</td>
    </tr>
    <tr>
      <td align="center">mem.shared</td>
      <td align="center">system.load1</td>
    </tr>
    <tr>
      <td align="center">mem.slab</td>
      <td align="center">system.load1_per_cpu</td>
    </tr>
    <tr>
      <td align="center">mem.swap_cached</td>
      <td align=”center”>jvm.statsd-jvm-profiler_heap_ps-old-gen_max.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_pending-finalization-count.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_total_committed.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_loaded-class-count.value</td>
      <td align=”center”>jvm.metrics_jvm_heapMemoryUsage_used.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_gc_PS_Scavenge_count.value</td>
      <td align=”center”>jvm.metrics_jvm_nonHeapMemoryUsage_used.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_metaspace_init.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_total_used.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-survivor-space_used.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_heap_ps-eden-space_init.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_gc_PS_MarkSweep_time.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_total_max.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-eden-space_max.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_compressed-class-space_max.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_total_init.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_code-cache_used.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_metaspace_used.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_compressed-class-space_init.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_metaspace_max.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_gc_PS_MarkSweep_count.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-eden-space_used.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_total-loaded-class-count.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_total_init.value</td>
      <td align=”center”>jvm.metrics_jvm_thread.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_total_used.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_heap_total_committed.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_compressed-class-space_committed.value</td>
      <td align=”center”>jvm.metrics_jvm_nonHeapMemoryUsage_committed.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_unloaded-class-count.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_code-cache_init.value</td>
    </tr>
    <tr>
      <td align="center">jvm.metrics_jvm_loadedClasses.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_code-cache_max.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_compressed-class-space_used.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_heap_ps-survivor-space_max.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_nonheap_code-cache_committed.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_heap_ps-old-gen_committed.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-survivor-space_committed.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_gc_PS_Scavenge_time.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-old-gen_used.value</td>
      <td align=”center”>jvm.metrics_jvm_heapMemoryUsage_committed.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_gc_PS_MarkSweep_runtime.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_nonheap_metaspace_committed.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-eden-space_committed.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_heap_ps-old-gen_init.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_total_max.value</td>
      <td align=”center”>jvm.statsd-jvm-profiler_gc_PS_Scavenge_runtime.value</td>
    </tr>
    <tr>
      <td align="center">jvm.statsd-jvm-profiler_heap_ps-survivor-space_init.value</td>
    </tr>
  </tbody>
</table>

### Examples and usages

From the `metrics` tab on the console. You can either open a Quantum console, an online WarpScript editor, or either send your WarpScript by your own way on the Warp 10 endpoint (provided by Quantum).

More information about [Quantum and Warp 10]({{< ref "doc/administrate/metrics/warp10.md" >}}) in our documentation.

For example, you could fetch the memory usage of an application for the last hour. Smoothed by a data average by
minute.

{{< callout type="warning" >}}
Computation can be time intensive.
{{< /callout >}}

```txt
// Fix the NOW timestamp to have the same on over the script
NOW 'NOW' STORE
// fetch data over 1 hour
[ <READ TOKEN> 'mem.available' { 'app_id' '<APPLICATION ID>' } $NOW 1 h ] FETCH
// Average the data by bucket of 1 min from the last point timestamped at NOW
[ SWAP bucketizer.mean $NOW 1 m 0 ] BUCKETIZE
// From the instance granularity to application granularity. Timestamps to timestamps merge
[ SWAP [ 'app_id' ] reducer.mean ] REDUCE
```

## Consumption metric

Consumption can also be inferred by our metrics. We provide some helper macros in the [Warp 10 documentation]({{< ref "doc/administrate/metrics/warp10.md" >}}).

Consumption unit is in **second**.

The following script provides the whole consumption from between start and end timestamps for all applications
under an organisation.

```txt
'<READ TOKEN>' '<ORGANISATION ID>' <START TIMESTAMP> <END TIMESTAMP> @clevercloud/app_consumption
```

## Publish your own metrics

We currently support two ways to push / collect your metrics: the `statsd` protocol and `prometheus`.

The statsd server listens on port `8125`. You can send metrics using regular statsd protocol or using an advanced one [as described here](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/statsd#influx-statsd).

We also support Prometheus metrics collection, by default our agent collects exposed metrics on `localhost:9100/metrics`.

If needed, you can override those settings with the two following environment variables:

- `CC_METRICS_PROMETHEUS_PORT`: Define the port on which the Prometheus endpoint is available
- `CC_METRICS_PROMETHEUS_PATH`: Define the path on which the Prometheus endpoint is available

As with Prometheus the exposed host can be the same as the application deployed, you can use a basic authentication to collect the metrics with the two following environment variables:

- `CC_METRICS_PROMETHEUS_USER`: Define the user for the basic auth of the Prometheus endpoint
- `CC_METRICS_PROMETHEUS_PASSWORD`: Define the password for the basic auth of the Prometheus endpoint

For large custom set of metrics to collect, the default response timeout of the `/metrics` query is 3 seconds. You can update it with the following environment variable:

- `CC_METRICS_PROMETHEUS_RESPONSE_TIMEOUT`: Define the timeout in seconds to collect the application metrics. This value **must** be below 60 seconds as data are collected every minutes. 

To access your metrics from Warp10 you need to use the prefix `prometheus.` or `statsd.` based on what you used to publish your metrics.

You can use this query to show all collected metrics:

```txt
[ 
  'TOKEN'
  '~prometheus.*'
  { 'app_id' 'app_xxxxxxxx' }
  NOW 5 m
]
FETCH
```

### Node.js example

You can use `node-statsd` to publish metrics:

```javascript
// npm install node-statsd

const StatsD = require("node-statsd"),
  client = new StatsD();

// Increment: Increments a stat by a value (default is 1)
client.increment("my_counter");

// Gauge: Gauge a stat by a specified amount
client.gauge("my_gauge", 123.45);
```

### Haskell example

<!-- Maybe this should be put in haskell documentation? -->

In Haskell, metrics are usually gathered with [EKG](https://hackage.haskell.org/package/ekg).
The package `ekg-statsd` allows to push EKG metrics over `statsd`.

If you're using [warp](https://hackage.haskell.org/package/warp), you can use
`wai-middleware-metrics` to report request distributions (request count,
responses count aggregated by status code,
responses latency distribution).

EKG allows you to have access to GC metrics, make sure you compile your application
with `"-with-rtsopts=-T -N"` to enable profiling.

```haskell
{-# LANGUAGE OverloadedStrings #-}

-- you need the following packages
-- ekg-core
-- ekg-statsd
-- scotty
-- wai-middleware-metrics

import           Control.Monad                   (when)
import           Network.Wai.Metrics             (WaiMetrics, metrics,
                                                  registerWaiMetrics)
import           System.Metrics                  (newStore, registerGcMetrics)
import           System.Remote.Monitoring.Statsd (defaultStatsdOptions,
                                                  forkStatsd)
import           Web.Scotty

handleMetrics :: IO WaiMetrics
handleMetrics = do
  store <- newStore
  registerGcMetrics store
  waiMetrics <- registerWaiMetrics store
  sendMetrics <- maybe False (== "true") <$> lookupEnv "ENABLE_METRICS"
  when sendMetrics $ do
    putStrLn "statsd reporting enabled"
    forkStatsd defaultStatsdOptions store
    return ()
  return waiMetrics

main = do
  waiMetrics <- handleMetrics
  scotty 8080 $ do
     middleware $ metrics waiMetrics
     get "/" $
       html $ "Hello world"
```
