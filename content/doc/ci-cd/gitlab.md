---
title: 'Deploy from GitLab'
description:
date: 2024-03-28T12:04:11+01:00
draft: false
type: docs
---

{{< hextra/hero-subtitle >}}
How to set up you CI/CD from GitLab to deploy to Clever Cloud.
{{< /hextra/hero-subtitle >}}

## Use the Components Catalog

GitLab provides its own way of deploying applications to any host provider. The CI/CD system differs from GitHub Actions, but Clever Cloud has already worked on ways to ease the process. Find components in [GitLab Components Catalog](https://gitlab.com/explore/catalog/CleverCloud/clever-cloud-pipeline) to build a modular pipeline for your project.

To use a component, add this snippet to your `.gitlab-ci.yml` file:

```yaml
include:
  - component: $CI_SERVER_HOST/<CI_PROJECT_PATH>/<component-name>@~latest
```

{{< content "ci-cd-configuration" >}}

### GitLab pipeline example

For example, to deploy any commit on your production app, use:

```yaml
include:
  - component: $CI_SERVER_HOST/<CI_PROJECT_PATH>/deploy-to-prod@~latest
```

This assumes you have a running app on Clever Cloud. Any commit on your default branch (`main`, `master` or other name) triggers a deployment for this app. [Inject the following variables in your GitLab repository settings](https://docs.gitlab.com/ee/ci/variables/index.html#for-a-project):

- `APP_ID`: Find it at the top right in [Clever Cloud Console](https://console.clever-cloud.com), in your application tab.
- `CLEVER_TOKEN` and `CLEVER_SECRET`

### `<CI_PROJECT_PATH>` configuration

In the project you want to deploy, replace `<CI_PROJECT_PATH>` with the actual path of the components, otherwise this variable fetches your project current path (which doesn't host the CI/CD components). Depending on your platform, path can be different.

#### On gitlab.com

```yaml
- component: $CI_SERVER_HOST/CleverCloud/clever-cloud-pipeline/deploy-to-prod@~latest
```

#### On Heptapod

```yaml
- component: $CI_SERVER_HOST/pipelines/clever-cloud-pipeline/deploy-to-prod@~latest
```

#### On your self-hosted instance

```yaml
- component: $CI_SERVER_HOST/<group>/<project>/deploy-to-prod@~latest
```

### Deploy from a self-hosted GitLab instance

You can use pipeline components to deploy from a self-hosted GitLab instance, by including it as a project and mirroring the pipeline repository. Follow [GitLab documentation](https://docs.gitlab.com/ee/ci/components/#use-a-gitlabcom-component-in-a-self-managed-instance) to get full instructions.

#### Deploy directly from Heptapod

The self-hosted GitLab service on Clever Cloud with [Heptapod]({{< ref "/doc/addons/heptapod" >}}) already hosts the components, you don't need to do any set up like you would in a self-hosted instance:

1. Create a `.gitlab-ci.yml` at the root of your repository with [the component to use]({{< ref "/doc/ci-cd/gitlab/#use-the-components-catalog" >}})
2. Add [the variables]({{< ref "/doc/ci-cd/gitlab/#mandatory-configuration" >}}) to your repository settings
3. Run the pipeline

## Troubleshooting

If you encounter troubles or bugs using the GitLab component, feel free to open an issue [on the repository](https://gitlab.com/CleverCloud/clever-cloud-pipeline/-/issues):

## 🎓 Go further

{{< cards >}}
  {{< card link="https://docs.gitlab.com/ee/ci/components" title="GitLab Components" subtitle="Learn how to use GitLab components" icon="gitlab" >}}
  {{< card link="../../cli" title="Clever Tools CLI" subtitle="Deploy and manage your applications and dependencies from your terminal." icon="command-line" >}}
{{< /cards >}}
