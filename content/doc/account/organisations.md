---
type: docs
title: Roles and organisations
weight: 4
description: Discover how to manage organisations within your Clever Cloud account. This guide covers creation of organisations and roles in our PaaS platform.
tags:
- dashboard-setup
keyworkds:
- roles
- users
- accounts
- organisations
- organisations
- collaboration
aliases:
- /doc/account/organizations/
---

In order to improve team collaboration between developers, accountants, managers and admins, we have introduced organisations. Each organisation has its own billing, leaning that you can create as much as orgnanization you'd like. Most use-cases include the billing separation of private and business applications, several businesses or business units (within one company, for instance).

Once you create an organisation, you can add collaborators and assign them [roles](#roles-and-privileges) which gives them rights.

Each organisation have its own identifier looking like `orga_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

## Add an organisation

organisation names are unique. It means that you cannot use an already used organisation name.

In order to add an organisation, just click on "Add an organisation" in the top left sidebar.

## Roles and privileges

The table below describes rights assigned to roles:

Role | Admin | Manager | Developer | Accountant |
-----|-------|---------|-----------|------------|
Add Member | ✓ | ✓ |  |  |
Remove Member | ✓ | ✓ |  |  |
Add Application | ✓ | ✓ | ✓ |  |
Remove Application | ✓ | ✓ |  |  |
Add / Remove add-on | ✓ | ✓ |  |  |
Edit organisation | ✓ | ✓ |  |  |
Delete organisation | ✓ |  |  |  |
Access Bills & Receive Invoices | ✓ |  |  | ✓ |
Access Repositories | ✓ | ✓ | ✓ |  |
