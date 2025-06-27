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
aliases:
- /changelog/2024-11-27-elastic-plugins-support
excludeSearch: true
---

When you create an Elasticsearch add-on, you can now activate plugins through [API](/developers/api) or the `--option` flag of [Clever Tools](/developers/doc/cli/addons/). You must pass the option as a comma-separated list: `plugins=plugin1,plugin2`.

- Learn more about [Elasticsearch plugins support on Clever Cloud](/developers/doc/addons/elastic/#plugins)
