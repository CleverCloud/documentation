---
title: 'Clever Tools 4.0 is available: a large clean up before big changes'
date: 2025-09-01
description: Multiple updates under the hood, Node.js 22, Clever Cloud JS client 12.0, TypeScript types, better code quality and tooling
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
excludeSearch: true
---

Clever Tools 4.0 is available. It's a new major version as there are multiple breaking changes. Not in commands nor behavior, but in runtime, code quality and tooling. This release is now based on Node.js 22 and [Clever Cloud JS client 11.0](https://www.npmjs.com/package/@clevercloud/client).

Under the hood we've also :
- Updated [CONTRIBUTING](https://github.com/CleverCloud/clever-tools/blob/master/CONTRIBUTING.md) and [README](https://github.com/CleverCloud/clever-tools/blob/master/README.md) files
- Removed lots of dependencies, updated those remaining
- Added scripts and tools to ease the development and contribution
- Renewed the complete CI/CD for checking, packaging and distribution steps
- Removed publishing to Chocolatey, we now use WinGet as Windows package manager
- Used `yao-pkg` for compilation, with native Apple Silicon version for macOS users
- Added TypeScript types via JSDoc (CI scripts only for now), quality code tools configuration (ESLint, Prettier)

These changes will pave the way for future major improvements and new features as we'll be able to iterate faster. Thus, we'll progressively introduce new commands management and better UX in the coming months.

- [Learn more about choices we made in Clever Tools 4.0](https://github.com/CleverCloud/clever-tools/pull/943)

## How to use Clever Tools 4.0?

We'll make this release available through package managers in the coming days. It will let you some time to stick to branch 3.x if needed. In the meantime, you can download and test Clever Tools 4.0 preview binaries directly. 

- [Download Clever Tools 4.0](https://github.com/CleverCloud/clever-tools/pull/959#issuecomment-3241165087)
- [Report any problem with an issue](https://github.com/CleverCloud/clever-tools/issues)
