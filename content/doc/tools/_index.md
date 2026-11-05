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

Deploying from GitHub needs no pipeline: the GitHub integration deploys each push to the branch an application follows. A GitHub Action can also create a review app for each pull request. In GitLab CI/CD, the Clever Cloud components add a deployment job, and in any other pipeline, Clever Tools runs in a job of your own. [Terraform](/doc/tools/terraform/) declares your resources as code, as the [Kubernetes operator](/doc/deploy/kubernetes/operator/) does for add-ons.

{{< cards >}}
  {{< card link="/developers/doc/tools/ci-cd" title="CI/CD" subtitle="Run Clever Tools in GitHub Actions, GitLab CI/CD, or any other pipeline" icon="arrow-path" >}}
  {{< card link="/developers/doc/tools/github" title="GitHub" subtitle="Deploy each push to a branch, and a review app for each pull request" icon="github" >}}
  {{< card link="/developers/doc/tools/gitlab" title="GitLab" subtitle="Pipeline components for gitlab.com, Heptapod Cloud, and self-managed instances" icon="git" >}}
  {{< card link="/developers/doc/tools/terraform" title="Terraform" subtitle="Declare applications, add-ons and networking as code" icon="document-check" >}}
{{< /cards >}}
