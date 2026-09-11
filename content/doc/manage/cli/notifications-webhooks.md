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

You can send email notifications or trigger webhooks when [events occur](/doc/account-billing/notifications/#available-events) during an application or add-on lifecycle.

By default, listing commands target the application linked to your current directory. Use `--list-all` to list notifications for your account, or `--org` (or `-o`) to target an organisation by ID or unambiguous name:

```bash
clever notify-email --list-all
clever webhooks --org platform-team
```

## notify-email

List email notifications in human or JSON format:

```bash
clever notify-email
clever notify-email --format json
```

To create a notification for your linked application, provide a name and at least one recipient:

```bash
clever notify-email add deployment-alerts --notify operations@example.com
```

The required `--notify` option accepts an email address, a user ID, or `ORGANISATION` to notify the whole organisation. Separate multiple recipients with commas. Use `--org` to create the notification in an organisation:

```bash
clever notify-email add deployment-alerts --org platform-team --notify ORGANISATION
```

Use `--event` to restrict event types and `--service` to restrict applications or add-ons. Both accept comma-separated values. The `--service` option requires `--org`.

To delete a notification, replace `notification_id` with an ID from the listing. Include `--org` when the notification belongs to an organisation:

```bash
clever notify-email remove notification_id --org platform-team
```

## webhooks

List webhooks in JSON format:

```bash
clever webhooks -F json
```

To create a webhook for your linked application, provide a name and your receiving endpoint URL. Replace the URL below with your endpoint:

```bash
clever webhooks add deployment-alerts https://hooks.example.com/deployments
```

For `webhooks add`, `--format` selects the request body format: `raw` (the default), `flowdock`, `gitter`, or `slack`. On the listing command, `--format` instead selects `human` or `json` output.

Use `--event` to restrict event types and `--service` to restrict applications or add-ons. Both accept comma-separated values. The `--service` option requires `--org`. Without `--service`, specifying `--org` creates a webhook for the organisation without restricting it to your linked application.

To delete a webhook, replace `notification_id` with an ID from the listing:

```bash
clever webhooks remove notification_id --org platform-team
```
