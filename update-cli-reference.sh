#!/bin/bash

FILE="content/doc/reference/cli.md"
URL="https://raw.githubusercontent.com/CleverCloud/clever-tools/refs/heads/davlgd-ai-doc/docs/llms-documentation.md"

front_matter="""---
type: docs
linkTitle: CLI reference
title: Clever Tools - CLI commands reference
description: Clever Tools commands reference to create and manage Clever Cloud applications, add-ons and services. Ideal to provide to LLMS and AI assisted IDEs.
comments: false
aliases:
- /doc/reference/clever-tools/configure
---
"""

echo "${front_matter}" > "${FILE}"
curl -fSL "${URL}" >> "${FILE}"
