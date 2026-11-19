---
title: "Java4Shell: fixed Java 17, 21 and 25 releases are available (Security update)"
description: Clever Cloud images ship the Eclipse Temurin releases of Java 17, 21 and 25 that follow the Java4Shell mitigation applied to Java applications
date: 2026-11-19
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Our Java/Scala runtimes now ship the [Eclipse Temurin](https://adoptium.net/temurin/releases/) releases that follow the [Java4Shell mitigation](/changelog/2026/11-17-java4shell-mitigation/). Deployment is in progress for all our users.

- Java 17: [17.0.21.1+2](https://github.com/adoptium/temurin17-binaries/releases/tag/jdk-17.0.21.1%2B2)
- Java 21: [21.0.13.1+2](https://github.com/adoptium/temurin21-binaries/releases/tag/jdk-21.0.13.1%2B2)
- Java 25: [25.0.5.1+2](https://github.com/adoptium/temurin25-binaries/releases/tag/jdk-25.0.5.1%2B2)

These releases fix [CVE-2026-114938](https://www.cve.org/CVERecord?id=CVE-2026-114938), the flaw in the Base64 decoder of the HotSpot JVM. Java 8 and 11 aren't affected by this vulnerability. If your application sets `CC_JAVA_VERSION` to `17`, `21` or `25`, or uses the default version, you have nothing to change.

Clever Cloud still adds the `-XX:-UseBASE64Intrinsics` option when it launches a Java application. If yours brings its own Java, in a Docker image for example, update it to a fixed release.

- [Learn more about Java on Clever Cloud](/doc/deploy/applications/java/)
