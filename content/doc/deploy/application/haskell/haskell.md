---
type: docs
title: Deploy Haskell applications
shortdesc: Haskell is love, haskell is life
tags:
- deploy
keywords:
- haskell
- stack
str_replace_dict:
  "@application-type@": "Haskell"
type: docs
---

## Overview

Haskell is a purely functional language, especially suited for robust web applications.

There are many ways to write web applications in haskell, from raw [WAI](https://hackage.haskell.org/package/wai) to full-stack frameworks like [Yesod](https://www.yesodweb.com/), simple libraries like [scotty](https://hackage.haskell.org/package/scotty) or type-safe solutions like [servant](https://haskell-servant.GitHub.io/).

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/language-specific-deploy/haskell.md" >}}

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
