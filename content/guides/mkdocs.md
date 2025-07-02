---
title: MkDocs
description: Build your website with the MkDocs Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- mkdocs
- python
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
If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and [pip](https://pip.pypa.io/en/stable/installation/)):
```bash
# Use pip or pip3 depending on your system
pip install mkdocs
mkdocs new myStaticApp
```

{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables
Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_WEBROOT "/site"
clever env set CC_OVERRIDE_BUILDCACHE "/site"
clever env set CC_PRE_BUILD_HOOK "python3 -m ensurepip --upgrade && pip3 install mkdocs"
clever env set CC_POST_BUILD_HOOK "mkdocs build"
```

{{< content "git-push" >}}