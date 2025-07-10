---
type: docs
title: Notifications
position: 6
shortdesc: How to setup and configure notifications via clever-tools
tags:
- cli
- reference
keywords:
- notification
- webhook
- e-mail
- email
- slack
- flowdock
aliases:
- /doc/administrate/clever-tools/notifications
- /developers/doc/cli/notifications/
draft: true
---

The *Notifications* service allows you to choose the events of interest to you
and decide where to send corresponding notifications.

## E-mails

Historically and by default, deployment result e-mails (deployment succeeded or
failed) were always sent to the owners of an application, namely the user
themselves or the organisation's members.

Using the `notify-email` command of *clever-tools*, you can choose to disable
this or to restrict it to only some applications.

To do this, you need to delete the hook named *Default deployment result
e-mails*, then add a new one and set it to your liking.

Issue this command to learn more about this: `clever help notify-email`.

In the future, this service will also handle credits warning notifications and
others to come. You will be able to choose wether or not to receive an e-mail
and/or for these events to be forwarded to a web service via a *webhook*.

## Webhooks

Webhooks are defined as follows:

> A webhook in web development is a method of augmenting or altering the
> behavior of a web page, or web application, with custom callbacks. These
> callbacks may be maintained, modified, and managed by third-party users and
> developers who may not necessarily be affiliated with the originating website
> or application.
> — <cite>Wikipedia[^1]</cite>

[^1]: Excerpted from Wikipedia's [webhook page](https://en.wikipedia.org/wiki/Webhook)

In practical terms, this means that you can choose to receive all deployment
result events on an endpoint of your application without having to listen to
all events via the Websocket API. No more lost events and having to reconnect
to the websocket if and when it fails.

*clever-tools* has a `webhooks` command which allows you to list existing
webhooks, remove one or add a new one.

You can issue this command to learn more about it: `clever help webhooks`.

### Example: Slack deployment results Webhook

First, you will have to create the *Incoming WebHooks* integration on Slack:

Let's go to the [custom integrations
page](https://slack.com/apps/manage/custom-integrations), once there go to
*Incoming WebHooks*.

You will find an *Add Configuration* button on the left which will take you to
the page where you need to configure the integration. You just need to select
the channel where you want the notifications to be posted, then it will show
you the Webhook URL, it starts with `https://hooks.slack.com/services/`. Copy
that URL.

Now, let's create the Webhook!

Go into the application directory for which you want to receive notifications
and there issue this command:

```shell
clever webhooks add "deployment results on Slack" https://hooks.slack.com/services/xxxxxx/yyyyyy/zzzzzzzzzzzzz --format slack --event META_DEPLOYMENT_RESULT
```

#### Events available

The list of values that can be assigned to `--event` option:

**Account:**

- `ACCOUNT_CREATION`
- `ACCOUNT_DELETION`
- `ACCOUNT_EDITION`

**Addon:**

- `ADDON_CREATION`
- `ADDON_DELETION`

**Application:**

- `APPLICATION_CREATION`
- `APPLICATION_DELETION`
- `APPLICATION_EDITION`
- `APPLICATION_REDEPLOY`
- `APPLICATION_STOP`

**Deployment:**

- `DEPLOYMENT_ACTION_BEGIN`
- `DEPLOYMENT_ACTION_END`
- `DEPLOYMENT_FAIL`
- `DEPLOYMENT_SUCCESS`
- `GIT_PUSH`

**Organisation:**

- `ORGANISATION_CREATION`
- `ORGANISATION_DELETION`
- `ORGANISATION_EDITION`
- `ORGANISATION_USER_ADDITION`

**Meta:**

- `META_SERVICE_LIFECYCLE` = APPLICATION_STOP, DEPLOYMENT_ACTION_BEGIN, DEPLOYMENT_FAIL, DEPLOYMENT_SUCCESS
- `META_DEPLOYMENT_RESULT` = DEPLOYMENT_FAIL, DEPLOYMENT_SUCCESS
- `META_SERVICE_MANAGEMENT` = ADDON_CREATION, ADDON_DELETION APPLICATION_CREATION, APPLICATION_EDITION, APPLICATION_DELETION`
- `META_CREDITS` = CREDITS_ADDED

**Others:**

- `CLEVER_TOOLS_REQUEST`
- `CREDITS_ADDED`

##### Examples

Get a message in a Slack channel when the deployment for an application failed:

```shell
clever webhooks add "The application failed to deploy" https://hooks.slack.com/services/xxxxxx/ --format slack --event DEPLOYMENT_FAIL
```

Notify your accounting service when credits are added:

```shell
clever webhooks add "credits added" https://hooks.slack.com/services/xxxxxx/yyyyyy/zzzzzzzzzzzzz --format raw --event META_CREDITS
```

All done! You can now push your application (`clever deploy`) or restart it
(`clever restart`) and you will see the result of the deployment in your Slack
channel.
