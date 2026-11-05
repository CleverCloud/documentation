---
type: docs
linkTitle: GitLab
title: Deploy from GitLab
description: Deploy to Clever Cloud from GitLab CI/CD with the Clever Cloud pipeline components, on gitlab.com, Heptapod Cloud, or a self-managed GitLab instance
keywords:
- gitlab
- gitlab ci/cd
- components
- ci/cd catalog
- heptapod
- deployment
aliases:
- /ci-cd/gitlab
- /doc/ci-cd/gitlab
- /doc/cicd/deploy-from-gitlab
- /doc/gitlab
---

The [Clever Cloud pipeline components](https://gitlab.com/explore/catalog/CleverCloud/clever-cloud-pipeline) add ready-made jobs to your GitLab CI/CD pipeline. The `deploy-to-prod` component deploys the commits of your default branch to an application. To write your own job instead, follow the [CI/CD page](/doc/tools/ci-cd/#gitlab-cicd).

## Deploy the default branch

The component deploys an existing application. Set these masked CI/CD variables in your GitLab project:

- `APP_ID`: the ID of the application, such as `app_…`
- `CLEVER_TOKEN` and `CLEVER_SECRET`: the credentials of Clever Tools, as the [CI/CD page explains](/doc/tools/ci-cd/#prepare-the-credentials)

Then include the component in your `.gitlab-ci.yml`:

```yaml {filename=".gitlab-ci.yml"}
include:
  - component: $CI_SERVER_FQDN/CleverCloud/clever-cloud-pipeline/deploy-to-prod@~latest
```

Each commit of the default branch adds a `deploy to prod` job to the pipeline. This job is manual: start it from the pipeline to deploy the commit. Commits of other branches don't add it.

To deploy each commit of the default branch automatically, set the `when` input:

```yaml {filename=".gitlab-ci.yml"}
include:
  - component: $CI_SERVER_FQDN/CleverCloud/clever-cloud-pipeline/deploy-to-prod@~latest
    inputs:
      when: on_success
```

`@~latest` selects the latest release of the components. To keep the same version until you change it, set a release instead, such as `@2.0.3`. The project also provides components to create, update, and delete review apps.

## Use Heptapod Cloud or a self-managed instance

GitLab includes components from the instance that runs the pipeline only. The path of the components then depends on this instance:

| Instance                                         | Component path                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------------- |
| gitlab.com                                       | `$CI_SERVER_FQDN/CleverCloud/clever-cloud-pipeline/deploy-to-prod@~latest` |
| [Heptapod Cloud](/doc/deploy/services/heptapod/) | `$CI_SERVER_FQDN/pipelines/clever-cloud-pipeline/deploy-to-prod@2.0.3`     |
| Self-managed GitLab                              | `$CI_SERVER_FQDN/<group>/clever-cloud-pipeline/deploy-to-prod@2.0.3`       |

Heptapod Cloud already hosts the components. On a self-managed instance, [mirror the clever-cloud-pipeline project](https://docs.gitlab.com/ci/components/#use-a-gitlabcom-component-on-gitlab-self-managed) first, and set a release such as `@2.0.3`: `@~latest` only works with the CI/CD Catalog.
