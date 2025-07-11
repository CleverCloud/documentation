---
type: docs
title: Elastic Stack

shortdesc: The Elastic Stack is Elasticsearch, Kibana, Beats, and Logstash (also known as the ELK Stack).
tags:
- addons
keywords:
- fulltext
- elsaticsearch
- elastic
- kibana
- apm
type: docs
aliases:
- /doc/deploy/addon/elastic/elastic
- /doc/deploy/addon/elastic/
comments: false
---

The Elastic Stack is Elasticsearch, Kibana, Beats, and Logstash (also known as the ELK Stack). Reliably and securely take data from any source, in any format, then search, analyze, and visualize it in real time. Find out more about it on [Elastic's website](https://www.elastic.co/products/elastic-stack).

Provisioning the Elastic Stack add-on on Clever Cloud will give you an Elasticsearch instance, Kibana and an APM server.

## Versions

The current versions supported at add-on creation are the following:
{{< software_versions_shared_dedicated elasticsearch>}}

## Elasticsearch

Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data so you can discover the expected and uncover the unexpected.

## Kibana

Kibana lets you visualize your Elasticsearch data and navigate the Elastic Stack so you can do anything from tracking query load to understanding the way requests flow through your apps.

It is available as an opt-in option of the Elastic add-on. It will be deployed and billed as a regular application. You can upscale/downscale/delete it at any time. This application will be updated by Clever Cloud on a regular basis.

The created application name follow the pattern *Kibana - addon_eb464a6d-ce5f-4780-b595-6772ebe33d06*. The provisioning of this application might take up a minute to show up in your organisation.

Learn more on [Kibana official documentation](https://www.elastic.co/guide/en/kibana/current/index.html).

### Authentication

Any member of the Clever Cloud organisation containing the Elastic add-on will be able to login to Kibana through an automatically configured SSO system.

## Elastic APM

Elastic APM is an Application performance management tool chain based on the Elastic Stack. See exactly where your application is spending time so you can quickly fix issues and feel good about the code you push. To use it you must install an *APM agent* to your application. In some cases, you'll need to add a configuration file, or add it as a dependency in you application. You can find configuration files examples in [our public repository](https://github.com/CleverCloud/Elastic-APM-example-configuration-files).

Once both your application and APM server are running, you application with automatically send APM datas to the APM server which will send them to Elastic and once indexed they will be available in your Kibana dashboard (this process is really fast, you won't see it as a human).

Currently, APM agents are available in the following languages:

- [Go](https://www.elastic.co/guide/en/apm/agent/go/1.x/introduction.html)
- [Java](https://www.elastic.co/guide/en/apm/agent/java/1.x/intro.html)
- [Node.js](https://www.elastic.co/guide/en/apm/agent/nodejs/2.x/intro.html)
- [PHP](https://www.elastic.co/guide/en/apm/agent/php/current/index.html)
- [Python](https://www.elastic.co/guide/en/apm/agent/python/5.x/getting-started.html)
- [Ruby](https://www.elastic.co/guide/en/apm/agent/ruby/3.x/introduction.html)

It is available as an opt-in option of the Elastic add-on. It will be deployed and billed as a regular application. You can upscale/downscale/delete it at any time. This application will be updated by Clever Cloud on a regular basis.

The created application name follow the pattern *APM - addon_eb464a6d-ce5f-4780-b595-6772ebe33d06*. The provisioning of this application might take up a minute to show up in your organisation.

Learn more on [APM official documentation](https://www.elastic.co/guide/en/apm/get-started/current/components.html).

### How to setup APM

Any applications linked to the APM application will have the right credentials and APM endpoint automatically available as environment variables. In some cases these variables will be picked up automatically by the APM agent you are using in your application and everything will work automatically. But in some other cases you have to configure it yourself. See for instance the [Rails documentation](https://www.elastic.co/guide/en/apm/agent/ruby/3.x/getting-started-rails.html#getting-started-rails). The list of agents configuration can be found on Elastic's [documentation](https://www.elastic.co/guide/en/apm/agent/index.html).

### APM Server custom configuration

The APM server is deployed as an application. As such it's configured as an application. Its default pre run hook is set to:

`CC_PRE_RUN_HOOK="curl https://api.clever-cloud.com/v2/providers/es-addon/apm-server-setup/7 | sh"`

You can change the URL to point to your own custom configuration.

Here is a configuration example for RUM activation:

```bash{filename="es-apm-serverconfig.sh"}
#!/bin/bash -l

cat <<EOF >apm-server.yml
apm-server:
    host: "0.0.0.0:8080"
    secret_token: "${ES_ADDON_APM_AUTH_TOKEN}"

output.elasticsearch:
    hosts: ["${ES_ADDON_HOST}:443"]
    protocol: "https"
    username: "${ES_ADDON_APM_USER}"
    password: "${ES_ADDON_APM_PASSWORD}"

path.home: "${APP_HOME}"

logging:
    to_syslog: true
    to_files: false

apm-server.rum.enabled: true
apm-server.rum.event_rate.limit: 300
apm-server.rum.event_rate.lru_size: 1000
apm-server.rum.allow_origins: ['*']
apm-server.rum.library_pattern: "node_modules|bower_components|~"
apm-server.rum.exclude_from_grouping: "^/webpack"
apm-server.rum.source_mapping.enabled: true
apm-server.rum.source_mapping.cache.expiration: 5m
apm-server.rum.source_mapping.index_pattern: "apm-*-sourcemap*"
```

### Kibana custom configuration

Kibana is deployed as an application. As such it's configured as an application. Its default pre run hook is set to:

`CC_PRE_RUN_HOOK="curl https://api.clever-cloud.com/v2/providers/es-addon/kibana-setup/7 | sh"`

You can change the URL to point to your own custom configuration.

### Java APM agent

You have multiple ways to use the APM agent. You can either add it in your dependencies and it should work out of the box or you can attach an agent to the JVM. If you prefer the last option, you have to define the following environment variable to attach the agent to the JVM: `CC_JAVA_APM_AGENT_ENABLE=true`.

The agent will list all JVMs on the system and attach to all of them, only once. If you know that your application will spawn multiple JVM processes (not threads) over time and you want the agent to also monitor those processes, you can add this environment variable: `CC_JAVA_APM_AGENT_CONTINUOUS=true`.

The agent will periodically scan for JVM processes and will attach to them if needed.

## Plugins

Elasticsearch managed by Clever Cloud comes with these plugins, you can activate at add-on creation:

| Plugin | Description |
| ------ | ----------- |
| analysis-icu | Adds extended Unicode support using the ICU libraries |
| analysis-kuromoji | Advanced analysis of Japanese using the Kuromoji analyzer |
| analysis-nori | Morphological analysis of Korean using the Lucene Nori analyzer |
| analysis-phonetic | Analyzes tokens into their phonetic equivalent using Soundex, Metaphone, Caverphone, and other codecs |
| analysis-smartcn | An analyzer for Chinese or mixed Chinese-English text |
| analysis-stempel | Provides high quality stemming for Polish |
| analysis-ukrainian | Provides stemming for Ukrainian |
| discovery-ec2 | Uses the AWS API to identify the addresses of seed hosts |
| discovery-azure-classic | Uses the Azure Classic API to identify the addresses of seed hosts |
| discovery-gce | Uses the GCE API to identify the addresses of seed hosts |
| mapper-size | Provides the `_size` metadata field which, when enabled, indexes the size in bytes of the original `_source` field |
| mapper-murmur3 | Allows hashes to be computed at index-time and stored in the index for later use with the cardinality aggregation |
| mapper-annotated-text | Provides the ability to index text that is a combination of free-text and special markup |

{{< callout type="info" >}}
Plugin activation is only available at add-on creation, through [API](/developers/api) or the `--option` flag of [Clever Tools](/developers/doc/cli/addons/#create--rename--delete). You must pass the option as a comma-separated list: `plugins=plugin1,plugin2`. To modify enabled plugins on an existing add-on, contact [support team](https://console.clever-cloud.com/ticket-center-choice).
{{< /callout >}}

## Backups

Your Elastic add-on backups are managed by Clever Cloud. When you provision the add-on, we automatically create a Cellar add-on instance named Backups. You will find it in your organisation. Backups are taken daily and are stored in this Cellar add-on instance. As such *additional credits will be consumed by your backups*.

Backups can be managed under the *Backup* tab of the elastic add-on. You can restore, delete or open it directly under Kibana if you opted-in.

{{< callout type="warning" >}}
If you are using Elasticsearch 6, backups are not deleted automatically, you will need to clean them up from time to time.
{{< /callout >}}

## Create an index on Elasticsearch

When creating an Elasticsearch add-on, a single node is setup. By default we apply `cc_singlenode_template` that forces the amount of data replication to zero. This index template is only available for data streams.

If you are using a tool that requires native Elasticsearch indexes or are accessing them through the Elasticsearch API, you will need an index template. They can be created either using Kibana or the Elasticsearch API. For the latter, you can use a cURL request such as:

```sh
curl 'https://${ELASTIC_SEARCH_HOST}/_index_template/test/' -u ${ELASTIC_SEARCH_USER} -H 'Content-Type: application/json' -X PUT -d'
{
  "index_patterns" : ["${ELASTIC_INDEX_PATTERN}*"],
  "priority": 2,
  "template": {
    "settings" : {
        "number_of_shards" : 1,
        "number_of_replicas": 0
    }
  }
}
'
```

It's important here to set `number_of_replicas` to zero to avoid triggering cluster problems. The priority must be greater than 1, as the `cc_singlenode_template` template has a default priority of 1.

## 🔑 Rights and permissions

Elastic Stack add-ons are **managed services**, with Clever Cloud in charge of configuring and maintaining native configuration files. Some operations like adding an oauth source to connect to Kibana can't be added, as well as some native settings modifications. This ensures optimal performances and security for managed services as configured by Clever Cloud.

Most settings are available for modifications and update from Kibana or by API, for example:

- Managing users permissions
- Frequencies of back-ups
- The lifecycle of backups indexes
- Backups destination

If you think your system might require some customization (like some plugins activation), contact Clever Cloud support to explain your use case and we will work with you to find a solution.
