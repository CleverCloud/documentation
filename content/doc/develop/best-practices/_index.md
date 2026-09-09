---
type: docs
weight: 61
linkTitle: Best practices
title: Best practices
description: Learn best practices for deploying and managing applications on Clever Cloud including security, performance, and scalability tips
keywords:
- best-practices
- deployment
- performance
- security
- scalability
- applications
aliases:
- /doc/best-practices
---

Applications behave well on Clever Cloud when they read their configuration from the environment, keep no state on the local disk of an instance, and start fast enough for the platform to replace an instance without a visible interruption. Blue/green deployment and load testing put those properties under pressure before production does.

{{< cards >}}
  {{< card link="/developers/doc/develop/best-practices/blue-green" title="Blue/green deployment" subtitle="Switch traffic between two production environments" icon="traffic-light" >}}
  {{< card link="/developers/doc/develop/best-practices/load-testing" title="Load testing" subtitle="Measure the limits of your application on the platform" icon="chart-bar" >}}
  {{< card link="/developers/doc/develop/best-practices/12-factors" title="The Twelve-Factor App" subtitle="The methodology behind cloud-ready applications" icon="clipboard-list" >}}
{{< /cards >}}
