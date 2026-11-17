---
title: "Java4Shell: mitigation applied to Java applications (Security update)"
description: Clever Cloud disables the Base64 intrinsics on Java applications to mitigate the critical vulnerability CVE-2026-114938, until fixed Java versions are available
date: 2026-11-17
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [OpenJDK security advisory](https://openjdk.org/groups/vulnerability/advisories/2026-11-17) and the [Oracle security alert](https://www.oracle.com/security-alerts/cspunov2026.html) describe a critical vulnerability affecting Java, [CVE-2026-114938](https://www.cve.org/CVERecord?id=CVE-2026-114938), known as [Java4Shell](https://calif.io/java4shell/). With a CVSS v4 score of 9.2, it can allow unauthenticated remote code execution on applications that decode Base64 data sent by an attacker, through an authentication header or a file upload for example.

The flaw is an out-of-bounds write in the hardware-accelerated Base64 decoder of the HotSpot JVM. It affects OpenJDK 17.0.6 and later, and the distributions built from it, on x86-64 processors with AVX-512 VBMI support.

## Active mitigation

Clever Cloud now adds the `-XX:-UseBASE64Intrinsics` option when it launches a Java application, as recommended by the researchers who found the vulnerability. It disables the affected code: the JVM uses its standard Base64 implementation instead. This can reduce the performance of Base64 encoding and decoding, but shouldn't have a significant impact on most applications.

We are restarting all our customers' instances so they run with it: in this case, you have nothing to do. If you start the JVM yourself, with `CC_RUN_COMMAND` or from another runtime such as Docker or Linux, add the same flag and redeploy:

```bash
CC_RUN_COMMAND="java -XX:-UseBASE64Intrinsics -jar <app>.jar"
```

We will update the Java versions available on Clever Cloud as soon as [Eclipse Temurin](https://adoptium.net/temurin/releases/) publishes its fixed releases.

## Managed and serverless services

Several Clever Cloud services rely on Java and received the same mitigation:

- [Keycloak](/doc/deploy/services/keycloak/), [Metabase](/doc/deploy/services/metabase/) and [Otoroshi](/doc/deploy/services/otoroshi/) add-ons, which run as Java applications
- [Elastic Stack](/doc/deploy/databases/elastic/) add-ons, for Elasticsearch
- [Jenkins](/doc/deploy/services/jenkins/) add-ons
- [Pulsar](/doc/deploy/pulsar/), our serverless messaging service

You have nothing to do for these services.

If you have any questions or need help, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about Java on Clever Cloud](/doc/deploy/applications/java/)
