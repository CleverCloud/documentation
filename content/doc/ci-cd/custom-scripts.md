---
title: 'Write your own CI/CD'
description:
date: 2024-03-28T12:28:19+01:00
draft: false
type: docs
---

{{< hextra/hero-subtitle >}}
  There are several ways to automate your workflow when deploying your application to Clever Cloud from either GitHub or GitLab. This page explains how to write your custom CI/CD from both platforms.
{{< /hextra/hero-subtitle >}}

## Use Clever Tools

You can write your own pipeline to deploy from either GitHub or GitLab. Use [Clever Cloud CLI](https://github.com/CleverCloud/clever-tools) with either Docker or Node image. Place the following snippets at the top of your `.gitlab-ci.yml` file:

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

{{< content "ci-cd-configuration" >}}

## 🎓 Go further

{{< cards >}}
  {{< card link="https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables" title="GitHub variables" subtitle="List of GitHub default CI/CD variables" icon="github" >}}
  {{< card link="https://docs.gitlab.com/ee/ci/variables/predefined_variables.html" title="GitLab variables" subtitle="List of GitLab predefined variables" icon="gitlab" >}}
  {{< card link="../../cli" title="Clever Tools CLI" subtitle="Deploy and manage your applications and dependencies from your terminal." icon="command-line" >}}
{{< /cards >}}
