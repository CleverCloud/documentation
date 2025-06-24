---
title: 'API tokens in Console… with API and Clever Tools tips'
date: 2025-06-05
tags:
  - console
  - tokens
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Florian Sanders
    link: https://github.com/florian-sanders-cc
    image: https://github.com/florian-sanders-cc.png?size=40
description: API tokens and tips everywhere!
excludeSearch: true
---

With [Clever Tools 3.12](/developers/changelog/2025/03-07-clever-tools-3.12/), we've introduced a new way to query Clever Cloud's API, with [the API bridge and API tokens](/developers/api/howto/#api-tokens). Starting today, you can create, edit and revoke API tokens directly [from your Clever Cloud profile page](https://console.clever-cloud.com/users/me/api-tokens).

## API tokens in the Clever Cloud Console

This interface also shows the token name, description, public ID, creation and expiration date.

To create an API token, you need to provide:

- Your current password
- Your 2FA code if active (activate it [here](https://console.clever-cloud.com/users/me/authentication))

If you created your Clever Cloud account through the GitHub integration, you'll be asked to set a password first.

![Manage API tokens in Clever Cloud Console](/images/changelog/console-api-tokens.webp)

## Clever Tools and API tips in the Console

This interface also introduces a new [Web Component](https://www.clever-cloud.com/developers/clever-components) to show Clever Tools commands and API requests related to the page you visit. In the coming weeks, we'll add more of these tips over the Clever Cloud Console.

![API Tokens API & Clever Tools Tips](/images/changelog/console-api-tokens-tips.webp)
