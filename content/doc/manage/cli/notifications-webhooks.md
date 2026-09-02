---
type: docs
linkTitle: Notifications, WebHooks
title: Notifications, WebHooks
description: Configure notifications and webhooks for Clever Cloud applications using CLI tools for automated alerts and integrations with external services
keywords:
- notifications
- webhooks
- alerts
- cli
- integrations
- automation
aliases:
- /doc/administrate/clever-tools/notifications
- /doc/clever-tools/notifications/
- /doc/cli/notifications
- /doc/cli/notifications-webhooks
- /doc/reference/clever-tools/notifications
- /reference/clever-tools/notifications
---

When events happen on Clever Cloud, during add-ons or applications lifecycle for example, you can send email notifications or trigger webhooks. For each of the following command, you can list all items and/or target a specific user/organisation through these parameters:

```console
[--org, -o, --owner]       Organisation ID (or name, if unambiguous)
[--list-all]               List all notifications for your user or for an organisation with the `--org` option (default: false)
```

## notify-email

You can send email notifications when [an event occurs](/doc/account/notifications/#available-events). To list them, use:

```console
clever notify-email
clever notify-email --format json
```

To add a notification process to an application, use:

```console
clever notify-email add --notify <EMAIL_ADDRESS>|<USER_ID>|"ORGANISATION" NAME
```

Available options are:

```console
[--event] TYPE                                        Restrict notifications to specific event types
[--service] SERVICE_ID                                Restrict notifications to specific applications and add-ons
--notify <EMAIL_ADDRESS>|<USER_ID>|"ORGANISATION"     Notify a user, a specific email address or the whole organisation (multiple values allowed, comma separated)
```

To delete a notification process, use:

```console
clever notify-email remove NOTIFICATION-ID
```

## webhooks

You can trigger Webhooks when an event occurs. To list them, use:

```console
clever webhooks -F json
```

To add a webhook to an application, use:

```console
clever webhooks add NAME URL
```

You can set the format, restrict to a service or [event types](/doc/account/notifications/#available-events) through these parameters:

```console
[--format] FORMAT          Format of the body sent to the webhook ('raw', 'slack', 'gitter', or 'flowdock') (default: raw)
[--event] TYPE             Restrict notifications to specific event types
[--service] SERVICE_ID     Restrict notifications to specific applications and add-ons
```

To delete a webhook, use:

```console
clever webhooks remove NOTIFICATION-ID
```
