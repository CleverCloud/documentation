---
title: "Montreal region (MTL): A records update for your domains/DNS"
date: 2024-02-23
tags:
  - sozu
  - applications
  - addons
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Florentin Dubois
    link: https://github.com/FlorentinDUBOIS
    image: https://github.com/FlorentinDUBOIS.png?size=40
description: But please, prefer CNAMEs
aliases:
- /changelog/2024-02-26-mtl-iplb-update
excludeSearch: true
---

As we're upgrading our infrastructure and load balancers in Montreal, we've added new failover IPs in this region.

If you configure your domains through CNAME records, this update will be transparent. But if you use A records, switch to CNAME or update your [DNS configuration](/developers/doc/administrate/domain-names/). Old IPs will continue to work for a while, but we recommend you to update your DNS as soon as possible to avoid any service interruption.

## Applications

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.mtl.clever-cloud.com.` |
| A<br>Only if CNAME is not available | @ 10800 IN A 158.69.109.229<br>@ 10800 IN A 149.56.117.183 |

## Add-ons

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain-sdc.mtl.clever-cloud.com.` |
| A<br>Only if CNAME is not available | @ 10800 IN A 54.39.154.128<br>@ 10800 IN A 167.114.35.164 |
