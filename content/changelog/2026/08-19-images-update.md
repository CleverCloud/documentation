---
title: "Images update: FFmpeg 9, Node.js 24.19, OpenSSH 10.5, rsync 3.5"
description: Runtime updates for Go, Node.js, Python and Ruby, with FFmpeg 9, OpenSSH 10.5, rsync 3.5 and new PDF tooling
date: 2026-08-19
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
  * Anubis 1.26.2
  * ClamAV 1.5.4
  * Chromium 151.0.7922.137
  * FFmpeg 9.0
  * Nano 9.2
  * OpenSSH 10.5_p1
  * Poppler 26.08.0
  * pdfio 1.6.4 is now available
  * qpdf is no longer included
  * rsync 3.5.0
* **Go:**
  * Update to 1.26.6
* **Node.js & Bun:**
  * Node.js 24.19.0 (npm 11.17.0)
* **Python:**
  * Update to 3.10.21
  * Update to 3.11.16
  * Update to 3.12.14
  * Update to 3.13.15
  * Update to 3.14.7
* **Ruby:**
  * Update to 3.3.12
  * Update to 3.4.10
  * Update to 4.0.6

## Health Check and Request Flow improvements

This release also improves the management of Health Checks and Request Flow across our application images. See the [Request Flow documentation](/doc/develop/request-flow/) to learn how to configure middleware chaining and automatic port allocation.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.1.10.
