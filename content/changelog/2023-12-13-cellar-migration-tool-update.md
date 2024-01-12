---
title: Cellar migration tool update
date: 2023-12-13
tags:
  - cellar
excludeSearch: true
description: Cellar migration tool update to 2.1.0
---

This release v2.1.0 of the [Cellar migration tool](https://github.com/CleverCloud/cellar-migration/releases/tag/v2.1.0) adds support for keep-alive in S3 clients and fixes a panic when a network error occurs.

## About the Cellar migration tool

The Cellar migration tool is a Command Line Interface tool to migrate your object storage buckets on Clever Cloud. This tool currently supports AWS-S3 and Cellar (Clever Cloud own Object Storage service) but it should work with any service implementing the S3 API.

This is an rsync like tool that will synchronize your buckets. You can start it in a loop and it will only synchronize objects that are different between the two buckets. It is best to run it on a machine with a high network bandwidth.

 Check this [project Github](https://github.com/CleverCloud/cellar-migration) {{< icon "github" >}}
