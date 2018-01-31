---
title: Unified Invoicing
position: 1
tags:
- support
keywords:
- invoice
- invoicing
- billing
- bill
- payment
- payments
---

Each month, for each organization, a single invoice is generated, including the whole activity (credits, add-on etc).

## Monthly invoice

At the begin of every month, a single new invoice is created. It provisions your account for the month to come:

* Credits provision based on the previous month consumption
* Optionally: regularisation for over-consumption from the previous month
* Add-ons

Addons with a fixed monthly price are listed in the invoice, one line per addon. Addons with pay-as-you-go plans are integrated in the credits consumption, on a daily basis.

## One-shot invoices

When creating an add-on with a fixed monthly add-on price, an initial invoice is emitted for the rest of the month plus the next month. After this period, the add-on will be part of the monthly invoice.

### Example:

If you order a new database (€40 / month) on March 25, an invoice of €47.74 will be emitted, covering March 25 - April 30.
Starting May 1st, the database will be integrated in the monthly invoice.

## Payment method management:

You can register payment methods for each organization. The monthly invoice is automatically paid with the default payment method. The other payment means can be used for one-shot invoices. This way, to use a new credit card, you just have to set it as the default one, it will automatically be used for new invoices.  

As of now, only credit cards can be used for monthly invoice payment. More payments methods will soon be available. [Please get in touch](mailto:support@clever-cloud.com) if you have specific needs.

## Over consumption / unpaid invoices:

If you desire a strong control on costs, you can set up a hard limit for consumption. If you reach it, applications will automatically be undeployed to prevent unexpected charges. By default this is disabled, [please get in touch](mailto:support@clever-cloud.com) if you want to activate it.

# Differences with pre-2017 invoicing

Unified invoicing has been rolled-out during February 2017. Here are the changes introduced by Unified Invoicing:

- Payment methods are now associated with organizations instead of users, which means you can see and change credit cards for organizations in an easier way.
- Credit consumption and add-ons are unified in a single monthly invoice. Each month, the consumption from the last month is credited on your account.  
- FS buckets and Cellar consumptions are now integrated in your daily consumption, along with apps.
- **Going out of credits no longer stops applications (by default).**
