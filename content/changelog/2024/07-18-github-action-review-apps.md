---
title: "Version 1.0 of our GitHub Action for review applications is available"
date: 2024-07-18
tags:
  - github
  - action
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Julia March
    link: https://github.com/juliamrch
    image: https://github.com/juliamrch.png?size=40
description: Simplify your GitHubworkflows
aliases:
- /changelog/2024-07-18-github-action-review-apps
excludeSearch: true
---

Some months ago, Clever Cloud released [a new GitHub Action](https://github.com/marketplace/actions/clever-cloud-review-app-on-prs) to deploy applications from GitHub to Clever Cloud. After some iterations, version 1.0 is available. We make it simpler to use by making it [composite](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action)). Now you can just add this in your workflow for example:

```yml
- name: Create review app
        uses: CleverCloud/clever-cloud-review-app@latest
        env:
          CLEVER_SECRET: ${{ secrets.CLEVER_SECRET }}
          CLEVER_TOKEN: ${{ secrets.CLEVER_TOKEN }}
          ORGA_ID: ${{ secrets.ORGA_ID }}
        with:
          type: '<type-of-app>'
```

- [Learn more about how to deploy from GitHub to Clever Cloud](/developers/doc/ci-cd/github/)