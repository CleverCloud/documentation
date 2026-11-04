---
title: The Console warns you six months before a runtime version reaches end of life
description: The overview and environment variables pages of an application warn you when the runtime version it sets reaches end of life within six months, starting with PHP 8.1 and Python 3.9
date: 2025-08-08
tags:
  - console
  - applications
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [Clever Cloud Console](https://console.clever-cloud.com) already warned you when an application sets an end-of-life version of its runtime through `CC_ELIXIR_VERSION`, `CC_JAVA_VERSION`, `CC_NODE_VERSION`, `CC_PHP_VERSION`, `CC_PYTHON_VERSION`, or `CC_RUBY_VERSION`. It now warns you up to six months before this date, so you can plan the upgrade instead of discovering it afterwards. The first versions concerned are Python 3.9, which reaches end of life on October 31, 2025, and PHP 8.1, on December 31, 2025.

The notice appears on the overview and environment variables pages of the application. It gives the end-of-life date of the version and links to the support policy of the runtime when available. It also recommends the version to set instead, with a link to the environment variables of the application.

The Console reads the version these variables set explicitly, such as `8.1` or `3.9.21`. It doesn't resolve version ranges, nor versions an application selects otherwise, such as through `engines.node` in a `package.json` file.

- [Learn more about environment variables](/doc/develop/common-configuration/environment-variables/)
