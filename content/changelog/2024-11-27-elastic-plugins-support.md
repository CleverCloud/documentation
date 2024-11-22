---
title: "Elasticsearch: plugins activation support"
date: 2024-11-22
tags:
  - addons
  - elastic
authors:
  - name: Aurélien Hebert
    link: https://github.com/aurrelhebert
    image: https://github.com/aurrelhebert.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: More flexibility for Elasticsearch add-ons
excludeSearch: true
---

When you create an Elasticsearch add-on, you can now activate plugins through [API](/api) or the `--option` flag of [Clever Tools](https://github.com/CleverCloud/clever-tools/blob/master/docs/addons-backups.md#create--rename--delete). You must pass the option as a comma-separated list: `plugins=plugin1,plugin2`.

- Learn more about [Elasticsearch plugins support on Clever Cloud](/doc/addons/elastic/#plugins)
