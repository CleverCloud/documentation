---
title: Eleventy (11ty)
description: Build your website with the Eleventy (11ty) Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- Eleventy
- 11ty
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
If you need an example source code, get [11ty base blog](https://github.com/11ty/eleventy-base-blog) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git clone https://github.com/11ty/eleventy-base-blog myStaticApp
```

{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables
Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/_site"
clever env set CC_OVERRIDE_BUILDCACHE "/_site"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_POST_BUILD_HOOK "npx @11ty/eleventy"
```

{{< content "git-push" >}}