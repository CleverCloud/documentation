---
title: JS Client 8.0.3 is available
date: 2024-01-30
tags:
  - js
  - api
  - client
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: The Clever Cloud JS Client has been updated to version 8.0.3
aliases:
- /changelog/2024-01-30-js-client-8.0.3
excludeSearch: true
---

If you want to use our API from a JavaScript application or module, we provide an easy-to-use open source client, available [as a npm package](https://www.npmjs.com/package/@clevercloud/client). It has just been updated to [version 8.0.3](https://github.com/CleverCloud/clever-client.js/blob/master/CHANGELOG.md#803-2024-01-30) where the options param of the `on` method is optional. There are fixes for the auto retry of logs SSE v2, event WS. But also for new logs SSE v4 ([ApplicationLogStream](https://github.com/CleverCloud/clever-client.js/pull/93)).

- Check this project [on GitHub](https://github.com/CleverCloud/clever-client.js) {{< icon "github" >}}
