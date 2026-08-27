---
type: docs
linkTitle: Kibana
title: Use Kibana with an Elastic Stack add-on
description: Enable and access a managed Kibana interface for an Elastic Stack add-on on Clever Cloud
keywords:
- kibana
- elasticsearch
- elastic stack
- analytics
- data visualization
aliases:
- /doc/deploy/addon/elastic/kibana
- /kibana
---

[Kibana](https://www.elastic.co/kibana) is the web interface for exploring, visualizing and managing data stored in Elasticsearch. Clever Cloud can provision a managed Kibana service with an [Elastic Stack add-on](/doc/addons/elastic/).

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com/)
- An organisation in which you can create add-ons

Install [Clever Tools](/doc/cli/install/) if you want to create the add-on from the command line.

## Enable Kibana

Kibana is an option selected when you create the Elastic Stack add-on. You cannot enable it later on an existing add-on.

### From the Console

1. In the [Clever Cloud Console](https://console.clever-cloud.com/), select **Create**, then **an add-on**
2. Select **Elastic Stack**
3. Choose the plan, version and region required by your project
4. Enable the **Kibana** option
5. Name and create the add-on

### With Clever Tools

Create an Elastic Stack add-on and enable Kibana with the `kibana=true` option:

```bash
clever addon create es-addon myElasticStack \
  -p xs \
  --addon-version 8 \
  --option kibana=true
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` to the command. Use `clever addon providers show es-addon` to list the plans, regions and major versions currently available.

Provisioning Elasticsearch and Kibana takes a few minutes. Open the Elastic Stack add-on in the Console once it is ready, then use its Kibana access link.

## Sign in to Kibana

Kibana uses Clever Cloud SSO by default. Any member of the organisation that owns the Elastic Stack add-on can sign in with their Clever Cloud account.

The managed configuration connects Kibana to the matching Elasticsearch version and keeps both services compatible. Clever Cloud updates the service within the selected major version.

## Customize Kibana

The Elastic Stack add-on is a managed service, so its native Kibana configuration is not exposed as an application environment variable or editable file. Most day-to-day settings, dashboards, spaces, roles and users can be managed from Kibana or through the Elasticsearch API.

If you need a custom authentication provider, domain name or native `kibana.yml` setting, [contact Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) to discuss your requirements. Configuration scripts for older Kibana releases should not be reused with a different version.

## Learn more

{{< cards >}}
  {{< card link="/doc/addons/elastic/" title="Elastic Stack" subtitle="Configure and manage the Elastic Stack add-on" icon="elastic" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://www.elastic.co/guide/en/kibana/current/index.html" title="Kibana documentation" subtitle="Explore Kibana features and settings" icon="external-link" >}}
  {{< card link="/doc/cli/addons/" title="Clever Tools add-ons" subtitle="Create and manage add-ons from the command line" icon="terminal" >}}
{{< /cards >}}
