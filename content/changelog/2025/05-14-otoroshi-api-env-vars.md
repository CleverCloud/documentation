---
title: "Link Otoroshi API credentials to your applications"
date: 2025-04-25
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

- `CC_OTOROSHI_API_URL`: the URL of the Otoroshi API
- `CC_OTOROSHI_API_CLIENT_ID`: the API key to access the Otoroshi API
- `CC_OTOROSHI_API_CLIENT_SECRET`: the API secret to access the Otoroshi API

Thus, you'll be able to link the add-on to an application and get the API URL and credentials as environment variables.

- [Learn more about service dependencies](/developers/doc/administrate/service-dependencies/)
- [Learn more about Otoroshi on Clever Cloud](/developers/doc/addons/otoroshi/)
