---
type: docs
title: Kibana
#position: 7
shortdesc: How  to deploy a custom Kibana for specific using cases.
tags:
- addons
keywords:
- custom
- elsaticsearch
- elastic
- kibana
aliases:
- /doc/deploy/addon/elastic/kibana
type: docs

---

{{< callout type="warning" >}}
To deploy a custom Kibana, you need to ask Clever Cloud Support team to enable superuser permissions for your user.
{{< /callout >}}

## Overview

[Kibana](https://www.elastic.co/fr/kibana/) is the web interface available on the Clever Cloud's platform to manage your Elastic Stack.

By default, you can enable Kibana when you create an Elastic Stack add-on.

## Enable Kibana with your Elastic Stack add-on

Kibana can be enabled at the add-on creation. Choose "Create an add-on" > "Elastic Stack". Select your plan, applications which will use the Elastic Stack and name the add-on. On the "options" step, enable Kibana. Then, confirm the options and your add-on will start with a Kibana instance.

### Customize the Kibana configuration file

The configuration is set with this deployment hook :
`CC_PRE_RUN_HOOK` = `curl https://api.clever-cloud.com/v2/providers/es-addon/kibana-setup/<your elastic version> | sh`

To modify this default configuration ([Configuration file for Kibana 8.3.3](https://api.clever-cloud.com/v2/providers/es-addon/kibana-setup/8.3.3)), you need to host your own config file (we strongly recommend [Cellar](/developers/doc/deploy/addon/cellar)).

Check other available configuration file on [Github](https://github.com/CleverCloud/custom-kibana-config)

### Disable SSO authentication

To disable SSO authentication and use elastic users instead, you need to modify Kibana's configuration file and `CC_PRE_RUN_HOOK` in environment variables.

For example for Kibana 8.3.3:
`CC_PRE_RUN_HOOK` = `curl https://raw.githubusercontent.com/CleverCloud/custom-kibana-config/master/8.3.3/no-sso-8.3.3 | sh`

Remember, you need to ask Clever Cloud Support team to grant superuser permissions to your user. After that, you will be able to add additional users via Kibana.

### Add custom domain name

You need to disable SSO authentication first. Then, you will be able to add a custom domain name in "Domain name" tab of your Kibana app.

## Deploy Kibana on localhost

The Kibana version should match with the ElasticSearch version.

Follow these steps :

1. Download/unzip Kibana in version which match with your Elastic Stack version
2. Edit kibana.yml :
   * line 43 : `elasticsearch.host: <elastic-addon-host>:443`
   * line 49 : `elasticsearch.username: kibana`
   * line 50 : `elasticsearch.password: <password>`
   * Launch Kibana (`<path_to_kibana>/bin/kibana`)
3. Go to Kibana through the dedicated local address: `http://localhost:5601`
4. Connect to ElasticSearch with your Elastic username and password
