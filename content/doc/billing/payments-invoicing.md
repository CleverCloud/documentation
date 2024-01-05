---
type: docs
title: Payments & invoicing
position: 5
shortdesc: Managing your Factur-X compatible invoices and payments on Clever Cloud
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
---

## Make a payment

In the sidebar of the organization section, there are three alternatives to buy credit for your applications:

* Credit card (powered by Stripe)
* Paypal
* Bank transfer: we accept international bank transfers. This option will generate a reference that you will have to add to your bank transfert, as a note.
* SEPA Direct Debit: we support payment via SEPA debit. More information in the [SEPA Direct Debit section](#sepa-direct-debit)


## Invoices

Invoices are available in the *Invoices* tab in the sidebar of the organization section. Once paid, they are moved to the "Paid invoice" table.

{{< callout type="info" >}}
  Since 2021, we provide invoices compatible with the [Factur-X e-invoice format](https://fnfe-mpe.org/factur-x/factur-x_en/). 
{{< /callout >}}

### Receive invoices

You can change the billing email for an organization in *Information > Billing details > Billing email*.

Also an organization member with the accountant role can receive invoices as described in the organization [roles](/doc/account/organizations/#roles-and-privileges).

## Change Billing Information

* for personal account: available in *Profile > Informations*

* for organization: available in *Information > Billing details*

{{< image "/images/doc/billing-infos.png" "Organization information" >}}

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

### About invoices issuance and notifications

As explained in the [Monthly Invoice documentation]({{< ref "doc/billing/unified-invoices.md#monthly-invoice" >}}),
we issue an invoice at the beginning of every month. We attach the invoice to an email we send you. In accordance with SEPA rules and the mandate your agreed to, this email will notify you that a debit we send you. 
Following SEPA rules and the mandate you agreed to, this email notifies you will be attempted the 5th of the month, so three to four days after the notification. that Clever Cloud is going to charge you on the 5th of the month, three to four days after
the notification.
