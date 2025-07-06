---
title: Clever Tools 3.1.0 is available
date: 2024-01-25
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
description: Be prepared for a new wave of Clever Tools starting this release 3.1.0!
aliases:
- /changelog/2024-01-25-clever-tools-3.1.0
excludeSearch: true
---

For several months, we were preparing our CLI, [Clever Tools](https://github.com/CleverCloud/clever-tools/), for big changes. It starts to be ready for prime time with the 3.1.0 release. First, the packaging process moved to GitHub Actions with some improvements:
- You can now get the [list of releases](https://github.com/CleverCloud/clever-tools/releases) with a changelog and source code archives
- No more beta channel: you'll be able to test new features easier
- Better process, quicker tests, more releases!

If 3.0.x branch brought new log stack (faster, longer, order), you now get updated runtimes and zones lists [in autocomplete](https://github.com/CleverCloud/clever-tools?tab=readme-ov-file#enabling-autocompletion), details about application owner during deployment, `git+ssh` URL in new linked/created applications information.

`clever deploy` can now be used with the `--same-commit-policy` or `-p` flag to set policy to apply when the local commit is the same as the remote one: `error`, `ignore`, `restart` or `rebuild` (default: `error`).

Of course, there are also some bug fixes. And be prepared: more new features are on the way!

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install). For example with `npm`:

```
npm update -g clever-tools
clever version
```
