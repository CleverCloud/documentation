---
type: docs
linkTitle: Best practices
title: Best practices
description: Build applications that behave well on Clever Cloud immutable instances, reduce the risks of a deployment, and measure their limits
keywords:
- best-practices
- immutable infrastructure
- deployment
- performance
- scalability
- applications
aliases:
- /doc/best-practices
---

Applications behave well on Clever Cloud when they follow its immutable model: the platform replaces instances rather than updating them, so configuration and data live outside of them. Blue/green deployment and load testing put these properties under pressure before production does.

{{< cards >}}
  {{< card link="/developers/doc/develop/best-practices/blue-green" title="Blue/green deployment" subtitle="How each deployment switches traffic, and how to roll back" icon="traffic-light" >}}
  {{< card link="/developers/doc/develop/best-practices/immutable-infrastructure" title="Immutable infrastructure" subtitle="Why Clever Cloud replaces instances, and what persists" icon="arrow-path" >}}
  {{< card link="/developers/doc/develop/best-practices/load-testing" title="Load testing" subtitle="Measure the limits of your application on the platform" icon="chart-bar" >}}
  {{< card link="/developers/doc/develop/best-practices/12-factors" title="The Twelve-Factor App" subtitle="The methodology behind cloud-ready applications" icon="clipboard-list" >}}
{{< /cards >}}
