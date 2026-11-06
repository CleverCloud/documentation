---
title: "Console logs: reconnection status, shareable filters, and clear button"
description: The logs interface of the Console shows when it reconnects to the logs stream, keeps its message filter in the URL, and clears the displayed lines on demand
date: 2026-10-26
tags:
  - console
  - logs
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The logs interface of the [Clever Cloud Console](https://console.clever-cloud.com), used for application, access, and add-on logs, now shows its reconnections. When the connection to the logs stream drops, the interface no longer looks stuck. It shows that it's reconnecting, with the number of the current attempt out of the maximum.

The message filter also lives in the URL of the page, in the `filter` and `filterMode` parameters. It survives a page reload, each browser tab keeps its own, and you can share a link to a filtered view with your team. A `Clear logs` button empties the view, to focus on the lines that come next during a long session.

- [Learn more about logs on Clever Cloud](/doc/observability/logs/)
