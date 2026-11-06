---
type: docs
linkTitle: CI/CD
title: Deploy from your own CI/CD pipeline
description: Run Clever Tools in a GitHub Actions workflow, a GitLab CI/CD job, or any other pipeline to deploy your application to Clever Cloud after your own steps
keywords:
- ci-cd
- pipelines
- github actions
- gitlab ci
- clever-tools
- deployment
aliases:
- /ci-cd
- /doc/administrate/ci-cd
- /doc/ci-cd
- /doc/tools-integrations/ci-cd/
- /doc/ci-cd/custom-scripts
---

To deploy from a pipeline you control, for example once your tests pass, run [Clever Tools](/doc/tools/cli/) in a job. To avoid writing this job yourself, the [GitHub integration](/doc/tools/github/) deploys each push to a branch without any pipeline, and the [GitLab components](/doc/tools/gitlab/) add a ready-made deployment job to your pipeline.

## Prepare the credentials

When `CLEVER_TOKEN` and `CLEVER_SECRET` are set, Clever Tools uses them instead of a login. To get them, log in with Clever Tools on your computer, then read the active profile from its configuration file. On Linux and macOS, with [`jq`](https://jqlang.org/) installed:

```bash
clever login
jq -r '.profiles[0] | "CLEVER_TOKEN=\(.token)\nCLEVER_SECRET=\(.secret)"' ~/.config/clever-cloud/clever-tools.json
```

Store both values as masked secrets of your pipeline, and the ID of your application, such as `app_…`, as a variable named `APP_ID`. These credentials expire: `clever profile` shows their expiration date, log in again before it to replace them.

## Write the deployment job

A deployment job runs two commands from the repository of your application:

```bash
# Not needed if a committed .clever.json already links the application
clever link "$APP_ID"
clever deploy --same-commit-policy rebuild
```

`clever deploy` pushes the commit the job checked out to Clever Cloud, then follows the deployment until it ends, and fails if the deployment fails. It doesn't accept `--app`: `clever link` selects the application first. It needs the complete history of the repository, while most CI systems clone only the last commit. From a shallow clone, it fails with `your repository is shallow and therefore cannot be pushed`.

Two options of `clever deploy` handle the cases a pipeline meets:

- `--same-commit-policy` sets what happens when this commit has already been pushed to Clever Cloud, for example when you rerun a job: `rebuild`, `restart`, `ignore`, or `error`, the default, which fails the job
- `--force` deploys a commit whose history differs from the one of the application, after you rewrite it for example. Without it, `clever deploy` refuses with `Push rejected because it was not a simple fast-forward`

## GitHub Actions

This workflow deploys each push to `main`. Set `CLEVER_TOKEN` and `CLEVER_SECRET` as repository secrets, and `APP_ID` as a repository variable:

```yaml {filename=".github/workflows/deploy.yml"}
name: Deploy to Clever Cloud

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v7
        with:
          node-version: 24
      - name: Deploy
        env:
          CLEVER_TOKEN: ${{ secrets.CLEVER_TOKEN }}
          CLEVER_SECRET: ${{ secrets.CLEVER_SECRET }}
          APP_ID: ${{ vars.APP_ID }}
        run: |
          # Not needed if a committed .clever.json already links the application
          npx --yes clever-tools@latest link "$APP_ID"
          npx --yes clever-tools@latest deploy --same-commit-policy rebuild
```

`fetch-depth: 0` clones the complete history, and `setup-node` installs Node.js 24, which Clever Tools uses. Add your test jobs before this one, and make it depend on them with `needs`.

## GitLab CI/CD

This job deploys each commit of the default branch, with the [clevercloud/clever-tools](https://hub.docker.com/r/clevercloud/clever-tools) Docker image. Set `CLEVER_TOKEN`, `CLEVER_SECRET`, and `APP_ID` as masked CI/CD variables of the project:

```yaml {filename=".gitlab-ci.yml"}
deploy:
  stage: deploy
  image:
    name: clevercloud/clever-tools:latest
    entrypoint: [""]
  variables:
    GIT_DEPTH: 0
  script:
    # Not needed if a committed .clever.json already links the application
    - clever link "$APP_ID"
    - clever deploy --same-commit-policy rebuild
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

`GIT_DEPTH: 0` clones the complete history, and `entrypoint: [""]` replaces the `clever` entrypoint, so GitLab can run the script in a shell.

## Other pipelines

Any pipeline that can run a container or Node.js 24 works the same way: clone the complete history, set the three variables, then run `clever link` and `clever deploy`. The [clevercloud/clever-tools](https://hub.docker.com/r/clevercloud/clever-tools) Docker image also includes `git`, which `clever deploy` needs. To pin a version of Clever Tools, use a tag such as `clevercloud/clever-tools:5.3.0`, or `npx --yes clever-tools@5.3.0`.
