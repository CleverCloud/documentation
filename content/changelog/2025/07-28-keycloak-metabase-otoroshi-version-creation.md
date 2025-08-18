---
title: Set Keycloak, Metabase and Otoroshi version at creation
description: More flexibility, and soon a great dashboard
date: 2025-07-28
tags:
  - operators
  - version
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

You can now set the version of Keycloak, Metabase and Otoroshi at creation time, from a list of supported and tested releases. It works from the [Clever Cloud Console](https://console.clever-cloud.com/), [API](/api) and [Clever Tools](/doc/cli). For example:

```bash
clever addon create keycloak --addon-version 26.2.5 myKeycloak
```

If you don't provide a valid version, supported values are printed in the error message.
