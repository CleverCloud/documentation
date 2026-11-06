---
type: docs
linkTitle: Organisations
title: Manage an organisation
description: Manage your organisation on Clever Cloud including user roles, permissions, billing settings, and administrative information
keywords:
- preferences
- organisation
- management
- billing
- team
- permissions
- collaboration
aliases:
- /doc/account/administrate-organisation
- /doc/account/administrate-organization
- /doc/account/organisations
- /doc/organisations
- /doc/administrate/organisations/
- /doc/manage/organisations/
- /doc/organisations/manage
---

After you create an account, your account is tied to a first organisation named as 'Personal Space'. You can use the Personal Space for individual projects or personal use, but only you as a user can access it.

To collaborate with others, manage team access, or handle separate billing for a group, you need to create an organisation.

## Create an organisation

In the Clever Cloud Web Console, open the organisation switcher at the top of the sidebar, then select **Add new organisation**.

Give it a name, description, specify if it's a company and add billing information.

## Administrate an organisation

Select an organisation from the organisation switcher, at the top of the sidebar. Tabs give access to its pages, depending on your [role](/doc/security/iam-roles/#roles-and-privileges) and the services enabled for your organisation. Only the Admin and Accountant roles get the billing tabs: Payment methods, Invoices, and Coupons & credits.

- **Overview**: Simple metrics about your applications within this organisation
- **Information**: See and edit organisation's name, description, billing address and image. That also is where you can delete your organisation.
- **Payment methods**: Manage provisioning of your organisation and manage credit cards.
- **Invoices**: See your recent invoices.
- **Coupons & credits**: Activate a coupon and see your free credits.
- **Members**: Manage team members. Team members must have a Clever Cloud account. On this page you can add and remove team members. You can also edit their roles to manage their permissions.
- **Metrics in Grafana**: Open the Grafana dashboards of your organisation.
- **Notifications**: Manage email notifications and web hooks for team members.
- **Shared software**: It's a section displaying third-party software, like [Heptapod](/doc/deploy/services/heptapod/)

## Delete an organisation

In the **Information** page, click the *remove this organisation* button. You're then prompted to enter the name of the organisation to confirm the organisation deletion.
