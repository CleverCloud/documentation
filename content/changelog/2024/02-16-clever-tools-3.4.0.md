---
title: Clever Tools 3.4.0 is available
date: 2024-02-16
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
description: JSON everywhere, create more easily!
aliases:
- /changelog/2024-02-16-clever-tools-3.4.0
excludeSearch: true
---

This week, we published two Clever Tools updates in a row. 3.3.0 was about adding [our new Gravelines HDS region](../02-12-new-grahds-region/) support and fixing a bug in our add-ons logs feature. 3.4.0 brings `json` and `json-stream` formats for applications logs. The latter uses the Newline delimited JSON (NDJSON) specification (`jq` compatible). You can learn more about [ndjson/ndjson-spec/ on GitHub](https://github.com/ndjson/ndjson-spec/blob/master/README.md).

But it's the `create` and `deploy` commands which are the most improved by this release. First, you'll now get the application or add-on name confirmed after creation. You can also get a JSON response adding `--format json` or `-F json` to the `create` or `create-addon` command. Second, the current folder name is now used as default application name if none is provided.

To create a Node.js application once logged in, you can now just:

```
clever create -t node
```

If you need a JSON response for a Go application deployed on Gravelines HDS:

```
clever create --type go --region grahds --format json
```

Last but not least: you can deploy a specific tag from your local git repository adding the `--tag` or `-t` option:

```
clever deploy --tag v0.4.2
```

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install). For example with `npm`:

```
npm update -g clever-tools
clever version
```
