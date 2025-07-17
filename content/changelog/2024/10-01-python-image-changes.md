---
title: "Python image: what's new and what's to come"
date: 2024-10-01
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: uv, Python 3.13 and some clean up
aliases:
- /changelog/2024-10-01-python-image-changes
excludeSearch: true
---

Python ecosystem is diverse, with lots of legacy versions and practices. But in the recent months, it evolved on many fronts. So, we've decided to handle it and start to revise how you can deploy Python applications on Clever Cloud.

## Package management: uv on Clever Cloud

We only support [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/), `requirements.txt` and `setup.py` natively. For some weeks, we've included [uv](https://docs.astral.sh/uv/getting-started/features/) in our Python image to make some tests. Based on Rust, this package and project manager is compliant with existing ecosystem and blazing fast. [It's now a part](/developers/doc/applications/python/#use-uv-as-a-package-manager) of our "Enthusiast tools" initiative and will be updated regularly. Thus, there is no active support for it yet.

We'll enhance its native support in coming releases of our Python image.

* [Learn more about uv](https://github.com/astral-sh/uv) {{< icon "github" >}}

## Python versions: time to clean up

We're in 2024 and Python 2.x still coexists with Python 3.x. As it's always used by some of our customers, we've decided to continue to support it. Python 3.x is now the default version for new Python applications. We'll make this change for other runtimes (where Python is also included), starting 2025. If you need Python 2.x, set `CC_PYTHON_VERSION=2` in your applications.

We'll also get closer to [the official Python release cycle](https://devguide.python.org/versions/#python-release-cycle), which is 5 years of support. Thus, we'll stop using Python 3.7 starting December 1st, 2024. Next year, we'll deprecate Python 3.8 and stop providing it. If an application is asking for a deprecated version, it will use the latest available by default. So, upgrade your `CC_PYTHON_VERSION` towards your needs.

If you need to sideload unsupported Python versions, `uv` [can help you](https://docs.astral.sh/uv/guides/install-python/). You can also deploy your applications through [Docker](/developers/doc/applications/docker), but you should avoid to use end of life runtime in your applications.

* Learn more about [Python on Clever Cloud](/developers/doc/applications/python/)

## What's next?

We'll enhance our Python images to better support modern Python ecosystem and simplify the deployment process. Python 3.13, [released today](https://docs.python.org/3.13/whatsnew/3.13.html), will be available on Clever Cloud in the coming weeks.

If you have any questions or suggestions, feel free to tell us on [our community page](https://github.com/CleverCloud/Community/discussions/categories/paas-runtimes).
