---
type: docs
weight: 180
linkTitle: Tools & Integrations
title: Tools & Integrations
description: Automate deployments and integrate Clever Cloud with CI/CD, GitHub, GitLab and Terraform
keywords:
- ci/cd
- github
- gitlab
- terraform
- kubernetes operator
- automation
aliases:
- /doc/reference
- /doc/tools/reference
- /doc/administrate/tools/
- /reference
---

Deploying from Git needs no pipeline: connect a GitHub repository and pick the branch each application tracks. Beyond that, a GitHub Action creates a review app per pull request, GitLab components drop a deploy job into `.gitlab-ci.yml`, and Clever Tools covers anything custom. Terraform declares resources instead, as does the Kubernetes operator for add-ons.

{{< cards >}}
  {{< card link="/developers/doc/tools/ci-cd" title="CI/CD" subtitle="Run Clever Tools from a Docker or Node image in your own pipeline" icon="arrow-path" >}}
  {{< card link="/developers/doc/tools/github" title="GitHub" subtitle="Branch-based integration, plus a review app Action for pull requests" icon="github" >}}
  {{< card link="/developers/doc/tools/gitlab" title="GitLab" subtitle="Components Catalog jobs for gitlab.com, self-hosted and Heptapod" icon="git" >}}
  {{< card link="/developers/doc/tools/terraform" title="Terraform" subtitle="Declare applications, add-ons and networking as code" icon="document-check" >}}
{{< /cards >}}
