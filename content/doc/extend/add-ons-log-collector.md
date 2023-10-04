---
title: Add-on Log Collector
position: 3
shortdesc: This article targets the add-on providers who want to integrate logs from their add-ons to Clever Cloud's logging system
tags:
- extend
keywords:
- log
- log collection
type: docs
---
This article targets the add-on providers who want to integrate logs
from their add-ons to Clever Cloud's logging system. Doing this
allows the users to get their add-on's logs in Clever Cloud's
dashboard.

## Send a line of log

Log lines must be sent via https. See the following example with the `curl` command:

```bash
$ curl -X POST "https://logs.cleverapps.io/logs" \
  --user "token:logtoken_foobar" \
  -d "72 <190>1 2013-03-27T20:02:24+00:00 hostname logtoken_foobar procid - - foo72 <190>1 2013-03-27T20:02:24+00:00 hostname logtoken_foobar procid - - bar" \
  -H "Content-Length: 150" \
  -H "Content-Type: application/logplex-1"
```

Let's explain this request:

* `-X POST` - This request is obvioulsy a POST one, since you need to send new data.

* `--user token:logtoken_foobar` - This is the basic authentication content. The user must be the string 'token', and the password must be your log token, as sent on a provisioning call.

* `Content-Length: 150` - Length of the body. Must be set.

* `Content-Type: application/logplex-1` - This is the expected content type.

* `72 <190>1 2013-03-27T20:02:24+00:00 hostname logtoken_foobar procid - - foo` - This a a log line. It is expected to respect the RFC 5424 notation. You can send multiple log lines in one request. Here is the log line decrypted:

```bash
length <prival>version time hostname logtoken procid msgid structured-data msg
```

This message format is documented by the [RFC 5424](https://tools.ietf.org/html/rfc5424).

* `length` - 72 in the example. It is the length *in bytes* of the encoded log line minus the length field and the following space. It *is not* the number of chars. In our example, this is how it could be done in java:
```text
("<190>1 2013-03-27T20:02:24+00:00 " +
"hostname logtoken_foobar procid - - foo").getBytes().length
```

* `prival` - The priority value of the message. Here `190` means "local7.info". ([More doc](https://tools.ietf.org/html/rfc5424#section-6.2.1))

* `version` - The syslog protocol version. Use `1` here. ([More doc](https://tools.ietf.org/html/rfc5424#section-6.2.2))

* `time` - The time the log line was created. The format must follow the [RFC 3339](https://tools.ietf.org/html/rfc3339). ([More doc](https://tools.ietf.org/html/rfc5424#section-6.2.3))

* `hostname` - Make it your add-on id.

* `logtoken` - The same token as in the Basic authentication password.

* `procid` - Id of the process emitting the log. Not really used by the log collector since it's more relevant for you to use in your own log system to debug processes.

* `msgid` - Not used, should be `-`.

* `structured-data` - Not used, should be `-`.
