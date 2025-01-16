---
title: IP list update on Paris zone
date: 2024-06-28
tags:
  - domain
  - IP
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Florentin Dubois
    link: https://github.com/FlorentinDUBOIS
    image: https://github.com/FlorentinDUBOIS.png?size=40
description: A big step forward for our open source reverse proxy
aliases:
- /changelog/2024-06-28-new-ip-list-paris
excludeSearch: true
---

As our network evolves, we've updated [IP list for Paris (PAR) zone](/developers/doc/administrate/domain-names/#your-application-runs-in-the-europeparis-par-zone). If you use A records for DNS configuration, update them. 4 new IP addresses should be added (`91.208.207.220` to `91.208.207.223`). **We strongly recommend using CNAME records instead.**

| Record Type | Value |
| ----------- | ----- |
| CNAME<br>Recommended | `{yoursubdomain} 10800 IN CNAME domain.par.clever-cloud.com.` |
| A<br>Only if CNAME is not available | `@ 10800 IN A 91.208.207.214`<br>`@ 10800 IN A 91.208.207.215`<br>`@ 10800 IN A 91.208.207.216`<br>`@ 10800 IN A 91.208.207.217`<br>`@ 10800 IN A 91.208.207.218`<br>`@ 10800 IN A 91.208.207.220`<br>`@ 10800 IN A 91.208.207.221`<br>`@ 10800 IN A 91.208.207.222`<br>`@ 10800 IN A 91.208.207.223`  |

We are going to remove 4 IPs that **you must stop to use between now and August 23rd**:

- 46.252.181.103
- 46.252.181.104
- 185.42.117.108
- 185.42.117.109

 After this date, they won't answer to requests anymore. You'll find the updated values in the `Domain names` section of your application in [the Console](https://console.clever-cloud.com). If you have any question about this change, feel free to ask [our customer support](https://console.clever-cloud.com/ticket-center-choice) about it.
