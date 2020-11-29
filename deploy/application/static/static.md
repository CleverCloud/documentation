---
title: Deploy static files
shortdesc: Perfect for pure-javascript applications
tags:
- deploy
keywords:
- static
str_replace_dict:
  "@application-type@": "Static"
---

## Overview

If you only need to serve static files without executing any code on the backend, for instance for a javascript Single Page Application (SPA), you can create a static application.

This runtime is based on apache, so shares a lot with the [PHP runtime]({{< ref "deploy/application/php/php-apps.md" >}}). This means you can use `.htaccess` files for redirection or access control.

{{< readfile "/content/partials/create-application.md" >}}

{{< readfile "/content/partials/set-env-vars.md" >}}

{{< readfile "/content/partials/env-injection.md" >}}

Application deployment on Clever Cloud is via **Git or FTP**.

{{< readfile "/content/partials/deploy-git.md" >}}

{{< readfile "/content/partials/deploy-ftp.md" >}}

{{< readfile "/content/partials/link-addon.md" >}}

{{< readfile "/content/partials/more-config.md" >}}
