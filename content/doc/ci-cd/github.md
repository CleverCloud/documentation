---
title: 'Deploy from GitHub'
description:
date: 2024-03-28T12:04:20+01:00
draft: false
type: docs
---

{{< hextra/hero-subtitle >}}
  How to set up you CI/CD from GitHub directly from Clever Cloud, and how to deploy review apps.
{{< /hextra/hero-subtitle >}}

## Use the GitHub integration

Clever Cloud provides a GitHub integration to deploy any repository hosted on GitHub to Clever Cloud. You can deploy the same repository to multiple Clever Cloud applications from different branches. Select the appropriate branch in you application menu, in **Information** > **Application edition** > **Used GitHub branch for deployment**.

![GitHub branch deployment](/images/doc/github-branches.png)

Clever Cloud asks for permission to access your GitHub repositories. Accept the permissions to allow the deployment. You can deploy both public or private repositories.

### Deploy review apps from a PR on GitHub

You can automate deployments for review apps when a Pull Request opens on your GitHub repository by using Clever Cloud [GitHub Action](https://github.com/marketplace/actions/clever-cloud-review-app-on-prs). This action uses [Clever Tools]({{< ref "doc/cli" >}}) to deploy a new app from the branch the Pull Request is based on and post a comment with the URL of the review app. The action redeploys the app on every new commit and deletes it when the Pull Request is closed (merged or not).

#### How to use the Review App GitHub Action

Two things are necessary to use the action:

1. **A workflow file to run the action**. For example, `.github/workflow/review-app.yml`. At the top of this file, define the event trigger for running the action:

```yaml
on:
  pull_request_target:
    types: [opened, closed, synchronize, reopened]
    branches: [ main ]
```
Then, use the action and define the mandatory input:

```yaml
- name: Create review app
        uses: CleverCloud/clever-cloud-review-app@latest
        env:
          CLEVER_SECRET: ${{ secrets.CLEVER_SECRET }}
          CLEVER_TOKEN: ${{ secrets.CLEVER_TOKEN }}
          ORGA_ID: ${{ secrets.ORGA_ID }}
        with:
          type: '<type-of-app>'
```

2. **Inject the environment variables from your repository:** From your GitHub repository go to **Settings** > **Secrets and variables**. Inject them both in "Environment secrets" and "Repository secrets" to allow deployments from forked repositories. Then add them with an `GH_` prefix in your workflow file (this will prevent the injection of the GitHub runner variables in your app). Finally, enable the injection with `set-env: true`:

```yaml
name: Create review app
        uses: CleverCloud/clever-cloud-review-app@latest
        env:
          CLEVER_SECRET: ${{ secrets.CLEVER_SECRET }}
          CLEVER_TOKEN: ${{ secrets.CLEVER_TOKEN }}
          ORGA_ID: ${{ secrets.ORGA_ID }}
          GH_CC_RUN_SUCCEEDED_HOOK: ${{ secrets.CC_RUN_SUCCEEDED_HOOK }} # This environment variable will be set on Clever Cloud
        with:
          type: '<type-of-app>'
          set-env: true # Enables the command to set en vars on Clever Cloud
```


{{< content "ci-cd-configuration" >}}

Full instructions are available on the [Action project](https://github.com/CleverCloud/clever-cloud-review-app).

#### Review App workflow example

To see a Review App workflow already in use, see [this workflow on GitHub](https://github.com/CleverCloud/clever-cloud-review-app/blob/main/.github/workflows/main.yml).

## Troubleshooting

If you encounter troubles or bugs using the GitHub Action, feel free to open an issue [on the repository](https://github.com/CleverCloud/clever-cloud-review-app/issues/new).

## 🎓 Go further

{{< cards >}}
  {{< card link="https://docs.github.com/en/actions" title="GitHub Actions documentation" subtitle="Find help in GitHub Actions documentation" icon="github" >}}
  {{< card link="../../cli" title="Clever Tools CLI" subtitle="Deploy and manage your applications and dependencies from your terminal." icon="command-line" >}}
{{< /cards >}}
