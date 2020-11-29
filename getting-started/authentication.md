---
title: Authentication
position: 1
shortdesc: How to be authenticated on Clever Cloud
tags:
- account-setup
keywords:
- auth
- authentication
- github
- 2FA
- two factor authentication
---

# Authentication On Clever Cloud

The API of Clever Cloud uses OAuth 1 to perform authentication actions.
There are two ways to signup to Clever Cloud: email or GitHub login.

## Email Authentication

This kind of auth requires a valid and non-temporary disposable e-mail, and a password having at least 6 characters.

## GitHub Authentication

The GitHub signup allows you to create an account or link your existing one to GitHub, in one click.
This process asks the following permsissions: 

* Read your Public Key
* Read User Repositories

The "repository permission" is used to deploy your GitHub apps directly to Clever Cloud, with a simple step.

If you need to give access to Clever Cloud's API to a specific GitHub organization, you
can [do it here](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

## Two Factor Authentication (2FA)

Clever Cloud supports 2FA. You can enable it here: https://console.clever-cloud.com/users/me/authentication

Please, backup your recovery codes, we won't be able to restore access to your account if you lose access to
your regular codes.
