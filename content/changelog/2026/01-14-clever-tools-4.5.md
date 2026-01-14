---
title: Clever Tools 4.5 is available
date: 2026-01-14
description: Clever Tools 4.5 comes with a rework of the file structure paving the way for future improvements
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
excludeSearch: true
---

[Clever Tools 4.5.1](https://github.com/CleverCloud/clever-tools/releases/tag/4.5.1) is available, with everything [from 4.5.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.5.0) plus a bug fix for Arch Linux users. This release is a big step forward in our CLI redesign, with major changes under the hood to the way commands are structured and implemented.

- [Learn more about Clever Tools file structure rework in our ADR](https://github.com/CleverCloud/clever-tools/blob/master/docs/adr/adr-0001-rework-file-structure.md)

## Better help our users

From a user perspective, this release mainly brings clearer `--help` outputs:

![Clever Tools help output example](/images/clever-tools-4.5-help.webp)

It also allows us to automatically generate [reference documentation](/doc/reference/cli/) during the release process with an [LLM-ready version](/doc/reference/cli/index.html.md).

## Pave the way for future improvements

These changes were an essential building block for the next major step: redesigning the Clever Tools commands and options. An effort that will be carried out gradually over the coming months.

## How to upgrade

To upgrade Clever Tools, [use your favorite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
