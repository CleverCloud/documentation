---
title: oTree
description: The most powerful platform for behavioral research and experiment, hosted on Clever Cloud.
tags:
- guides
keywords:
- otree
- python
type: "docs"
comments: false
draft: false
---

{{< hextra/hero-subtitle >}}
The most powerful platform for behavioral research and experiments.
{{< /hextra/hero-subtitle >}}

## Deploy oTree

oTree runs using:
- a **Python** application for the web and the worker
- a **PostgreSQL** database for the storage

If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and [pip](https://pip.pypa.io/en/stable/installation/)):

```bash
# Use pip or pip3 depending on your system
pip install otree
otree startproject myproject
```

### Deploy the Python application

{{% steps %}}

#### Create a PostgreSQL add-on

#### Create a Python application

Select at least an `XS` plan, then link the PostgreSQL add-on to it.

Inject the following environment variables
```env
CC_PYTHON_VERSION="3"
CC_RUN_COMMAND="otree prodserver 9000"
DATABASE_URL="<the postgresql URL from the previously defined add-on>"
OTREE_ADMIN_PASSWORD="<enter your password>"
OTREE_AUTH_LEVEL="DEMO"
OTREE_PRODUCTION="1"
```
{{% /steps %}}
