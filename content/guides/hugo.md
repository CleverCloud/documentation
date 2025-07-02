---
title: Hugo
description: Build your website with the Hugo Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- hugo
- static
- ssg
- html
- js
- css
- website
type: "docs"
comments: false
draft: false
---

If you need an example source code, use [Theme mini](https://github.com/nodejh/hugo-theme-mini) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Hugo](https://gohugo.io/installation/)):

```bash
git clone https://github.com/nodejh/hugo-theme-mini myStaticApp
```

{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables and deploy script

Next, configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_WEBROOT "/public"
clever env set CC_OVERRIDE_BUILDCACHE "/public"
clever env set CC_PRE_BUILD_HOOK "bash setup_hugo.sh"
clever env set CC_POST_BUILD_HOOK "hugo --minify --gc"
```

Edit the deploy script (`setup_hugo.sh`) with this content:

```bash
HUGO_VERSION="0.121.1"
HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
DEST_BIN="${HOME}/.local/bin"
FILENAME="hugo.tar.gz"

# Download Hugo Extended and place it in a folder in the $PATH
curl --create-dirs -s -L -o ${DEST_BIN}/${FILENAME} ${HUGO_URL}
cd ${DEST_BIN}
tar xvf ${FILENAME} -C ${DEST_BIN}
rm ${FILENAME}
```

{{< content "git-push" >}}

## 404 Redirections

Since your are using [`CC_WEBROOT`](../../doc/reference/reference-environment-variables/#php) environment variable, this is where Apache is going to looks for directives. To allow redirecting to your `404.html` theme or custom page in Hugo, put the following `.htaccess` file in your `/static` folder :

```ApacheConf {filename=".htaccess"}
RewriteEngine On
ErrorDocument 404 /404.html
```

This file will be copied to the root of your web server in `/public` on build.
