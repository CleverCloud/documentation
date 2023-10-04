---
title: Unified Invoicing
position: 1
shortdesc: Each month, for each organization, a single invoice is generated, including the whole activity (credits, add-on etc).
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
---

Each month, for each organization, a single invoice is generated, including the whole activity (credits, add-on etc).

## Monthly invoice

At the beginning of each month, a new invoice is generated for each organisation. It details the consumption of services, and the provisioning of your account for the coming month.

The invoice is made up of three distinct sections:

* A summary of the total amount to be paid for the current month
* An exploded view of the invoice calculation, including credits used, coupons, provision for the coming month etc.
* and full details of the operating time of each service, of each service invoiced, of storage used etc.

To find your invoices, go to your organisation and click on **Invoices** to see a list of them and their payment status:

{{< image "/images/invoices/invoice-list.png" "The list of invoices" >}}

### First section

This first section shows the fee for the use of Clever Cloud over a month. Any discounts are explained here.

{{< image "/images/invoices/invoice-amount-to-pay.png" "The second section of the invoice"  >}}

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

{{< image "/images/invoices/invoice-credits-balance.png" "The second section of the invoice"  >}}

### Third section

This section of the invoice details the usage of each cloud service.

{{< image "/images/invoices/invoice-runtime-detail.png" "The third section of the invoice"  >}}

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

For each organisation it is possible to register one or more payment methods ([see list of payment methods here]](/doc/billing/payments-invoicing/)). Invoices will be automatically paid with the default payment method a few days after their generation. For the one-off invoices mentioned above, the invoice must be paid manually, via the invoice page via the "Pay" button.

## Unpaid invoices

If a bill is unpaid, several steps are taken before the service is cut off:

* email reminders (on the 5th, 10th, 15th, 20th, 21st, 22nd, 23rd, 24th and 25th of each month)
* an announcement of the cut-off from the 15th of the month
* the effective termination of services and blocking of deployments (variable date)

Support and access to your account will remain available to regularise non-payment situations.
