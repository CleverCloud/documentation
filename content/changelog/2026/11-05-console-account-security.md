---
title: "Console: recovery codes shown once, and a password for accounts created with GitHub"
description: The Authentication page of the Console shows two-factor authentication recovery codes only once, counts those left and regenerates them, and lets an account without a password create one. Logging out now revokes the session
date: 2026-11-05
tags:
  - console
  - security
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [Authentication](https://console.clever-cloud.com/users/me/authentication) page of your profile in the [Clever Cloud Console](https://console.clever-cloud.com) changes how it handles the recovery codes of two-factor authentication (2FA). You can now get a new set at any time.

## Recovery codes shown once

When you enable 2FA, the Console shows your recovery codes in a window, only this once. Copy them or download them as a text file, and store them somewhere safe such as a password manager. Then confirm you saved them: it's the only way to close the window. Each code lets you sign in once if you lose access to your authenticator app.

Once 2FA is on, the page tells how many codes you have left. `Regenerate recovery codes` replaces them with a new set, shown once the same way, and the previous codes stop working. When you have a single code left or none, a warning asks you to regenerate them. Enabling or disabling 2FA and regenerating the codes ask for your password.

## Accounts without a password

An account created with GitHub may have no password, which 2FA requires. The page used to show it a password change form it couldn't use. It now offers to send a link to the email address of the account to create one, without ending your Console session. Once you set the password, the page shows the password and 2FA blocks, without a reload.

## Logout and invoices

The `Logout` button of the Console header now asks the API to revoke your session token. It used to only remove the token from your browser. Invoice PDF links, in the invoice list and on the payment page, go through the Console server. They no longer put a token in the URL.

- [Learn more about two-factor authentication](/doc/account-billing/user/#two-factor-authentication-2fa)
- [Handle the recovery codes in your own tools with the JS client](/changelog/2026/11-03-js-client-12.6.10/#mfa-backup-codes)
