---
title: 'JS Client 11.2 is available with better application creation'
description: Prepare to build Clever Cloud applications from public Git repositories
date: 2025-09-16
tags:
  - client
  - javascript
authors:
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 11.2](https://github.com/CleverCloud/clever-client.js/blob/master/CHANGELOG.md#1120-2025-09-16) is available. It fixes a bug with application rebuild (reboot without cache) in the "next" implementation. It's also easier to create an application with `CreateApplicationCommandInput` as there are fewer required parameters. And it supports `publicGitRepositoryUrl` to deploy an application based on a public Git repository.
