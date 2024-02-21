---
type: docs
title: Haskell
shortdesc: Haskell is love, haskell is life
tags:
- deploy
keywords:
- haskell
- stack
str_replace_dict:
  "@application-type@": "Haskell"
type: docs
aliases:
- /doc/deploy/application/haskell
- /doc/deploy/application/haskell/haskell
- /doc/getting-started/by-language/haskell
- /doc/partials/language-specific-deploy/haskell
---

## Overview

Haskell is a purely functional language, especially suited for robust web applications.

There are many ways to write web applications in haskell, from raw [WAI](https://hackage.haskell.org/package/wai) to full-stack frameworks like [Yesod](https://www.yesodweb.com/), simple libraries like [scotty](https://hackage.haskell.org/package/scotty) or type-safe solutions like [servant](https://haskell-servant.GitHub.io/).

{ {{% content/create-application %}}

 {{% content/set-env-vars %}}

{{< readfile file="language-specific-deploy/haskell.md" >}}

 {{% content/deploy-git %}}

 {{% content/link-addon %}}

{{% content/more-config %}}
