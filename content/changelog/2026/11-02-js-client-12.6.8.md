---
title: 'JS Client 12.6.8: stream reconnection and invoice links'
description: Clever Cloud JS client 12.6.7 and 12.6.8 rework stream reconnection with onRetry(), remove credentials from invoice URLs and recognize objects from another copy of the client
date: 2026-11-02
tags:
  - client
  - javascript
authors:
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
  - name: Florian Sanders
    link: https://github.com/florian-sanders-cc
    image: https://github.com/florian-sanders-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 12.6.8](https://github.com/CleverCloud/clever-client.js/releases/tag/v12.6.8) is available. Along with 12.6.7, it changes how streams report their reconnections and removes the methods that put credentials in invoice URLs. Both releases require changes in your code if you rely on these features.

## Stream reconnection

`onRetry()` replaces `onError()` and the `error` event of streams. `onError()` was only called when a stream was about to reconnect, never for an error ending it, which still rejects the promise `start()` returns. `onRetry()` is called at the same moment with `{ error, retryCount, maxRetryCount, retryAt }`, and `retryCount` starts at 1. While a stream waits to reconnect, its `state` is now `retrying` instead of `paused`, which now only means you paused it:

```diff
-stream.onError((error) => showReconnecting(error, stream.retryCount + 1));
+stream.onRetry(({ error, retryCount }) => showReconnecting(error, retryCount));

-if (stream.state === 'paused') showReconnecting();
+if (stream.state === 'retrying') showReconnecting();
```

`pause()` now works while a stream connects or waits to reconnect, and cancels the reconnection. The first reconnection waits `initRetryTimeout`, and a stream whose response isn't an event stream fails with `SSE_INVALID_CONTENT_TYPE` once its retries are spent, instead of reconnecting forever.

## Invoice links

`GetInvoiceUrl` and the `getUrl()` method of the clients are removed. They built links carrying credentials in their query string, where they leak into browser history, server logs and `Referer` headers. Fetch the PDF with `GetInvoicePdfCommand`, which authenticates through the `Authorization` header, or the HTML version with `GetInvoiceHtmlCommand`:

```diff
-import { GetInvoiceUrl } from '@clevercloud/client/cc-api-commands/invoice/get-invoice-url.js';
-const url = client.getUrl(new GetInvoiceUrl({ ownerId, invoiceNumber, format: 'pdf' }));
-link.href = url.toString();
+import { GetInvoicePdfCommand } from '@clevercloud/client/cc-api-commands/invoice/get-invoice-pdf-command.js';
+const pdf = await client.send(new GetInvoicePdfCommand({ ownerId, invoiceNumber }));
+link.href = URL.createObjectURL(pdf);
```

## Several copies of the client

An application whose dependencies resolve two versions of `@clevercloud/client` can now send a composite command built with one copy through a client built with the other. Error predicates such as `isCcHttpError()` or `isNetworkError()` also match the errors raised by either copy, as long as both include this release.

## How to upgrade

Update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.6.8
```
