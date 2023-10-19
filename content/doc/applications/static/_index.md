---
type: docs
title: Static
shortdesc: Deploy Static files on Clever Cloud
tags:
- deploy
keywords:
- static
str_replace_dict:
  "@application-type@": "Static"
type: docs
aliases:
- /doc/deploy/application/static/static
comments: false
---

## Overview

If you only need to serve static files without executing any code on the backend, for instance for a javascript Single Page Application (SPA), you can create a static application.

This runtime is based on apache, so shares a lot with the [PHP runtime]({{< ref "doc/applications/php" >}}). This means you can use `.htaccess` files for redirection or access control.

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/env-injection.md" >}}

Application deployment on Clever Cloud is via **Git or FTP**.

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/deploy-ftp.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}

## Serving index.html for SPA (Single Page Application) routers

When you work with an SPA framework like React, Vue.js, Angular..., you're using client side routing.
This means when you click on a link going to `/the-page`, your browser doesn't make an HTTP request for `/the-page`.
Instead, the client side router highjacks the clicks on links, changes the DOM to display the page and ask the browser to change the URL in the address bar to `/the-page`.

What happens if you try to refresh the page?
If you do this, the browser will try to make an HTTP request for `/the-page`.
In most situations, SPA only have one HTML document at the root called `index.html`.
This is why, you'll probably get a 404 error.

To fix this, most people using SPA frameworks configure their HTTP server to serve the `index.html` for all unkown requests.
By this we mean for all requests that don't have a matching file on disk to serve.

To do this with our static applications, you need a `.htaccess` file like this at the root of your project:

```
RewriteEngine On

# If an existing asset or directory is requested, serve it
RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} -f [OR]
RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} -d
RewriteRule ^ - [L]

# If the requested resource doesn't exist, use index.html
RewriteRule ^ /index.html
```
