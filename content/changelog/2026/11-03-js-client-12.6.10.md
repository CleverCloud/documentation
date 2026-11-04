---
title: 'JS Client 12.6.10: stream reconnection, invoice links and second factor'
description: Clever Cloud JS client 12.6.7 to 12.6.10 rework stream reconnection with onRetry(), remove credentials from invoice URLs, return multi-factor authentication (MFA) backup codes once and reject account security commands with named error codes
date: 2026-11-03
tags:
  - client
  - javascript
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
aliases:
  - /changelog/2026/11-02-js-client-12.6.8/
excludeSearch: true
---

[Clever Cloud JS client 12.6.10](https://github.com/CleverCloud/clever-client.js/releases/tag/v12.6.10) is available. Along with 12.6.7 to 12.6.9, it changes how streams report their reconnections, removes the methods that put credentials in invoice URLs and reworks the commands managing multi-factor authentication (MFA) and the password of an account. These releases require changes in your code if you rely on these features.

## Stream reconnection

`onRetry()` replaces `onError()` and the `error` event of streams. Streams only called `onError()` when they were about to reconnect, never for an error ending them, which still rejects the promise `start()` returns. They now call `onRetry()` at the same moment with `{ error, retryCount, maxRetryCount, retryAt }`, and `retryCount` starts at 1. While a stream waits to reconnect, its `state` is now `retrying` instead of `paused`, which now only means you paused it:

```diff
-stream.onError((error) => showReconnecting(error, stream.retryCount + 1));
+stream.onRetry(({ error, retryCount }) => showReconnecting(error, retryCount));

-if (stream.state === 'paused') showReconnecting();
+if (stream.state === 'retrying') showReconnecting();
```

`pause()` now works while a stream connects or waits to reconnect, and cancels the reconnection. The first reconnection waits `initRetryTimeout`, and a stream whose response isn't an event stream fails with `SSE_INVALID_CONTENT_TYPE` once its retries are spent, instead of reconnecting forever.

## Invoice links

These releases remove `GetInvoiceUrl` and the `getUrl()` method of the clients. They built links carrying credentials in their query string, where they leak into browser history, server logs and `Referer` headers. Fetch the PDF with `GetInvoicePdfCommand`, which authenticates through the `Authorization` header, or the HTML version with `GetInvoiceHtmlCommand`:

```diff
-import { GetInvoiceUrl } from '@clevercloud/client/cc-api-commands/invoice/get-invoice-url.js';
-const url = client.getUrl(new GetInvoiceUrl({ ownerId, invoiceNumber, format: 'pdf' }));
-link.href = url.toString();
+import { GetInvoicePdfCommand } from '@clevercloud/client/cc-api-commands/invoice/get-invoice-pdf-command.js';
+const pdf = await client.send(new GetInvoicePdfCommand({ ownerId, invoiceNumber }));
+link.href = URL.createObjectURL(pdf);
```

## MFA backup codes

The API now shows the backup codes of a second factor only once, when it issues them. `ConfirmAuthMfaCommand` returns them when it turns the factor on, instead of `undefined`: save them or show them to the user right away. `GetAuthMfaBackupCodesCommand` no longer exists. `GetAuthMfaCommand` tells whether a factor is on and how many backup codes are left, without asking for the password. `ResetAuthMfaBackupCodesCommand` replaces the codes with a new set, which invalidates the previous one:

```diff
-import { GetAuthMfaBackupCodesCommand } from '@clevercloud/client/cc-api-commands/auth/get-auth-mfa-backup-codes-command.js';
-const backupCodes = await client.send(new GetAuthMfaBackupCodesCommand({ kind: 'TOTP', password }));
+import { ResetAuthMfaBackupCodesCommand } from '@clevercloud/client/cc-api-commands/auth/reset-auth-mfa-backup-codes-command.js';
+const { backupCodes } = await client.send(new ResetAuthMfaBackupCodesCommand({ kind: 'TOTP', password }));
```

Call `ResetAuthMfaBackupCodesCommand` only when the user asks for a new set of codes. If the response of `ConfirmAuthMfaCommand` gets lost, replaying it rejects with `clever.auth.mfa-enrolment-not-found`, although the factor is on: check `GetAuthMfaCommand`, then offer to generate new backup codes.

## MFA and password errors

`CreateAuthMfaCommand`, `ConfirmAuthMfaCommand`, `DeleteAuthMfaCommand`, `RequestAuthPasswordResetCommand` and `UpdateAuthPasswordCommand` now reject with named error codes, such as `clever.auth.invalid-password` or `clever.auth.invalid-mfa-code`, instead of the raw numeric IDs of the API. Each command exports them as constants, such as `CONFIRM_AUTH_MFA_ERROR_CODES`. `UpdateAuthPasswordCommand` now tells a wrong current password from an invalid new one, and rejects with `clever.auth.password-not-set` for an account that has no password yet, such as one created through an OAuth provider. Such an account sets its first password with `RequestAuthPasswordResetCommand`.

As `CreateApiTokenCommand` already does, the MFA commands asking for the password accept `shouldResolveRefusedCredential: true`. A wrong password, or a wrong code for `ConfirmAuthMfaCommand`, then resolves as a result without reaching the `onError` hook, where the 401 of a wrong password can read as an expired session:

```javascript
const result = await client.send(
  new CreateAuthMfaCommand({ kind: 'TOTP', password, shouldResolveRefusedCredential: true }),
);
if (result.type === 'invalid-password') {
  askForThePasswordAgain();
}
```

## Several copies of the client

An application whose dependencies resolve two versions of `@clevercloud/client` can now send a composite command built with one copy through a client built with the other. Error predicates such as `isCcHttpError()` or `isNetworkError()` also match the errors raised by either copy, as long as both include 12.6.8 or later.

## How to upgrade

Update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.6.10
```
