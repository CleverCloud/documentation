---
title: "Metabase 63 is available, with treemaps, two-factor authentication and PDF subscriptions"
description: Treemap charts, two-factor authentication, PDF attachments, more Metabot providers, one-step dashboard sharing and more
date: 2026-08-07
tags:
  - addons
  - metabase
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The `x.63` branch of Metabase is now available on Clever Cloud with version `0.63.5`. It introduces treemap charts for hierarchical data, two-factor authentication for users signing in with a password, and PDF attachments in dashboard subscriptions. Two-factor authentication is available with Pro and Enterprise plans.

Metabot can now use OpenAI, AWS Bedrock and Microsoft Azure models in addition to Anthropic, including on the open source edition with your own API key. This release also adds one-step invitations from dashboards and questions, CSV uploads to Snowflake, custom visualizations in the Modular Embedding SDK, and audit logs for MCP authorizations. The Sample Database now uses SQLite instead of H2, and Metabase introduces a predictable support policy with at least 60 days of support for every version and regular Long Term Support releases.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.63` or `1.63` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/manage/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.63
```

- [Learn more about Metabase 63](https://www.metabase.com/releases/metabase-63)
- [Watch the Metabase 63 video playlist](https://www.youtube.com/playlist?list=PLTC-ts2h37r4)
- [Learn more about Metabase on Clever Cloud](/doc/deploy/services/metabase/)

{{< youtube id="ZZ-KSyG7OVc" >}}
