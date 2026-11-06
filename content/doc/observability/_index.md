---
type: docs
weight: 100
linkTitle: Observability
title: Observability
description: Monitor applications and add-ons on Clever Cloud with logs, metrics, access logs, drains, and third-party observability integrations
keywords:
- observability
- metrics
- logs
- monitoring
- grafana
aliases:
- /doc/develop/observability
- /doc/administrate/monitoring
---

Every application emits three streams you can read without instrumenting anything: logs from your process, access logs from the load balancers in front of it, and metrics collected on the instance. Logs stay available for 7 days, so drains forward them to the tool your team already queries. Metrics are stored in Warp 10 and stay open to WarpScript.

{{< cards >}}
  {{< card link="/developers/doc/observability/blackfire" title="Blackfire" subtitle="Profile PHP applications" icon="fire" >}}
  {{< card link="/developers/doc/observability/drains" title="Logs Drains" subtitle="Forward your logs to an external tool" icon="external-link" >}}
  {{< card link="/developers/doc/observability/logs" title="Logs" subtitle="Read and filter the logs and access logs of your applications" icon="document-text" >}}
  {{< card link="/developers/doc/observability/metrics" title="Metrics" subtitle="Monitor performance and resource usage" icon="chart-bar" >}}
  {{< card link="/developers/doc/observability/new-relic" title="New Relic" subtitle="Send metrics to New Relic" icon="chart-pie" >}}
  {{< card link="/developers/doc/observability/warp10" title="Warp 10" subtitle="Query raw metrics with WarpScript" icon="beaker" >}}
{{< /cards >}}
