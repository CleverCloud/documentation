---
title: 'JS Client 11.1 is available, help us to enhance the next major release'
description: Test the next JS client v12 with API tokens, typechecking and better DX, share your feedbacks
date: 2025-09-10
tags:
  - client
  - javascript
authors:
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 11.1](https://github.com/CleverCloud/clever-client.js/blob/master/CHANGELOG.md#1110-2025-09-10) is available. It fixes some bugs but more importantly, it is the first public release including the next major release structure (v12). For this project, we completely overhauled the way we manage v2 and v4 API endpoints.

We tested each of them, developed analysis scripts to ensure that we cover correctly all endpoints and methods, including legacy parts with inconsistent naming and responses. We thought it to be easier to use, more powerful with less code. It brings type checking, better DX, and a more consistent usage.

For example, you can now get you profile information only with this code:

```javascript

```

This JavaScript client supports the new API Bridge and API tokens for authentication, our Redis HTTP client used for KV explorer, and paves the way for multiple incoming projects based on it, including our new public API.

You can start to use this incoming release by adding `@clevercloud/client` to your project and reading [its dedicated documentation](https://github.com/CleverCloud/clever-client.js/blob/master/NEW_CLIENT.md). Feel free to share your feedbacks and needs in the [GitHub repository](https://github.com/CleverCloud/clever-client.js/issues).

> [!NOTE] The new JS client is still early to use in production
> As we'll make it evolve over the coming weeks, next releases will break things. If you need stability, use it with current client imports. If you don't change anything to your code, it will keep working as before, even if you use 11.1 release.
