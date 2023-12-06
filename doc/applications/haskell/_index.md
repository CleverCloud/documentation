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
- /doc/deploy/application/haskell/haskell
- /doc/getting-started/by-language/haskell
---

## Overview

Haskell is a purely functional language, especially suited for robust web applications.

There are many ways to write web applications in haskell, from raw [WAI](https://hackage.haskell.org/package/wai) to full-stack frameworks like [Yesod](https://www.yesodweb.com/), simple libraries like [scotty](https://hackage.haskell.org/package/scotty) or type-safe solutions like [servant](https://haskell-servant.GitHub.io/).

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="language-specific-deploy/haskell.md" >}}

{{< readfile file="deploy-git.md" >}}

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}

