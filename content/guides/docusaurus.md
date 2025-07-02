---
title: Docusaurus
description: Build your website with the Docusaurus Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- docusaurus
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
If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
npx create-docusaurus@latest myStaticApp classic
```

{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables
Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/build"
clever env set CC_OVERRIDE_BUILDCACHE "/build"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_POST_BUILD_HOOK "npx docusaurus build"
```

{{< content "git-push" >}}