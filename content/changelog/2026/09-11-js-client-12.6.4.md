---
title: 'JS Client 12.6.4: TypeScript, Cellar and Kubernetes commands, consistent naming'
description: Clever Cloud JS client 12.6 is rewritten in TypeScript, adds Cellar, Kubernetes and log drain commands, and aligns every command on the same naming conventions
date: 2026-09-11
tags:
  - client
  - javascript
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 12.6.4](https://github.com/CleverCloud/clever-client.js/releases/tag/v12.6.4) is available. The patch releases published since 12.6.0 rewrite the client in TypeScript, add 43 commands and review all the existing ones against the API. Despite their version number, they rename fields and change the shape of several commands: check your code before upgrading from an earlier release.

## TypeScript and release process

Since 12.6.1, the client codebase uses TypeScript and its published type declarations come from the sources. Every command, input and output field now carries a description, and a field named differently from the API payload says so with a `@renamedFrom` tag. Since 12.6.2, git tags start with `v`, such as `v12.6.4`. Update any submodule, install-from-git URL or CI checkout pinned on a tag.

## New commands

Release 12.6.3 adds commands to manage [Cellar](/doc/deploy/storage/cellar/) buckets, objects and credentials, with `UploadCellarObjectCommand` storing an object in a single call. It covers [Kubernetes](/doc/deploy/kubernetes/) clusters and node groups: creation, update, version check and upgrade, `kubeconfig`, persistent storage, quotas, usage and events. It also adds `ListAddonInstanceCommand` to list the instances of an add-on, `GetCurrentOauthTokenInfoCommand` and `RequestAuthPasswordResetCommand`.

[Log drain](/doc/observability/drains/) commands accept an add-on as source again, and `ListLogDrainCommand` can list every drain of an organisation. They support the `BETTERSTACK`, `OVH_TCP` and `SPLUNK` (HTTP Event Collector) targets. `CheckLogDrainCommand` checks whether the target of a drain can be reached, `ResetLogDrainCursorCommand` drops its backlog to ship only new logs, and `skipCheck` creates a drain before its target is reachable.

## Naming and errors

Fields now follow the same conventions across the client: flags start with `is`, `has`, `can` or `should`, dates end with `At`, arrays are plural. For example, `homogeneous` becomes `isZeroDowntimeDeploymentEnabled` with its value inverted, and the syslog `structuredDataParameters` becomes `rfc5424StructuredDataParameters`. `GetOrganisationSummariesCommand` becomes `GetOrganisationSummaryCommand`, and `ListLogCommand` is removed: use the log stream commands instead. Duration inputs accept milliseconds besides ISO 8601 strings.

Commands mapping API errors to named codes export them as constants, such as `CREATE_DOMAIN_ERROR_CODES`, to use with the `isCcHttpErrorWithCode()` predicate instead of hardcoded strings:

```javascript
import { CREATE_DOMAIN_ERROR_CODES, CreateDomainCommand } from '@clevercloud/client/cc-api-commands/domain/create-domain-command.js';
import { isCcHttpErrorWithCode } from '@clevercloud/client/utils/error-utils.js';

try {
  await client.send(new CreateDomainCommand({ applicationId: 'app_xxxxxxxx', domain: 'shop.acme-store.com' }));
} catch (error) {
  if (isCcHttpErrorWithCode(error, CREATE_DOMAIN_ERROR_CODES.ALREADY_USED)) {
    console.error('This domain is already used by another application');
  } else {
    throw error;
  }
}
```

`CcNetworkError` now tells network failures apart: `networkCode` holds the code behind the failure, such as `ECONNREFUSED` or `ENOTFOUND`, and `explanation` describes it in a sentence you can show to users. Release 12.6.4 fixes the defects left by the 12.6.3 review.

## How to upgrade

Update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.6.4
```
