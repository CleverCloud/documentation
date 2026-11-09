---
type: docs
linkTitle: Account
title: Account
description: Create your Clever Cloud account with an email or GitHub, sign in from Clever Tools and the API, secure it with two-factor authentication, and delete it
keywords:
- account
- user
- profile
- signup
- github
- authentication
- 2fa
- api tokens
- delete account
aliases:
- /account
- /doc/account-billing/account
- /doc/account-setup
- /doc/account/create-account
- /doc/account/delete-account
- /doc/account/manage-account
- /doc/account/user-account
- /doc/admin-console/authentification
- /doc/getting-started/authentication
---

Your Clever Cloud account identifies you on the Console, Clever Tools, and the API. It gives you access to the [organisations](/doc/account-billing/organisations/) you're a member of, with the [role](/doc/security/iam-roles/#roles-and-privileges) you hold in each, and to your Personal Space, the organisation that signing up creates for you. Your applications, add-ons, and [invoices](/doc/account-billing/invoices/) belong to these organisations, not to your account.

## Create an account

[Sign up](https://api.clever-cloud.com/v2/session/signup) with an email address or with your GitHub account, and accept the terms and conditions.

### With an email address

Use an address you can read: Clever Cloud refuses temporary and disposable addresses. Choose a password of at least 12 characters. Then, confirm your address with the link of the email you receive: until you do, you can't create applications or organisations.

### With GitHub

Signing up with GitHub creates your account from your GitHub profile, to [deploy your repositories](/doc/tools/github/). GitHub asks for these permissions:

| Permission        | Clever Cloud uses it to                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| `user:email`      | Read your email addresses                                                       |
| `read:public_key` | Read your public SSH keys, to [deploy with Git](/doc/account-billing/ssh-keys/) |
| `repo`            | Clone your repositories, private ones included                                  |
| `admin:repo_hook` | Create the webhooks that redeploy your application on each push                 |

To deploy the repositories of a GitHub organisation, [grant Clever Cloud access to it](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc) in your GitHub settings. To link an existing account to GitHub, or to unlink it, open the **Profile** tab of your account in the Console. An account created with GitHub may have no password: create one from the **Authentication** tab before you unlink GitHub, to keep signing in.

## Sign in from your tools

[Clever Tools](/doc/tools/cli/) signs in with your account: [`clever login`](/doc/tools/cli/#login--logout) opens the Console in your browser, where you authorize it. Each authorization creates an OAuth token, listed in the **OAuth tokens** tab, where you can revoke it.

For scripts, create an API token in the **API tokens** tab, or with [`clever tokens create`](/doc/tools/cli/#tokens), which asks for your password and, if enabled, a 2FA code. The token shows only once: use it as a bearer token, as the [API documentation](/api/#api-tokens) explains.

Creating an API token requires a password: an account created with GitHub may need to add one first. A token acts with all the rights of your account: give it an expiration date, and revoke it once you no longer need it.

## Two-factor authentication (2FA)

Two-factor authentication asks for a code from an authenticator app when you sign in, in addition to your password. To enable it, open the [Authentication](https://console.clever-cloud.com/users/me/authentication) page of your profile, select `Enable 2FA`, and enter your password. Scan the QR code with your authenticator app, or enter the key the dialog gives instead. Then type the 6-digit code the app generates. By default, enabling 2FA revokes your other tokens and sessions, such as those of Clever Tools, but not your current Console session. Clear the checkbox in the dialog to keep them.

2FA requires a verified email address and a password. Without a password, the Authentication page offers to email you a link to create one.

Once 2FA is on, the Console shows your recovery codes. Each code lets you sign in once if you lose access to your authenticator app. They're shown only this once: copy or download them and store them somewhere safe, such as a password manager. Clever Cloud can't restore access to your account if you lose both your authenticator app and your recovery codes.

The Authentication page then tells how many recovery codes you have left. Select `Regenerate recovery codes` to get a new set, shown once the same way: the previous codes stop working. To turn 2FA off, select `Disable 2FA`. Both actions ask for your password.

## Manage your account

In the [Console](https://console.clever-cloud.com/), open the profile menu at the top right of the header, then select **Profile**. Its tabs give access to your account:

- **Profile**: your name, address, phone number, and picture, the link with your GitHub account, and the language of the Console
- **Emails**: your primary email address, and the secondary ones
- **SSH Keys**: the [SSH keys](/doc/account-billing/ssh-keys/) you deploy with, and those of your GitHub account
- **Authentication**: your password, [two-factor authentication](#two-factor-authentication-2fa), and its recovery codes
- **API tokens**: the [tokens](#sign-in-from-your-tools) of your scripts and integrations
- **Console sessions**: your open Console sessions, which you can revoke
- **OAuth tokens**: the tokens of the tools you authorized, such as Clever Tools
- **Labs**: features in preview, such as creating Kubernetes clusters from the Console, and the color theme of the Console, saved in your browser
- `Delete my account`: the [deletion of your account](#delete-your-account)

## Delete your account

From the `Delete my account` tab, select `Confirm the account deletion request`. Clever Cloud emails a confirmation link to your primary address: the deletion happens when you open it. It's irreversible and immediate:

- The organisations where you're the only member, your Personal Space included, are deleted, with their applications and add-ons
- You're removed from the other organisations, which keep their resources
- Your SSH keys, secondary email addresses, and tokens are deleted

Clever Cloud bills the services you used until the deletion that your [credits](/doc/account-billing/consumption/) don't cover, and doesn't refund the remaining credits. If you're the last admin of an organisation with other members, the Console asks you to appoint another admin first. An organisation that provides add-ons on the [Marketplace](/doc/develop/marketplace/) can't be deleted while it has add-on providers.

Some accounts, managed by an organisation, can't delete themselves: the tab then tells you to ask your administrator.
