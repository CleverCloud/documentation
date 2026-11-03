---
title: 'JS Client 12.6.6: request cancellation, error reporting and API token creation'
description: Clever Cloud JS client 12.6.5 and 12.6.6 change how aborted requests reject, report each error once and let API token creation resolve refused credentials
date: 2026-10-01
tags:
  - client
  - javascript
authors:
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 12.6.6](https://github.com/CleverCloud/clever-client.js/releases/tag/v12.6.6) is available. Along with 12.6.5, it reworks request cancellation and error reporting, fixes many concurrency issues and lets you tell a wrong password from an expired session when creating an API token.

## Aborted requests

An aborted `send()` now rejects with the reason of its `signal`, as `fetch()` does: a `DOMException` named `AbortError`, unless you gave `abort()` another reason. It used to reject with a `CcRequestError` carrying the `ABORTED` code, which no longer exists. To detect an abort, check the signal you passed:

```diff
 try {
   await client.send(command, { signal });
 } catch (error) {
-  if (isCcRequestErrorWithCode(error, 'ABORTED')) {
+  if (signal.aborted) {
     return;
   }
   throw error;
 }
```

A stream now closes as soon as the `signal` of its request aborts, whatever its state, and `start()` rejects with the same reason. Setting `retry: null` in a stream configuration now disables its retries, and an option set to `undefined` keeps its default value instead of overriding it.

## Error reporting

The `onError` hook is now called once per failed `send()`, never for an error a composite command recovers from, such as the 404 a polling command expects. Errors are named after their class, such as `CcHttpError` or `CcNetworkError`, instead of `Error`. Concurrent requests and streams sharing the same URL no longer fail together when one of them is aborted, and streams reconnect in Firefox when the server cuts the connection.

## API token creation

A wrong password or MFA code makes `CreateApiTokenCommand` reject with a 401, which reaches the `onError` hook of `CcApiBridgeClient` and can read as an expired session. Set `shouldResolveRefusedCredential: true` to get it as a result instead: the output `type` is then `created`, `invalid-credential` or `invalid-mfa-code`.

```javascript
const result = await client.send(new CreateApiTokenCommand({ ...input, shouldResolveRefusedCredential: true }));
if (result.type === 'created') {
  store(result.apiToken);
}
```

## How to upgrade

Update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.6.6
```
