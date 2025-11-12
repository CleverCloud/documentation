---
title: Otoroshi 17.5 is available with new plugins and a WYSIWYG workflow designer
description: Fail2ban, Splunk exporter, body rewrite plugins and resumable workflows
date: 2025-09-10
tags:
  - addons
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v17.5](https://github.com/MAIF/otoroshi/releases/tag/v17.5.0) is available with multiple improvements and bug fixes. It brings resumable workflows, a WYSIWYG designer for workflows, plugins to rewrite HTTP request/response bodies based on regex, a fail2ban plugin and a Splunk data exporter.

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.5.1_1757489873` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.5.1_1757489873
```

- [Learn more about Otoroshi Workflows](https://maif.github.io/otoroshi/manual/topics/workflows.html)
- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)

