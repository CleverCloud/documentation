---
title: "Images update: .Net 10, Go 1.26, Mise 2026.2, Python 3.14, uv 0.10"
description: "Many tiny updates, and some surprises we'll detail soon"
date: 2026-02-12
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * git 2.53.0
  * Mise 2026.2.8
  * nginx 1.28.2
  * pgpool2 4.7
* **.Net:**
  * Update to 10.0.102
* **Docker:**
  * Docker 29.2.1
* **Go:**
  * Update to 1.26.0
* **Node.js & Bun:**
  * Bun 1.3.9
  * nvm 0.40.4
* **Python:**
  * Update to 3.13.12
  * Update to 3.14.3
  * pip 26.0.1
  * uv 0.10.2

## .Net 10 support

You can now set `CC_DOTNET_VERSION=10.0`, default version is still `8.0`. We'll move to `10.0` in the coming weeks.

## Python 3.14 support

You can now set `CC_PYTHON_VERSION=3.14`, default version is still `3.13`. We'll move to `3.14` in the coming weeks.

## Mise 2026.2

Latest branch of Mise includes many changes such as Node.js version detection from `package.json`, hooks overhaul or Shell-style variable expansion in env values. You can benefit from them with this release.

- [Learn more about latest versions of Mise](https://github.com/jdx/mise/releases)

## Fixes

This release includes:
- A fix for [Mise Tasks management in Linux Runtime](/doc/applications/linux/#build-and-run-commands)
- A fix for `CC_NODE_BUILD_TOOL=yarn-berry`
