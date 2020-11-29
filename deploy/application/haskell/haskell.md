---
title: Deploy Haskell applications
shortdesc: Haskell is love, haskell is life
tags:
- deploy
keywords:
- haskell
- stack
str_replace_dict:
  "@application-type@": "Haskell"
---

## Overview

Haskell is a purely functional language, especially suited for robust web applications. There are many ways to write web applications in haskell, from raw [WAI](https://hackage.haskell.org/package/wai) to full-stack frameworks like [Yesod](https://www.yesodweb.com/), simple libraries like [scotty](https://hackage.haskell.org/package/scotty) or type-safe solutions like [servant](https://haskell-servant.GitHub.io/).

Clever Cloud uses stack to build Haskell applications.
{{< alert "warning" "Haskell support is in public beta" >}}
    Haskell support is still new and rough around the edges, so please contact the support to give feedback (good or bad).
{{< /alert >}}

{{< readfile "/content/partials/create-application.md" >}}

{{< readfile "/content/partials/set-env-vars.md" >}}

{{< readfile "/content/partials/language-specific-deploy/haskell.md" >}}

{{< readfile "/content/partials/deploy-git.md" >}}

{{< readfile "/content/partials/link-addon.md" >}}

{{< readfile "/content/partials/more-config.md" >}}
