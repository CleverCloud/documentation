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

Provisioning the Elastic Stack addon on Clever Cloud will give you an Elasticsearch instance, Kibana and an APM server.

## Versions

The current versions supported at add-on creation are 7 and 8.

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

A configuration example for RUM activation can be found here: [es-apm-serverconfig.sh](https://gist.githubusercontent.com/ldoguin/d7aa23fd44cfaed04165275aaf229a3c/raw/93aa1d39d8c1e444969ae114dbcfe0a5868f8d84/es-apm-serverconfig.sh).

### Kibana custom configuration

Kibana is deployed as an application. As such it's configured as an application. Its default pre run hook is set to:

`CC_PRE_RUN_HOOK="curl https://api.clever-cloud.com/v2/providers/es-addon/kibana-setup/7 | sh"`

You can change the URL to point to your own custom configuration.

### Java APM agent

You have multiple ways to use the APM agent. You can either add it in your dependencies and it should work out of the box or you can attach an agent to the JVM. If you prefer the last option, you have to define the following environment variable to attach the agent to the JVM: `CC_JAVA_APM_AGENT_ENABLE=true`.

The agent will list all JVMs on the system and attach to all of them, only once. If you know that your application will spawn multiple JVM processes (not threads) over time and you want the agent to also monitor those processes, you can add this environment variable: `CC_JAVA_APM_AGENT_CONTINUOUS=true`.

The agent will periodically scan for JVM processes and will attach to them if needed.

## Backups

Your Elastic add-on backups are managed by Clever Cloud. When you provision the add-on, we automatically create a Cellar add-on instance named Backups. You will find it in your organisation. Backups are taken daily and are stored in this Cellar add-on instance. As such *additional credits will be consumed by your backups*.

Backups can be managed under the *Backup* tab of the elastic add-on. You can restore, delete or open it directly under Kibana if you opted-in.

{{< callout type="warning" >}}
If you are using Elasticsearch 6, backups are not deleted automatically, you will need to clean them up from time to time.
{{< /callout >}}

