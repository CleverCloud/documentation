---
title: "Java servlet containers cleanup, Wildfly upgrade"
date: 2024-08-26
tags:
  - applications
  - java
authors:
  - name: Julien Durillon
    link: https://github.com/judu
    image: https://github.com/judu.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Wildfly 27.0.1 and 33.0.1 are now supported
aliases:
- /changelog/2024-08-26-java-containers-update
excludeSearch: true
---

As part of our images' enhancement process, we've tidied up the [list of supported servlet containers](/developers/doc/applications/java/java-war/#available-containers). Those that are no longer used by our customers are removed from the Java image. If you need a container which is not listed in [the servlet container list](/developers/doc/applications/java/java-war/#available-containers) or a specific version, please contact [our support team](https://console.clever-cloud.com/ticket-center-choice). This release also includes a [Wildfly](https://github.com/wildfly/wildfly) upgrade. Versions 27.0.1 and 33.0.1 are now available.

- Learn more about [Java on Clever Cloud](/developers/doc/applications/java/)
