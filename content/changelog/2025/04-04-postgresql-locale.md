---
title: PostgreSQL locale support at database creation
date: 2025-04-04
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Choose the locale of your PostgreSQL database at creation
excludeSearch: true
---

You can now define the locale of your PostgreSQL database when creating a new add-on with [Clever Tools](/developers/doc/cli):

```bash
clever addon create postgresql-addon pgLocaleTest --plan xxs_sml --option locale=en_US
```

This will create a PostgreSQL database with the `en_US` locale instead of the default `en_GB` locale.

* [PostgreSQL versioning policy](https://www.postgresql.org/support/versioning/)
* [Learn more about PostgreSQL on Clever Cloud](/developers/doc/addons/postgresql/)
