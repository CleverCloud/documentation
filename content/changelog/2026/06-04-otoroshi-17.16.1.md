---
title: Otoroshi 17.16.1 is available with AlphaEdge and OCR support
description: A patch release fixing workflows and OAuth2Caller, shipped with LLM extension 0.0.78 introducing OCR models and the AlphaEdge provider
date: 2026-06-04
tags:
  - addons
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v17.16.1](https://github.com/MAIF/otoroshi/releases/tag/v17.16.1) is available. This patch release fixes the workflow backend response parsing, an `OAuth2Caller` bug where the plugin always tried to read `auth_ref`, and a Monaco editor issue swallowing scroll events. It also cleans up the HTTP client workflow node interface.

This release ships with LLM extension [0.0.78](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.78), which introduces OCR models as a first-class entity alongside audio, image, embedding and moderation models. You can expose them through a dedicated plugin, the unified OpenAI-compatible API or the `ocr_call` workflow function, with Mistral models support. The French provider [AlphaEdge](https://www.alphaedge-ai.com/) joins the extension for both speech transcription, with diarization and linguistic post-correction options, and optical character recognition.

You can update through your add-on dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.16.1_1780575469` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.16.1_1780575469
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
