---
type: docs
weight: 60
linkTitle: MailPace
title: Send transactional emails with MailPace
description: Send your application's transactional emails from your own domain with the MailPace add-on, over its HTTP API or SMTP
keywords:
- mailpace
- transactional email
- smtp
- email api
- php mail
- dkim
aliases:
- /doc/addons/mailpace
- /doc/deploy/addon/mailpace
- /doc/services/mailpace
---

[MailPace](https://mailpace.com/) sends your application's transactional emails, such as password resets or notifications, from a domain you own. Your application sends them over the MailPace HTTP API or SMTP, from any language. MailPace doesn't accept newsletters or bulk marketing emails.

## Create the add-on

In the [Console](https://console.clever-cloud.com), create a MailPace add-on, choose its plan, then link it to your applications. Plans set the number of emails per month, from 1,000 with the Solo plan. With [Clever Tools](/doc/manage/cli/), from a folder linked to your application, set its alias with `--link`:

```bash
clever addon create mailpace my-mail --plan clever_solo --link my-app
clever restart
```

The add-on is then created in the organisation of the application and linked to it. The linked applications receive the API key of the add-on in `MAILPACE_API_KEY`. Linking an add-on doesn't redeploy an application: restart it to receive the variable.

## Verify your domain

MailPace only sends emails once it has verified your domain. Open the **Dashboard** tab of the add-on in the Console and enter your domain. MailPace then shows a DKIM record to create at your DNS provider: a `TXT` record named `ohmysmtp._domainkey`, with the provided contents. Once it's published, click **Verify** followed by your domain name. MailPace indicates that verification can take up to 48 hours after the DNS update.

Until then, MailPace refuses each email with `Domain DKIM DNS not verified, please complete DKIM Verification`. It also refuses a `From` address outside the domain of the API key. To also set a custom Return-Path, follow the [MailPace verification guide](https://docs.mailpace.com/guide/verification/).

## Send with the HTTP API

Send an email with a `POST` request to the MailPace API, with the API key in the `MailPace-Server-Token` header. From your application, `MAILPACE_API_KEY` is already set. Replace the sender with an address on your verified domain, and the recipient with your test mailbox:

```bash
curl -X POST https://app.mailpace.com/api/v1/send \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "MailPace-Server-Token: $MAILPACE_API_KEY" \
  -d '{"from":"hello@example.com","to":"customer@example.org","subject":"Welcome","textbody":"Thanks for signing up."}'
```

MailPace answers `{"id":49593530,"status":"queued"}`: it accepted the email, which doesn't yet mean the recipient received it. The [API reference](https://docs.mailpace.com/reference/send/) describes the other fields, such as `htmlbody` or attachments. To retry a request without sending the email twice, reuse the same [`Idempotency-Key`](https://docs.mailpace.com/guide/idempotency/) with the same API key within 24 hours.

## Send over SMTP

Configure your application or its email library with these settings:

| Setting               | Value                                                   |
| --------------------- | ------------------------------------------------------- |
| Host                  | `smtp.mailpace.com`                                     |
| Port and encryption   | `465` with TLS, or `587`, `2525`, or `25` with STARTTLS |
| Username and password | The value of `MAILPACE_API_KEY`, for both               |

The `From` address of each email must use your verified domain.

## Send from your application

Use an SMTP library with the settings above, or one of the MailPace libraries. In these examples, use the value of `MAILPACE_API_KEY` as the API key, replace the sender with an address on your verified domain, and the recipient with your test mailbox:

{{< tabs >}}

{{< tab name="Go" icon="simple:go" >}}

In your Go module, add the [MailPace package](https://docs.mailpace.com/integrations/go/) with `go get github.com/mailpace/gomailpace`, then send an email through the API:

```go
package main

import (
    "context"
    "log"
    "os"

    "github.com/mailpace/gomailpace"
)

func main() {
    client := gomailpace.NewClient(os.Getenv("MAILPACE_API_KEY"))
    err := client.Send(context.Background(), gomailpace.Payload{
        From:     "hello@example.com",
        To:       "customer@example.org",
        Subject:  "Welcome",
        TextBody: "Thanks for signing up.",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

{{< /tab >}}

{{< tab name="Node.js" icon="simple:nodedotjs" >}}

Install the [MailPace library](https://docs.mailpace.com/integrations/javascript/node/) with `npm install @mailpace/mailpace.js`, then send an email through the API from an ES module:

```javascript
import { DomainClient } from "@mailpace/mailpace.js";

const client = new DomainClient(process.env.MAILPACE_API_KEY);

await client.sendEmail({
  from: "hello@example.com",
  to: "customer@example.org",
  subject: "Welcome",
  textbody: "Thanks for signing up.",
});
```

{{< /tab >}}

{{< tab name="PHP" icon="php" >}}

PHP applications on Clever Cloud can send emails with the `mail()` function, through the SMTP server set in the `CC_MTA_*` variables. To use MailPace, set its host and the value of `MAILPACE_API_KEY` as username and password, then restart the application:

```bash
clever env set CC_MTA_SERVER_HOST smtp.mailpace.com
clever env set CC_MTA_AUTH_USER "your-api-key"
clever env set CC_MTA_AUTH_PASSWORD "your-api-key"
clever restart
```

These variables use port `465` with TLS by default:

```php
<?php
mail('customer@example.org', 'Welcome', 'Thanks for signing up.', 'From: hello@example.com');
```

`mail()` returns `true` once MailPace accepts the email. To use port `587` instead, set `CC_MTA_SERVER_PORT=587`, and both `CC_MTA_SERVER_USE_TLS=true` and `CC_MTA_SERVER_STARTTLS=true`: with STARTTLS alone, the connection stays unencrypted and `mail()` fails. The [PHP emails page](/doc/deploy/applications/php/sessions-emails/#configure-the-smtp-server) lists all the variables.

Symfony and Laravel can use the `symfony/mail-pace-mailer` bridge, as the MailPace guides for [Symfony](https://docs.mailpace.com/integrations/php/symfony/) and [Laravel](https://docs.mailpace.com/integrations/php/laravel/) explain.

{{< /tab >}}

{{< tab name="Python" icon="simple:python" >}}

The `smtplib` module of the standard library sends emails over SMTP:

```python
import os
import smtplib
import ssl
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "hello@example.com"
msg["To"] = "customer@example.org"
msg["Subject"] = "Welcome"
msg.set_content("Thanks for signing up.")

key = os.environ["MAILPACE_API_KEY"]
with smtplib.SMTP_SSL("smtp.mailpace.com", 465, context=ssl.create_default_context()) as smtp:
    smtp.login(key, key)
    smtp.send_message(msg)
```

{{< /tab >}}

{{< tab name="Ruby" icon="ruby" >}}

The `net-smtp` gem sends emails over SMTP. With Bundler, add `gem "net-smtp"` to your `Gemfile` and run `bundle install`:

```ruby
require "net/smtp"

key = ENV.fetch("MAILPACE_API_KEY")
message = <<~MAIL
  From: hello@example.com
  To: customer@example.org
  Subject: Welcome

  Thanks for signing up.
MAIL

Net::SMTP.start("smtp.mailpace.com", 465, tls: true, user: key, secret: key) do |smtp|
  smtp.send_message(message, "hello@example.com", "customer@example.org")
end
```

Rails applications can use the [`mailpace-rails` gem](https://docs.mailpace.com/integrations/rails/) with Action Mailer.
{{< /tab >}}

{{< tab name="Rust" icon="simple:rust" >}}

Add the [`lettre`](https://crates.io/crates/lettre) crate with `cargo add lettre`. Its `relay()` transport connects to port `465` with TLS:

```rust
use lettre::transport::smtp::authentication::Credentials;
use lettre::{Message, SmtpTransport, Transport};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let email = Message::builder()
        .from("hello@example.com".parse()?)
        .to("customer@example.org".parse()?)
        .subject("Welcome")
        .body(String::from("Thanks for signing up."))?;

    let key = std::env::var("MAILPACE_API_KEY")?;
    let mailer = SmtpTransport::relay("smtp.mailpace.com")?
        .credentials(Credentials::new(key.clone(), key))
        .build();

    mailer.send(&email)?;
    Ok(())
}
```

{{< /tab >}}

{{< /tabs >}}

The [MailPace documentation](https://docs.mailpace.com/) covers the libraries for other languages.

## Track your emails

Open the **Dashboard** tab of the add-on to review the emails your applications sent and their statuses. To receive these statuses in your application, configure [MailPace webhooks](https://docs.mailpace.com/guide/webhooks/): `delivered` means the server of the recipient accepted the email, not that it reached the inbox.
