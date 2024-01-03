---
type: docs
title: Roles and Organizations
weight: 4
description: Discover how to manage organizations within your Clever Cloud account. This guide covers creation of organizations and roles in our PaaS platform.
tags:
- dashboard-setup
keyworkds:
- roles
- users
- accounts
- organizations
- organizations
- collaboration
---

In order to improve team collaboration between developers, accountants, managers and admins, we have introduced organizations. Each organization has its own billing, leaning that you can create as much as orgnanization you'd like. Most use-cases include the billing separation of private and business applications, several businesses or business units (within one company, for instance).

Once you create an organization, you can add collaborators and assign them [roles](#roles-and-privileges) which gives them rights.

Each organization have its own identifier looking like `orga_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.


## Add an organization

Organization names are unique. It means that you cannot use an already used organization name.

In order to add an organization, just click on "Add an organization" in the top left sidebar.


## Roles and privileges

The table below describes rights assigned to roles:

Role | Admin | Manager | Developer | Accountant |
-----|-------|---------|-----------|------------|
Add Member | ✓ | ✓ |  |  |
Remove Member | ✓ | ✓ |  |  |
Add Application | ✓ | ✓ | ✓ |  |
Remove Application | ✓ | ✓ |  |  |
Add / Remove add-on | ✓ | ✓ |  |  |
Edit Organization | ✓ | ✓ |  |  |
Delete Organization | ✓ |  |  |  |
Access Bills & Receive Invoices | ✓ |  |  | ✓ |
Access Repositories | ✓ | ✓ | ✓ |  |
