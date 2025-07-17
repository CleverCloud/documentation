---
title: "Simpler Node.js version management"
date: 2025-05-16
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: One rule to rule them all
excludeSearch: true
---

Until now, to set Node.js version on Clever Cloud, you had to use the `engines.node` field in `package.json` for Node.js applications, or the `CC_NODE_VERSION` environment variable for all other runtimes. Now, you can use `CC_NODE_VERSION` for Node.js applications too. It won't change anything for existing applications, but we recommend you to switch for such behavior.

- [Learn more about Node.js on Clever Cloud](/developers/doc/applications/nodejs)
