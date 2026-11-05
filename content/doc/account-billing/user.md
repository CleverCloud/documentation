---
type: docs
weight: 231
linkTitle: Account
title: Account
description: Create, configure and delete your Clever Cloud account, from sign-up methods to two-factor authentication and account removal
keywords:
- account
- user
- profile
- signup
- authentication
- 2fa
aliases:
- /account
- /doc/account-billing/account
- /doc/account-setup
- /doc/account/create-account
- /doc/account/delete-account
- /doc/account/manage-account
- /doc/account/user-account
- /doc/admin-console/authentification
- /doc/getting-started/authentication
---

Your Clever Cloud account identifies you on the platform and owns the organisations you belong to. This page covers creating it, configuring it and deleting it.

## Create an account

The API of Clever Cloud uses OAuth 1 to perform authentication actions.
There are two ways to sign up to Clever Cloud: **email** or **GitHub login**.

### Email

This kind of auth requires a valid and non-temporary disposable e-mail, and a password having at least 6 characters.

Do not forget to validate your email by clicking the link you will receive.

### GitHub

The GitHub signup allows you to create an account or link your existing one to GitHub, in one click.

This process asks the following permissions:

- Read your Public Key
- Read User Repositories

The "repository permission" is used to deploy your GitHub apps directly to Clever Cloud, with a simple step.

If you need to give access to Clever Cloud's API to a specific GitHub organisation, you
can [do it here](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

Go to the [Clever Cloud Console](https://console.clever-cloud.com/) and select the method you prefer.

### Two-factor authentication (2FA)

Two-factor authentication asks for a code from an authenticator app when you sign in, in addition to your password. To enable it, open the [Authentication](https://console.clever-cloud.com/users/me/authentication) page of your profile, select `Enable 2FA`, and enter your password. Scan the QR code with your authenticator app, or enter the key the dialog gives instead. Then type the 6-digit code the app generates. By default, enabling 2FA revokes your other tokens and sessions, such as those of Clever Tools, but not your current Console session. Clear the checkbox in the dialog to keep them.

2FA requires a verified email address and a password. An account created with GitHub may have no password: the Authentication page then offers to email you a link to create one.

Once 2FA is on, the Console shows your recovery codes. Each code lets you sign in once if you lose access to your authenticator app. They're shown only this once: copy or download them and store them somewhere safe, such as a password manager. Clever Cloud can't restore access to your account if you lose both your authenticator app and your recovery codes.

The Authentication page then tells how many recovery codes you have left. Select `Regenerate recovery codes` to get a new set, shown once the same way: the previous codes stop working. Regenerate them before you run out. To turn 2FA off, select `Disable 2FA`. Both actions ask for your password.

## Manage your account

In the Clever Cloud Web Console, open the profile menu at the top right of the header, then select **Profile**.

Tabs give access to the pages of your account:

- **Profile**: edit your name, address, phone number, and profile picture. You can also manage the link between your Clever Cloud and GitHub accounts, and select the language of the Console.
- **Emails**: manage your linked email addresses.
- **SSH Keys**: add or remove your SSH keys, manage your GitHub SSH keys if you have linked your GitHub account.
- **Authentication**: change your password, or create one if your account has none, and manage two-factor authentication and its recovery codes.
- **API tokens**: create, edit, and revoke your API tokens.
- **Console sessions**: see and revoke your active Console sessions.
- **OAuth tokens**: See and revoke your access tokens
- **Labs**: enable features in beta, such as Clever Kubernetes Engine, and pick a color theme for the Console.
- **Delete my account**: Delete your Clever Cloud account

## Delete your account

To delete your account:

1. Open the Clever Cloud Web Console.
2. Open the profile menu at the top right of the header, then select **Profile**.
3. Select the **Delete my account** tab.
4. Click the **Confirm the account deletion request** button.

You get an email with a link you must click to confirm your account deletion.

If you're the last admin of an organisation that has other members, appoint a new admin first. Until then, the Console lists these organisations and doesn't let you delete your account.
