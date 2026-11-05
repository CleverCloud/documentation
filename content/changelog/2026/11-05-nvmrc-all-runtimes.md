---
title: ".nvmrc files ignored on every runtime"
description: From the next images update, Clever Cloud ignores and deletes the .nvmrc file of applications on every runtime, not only Node.js; set the Node.js version with CC_NODE_VERSION, or with mise for a file in your repository
date: 2026-11-05
tags:
  - runtimes
  - configuration
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Clever Cloud already ignores and deletes the `.nvmrc` file of Node.js applications during deployment. From the next images update, it will do the same on every runtime. In a PHP, Python or Ruby application, for example, the deployment will delete the `.nvmrc` file, which won't select a Node.js version.

To set the Node.js version of your application, use the `CC_NODE_VERSION` environment variable, such as `24`:

```bash
clever env set CC_NODE_VERSION 24
clever restart --without-cache
```

In Node.js applications, the `engines.node` field of `package.json` still takes precedence over this variable [until December 1, 2026](/changelog/2026/11-04-node-version-precedence/).

If you prefer to declare the version in a file of your repository, use [mise](/doc/develop/mise/):

```toml {filename="mise.toml"}
[tools]
node = "24"
```

- [Learn more about Node.js versions on Clever Cloud](/doc/deploy/applications/nodejs/#set-nodejs-version)
- [Learn more about mise on Clever Cloud](/doc/develop/mise/)
