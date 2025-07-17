---
title: "Images update: news for Tailscale, SQL Server extensions for PHP"
date: 2025-04-03
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Multiple new features and a fix for this week!
excludeSearch: true
---

We deployed and updated all our images, with no impact for our users.

* **Common:**
  * Fix an issue with scaling feature
  * Linux kernel 6.13.9
  * Mise 2025.3.11
  * Tailscale 1.82.0
* **Go:**
  * Update to 1.24.2

SQL Server extensions (`sqlsrv` and `pdo_sqlsrv`) are now available for PHP 8.1 to 8.4. To enable them, add `ENABLE_SQLSRV=true` or `ENABLE_PDO_SQLSRV=true` environment variables to your application.

We enhanced our Tailscale native integration. It now supports `--accept-dns` and `--accept-routes` [flags](https://tailscale.com/kb/1072/client-preferences?q=accept-route#use-tailscale-dns-settings). To disable or enable them, set `TAILSCALE_ACCEPT_DNS` and `TAILSCALE_ACCEPT_ROUTES` environment variables to `false` or `true` in your application.

- [Learn more about Tailscale on Clever Cloud](/developers/doc/reference/reference-environment-variables/#tailscale-support)
- [Learn more about PHP with Apache on Clever Cloud](/developers/doc/applications/php/)
