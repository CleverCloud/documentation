---
type: docs
weight: 1
linkTitle: Create an Account
title: Create an Account
description: Step-by-step guide to create your Clever Cloud account and start deploying applications on the cloud platform efficiently
keywords:
- account creation
- user registration
- github oauth
- clever cloud signup
- authentication
- email verification
aliases:
- /doc/account-setup
- /doc/getting-started/authentication
---


The API of Clever Cloud uses OAuth 1 to perform authentication actions.
There are two ways to sign up to Clever Cloud: **email** or **GitHub login**.

## Email

This kind of auth requires a valid and non-temporary disposable e-mail, and a password having at least 6 characters.

Do not forget to validate your email by clicking the link you will receive.

## GitHub

The GitHub signup allows you to create an account or link your existing one to GitHub, in one click.

This process asks the following permissions:

* Read your Public Key
* Read User Repositories

The "repository permission" is used to deploy your GitHub apps directly to Clever Cloud, with a simple step.

If you need to give access to Clever Cloud's API to a specific GitHub organisation, you
can [do it here](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

Go to the [Clever Cloud Console](https://console.clever-cloud.com/) and select the method you prefer.

### 🔐 Two Factor Authentication (2FA)

Clever Cloud supports 2FA. You can enable it here: <https://console.clever-cloud.com/users/me/authentication>

Please, backup your recovery codes, we won't be able to restore access to your account if you lose access to your regular codes.
