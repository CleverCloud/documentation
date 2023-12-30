---
title: Deploy an Astro based static website on Clever Cloud
description: Build your website with the Astro Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
weight: 1
tags:
- guides
keywords:
- astro 
- nodejs
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
If you need an example source code, get [Astrowind](https://github.com/onwidget/astrowind) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git clone https://github.com/onwidget/astrowind myStaticApp
```

{{< readfile file="guides/create-static.md" >}}

## Configure environment variables
Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/dist"
clever env set CC_OVERRIDE_BUILDCACHE "/dist"
clever env set CC_PRE_BUILD_HOOK "npm install && npm run astro telemetry disable"
clever env set CC_POST_BUILD_HOOK "npm run build"
```

{{< readfile file="guides/git-push.md" >}}