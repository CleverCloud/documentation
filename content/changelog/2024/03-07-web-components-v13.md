---
title: Clever Web Components v13
date: 2024-03-07
tags:
  - console
  - components
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Florian Sanders
    link: https://github.com/florian-sanders-cc
    image: https://github.com/florian-sanders-cc.png?size=40
description: Console update with new icons for the documentation
aliases:
- /changelog/2024-03-07-web-components-v13
excludeSearch: true
---

Clever Cloud's [Web Components](https://www.clever-cloud.com/developers/clever-components) v13 are available, with bug fixes, refactoring, and new features. We introduced new possibilities to highlight form fields (larger labels, with color), paving the way for our new add-on/application creation process.

A standardized API is used for UI components that depend on a smart component. It includes a `state` property receiving state type: `loaded`, `loading`, `error` and data. Latest smart components no longer rely on `rxjs`, making them easier to maintain.

- Read the [full changelog](https://github.com/CleverCloud/clever-components/releases/tag/13.0.0) {{< icon "github" >}}
