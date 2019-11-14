---
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
---

## Make a payment

In the sidebar of the organization section, there are three alternatives to buy credit for your applications:

* Credit card (powered by Stripe)
* Paypal
* Bank transfer: we accept international bank transfers. This option will generate a reference that you will have to add to your bank transfert, as a note.
* SEPA Direct Debit: we support payment via SEPA debit. More information in the [SEPA Direct Debit section](#sepa-direct-debit)


## Invoices

Invoices are available in the *Invoices* tab in the sidebar of the organization section. Once paid, invoices are moved to the "Paid invoice" table.

## Change Billing Information

* for personal account: available in *Profile > Informations*

* for organization: available in *Information > Billing details*

<figure class="cc-content-img">
  <img src="/doc/assets/images/billing-infos.png" data-action="zoom"/>
  <figcaption>Organization information</figcaption>
</figure>

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
> <ul>
>    <li>when you confirm an invoice payment;</li>
>    <li>on the 5th of the month, when we issue an automatic invoice on
>       the 1st of that month, would you set your IBAN as default payment method;</li>
>    <li>would the first debit fail, new attempts will be made on the 5th, 10th, 15th and
>       20th of that month.</li>
> </ul>
> Your rights are explained in a statement that you can obtain from your bank.

### A bit more on invoice issuance and notification:

As explained in the [Monthly Invoice documentation](/doc/clever-cloud-overview/unified-invoicing/#monthly-invoice),
at the beginning of every month, we issue an invoice. We attach the invoice to an email
we send you. In accordance with SEPA rules and the mandate your agreed to, this email will notify you that a debit
will be attempted the 5th of the month, so three to four days after the notification.
