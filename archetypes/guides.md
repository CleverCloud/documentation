---
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
description:
tags:
- guides
keywords:
-

draft: true
type: docs
---

{{< hextra/hero-subtitle >}}
  Framework short description.
{{< /hextra/hero-subtitle >}}

## Overview

Macro description of the needed setup (type of runtime, possible add-ons) to deploy <framework> on Clever Cloud.

If you need an example source code, get [Example application](https://github.examplec.com/something/framework) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)):
```bash
git clone https://github.example.com/something/framework myApp
```

## How to Configure and Deploy [...] on Clever Cloud

{{% steps %}}

{{% content/guides/create-application framework="<framework> runtime="Node" flavor="nano" %}}

{{< content/guides/set-environment >}}
CC_VARIABLE="value"
{{< /content/guides/set-environment >}}

{{% content/guides/deploy-application %}}

###

{{% /steps %}}

## 🎓 Further Help

{{< cards >}}
  {{< card link="" title="Card title" subtitle="Card subtiltle" icon="adjustments-horizontal" >}}
{{< /cards >}}
