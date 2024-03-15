---
weight: 9
title: 'CI/CD'
date: 2024-03-15T13:14:53+01:00
description: Deploy to Clever Cloud from GitLab or GitHub
draft: false
type: docs
---

{{< hextra/hero-subtitle >}}
  There are several ways to automate your workflow when deploying your application to Clever Cloud from either GitHub or GitLab. This page explains how to set up you CI/CD from both platforms.
{{< /hextra/hero-subtitle >}}

## Deploy from GitHub

Clever Cloud provides a GitHub integration to deploy any repository hosted on GitHub to Clever Cloud. You can deploy the same repository to multiple Clever Cloud applications from different branches. Select the appropriate branch in you application menu, in **Information** > **Application edition** > **Used GitHub branch for deployment**.

![GitHub branch deployment](/images/doc/github-branches.png)

Clever Cloud asks for permission to access your GitHub repositories. Accept the permissions to allow the deployment. You can deploy both public or private repositories.

### Deploy review apps from a PR on GitHub

You can automate deployments for review apps when a Pull Request opens on your GitHub repository by using Clever Cloud [GitHub Action](https://github.com/marketplace/actions/clever-cloud-review-app-on-pull-requests). This action uses Clever Cloud [CLI](/doc/CLI) to deploy a new app from the branch the Pull Request is based on and post a comment with the URL of the review app. The action redeploys the app on every new commit and deletes it when the Pull Request is closed (merged or not).

#### How to use the Review App GitHub Action

Two things are necessary to use the action:

1. **Use the script:** Place [the script](https://github.com/CleverCloud/clever-cloud-review-app/blob/main/action.yml) in your `.github/workflows` directory and input the appropriate value to deploy your app. The script already provides a template you can modify at your convenience.
2. **Inject the environment variables from your repository:** From your GitHub repository go to **Settings** > **Secrets and variables**. Inject them both in "Environment secrets" and "Repository secrets" to allow deployments from forked repositories.

Full instructions are available on the [Action project](https://github.com/CleverCloud/clever-cloud-review-app).

#### Review App workflow example

To see a Review App workflow already in use, see [this workflow on GitHub](https://github.com/CleverCloud/documentation/blob/main/.github/workflows/review-app.yml).

## Deploy from GitLab

GitLab provides it's own way of deploying applications to any host provider. The CI/CD system differs from GitHub Actions, but Clever Cloud has already worked on ways to ease the process. Find Clever Cloud pipeline components in [GitLab Components Catalog](https://gitlab.com/explore/catalog/CleverCloud/clever-cloud-pipeline) to build a modular pipeline for your project.

To use a component, add this snippet to your `.gitlab-ci.yml` file:

```yaml
include:
  - component: gitlab.com/CleverCloud/clever-cloud-pipeline/<component-name>@~latest
```

### GitLab pipeline example

For example, to deploy any commit on your production app, use: 

```yaml
include:
  - component: gitlab.com/CleverCloud/clever-cloud-pipeline/deploy-to-prod@~latest
```

This assumes you have a running app on Clever Cloud. Any commit on your default branch (`main`, `master` or other name) triggers
 a deployment for this app. [Inject the following variables in your GitLab repository settings](https://docs.gitlab.com/ee/ci/variables/index.html#for-a-project):

- `APP_ID`: you app_id on Clever Cloud, find it at the top right in Clever Cloud Console, in your application tab.
- `CLEVER_TOKEN` and `CLEVER_SECRET`: find it in your machine, usually in `~/.config/clever-cloud/clever-tools.json`, after [installing the CLI](/doc/CLI).

{{< callout type="warning" >}}
  `CLEVER_TOKEN` and `CLEVER_SECRET` expire after one year. Make sure to set a reminder to inject the new ones to avoid breaking your pipelines.
{{< /callout >}}

### Deploy from a self-hosted GitLab instance

You can use pipeline components to deploy from a self-hosted GitLab instance, by including it as a project and mirroring the Pipeline repository. Follow [GitLab documentation](https://docs.gitlab.com/ee/ci/components/#use-a-gitlabcom-component-in-a-self-managed-instance) to get full instructions.

### Write your own CI/CD script

You can write your own pipeline following the same model. Use Clever Cloud CLI using either [clever-tools](https://github.com/CleverCloud/clever-tools) Docker or Node image. Place the following snippets at the top of your `.gitlab-ci.yml` file:

{{< tabs items="Docker image, Node image" >}}

  {{< tab >}}**Docker image**:
  
  ```yaml
  variables:
  GIT_DEPTH: "0" # Unshallow the repository by default

image:
  name: clevercloud/clever-tools:latest
  entrypoint: [""]
  ```
  
  {{< /tab >}}
  
  {{< tab >}}**Node image**:  
  
  ```yaml
  variables:
  GIT_DEPTH: 0 # Unshallow the repository by default

before_script: # Download clever-tools before any script executes
  - CC_VERSION=latest
  - curl -s -O https://clever-tools.clever-cloud.com/releases/${CC_VERSION}/clever-tools-${CC_VERSION}_linux.tar.gz
  - tar -xvf clever-tools-${CC_VERSION}_linux.tar.gz
  - PATH=${PATH}:$(pwd)/clever-tools-${CC_VERSION}_linux
  ```
  
  {{< /tab >}}

{{< /tabs >}}

{{< callout type="warning" >}}
  Using `before_script` in your GitLab pipeline affects your other scripts as well. Consider including it **in a separate job** if you run other test scripts unrelated to Clever Cloud deployments in your pipeline.
{{< /callout >}}

## Troubleshooting

If you encounter troubles or bugs using either the GitHub Action or the GitLab component, feel free to open an issue on one of the repositories:

- [Open an issue on GitHub](https://github.com/CleverCloud/clever-cloud-review-app/issues/new)
- [Open an issue on GitLab](https://gitlab.com/CleverCloud/clever-cloud-pipeline/-/issues/new)

## 🎓 Go further

{{< cards >}}
  {{< card link="https://docs.github.com/en/actions" title="GitHub Actions documentation" subtitle="Find help in GitHub Actions documentation" icon="github" >}}
  {{< card link="https://docs.gitlab.com/ee/ci/components" title="GitLab Components" subtitle="Learn how to use GitLab components" icon="gitlab" >}}
  {{< card link="/doc/cli" title="Clever Tools CLI" subtitle="Deploy and manage your applications and dependencies from your terminal." icon="command-line" >}}
{{< /cards >}}
