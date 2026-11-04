---
type: docs
sidebar:
  exclude: true
linkTitle: Contribute
weight: 290
title: Contribute
description: Learn how to contribute to Clever Cloud documentation, from the issue that describes your idea to the checks to run before a pull request
keywords:
- contribution
- shortcode
- writing
- documentation
- github
- hugo
- markdown
aliases:
- /administrate/guides/contribute
- /contribute
- /contribute/writing
- /doc/contribute/shortcodes/
- /doc/contribute/writing
- /doc/get-help/community
- /readme
---

You can contribute to this documentation on [GitHub](https://github.com/CleverCloud/documentation), with an issue or a pull request.

## Before you write

Before you start new content, open a [GitHub issue](https://github.com/CleverCloud/documentation/issues) to describe it. This lets the team discuss the topic with you and check that nobody already works on it.

## Write and check your content

The documentation uses Markdown files and [Hugo](https://gohugo.io/) with the [Hextra](https://imfing.github.io/hextra/) theme. The [contributing guidelines](https://github.com/CleverCloud/documentation/blob/main/CONTRIBUTING.md) describe the writing standards, and the [README](https://github.com/CleverCloud/documentation/blob/main/README.md) explains how to install the tools, preview the site, and run the checks.

Before you open a pull request, build the site with `hugo` and run markdownlint and Vale on the files you change. Fix every error and warning on the lines you change, and review each Vale suggestion.
