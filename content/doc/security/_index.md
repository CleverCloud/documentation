---
type: docs
weight: 150
linkTitle: Security & Compliance
title: Security & Compliance
description: Secure your applications and data on Clever Cloud with encryption, TLS, access control and secrets
keywords:
- security
- compliance
- encryption
- tls
- secrets
- access control
---

Certifications cover what the infrastructure is audited against. Everything else is a control you hold, and most are opt-in: roles decide what each member of an organisation can do, secrets belong outside your code, and encryption at rest and antivirus scanning are enabled per resource. TLS certificates are the exception, generated and renewed for your domains without configuration.

{{< cards >}}
  {{< card link="/developers/doc/security/certifications" title="Certifications" subtitle="Standards the infrastructure is audited against" icon="document-check" >}}
  {{< card link="/developers/doc/security/clamav" title="ClamAV" subtitle="Antivirus scanning inside your application" icon="magnifying-glass" >}}
  {{< card link="/developers/doc/security/encryption-at-rest" title="Encryption at rest" subtitle="Encrypt add-on data stored on disk" icon="lock-closed" >}}
  {{< card link="/developers/doc/security/iam-roles" title="IAM (Roles)" subtitle="Organisations, members and their privileges" icon="user-group" >}}
  {{< card link="/developers/doc/security/kms" title="Secrets & Transit" subtitle="Serverless secret store on Materia, compatible with Vault and Bao" icon="key" >}}
  {{< card link="/developers/doc/security/ssl" title="TLS Certificates" subtitle="Automatic Let's Encrypt certificates, or bring your own" icon="shield-check" >}}
{{< /cards >}}
