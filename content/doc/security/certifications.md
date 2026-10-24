---
type: docs
weight: 151
linkTitle: Certifications
title: Certifications
description: Where your resources run on Clever Cloud, and what the ISO 27001, HDS and SecNumCloud frameworks cover
keywords:
- certifications
- compliance
- hds
- iso 27001
- secnumcloud
- audit
aliases:
- /doc/certifications
---

Compliance on Clever Cloud is a property of the zone your resources run in, not of your account. The same platform, API and tooling drive every deployment, but the infrastructure underneath and the contract attached to it change what you can host. This page explains that split, then what each framework covers.

## Versatile cloud

Clever Cloud runs on three kinds of infrastructure, with the same control plane and the same deployment workflow on each. Some zones run on hardware Clever Cloud owns and operates. Others run on partner infrastructure, from IONOS, OVHcloud or Scaleway. The last kind are private zones, provisioned for a single organisation on-premise, at the edge, or fully air-gapped.

Zones and the infrastructure behind them are exposed by the API, so you never have to guess which is which:

```bash
curl -sS https://api.clever-cloud.com/v4/products/zones | jq -r '.[] | "\(.name)\t\(.city)\t\(.tags | join(" "))"' | sort
```

Each zone carries an `infra:` tag naming the operator, and a `contract:` tag when a compliance contract applies. A `tag` query parameter filters on either, so `?tag=infra:clever-cloud` lists the zones running on Clever Cloud hardware. That call returns the public zones only. Private zones exist for a single organisation, so ask for them with `ownerId`:

```bash
curl -sS "https://api.clever-cloud.com/v4/products/zones?ownerId=orga_xxx" | jq -r '.[].name'
```

The answer is the list of zones that organisation can deploy to, its private zones included. See the [Products zones endpoint](/developers/api/v4/#products-zones) for the full response.

That distinction has an operational consequence worth knowing before you pick a zone. Public zones hosted on partner infrastructure depend on the `par` control plane to deploy, scale and restart. Private and on-premise zones carry their own, and keep operating when the Paris control plane does not. An air-gapped zone goes further and runs with no internet connection at all, its updates delivered on encrypted physical media and applied under your supervision.

Deployments that need guaranteed response and resolution times, a 24/7 line to the support engineers, or regular steering meetings, are covered by a premium support contract rather than by a technical option. See [Find help](/developers/doc/find-help/) for what the base and premium offers include.

## ISO/IEC 27001:2022

The certification covers Clever Cloud's information security management system across the whole platform and its own infrastructure, rather than a single product or region. Bureau Veritas issued certificate `FR086307` under the 2022 revision of the standard, for a cycle running to December 19, 2027.

In practice this is the framework behind the controls documented elsewhere in this section: role separation inside an organisation, [encryption at rest](/developers/doc/security/encryption-at-rest/) on add-ons, key and secret storage, and the incident handling you see reported in the [postmortems](/developers/postmortem/).

## Health data hosting (HDS)

Hosting personal health data in France requires an HDS-certified host. Clever Cloud holds certificate `FR094504`, issued by Bureau Veritas Certification under COFRAC accreditation and valid to December 19, 2027, covering all six activities of the referential: physical, hardware and virtual infrastructure, application hosting platform, system administration, and externalised backup.

Four zones carry the HDS contract, identified by the `contract:hds` tag: `parhds` in Paris on Clever Cloud infrastructure, and `fr-north-hds`, `grahds` and `rbxhds` on OVHcloud HDS infrastructure. Create resources there with the region flag, for example `clever create --type node --region parhds` for an application, or `--region` on `clever addon create` for an add-on. Not every product is available in every HDS zone, so check the zones listed for each provider in the [Clever Tools reference](/developers/doc/cli-reference/#add-on-providers-plans-and-zones-region) before you design a health data architecture.

> [!NOTE] The certification covers the host, not your service
> Hosting on an HDS zone does not make your own organisation HDS-certified. It requires a specific HDS contract with Clever Cloud, and your data must stay within the European Economic Area. Contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) before deploying health data.

## SecNumCloud

SecNumCloud is the French cybersecurity agency's qualification for cloud providers, and it raises the bar above ISO 27001 on traceability, access control, logging and auditability. Public bodies handling data of particular sensitivity, including personal data of French citizens, are required to use a qualified provider. Private organisations are not, though operators of vital importance often choose it.

Clever Cloud does not hold the qualification for its own infrastructure yet. Work towards it is under way with support from Bpifrance, the ANSSI and the DGE under the France 2030 plan, and covers both the PaaS offer and the servers running it. Deployments that need the qualification today run on partner infrastructure that already holds it, with a dedicated zone provisioned for the customer. Contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) to have that zone opened.
