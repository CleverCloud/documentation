---
type: docs
linkTitle: Organisations and members
title: Organisations and members
description: List and update your organisations with Clever Tools, invite members, change their role, and find the accounts without two-factor authentication
keywords:
- organisations
- members
- roles
- invitations
- billing
- cli
---

Clever Tools manages your [organisations](/doc/account-billing/organisations/) and their members from a terminal. `clever orgs` reads and updates the details of an organisation, and `clever members` handles who belongs to it, with which role. Both suit scripts, such as an audit of the members.

What you can do depends on your [role](/doc/security/iam-roles/#roles-and-privileges) in the organisation, as in the Console. Clever Tools doesn't create or delete an organisation, and doesn't manage its payment methods: use the [Console](https://console.clever-cloud.com) for these tasks.

## List your organisations

`clever orgs list` shows the organisations of your account in a table, with their name, their ID, and your role in each. Your Personal Space comes first, then the others in alphabetical order:

```bash
clever orgs list
clever orgs list --format json
```

The JSON output holds the same fields, and an `isPersonal` field, `true` for your Personal Space. Roles are in upper case, so this command prints the ID of each organisation where you're an admin:

```bash
clever orgs list --format json | jq -r '.[] | select(.role == "ADMIN") | .id'
```

## Target an organisation

The other commands take the organisation as their first argument: its ID, as `clever orgs list` shows it, or its exact name. A name is case-sensitive, and needs quotes when it contains spaces:

```bash
clever orgs get orga_00000000-0000-4000-8000-000000000200
clever orgs get "My Other Organisation"
```

When several of your organisations share a name, the command fails and lists them: use the ID instead. Your Personal Space appears under your own name, with an ID that starts with `user_`. The examples of this page use an organisation named `my-organisation`.

## Get the details of an organisation

`clever orgs get` prints the details of an organisation in three sections. General shows your role, the description, and the number of members and admins. Billing shows the contact name and email, the company and its value-added tax (VAT) number, and the address. Support shows whether the organisation has Premium support, and its emergency number.

```bash
clever orgs get my-organisation
clever orgs get my-organisation --format json | jq -r '.billingEmail'
```

A warning ends the output when the billing details are incomplete, which prevents payments. In JSON, `membersCount` and `adminsCount` are `null` for your Personal Space, and for an organisation whose member list isn't available to you.

## Update an organisation

`clever orgs update` changes the fields you give as options, and keeps the others. It requires the Admin or Manager role, and prints each changed field with its previous and new values:

```bash
clever orgs update my-organisation --description "Production services"
clever orgs update my-organisation --billing-name "Giulia Rossi" --billing-email billing@example.com
clever orgs update my-organisation --address "3 rue de l'Allier" --zipcode 44000 --city Nantes --country FR
```

`--country` takes a two-letter ISO code. An empty value clears a field, but the name and the description can't be empty. A VAT number requires a company: set `--company` with it unless the organisation already has one, and clear both to switch back to an individual. The API validates the number, so replace the one of this example with yours:

```bash
clever orgs update my-organisation --company "My Company" --vat-number FR12345678901
clever orgs update my-organisation --company "" --vat-number ""
```

Without any option, in a terminal, the command asks for each field in turn. Press Enter to keep the current value, or type `-` to clear it, which the name and the description refuse. In a script, where no terminal is attached, the command fails if you give no option.

To rename an organisation, use `--name`. The commands that follow must then target the new name, or the ID, which doesn't change:

```bash
clever orgs update my-organisation --name "My Company"
```

## List the members

`clever members list` shows the members of an organisation, sorted by role then by name. For each of them, it gives the role, name, email, ID, and whether two-factor authentication (2FA) is enabled:

```bash
clever members list my-organisation
```

Filter the list with `--role`, or with `--without-2fa` to find the accounts to secure. Both combine, and work with the JSON output, where `isMfaEnabled` gives the 2FA status and `isCurrentUser` identifies your own account:

```bash
clever members list my-organisation --role admin
clever members list my-organisation --without-2fa --format json | jq -r '.[].email'
```

Your Personal Space has no members: the `clever members` commands refuse it.

## Invite a member

`clever members invite` sends an invitation by email to the address you give, valid for two days, with the role the person gets once they accept it. `--role` is required, and takes `admin`, `manager`, `developer`, or `accounting` for the Accountant role:

```bash
clever members invite my-organisation giulia.rossi@example.com --role developer
```

Inviting, updating, and removing members requires the Admin or Manager role. An Admin assigns any role. A Manager only assigns the Manager and Developer roles, and can't change or remove an Admin or an Accountant.

The API limits how many invitations a member sends and an address receives each hour: a script that invites many people must spread them.

## Change the role of a member

`clever members update` gives a new role to the member whose email or ID you give. It prints the previous and the new role, and sends nothing when the member already has this role:

```bash
clever members update my-organisation giulia.rossi@example.com --role manager
clever members update my-organisation user_00000000-0000-4000-8000-000000000101 --role developer
```

## Remove a member or leave an organisation

`clever members remove` removes a member, by email or by ID, after a confirmation. Add `--yes` to skip it, which a script requires:

```bash
clever members remove my-organisation giulia.rossi@example.com
clever members remove my-organisation giulia.rossi@example.com --yes
```

To leave an organisation, remove yourself, whatever your role: the command asks you to confirm that you lose access to it. An organisation keeps an admin, so the command fails for the last one.

When the member list of an organisation isn't available to you, Clever Tools can't match an email to a member. Give the member ID to `clever members update` and `clever members remove` instead.

## Go further

{{< cards >}}
  {{< card link="/developers/doc/account-billing/organisations" title="Organisations" subtitle="Create and administrate an organisation in the Console" icon="building-library" >}}
  {{< card link="/developers/doc/security/iam-roles" title="Roles and privileges" subtitle="What each role can do in an organisation" icon="lock-closed" >}}
  {{< card link="/developers/doc/cli-reference" title="Commands reference" subtitle="Every command and option of Clever Tools" icon="book-open" >}}
{{< /cards >}}
