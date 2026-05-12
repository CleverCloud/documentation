---
title: "Cellar: new dashboard and Cellar Explorer"
description: A new Cellar add-on dashboard surfaces access information, consumption, the s3cfg configuration file, and the Cellar Explorer to browse buckets and objects directly from the Console.
date: 2026-05-12
tags:
  - addons
  - cellar
  - console
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Cellar](/doc/addons/cellar/), our S3-compatible object storage service, gets a new dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). It puts the information you need to connect and operate your add-on within reach: access key ID and secret, endpoint, region, current storage and bandwidth consumption, plan and billing details. The pre-filled `s3cfg` configuration file is one click away, ready to drop into your home directory and use with `s3cmd` or any compatible tool.

## Cellar Explorer

The new dashboard also opens the door to the **Cellar Explorer**, a browser-side file manager for your Cellar buckets, built in the spirit of the [KV Explorer](/doc/addons/materia-kv/#clever-cloud-kv-explorer) we shipped for Materia KV and Redis® add-ons. It lists every bucket of the add-on, lets you navigate objects as folders, and supports the operations you reach for most often: download an object, upload one or several files, copy a public URL, inspect object metadata, all without leaving the Console or installing a third-party S3 client.

Under the hood, the Cellar Explorer relies on the new Cellar APIs we've been rolling out, which also power upcoming features around versioning and usage reporting. Expect the tool to keep evolving over the coming months, with more operations exposed directly in the interface.

The Cellar Explorer is available in Beta for every Cellar add-on. Share your feedback and feature requests on our [GitHub Community](https://github.com/CleverCloud/Community/discussions/155).

- [Learn more about Cellar on Clever Cloud](/doc/addons/cellar/)
- [Share your feedback on the Cellar Explorer](https://github.com/CleverCloud/Community/discussions/155)
