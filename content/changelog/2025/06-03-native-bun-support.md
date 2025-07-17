---
title: "Bun native support on Clever Cloud"
description: Run Bun without any efforts
date: 2025-06-03
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Since April](/developers/changelog/2025/04-16-images-update/), Bun is included in our images. It helped customers to deploy their applications faster, profit from its native [Redis®](https://bun.sh/docs/api/redis) and [object storage](https://bun.sh/docs/api/s3) support. Starting today, you can deploy your Bun applications on Clever Cloud without any efforts.

If a `bun.lock` file is detected at the root of your project, and you didn't ask for another JavaScript runtime or package manager, your application will be deployed with [Bun](https://bun.sh) as a package manager and runtime. You can also ask for Bun explicitly by setting the `CC_NODE_BUILD_TOOL` environment variable to `bun`.

Want to give it a try? Just launch these commands with Bun and [Clever Tools CLI](/developers/doc/cli/install) installed on your system:

```
mkdir bunDemo
cd bunDemo

git init
bun init --yes --react

git add .
git commit -m "Initial commit"

clever create --type node
clever deploy
clever open
```

You'll get a basic React application running on Bun, deployed on Clever Cloud.

* [Learn more about Bun & Node.js on Clever Cloud](/developers/doc/applications/nodejs)
