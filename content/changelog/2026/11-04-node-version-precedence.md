---
title: "CC_NODE_VERSION takes precedence over engines.node from December 1"
description: From December 1, 2026, the CC_NODE_VERSION environment variable takes precedence over the engines.node field of package.json to select the Node.js version of an application
date: 2026-11-04
tags:
  - runtimes
  - configuration
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

In May 2025, we [added `CC_NODE_VERSION` support to Node.js applications](/changelog/2025/05-16-node-versions/) and recommended it over the `engines.node` field of `package.json`. For legacy reasons, `engines.node` still takes precedence in Node.js applications when you set both. From December 1, 2026, `CC_NODE_VERSION` will take precedence, and `engines.node` will only apply when this variable isn't set.

The npm documentation describes `engines.node` as the Node.js versions your package works on, an advisory field that npm only checks with warnings, unless you enable [`engine-strict`](https://docs.npmjs.com/cli/v11/using-npm/config#engine-strict). A dedicated environment variable makes the version you deploy explicit, and lets you change it without a new commit. It also works in every non-Docker runtime, not only in Node.js applications.

This change only affects Node.js applications that set both, to values that resolve to different versions. To check yours, compare both values from a folder linked to the application, on the revision you deploy:

```bash
clever env | grep '^CC_NODE_VERSION='
node -p "require('./package.json').engines?.node"
```

If they differ, set `CC_NODE_VERSION` to the version you want, or remove it to keep the one `engines.node` selects today, then redeploy:

```bash
clever env rm CC_NODE_VERSION
clever restart --without-cache
```

Applications that set only one of them, or none, keep the same behavior.

- [Learn more about Node.js versions on Clever Cloud](/doc/deploy/applications/nodejs/#set-nodejs-version)
