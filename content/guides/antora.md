---
title: Antora
description: Build your website with the Antora Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- antora
- asciidoc
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
[Antora](https://antora.org/) is an [AsciiDoc](https://asciidoc.org/) based Static Site Generator focused on technical documentation writing. It promotes *docs as code*, using a YAML playbook and git repositories to organize and host content. If you need an example source code, use the [demo playbook](https://docs.antora.org/antora/latest/install-and-run-quickstart/#create-a-playbook) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git init
npm i -D -E @antora/cli @antora/site-generator
echo -e "site:\n  title: Antora Docs\n  start_page: component-b::index.adoc\ncontent:\n  sources:\n  - url: https://gitlab.com/antora/demo/demo-component-a.git\n    branches: HEAD\n  - url: https://gitlab.com/antora/demo/demo-component-b.git\n    branches: [v2.0, v1.0]\n    start_path: docs\nui:\n  bundle:\n    url: https://gitlab.com/antora/antora-ui-default/-/jobs/artifacts/HEAD/raw/build/ui-bundle.zip?job=bundle-stable\n    snapshot: true" > antora-playbook.yml

```

{{< readfile file="guides/create-static.md" >}}

## Configure environment variables
Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/build/site"
clever env set CC_OVERRIDE_BUILDCACHE "/build/site"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_POST_BUILD_HOOK "npx antora --fetch antora-playbook.yml"
```

{{< readfile file="guides/git-push.md" >}}