---
title: "OAuth tokens expiration"
date: 2024-03-12
tags:
  - api
  - security
authors:
  - name: Mathieu Degand
    link: https://github.com/galimede
    image: https://github.com/galimede.png?size=40
  - name: Julien Durillon
    link: https://github.com/judu
    image: https://github.com/judu.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: More security and information for our users
aliases:
- /changelog/2024-03-12-oauth-token-expiration
excludeSearch: true
---

When you connect to Clever Cloud's interfaces, such as API, Console or CLI, you use OAuth tokens. They are now valid for a certain amount of time, and you need to refresh it before it expires.

The duration of the token is 1 year for [Clever Tools](https://github.com/CleverCloud/clever-tools), 3 months for [Console](https://console.clever-cloud.com) and any other integration. The expiration date of the token is mentioned at the time of its creation from CLI, you can also check it from [Console](https://console.clever-cloud.com/users/me/oauth-tokens). You can still revoke tokens at any time from the same (enhanced) page. We'll add such information in future releases of Clever Tools.

Please note that if you ask a member of our support team to access your account, this interface will show their own token, you can revoke, valid for 12 hours. This change is part of our ongoing effort to improve [the security](https://www.clever-cloud.com/security/) of our users' accounts and data. If you have any questions or concerns, please [contact us](https://console.clever-cloud.com/ticket-center-choice).