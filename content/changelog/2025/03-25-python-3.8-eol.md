---
title: "Python 3.8 end of life"
description: Python 3.9 is next, prepare to Python 3.14 update
date: 2025-03-25
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[As announced last year](/developers/changelog/2024/10-01-python-image-changes/), our new update process is getting closer to [the official Python release cycle](https://devguide.python.org/versions/#python-release-cycle), which is 5 years of support. Starting April 30th, we'll remove Python 3.8, released in 2019 and end-of-life since last October, from our images.

To upgrade to a more recent version of Python, you only need to update `CC_PYTHON_VERSION` of your applications and rebuild them. Use `3` as value to always get the latest release available on Clever Cloud.

If you need to keep Python 3.8 for legacy reasons, you can [use uv](https://docs.astral.sh/uv/guides/install-python/#installing-a-specific-version) or [Mise](https://mise.jdx.dev/lang/python.html) which are available in all our recently updated images.

* [Learn more about Python on Clever Cloud](/developers/doc/applications/python/)
* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)
