---
title: Lume (Deno)
description: Build your website with Lume Static Site Generator (SSG) using Deno and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- deno
- lume
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
If you need an example source code, use [Lume website](https://github.com/lumeland/lume.land) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Deno](https://docs.deno.com/runtime/manual#install-deno)):
```bash
git clone https://github.com/lumeland/lume.land myStaticApp
```
{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables and deploy script
Next, configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_WEBROOT "/_site"
clever env set CC_OVERRIDE_BUILDCACHE "/_site"
clever env set CC_PRE_BUILD_HOOK "bash setup_deno.sh"
clever env set CC_POST_BUILD_HOOK "deno task lume"
```
Edit the deploy script (`setup_deno.sh`) with this content:
```bash
DENO_VERSION="1.39.1"
DENO_URL="https://github.com/denoland/deno/releases/download/v${DENO_VERSION}/deno-x86_64-unknown-linux-gnu.zip"
DEST_BIN="${HOME}/.local/bin"
FILENAME="deno.zip"

# Download Deno and place it in a folder in the $PATH
curl --create-dirs -s -L -o ${DEST_BIN}/${FILENAME} ${DENO_URL}
cd ${DEST_BIN}
unzip ${FILENAME} -d ${DEST_BIN}
rm ${FILENAME}
```

{{< content "git-push" >}}