---
title: Load custom plugins in your Otoroshi instances
description: Want new features? You can make your own plugins and share them with the world!
date: 2025-11-13
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

Otoroshi on Clever Cloud comes with many included plugins to manage AI based APIs, Model Context Protocol (MCP), API Portal, Biscuit authentication, Dynamic JS or Mailer, etc.  Now you can also load any other custom plugin by setting the `CC_OTOROSHI_PLUGINS_URLS` environment variable of the underlying Java application:
- Add URLs pointing to the plugins JAR files, separated by a space or a new line
- Rebuild the application

This works for any Otoroshi version deployed on Clever Cloud. If you want to learn more about Otoroshi plugins and how to create your own, check the [Otoroshi documentation](https://maif.github.io/otoroshi/manual/plugins/create-plugins.html).
- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
