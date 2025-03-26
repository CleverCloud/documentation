---
title: "FrankenPHP is available as a runtime on Clever Cloud"
description: Use it, help us to improve
date: 2025-03-28
tags:
  - images
  - frankenphp
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[As announced last year](https://www.clever-cloud.com/blog/company/2024/10/09/news-php-on-clever-cloud/), we worked to make FrankenPHP available on Clever Cloud as simple as we can.

First, we started to document how to deploy it with practical examples. Then, we packaged it and included it in our images to make some tests internally and with customers. Starting today, anyone can deploy a PHP application using FrankenPHP on Clever Cloud without needing any Docker container or complex configuration.

Just create a FrankenPHP application [from API](/developers/api), [Console](https://console.clever-cloud.com) or with [Clever Tools](/developers/doc/cli) and deploy it:

```bash
echo '<?php echo phpinfo();' > index.php
git init
git add .
git commit -m "Initial FrankenPHP release"

clever create --type frankenphp
clever deploy
clever open
```

FrankenPHP on Clever Cloud comes with [lots of extensions](/developers/doc/applications/frankenphp/#included-extensions) included and we simplified many aspects of application management: if a `composer.json` file is present at the root of your project it's automatically used to install dependencies, you can also use your own `composer.phar` file, Composer flags, define where are the files to serve, define a script to use with FrankenPHP worker feature or a custom run command with environment variables.

As it's a new image, help us improve it by reporting any issue or suggestion on the [Clever Cloud Community](https://github.com/CleverCloud/Community/discussions/categories/frankenphp).

* [FrankenPHP and Materia KV example](https://github.com/CleverCloud/frankenphp-kv-json-example)
* [Learn more about FrankenPHP on Clever Cloud](/developers/doc/applications/frankenphp/)
* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)
