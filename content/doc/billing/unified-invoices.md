---
type: docs
title: Unified Invoicing
position: 1
shortdesc: Each month, for each organisation, a single invoice is generated, including the whole activity (credits, add-on etc).
tags:
- billing
keywords:
- invoice
- invoicing
- billing
- bill
- payment
- payments
type: docs
aliases:
- /developers/doc/clever-cloud-overview/unified-invoicing
- /doc/clever-cloud-overview/unified-invoicing
---

Each month, for each organisation, a single invoice is generated, including the whole activity (credits, add-on etc).

## Monthly invoice

At the beginning of each month, a new invoice is generated for each organisation. It details the consumption of services, and the provisioning of your account for the coming month.

The invoice is made up of three distinct sections:

* A summary of the total amount to be paid for the current month
* An exploded view of the invoice calculation, including credits used, coupons, provision for the coming month etc.
* and full details of the operating time of each service, of each service invoiced, of storage used etc.

To find your invoices, go to your organisation and click on **Invoices** to see a list of them and their payment status:

![List of invoices from the console](/images/doc/invoice-list.png "The list of invoices")

### First section

This first section shows the fee for the use of Clever Cloud over a month. Any discounts are explained here.

![First section of the invoice](/images/doc/invoice-amount-to-pay.png "The first section of the invoice")

### Second section

This part details line by line the evolution of your credit with:

* The balance of free credits (a)
* Pre-paid credits (b)
* The use of free credits (c)
* Expired credits (d)
* Use of your prepaid credits (e)
* Estimated consumption for the next period (f)
* Invoiced credits pending payment (g)
* Amount of prepaid credits to be topped up (h)

The **amount of prepaid credits to be topped up** and the **new balance of credits after settlement** are explained via calculations of the different types of credits and their use over time.

![Credit balance on invoice](/images/doc/invoice-credits-balance.png "The second section of the invoice")

### Third section

This section of the invoice details the usage of each cloud service.

![Runtime section on invoice](/images/doc/invoice-runtime-detail.png "The third section of the invoice")

## Managed Services

While applications are billed on a per second basis, this may be different for managed services.
From a billing point of view there are X categories

* time-based billing (per second)
* resource consumption billing

For example, dedicated databases are charged by the second, just like applications.
In contrast, services such as Cellar object storage or Pulsar are charged according to the volume of data stored and the volume of outgoing traffic.

## Specific invoices

For specific services performed by the support teams, specific invoices can be created by the administration or support teams. These invoices usually indicate a specific service act.

## Management of payment methods

For each organisation it is possible to register one or more payment methods ([see list of payment methods here]({{< ref "/doc/billing/payments-invoicing/">}})). Invoices will be automatically paid with the default payment method a few days after their generation. For the one-off invoices mentioned above, the invoice must be paid manually, via the invoice page via the "Pay" button.

## Payments and reminders

As long as an invoice remains *pending*, we'll perform these actions on specific days:

* Try to issue an automatic payment using your favorite payment method everyday from the
  5th to the 15th day after issuing the invoice, then every 5 days after that.
* Send a reminder via email every 5 days if the payment remains unsuccessful.
* Shutdown of your services everyday starting day 31 after invoice issue.

This schedule can adapt according to your company's payment delays.
Please reach out to us via the support to ensure the best experience.

Support and access to your account will remain available to regularise non-payment situations.
