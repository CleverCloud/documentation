---
type: docs
title: MailPace
shortdesc: MailPace is a fast & Reliable Transactional Email 
tags:
- addons
keywords:
- mailpace
- mail
- email
- smtp
- php mail function
aliases:
- /doc/deploy/addon/mailpace
type: docs
---

MailPace is a fast & Reliable Transactional Email.

## Overview

[MailPace](https://mailpace.com/) is a SMTP provider which can be used on Clever Cloud to send emails.

MailPace provides an HTTPS API, SMTP Server and several libraries for sending emails that completely removes the need for any email setup or active email management. Emails sent through the MailPace API can come from any address for any domain that you are able to verify ownership of through a simple DNS update.

## Add-on configuration

Create the add-on from Clever Cloud's Console. You need to verify you domain name by adding the provided DNS entry in your DNS provider's dashboard. Then, you will get an `API KEY` that you should add to your application (as environment variable with PHP, see section below).

- Host : `smtp.mailpace.com`
- Port : `25`, `465`, `587`, `2525`
- User : `API KEY`
- Password : `API KEY`
- Encryption : usage of `TLS` or `STARTTLS` are highly recommended.

## MailPace for Erlang, Go, Node.js, Rust and Ruby

Check [MailPace documentation](https://docs.mailpace.com/)

## MailPace for PHP

### PHP `mail()` function usage

**You have to turn TLS on with port 465** (environment variable `CC_MTA_SERVER_USE_TLS=true`) to make Mailpace working. Enable `STARTTLS` allows to use another port.

These environment variables have to be set with the value of :

- `CC_MTA_SERVER_HOST`: Host of MailPace's SMTP server is `smtp.mailpace.com`.
- `CC_MTA_SERVER_PORT`: Server port has to be set to `465`. Defaults to `465` whether TLS is enabled or not.
- `CC_MTA_AUTH_USER`: User to authenticate to MailPace's SMTP server has to be set with `MAILPACE_API_KEY`.
- `CC_MTA_AUTH_PASSWORD`: Password to authenticate to the SMTP server has to be set with `MAILPACE_API_KEY`.
- `CC_MTA_SERVER_USE_TLS`: Have to be enabled. Defaults to `true`.
- `CC_MTA_SERVER_STARTTLS`: Enable or disable STARTTLS. Defaults to `false`.
- `CC_MTA_SERVER_AUTH_METHOD`: Authentication has to be enabled. Defaults to `on`.

Then, redeploy your application on Clever Cloud for the changes to take effect. A few minutes later, your application will be able to send mails with `mail()` function thanks to MailPace's SMTP server.

### PHP frameworks

To use frameworks such as Symfony, you can check [MailPace documentation](https://docs.mailpace.com/integrations/php/symfony).
