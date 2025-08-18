---
title: Better support of pnpm and Yarn
date: 2025-08-12
tags:
  - runtimes
  - configuration
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: One runtime, your favorite tools
excludeSearch: true
---

After [adding support for CC_NODE_VERSION](/changelog/2025/05-16-images-update) and [Bun](/changelog/2025/06-03-native-bun-support) to deploy JavaScript and TypeScript applications on Clever Cloud, we're enhancing our support of alternative package managers like `pnpm` and `yarn`.

## pnpm and Yarn better support

As our platform is flexible, it was already possible to use them. However, it was not as easy as it could be. With our latest image, you can set the `CC_NODE_BUILD_TOOL` environment variable in [Bun & Node.js runtime](/doc/applications/nodejs/) to:

- `pnpm`: to use [pnpm](https://pnpm.io/) as your package manager
- `yarn-berry`: to use [Yarn](https://yarnpkg.com/) 3.x or 4.x as your package manager

It will automatically adapt the command used to install dependencies during the build phase, cached dependencies and run command.

## Version management

To load a specific version, set the `packageManager` field in your `package.json` file. For example, to use `pnpm@10.14.0`:

```json
{
  "packageManager": "pnpm@10.14.0"
}
```

This is the default way to manage version for pnpm and Yarn when a new project is initialized.

## Auto-detection

If a `pnpm-lock.yaml` file is present as the root of your project, it's automatically detected during deployment and `pnpm` used as the package manager. If a `yarn.lock` file is present, and the `packageManager` field in your `package.json` file is set to a Yarn 3.x or 4.x version, `yarn-berry` is used as the package manager.

## Yarn system version, 1.x and 2.x deprecation

Yarn 1.x is still the default version included in our images for legacy reasons. If `CC_NODE_BUILD_TOOL` is set to `yarn-berry`, the latest packaged version of Yarn (currently `4.9.2`) will be used as for the system. **This work in any Clever Cloud runtime.** In the coming months Yarn 4.x will become the default version in our images.

If you use a Yarn 1.x or Yarn 2.x version, a deprecation warning is displayed during deployment as they're not maintained anymore.

- [Learn more about Bun & Node.js runtime](/doc/applications/nodejs/)
