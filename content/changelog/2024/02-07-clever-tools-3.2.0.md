---
title: Clever Tools 3.2.0 is available
date: 2024-02-07
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
description: And more is coming!
aliases:
- /changelog/2024-02-07-clever-tools-3.2.0
excludeSearch: true
---

As mentioned [in the previous release](../01-25-clever-tools-3.1.0/), the packaging process moved to GitHub Actions to provide a better process, quicker tests and more frequent releases. We start with [the 3.2.0](https://github.com/CleverCloud/clever-tools/releases/tag/3.2.0) adding the log auto retry feature on network failures and some fixes:

* **api:** improve error message with `EAI_AGAIN` and `ECONNRESET` ([b134213](https://github.com/CleverCloud/clever-tools/commit/b134213f30d46dd7f5690a38425deb4fd752148c))
* **logs:** improve error message with `EAI_AGAIN` and `ECONNRESET` ([fada067](https://github.com/CleverCloud/clever-tools/commit/fada06771369173e579f5fd3a708ff3cef40c95f))
* **logs:** improve open and error debug message ([28dd996](https://github.com/CleverCloud/clever-tools/commit/28dd9968bec8de9545c6b940be732d3f8f87a8f9))
* **logs:** increase connection timeout ([a4ec4b9](https://github.com/CleverCloud/clever-tools/commit/a4ec4b90b5d3938e27679edeb7d375281def3776))
* **logs:** only print SSE errors as debug when verbose mode is enabled ([3ea21c6](https://github.com/CleverCloud/clever-tools/commit/3ea21c6a4ff75db8df5f8177bba10ef17c2962e0))

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install). For example with `npm`:

```
npm update -g clever-tools
clever version
```
