---
type: docs
title: Payments & invoicing
position: 5
shortdesc: Managing invoices and payment on Clever Cloud
tags:
- billing
keywords:
- invoices
- tax
- pricing
- billing
- payment
- stripe
- sepa
type: docs
aliases:
- /developers/doc/admin-console/invoices-payments
- /doc/admin-console/invoices-payments
---

## Make a payment

In the sidebar of the organisation section, there are three alternatives to buy credit for your applications:

* Credit card (powered by Stripe)
* Paypal
* Bank transfer: we accept international bank transfers. This option will generate a reference that you will have to add to your bank transfert, as a note.
* SEPA Direct Debit: we support payment via SEPA debit. More information in the [SEPA Direct Debit section](#sepa-direct-debit)

## Invoices

Invoices are available in the *Invoices* tab in the sidebar of the organisation section. Once paid, invoices are moved to the "Paid invoice" table.

### Receive invoices

You can change the billing email for an organisation in *Information > Billing details > Billing email*.

Also an organisation member with the accountant role can receive invoices as described in the organisation [roles]({{<  ref "/doc/account/organisations/#roles-and-privileges" >}}).

## Change Billing Information

* for personal account: available in *Profile > Informations*

* for organisation: available in *Information > Billing details*

![Clever Cloud Console: "Information menu from the organisation"](/images/doc/billing-infos.png "organisation information")

## SEPA Direct Debit

When adding your IBAN in the admin console, you accept the following SEPA Direct Debit
Mandate:

> By providing your IBAN or confirming this payment, you are authorizing Clever Cloud and
> Stripe, our payment service provider, to send instructions to your bank to debit your
> account and your bank to debit your account in accordance with those instructions.
> You also agree to be debited in the future 2 days after receiving a debit notification.
>
> You are entitled to a refund from your bank under the terms and conditions of your
> agreement with your bank. A refund must be claimed within 8 weeks starting from the date
> on which your account was debited.
>
> Debit instructions are issued in the following cases:
>
> * when you confirm an invoice payment;
> * starting 5 days after issuing the invoice, would you set your IBAN as default payment method;
> * would the first debit fail, new attempts will be made every day up to 15 days after invoice issuance and every 5 days after that.
> Your rights are explained in a statement that you can obtain from your bank.

### About invoices issuance and notifications

As explained in the [Monthly Invoice documentation]({{< ref "doc/billing/unified-invoices.md#monthly-invoice" >}}), Clever Cloud issues an invoice at the beginning of every month.
This invoice is sent to both primary and secondary email address of any Admin or Accountant within the organisation.
In accordance with SEPA rules and the mandate your agreed to, this email also notifies you that a debit will be attempted 5 days after invoice issuance.
