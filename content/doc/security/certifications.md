---
type: docs
weight: 151
linkTitle: Certifications
title: Certifications
description: Where your resources run on Clever Cloud, and what the ISO 27001, health data hosting (HDS), and SecNumCloud frameworks cover
keywords:
- certifications
- compliance
- hds
- iso 27001
- secnumcloud
- audit
---

Your compliance requirements determine which services, zones, and contracts you need. Each Clever Cloud certification has a specific scope, and your own obligations as a customer still apply. This page explains where your resources run, then what each framework covers.

## Versatile cloud

Clever Cloud runs on three kinds of infrastructure, with the same platform software and the same deployment workflow on each. Some zones run on hardware Clever Cloud owns and operates. Others run on partner infrastructure, from IONOS, OVHcloud, and Scaleway. The last kind are private zones, provisioned for a single organisation on-premise, at the edge, or fully air-gapped.

The API exposes zones and the infrastructure behind them, so you never have to guess which is which:

```bash
curl -sS https://api.clever-cloud.com/v4/products/zones | jq -r '.[] | "\(.name)\t\(.city)\t\(.tags | join(" "))"' | sort
```

Each zone carries an `infra:` tag naming the operator, and a `contract:` tag when a compliance contract applies. A `tag` query parameter filters on either, so `?tag=infra:clever-cloud` lists the zones running on Clever Cloud hardware. That call returns the public zones only.

Private zones belong to a single organisation. Log in to Clever Tools with an account that can access the organisation, then replace `orga_xxx` with its ID:

```bash
clever curl -sS "https://api.clever-cloud.com/v4/products/zones?ownerId=orga_xxx" | jq -r '.[].name'
```

The answer lists the zones that organisation can deploy to, its private zones included. Without access to the organisation, the API ignores `ownerId` and returns the public zones. See the [zones endpoint](/developers/api/swagger/#/Zones/listRegions) for the full response.

That distinction has an operational consequence worth knowing before you pick a zone. Public zones hosted on partner infrastructure depend on the `par` control plane to deploy, scale, and restart. Private and on-premise deployments have different dependencies, according to the offer you choose. Confirm with Clever Cloud whether yours has its own control plane before you rely on it for continuity. An air-gapped zone runs with no internet connection at all, its updates delivered on encrypted physical media and applied under your supervision.

A premium support contract covers guaranteed response and resolution times, a 24/7 line to the support engineers, and regular steering meetings. These come with the contract, not with a technical option. See [Find help](/developers/doc/find-help/) for what the base and premium offers include.

## ISO/IEC 27001:2022

The certification covers Clever Cloud's information security management system for its public and private PaaS services, within the scope the certificate lists. Bureau Veritas issued certificate [`FR086307`](https://cdn.clever-cloud.com/uploads/2024/03/certificateclevercloud17499349iso27001fr.pdf) under the 2022 revision of the standard, valid from March 15, 2024 to March 14, 2027.

In practice this is the framework behind the controls documented elsewhere in this section: role separation inside an organisation, [encryption at rest](/developers/doc/security/encryption-at-rest/) on add-ons, key and secret storage, and the incident handling you see reported in the [postmortems](/developers/postmortem/).

## Health data hosting (HDS)

If you outsource the hosting of personal health data covered by article L1111-8 of the French Public Health Code, you must use an HDS-certified host. Clever Cloud holds certificate [`FR094504-1`](https://cdn.clever-cloud.com/uploads/2026/09/certificate-clever-cloud-24357609-hds-v2-expire-2027-12-19.pdf), issued by Bureau Veritas Certification under COFRAC accreditation and valid to December 19, 2027. It covers all six activities of the referential: physical, hardware, and virtual infrastructure, the application hosting platform, system administration and operation, and backup.

Four zones carry the HDS contract, identified by the `contract:hds` tag: `parhds` in Paris on Clever Cloud infrastructure, and `fr-north-hds`, `grahds`, and `rbxhds` on OVHcloud HDS infrastructure. Create resources there with the region flag, for example `clever create --type node --region parhds` for an application, or `--region` on `clever addon create` for an add-on.

Not every product is available in every HDS zone. The [Clever Tools reference](/developers/doc/cli-reference/#add-on-providers-plans-and-zones-region) lists the zones of each add-on provider. The full catalog of certified services is in the HDS annex to the Clever Cloud general terms of service. Ask support for a copy before you design a health data architecture.

> [!NOTE] The certification covers the host, not your service
> Hosting on an HDS zone doesn't make your own organisation HDS-certified. It requires a specific HDS contract with Clever Cloud, and the certified hosting physically stores the covered health data within the European Economic Area. Contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) before deploying health data.

## SecNumCloud

SecNumCloud is the qualification that the French National Cybersecurity Agency (ANSSI) grants to specific cloud service offers, not to a provider as a whole. It raises the bar above ISO 27001 on traceability, access control, logging, auditing, and protection against non-European laws with extraterritorial reach.

Article 31 of the French law on securing and regulating the digital space (SREN) applies to State administrations, listed State operators, and designated public-interest groups. It concerns cloud services supplied by private-sector providers, when both its sensitivity and potential-harm criteria apply. Under its implementing decree, the service must hold the SecNumCloud qualification, or a European certification that the ANSSI recognizes as equivalent. Limited exemptions can apply to existing projects. The article doesn't impose a general obligation on private organisations, which can still choose qualified services.

Clever Cloud is working towards the qualification of its PaaS offer and of the infrastructure running it. France 2030 funds this work through a program operated by Bpifrance, and the ANSSI runs the qualification process.

You can request a dedicated zone on a partner's SecNumCloud-qualified infrastructure as a service (IaaS) offer. That qualification doesn't extend to the Clever Cloud PaaS running on it: confirm this scope meets your requirements before you deploy. Contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) to have that zone opened.
