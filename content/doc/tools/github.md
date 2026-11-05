---
type: docs
linkTitle: GitHub
title: Deploy from GitHub
description: Deploy each push to a branch of a GitHub repository with the Clever Cloud GitHub integration, and create a review app for each pull request with a GitHub Action
keywords:
- github
- github integration
- review apps
- pull requests
- github actions
- deployment
aliases:
- /doc/ci-cd/github
- /doc/tools-integrations/github/
- /doc/github
---

The Clever Cloud GitHub integration deploys each push to a branch of your repository, without any pipeline. To deploy only after your tests pass, use a [GitHub Actions workflow](/doc/tools/ci-cd/#github-actions) instead, and to deploy a review app for each pull request, use the [review app Action](#deploy-a-review-app-for-each-pull-request).

## Create an application from a GitHub repository

In the [Console](https://console.clever-cloud.com), create an application. In the **Create an application from a GitHub repository** section, click **Link your GitHub account**, then authorize Clever Cloud on GitHub. Once your account is linked, select your repository in **Select your GitHub repository**: the Console lists the public and private repositories your GitHub account can access. Then choose the runtime and the other settings of your application.

With [Clever Tools](/doc/manage/cli/), set the repository with `--github`, once your GitHub account is linked:

```bash
clever create --type node my-app --github my-org/my-repository
```

Clever Cloud then adds a webhook to the repository, which requires administration rights on it. Each push to the branch the application follows, the default one at first, deploys it right away, without waiting for the checks of the commit.

## Choose the deployed branch

To deploy another branch, open your application in the [Console](https://console.clever-cloud.com), then its **Information** tab. Select the branch in **Application edition** > **Used GitHub branch for deployment**, then click **Save**. The application deploys it on the next push to this branch, or on a restart.

Several applications can deploy the same repository, each from its own branch, such as a `staging` application that follows `staging` and a production one that follows `main`. A push to a branch then only deploys the applications that follow it.

## Deploy a review app for each pull request

The [Clever Cloud review app Action](https://github.com/marketplace/actions/clever-cloud-review-app-on-prs) creates an application for each pull request, and keeps it up to date:

- When the pull request opens or reopens, it creates an application named `<repository>-PR-<number>`, adds the `<repository>-pr-<number>.cleverapps.io` domain, deploys the branch, and comments the pull request with its URL
- On each new push to the branch, it deploys the new commit
- When the pull request closes, merged or not, it deletes the application

Set `CLEVER_TOKEN` and `CLEVER_SECRET` as repository secrets, as the [CI/CD page explains](/doc/tools/ci-cd/#prepare-the-credentials). Set the ID of the organisation where the action creates the applications, such as `orga_…`, as a repository variable named `ORGA_ID`. Then add this workflow:

```yaml {filename=".github/workflows/review-app.yml"}
name: Review app

on:
  pull_request:
    types: [opened, reopened, synchronize, closed]
    branches: [main]

permissions:
  contents: read
  pull-requests: write

jobs:
  review-app:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
      - uses: CleverCloud/clever-cloud-review-app@v2
        env:
          CLEVER_TOKEN: ${{ secrets.CLEVER_TOKEN }}
          CLEVER_SECRET: ${{ secrets.CLEVER_SECRET }}
          ORGA_ID: ${{ vars.ORGA_ID }}
        with:
          type: static
```

Set `type` to the runtime of your application, such as `node` or `php`. The action doesn't check out your code: the `actions/checkout` step checks out the latest commit of the pull request, with the complete history `clever deploy` needs. The `pull-requests: write` permission lets the action comment the pull request. The domain of a new review app can take a minute to answer.

GitHub doesn't pass secrets to the workflows of pull requests from forks: the `if` condition skips them, so this workflow creates review apps for branches of your repository only. The [Action repository](https://github.com/CleverCloud/clever-cloud-review-app) lists its other inputs, such as the region or the flavor, and is where to report an issue.
