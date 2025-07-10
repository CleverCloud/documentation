---
type: docs
title: Notifications
weight: 5
description: Learn how to customize notifications for account and deployment activity on Clever Cloud, service updates, and more on our PaaS service.
tags:
- admin-console
keywords:
- notification
- webhook
- e-mail
- email
- slack
- flowdock
---

The *Notifications* service allows you to choose the events of interest to you
and decide where to send corresponding notifications.

## E-mails

Historically and by default, deployment result e-mails (deployment succeeded or
failed) were always sent to the owners of an application, namely the user
themselves or the organisation's members.

To disable the deployment result e-mails or restrict it to only some applications:

1. Go in **organisation Manager** > **Notifications** panel.
2. Delete the hook named *Default deployment result e-mails*.
3. Add a new one.
4. Set it to your liking.

In the future, this service will also handle credits warning notifications and
others to come. You will be able to choose wether or not to receive an e-mail
and/or for these events to be forwarded to a web service via a *webhook*.

## Webhooks

From Wikipedia:

> A webhook in web development is a method of augmenting or altering the
> behavior of a web page, or web application, with custom callbacks. These
> callbacks may be maintained, modified, and managed by third-party users and
> developers who may not necessarily be affiliated with the originating website
> or application.

In practical terms, this means that you can choose to receive all deployment
result events on an endpoint of your application without having to listen to
all events via the Websocket API. No more lost events and having to reconnect
to the websocket if and when it fails.

To create a webhook stay on the **Notifications** panel:

1. Click on **Webhooks** button at the top of the Notifications window.
2. Add a new one.
3. Choose the URL which will receive the data through a *POST* request and the format it will be sent as.

As of now, you can choose between 3 formats: *raw*, *slack* and *flowdock*. The *raw* format is the Clever Cloud internal representation of events, it is identical to events sent by the Websocket API. *Slack* and *Flowdock* formats are to be used with the corresponding services.

You can also choose which events you want and restrict notifications to a list
of applications and add-ons.

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

You should already have a tab opened on the Webhook creation page; if it's not
the case, follow the *Webhooks* section above.

There, you just need to paste the URL you copied before in the Webhook URL
field, then select *Result of deployments (success/fail)* in the *Only send
notification for these events* menu.

You can now push your application or restart it and you will see
the result of the deployment in your Slack channel.
