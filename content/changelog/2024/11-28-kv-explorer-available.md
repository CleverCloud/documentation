---
title: "Clever Cloud KV Explorer is available for Materia KV and Redis® add-ons"
date: 2024-11-28
tags:
- addons
- kv
authors:
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Lot of changes, just an environment variable to update
aliases:
- /changelog/2024-11-28-kv-explorer-available
excludeSearch: true
---

Since we've launched [Materia KV](https://www.clever-cloud.com/materia/materia-kv/), our serverless key-value database compatible with third-party protocols such as Redis® (and soon DynamoDB or GraphQL), customers were asking about a way to explore data directly from the Clever Cloud Console. This summer, we started to work on such a project, to provide a pleasant and easy-to-use interface, not only for Materia KV, but for any key-value add-on. After some months of internal alpha testing, it's available in Beta for all our Materia KV and Redis® add-ons.

To use it, just open the `KV Explorer` tab of any compatible add-on, it's part of the Clever Cloud experience. This first public iteration supports hash, list, set and string data types, only strings for Materia KV add-ons as other types are yet to come.

![KV Explorer](/images/doc/kv-explorer.webp "The KV Explorer tool in the Console")

You can filter keys by type, with a filter (`*value_to_search*` for example), value text fields are multi-lines, and you can copy/paste values directly from the interface. As usual, we've worked on keyboard shortcuts and accessibility. At the bottom, the KV Explorer Terminal allows you to type any command you want as you would do in a CLI client. It works the same, you type a command, press Enter, and you get the result (yes, also when you type `FLUSHDB` or `FLUSHALL`, so be careful).

Of course, we'll continue to improve this tool, over the coming months, thanks to your feedback and suggestions. So feel free to share them and ask your questions in our [GitHub Community](https://github.com/CleverCloud/Community/discussions/categories/kv-explorer).

- [Learn more about Materia KV](/developers/doc/addons/materia-kv/)
- [Learn more about Redis® on Clever Cloud](/developers/doc/addons/redis/)
