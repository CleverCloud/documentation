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
- /doc/account-setup
- /doc/account/create-account
- /doc/account/delete-account
- /doc/account/manage-account
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

### 🔐 Two Factor Authentication (2FA)

Clever Cloud supports 2FA. You can enable it here: <https://console.clever-cloud.com/users/me/authentication>

Please, backup your recovery codes, we won't be able to restore access to your account if you lose access to your regular codes.

## Manage your account

In the Clever Cloud Web Console, select **Profile** in the bottom left menu.

You see several menu entries.

- **Information**: on that page you can edit your name, address, phone number, profile picture, manage the link between your Clever Cloud and GitHub account and select the language of your Clever Cloud web console.
- **Emails**: manage your linked email addresses.
- **Authentication**: Change your password, enable or turn off Two Factor Authentication.
- **SSH keys**: add or remove your SSH keys, manage your GitHub SSH keys if you have linked your GitHub account.
- **Oauth tokens**: See and revoke your access tokens
- **Delete my account**: Delete your Clever Cloud account

## Delete your account

To delete your account:

1. Open the Clever Cloud Web Console.
2. Select **Profile** in the bottom left menu.
3. Select **Delete my account** in the top menu of the freshly opened page.
4. Click the red **Send me a confirmation email** button.

You will get an email with a link you must click to confirm your account deletion.
