---
title: "Linux kernel 7.0.6 available"
description: The Linux kernel can now be updated independently from the rest of our images. Restart your application to run on 7.0.6.
date: 2026-05-12
tags:
  - images
  - update
  - kernel
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Over the last few weeks, we worked on decoupling the Linux kernel from the rest of our runtime images. This work is now complete: kernel upgrades no longer require a full image refresh and can roll out on their own cadence, which means faster delivery of security fixes and hardware support improvements without touching the language runtimes, build tools, or system libraries shipped in each image.

As a first step on this new pipeline, **Linux 7.0.6** is now available. To run your application on this kernel, restart it from the [Clever Cloud Console](https://console.clever-cloud.com) or with `clever restart`. Newly deployed applications pick up the new kernel automatically.

- [What's new in Linux 7.0](https://kernelnewbies.org/Linux_7.0)
- [Linux 7.0.6 changelog](https://cdn.kernel.org/pub/linux/kernel/v7.x/ChangeLog-7.0.6)
