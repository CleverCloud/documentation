---
title: Logs management
position: 3
shortdesc: How to manage addons and applications log drains
tags:
 - administrate
keywords:
- logs
- log
- logging
- log drains
- drain
- drains
---

Log management is currently only available through our API and [clever-tools]({{< ref "/getting-started/cli.html" >}}).

## Get continuous logs from your application

You can see logs with the command down below.

    clever logs

You can also add a flag `--before` or `--after` followed by a date (ISO8601 format).

    # Here is an example
    clever logs --before 2016-08-11T14:54:33.971Z

### Logs drains: exporting logs to an external tools

You can use the logs drains to send your application's logs to an external server with the following command.


    clever drain create [--alias <alias>] <DRAIN-TYPE> <DRAIN-URL> [--username <username>] [--password <password>]

Where `DRAIN-TYPE` is one of:

 - `TCPSyslog`: for TCP syslog endpoint;
 - `UDPSyslog`: for UDP syslog endpoint;
 - `HTTP`: for TCP syslog endpoint (note that this endpoint has optional username/password parameters as HTTP Basic Authentication);
 - `ElasticSearch`: for ElasticSearch endpoint (note that this endpoint requires username/password parameters as HTTP Basic Authentication);
 - `DatadogHTTP`: for Datadog endpoint (note that this endpoint needs your Datadog API Key).

You can list the currently activated drains with this command.

    clever drain [--alias <alias>]

And remove them if needed

    clever drain remove [--alias <alias>] <DRAIN-ID>

#### ElasticSearch logs drains

ElasticSearch drains use the Elastic bulk API. To match this endpoint, specify `/_bulk` at the end of your ElasticSearch endpoint.

Each day, we will create an index `logstash-<yyyy-MM-dd>` and push logs to it.

#### Datadog logs drains

Datadog has two zones, EU and COM. An account on one zone is not available on the other, make sure to target the good EU or COM intake endpoint.

To create a [Datadog](https://docs.datadoghq.com/api/?lang=python#send-logs-over-http) drain, you just need to use:

    clever drain create DatadogHTTP "https://http-intake.logs.datadoghq.com/v1/input/<API_KEY>?ddsource=clevercloud&service=<SERVICE>&host=<HOST>"
