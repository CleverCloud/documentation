---
type: docs
title: Clamav
position: 3
shortdesc: Configuring Clamav on Clever Cloud
tags:
- administrate
keywords:
- apps
- antivirus
- clamav
type: docs
---

[Clam AntiVirus](https://www.clamav.net/) is an open source (GPLv2) anti-virus toolkit, designed especially for e-mail scanning on mail gateways. It provides a number of utilities including a flexible and scalable multi-threaded daemon, a command line scanner and advanced tool for automatic database updates. The core of the package is an anti-virus engine available in a form of shared library.

## ClamAV for all applications

ClamAV is not enabled by default but it's available for all Clever Cloud applications.

## Activate ClamAV

You can set the **CC_CLAMAV** environment variable to enable ClamAV for your application:

```bash
CC_CLAMAV=true
```

This variable is used to start these two services:

* **clamav-daemon.service** (multi-threaded daemon that uses libclamav to scan files for viruses).
* **clamav-freshclam.service** (used to update signature database sets to the latest version).

The signature database is updated every 2 hours.

## Memory consumption

ClamAV can consume a lot of resources, make sure you have a scaler with enough memory (at least 1GB available) to avoid a complete shutdown / crash of your application (OOM).

## Unix and/or TCP sockets connections

The ClamAV daemon on Clever Cloud instances listens for incoming connections on the following sockets:

Unix socket:

```bash
/run/clamav/clamd.ctl
```

TCP socket:

```bash
localhost:3310
```

Be sure to use these settings when configuring your ClamAV client.

## Additional configurations

`CC_CLAMAV_MAXTHREADS`: Maximum number of threads running at the same time.
`CC_CLAMAV_MAXQUEUE`: Maximum number of queued items.

If you have special needs, you can make a request on [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).
