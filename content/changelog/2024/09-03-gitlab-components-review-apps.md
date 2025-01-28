---
title: "Version 2.0 of our GitLab Component for review applications is available"
date: 2024-09-03
tags:
  - gitlab
  - component
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Julia March
    link: https://github.com/juliamrch
    image: https://github.com/juliamrch.png?size=40
description: Simplify your GitLab workflows
aliases:
- /changelog/2024-09-03-gitlab-components-review-apps
excludeSearch: true
---

Some months ago, we released [a new GitLab Component](https://gitlab.com/explore/catalog/CleverCloud/clever-cloud-pipeline) to deploy applications from GitLab to Clever Cloud. Version 2.0 is available with variables injection from GitLab CI/CD and automatic releases. You can now use it with the `latest` tag for tests, or `2.0.1` tag for production.

**Breaking changes**: Input `deploy` have been removed to prevent users to script the environment variables injection before deploying the app. Remove it from your `.gitlab-ci.yml` file if it's set up, to avoid breaking your pipeline.

- [Learn more about how to deploy from GitLab to Clever Cloud](/developers/doc/ci-cd/gitlab/)
