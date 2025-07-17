---
title: "Link Otoroshi API credentials to your applications"
date: 2025-05-14
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
description:
excludeSearch: true
---

Starting today, new Otoroshi add-ons deployed on Clever Cloud will expose API related environment variables as service dependencies:

- `CC_OTOROSHI_API_URL`: the base URL of the Otoroshi API
- `CC_OTOROSHI_API_CLIENT_ID`: the API key to query the Otoroshi API
- `CC_OTOROSHI_API_CLIENT_SECRET`: the API secret to query the Otoroshi API

Thus, you'll be able to link the add-on to an application and get the API URL and credentials as environment variables.

`ADMIN_API_CLIENT_ID` and `ADMIN_API_CLIENT_SECRET` environment variables of the Java application are replaced by `CC_OTOROSHI_API_CLIENT_ID` and `CC_OTOROSHI_API_CLIENT_SECRET` but are still supported during deployment for legacy reasons. The `CC_OTOROSHI_SSO_URL` is removed from service dependencies on new add-ons as it's not useful here.

- [Learn more about service dependencies](/developers/doc/administrate/service-dependencies/)
- [Learn more about Otoroshi on Clever Cloud](/developers/doc/addons/otoroshi/)
