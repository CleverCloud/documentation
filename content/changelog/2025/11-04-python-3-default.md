---
title: Python 3 used by default in all our runtimes from December 1st, 2025
description: Time to update or migrate your applications to Python 3 if you are still using Python 2.7
date: 2025-11-04
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Last year](/changelog/2024/10-01-python-image-changes/), we moved the Python runtime default from 2.x to 3.x. Starting December 1st, 2025, Python 3.x will also become the default for all other runtimes. If you still need to use Python 2.7, you must explicitly set `CC_PYTHON_VERSION=2` in your application settings.
