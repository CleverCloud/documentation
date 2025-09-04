---
type: docs
linkTitle: Git
title: Git on Clever Cloud
description: Learn how Git-based deployments work on Clever Cloud, including remotes, branches, shallow clones, monorepos, and private submodules
keywords:
- git
- deployment
- submodule
- commit
---
{{< hextra/hero-subtitle >}}
  Clever Cloud uses Git-based deployments. This guide explains how to deploy with Git and handle common scenarios.
{{< /hextra/hero-subtitle >}}
## Git-based deployments

Clever Cloud deploys your application when you push to the Clever Git remote.

### Configure the Git remote

```bash
git remote add clever <your-git-deployment-url>
```

Find the deployment URL in the Console → your application → Information. See [Troubleshooting](/doc/find-help/troubleshooting/) for additional examples.

### Push branches

```bash
# If your local branch is main
git push clever main:master

# If your local branch is master
git push clever master
```

The Clever remote expects the branch named `master`. Map your local branch accordingly.

### Shallow clone vs full clone

By default, deployments perform a full clone. To speed up deployments, set `CC_GIT_FULL_CLONE=false` to use a shallow clone (`--depth 1`). See the [Environment variable reference](/doc/reference/reference-environment-variables/#variables-you-can-define).

### Monorepos (subdirectory deploy)

If your application lives in a subdirectory, set `APP_FOLDER` to that path (relative to the repository root). See the [Environment variable reference](/doc/reference/reference-environment-variables/#variables-you-can-define).

### Deploy private Git submodules

If your application uses private Git submodules, avoid storing credentials in `.gitmodules`. Use SSH URLs and provide an SSH key at deploy time.

1. Use an SSH URL for each submodule

```bash
# Add a new submodule (example)
git submodule add git@github.com:org/repo.git path/to/subdir
```

2. Provide an SSH key for the build

  - Set the `CC_SSH_PRIVATE_KEY` environment variable with a private key that has read access to your submodule(s).
  - Optionally set `CC_SSH_PRIVATE_KEY_FILE` to control the filename used on the instance.
  - The key is installed into `~/.ssh` before the build so Git operations (including submodules) can authenticate.
  - Alternatively, commit `clevercloud/ssh.json` to reference a private key file in your repo (see the linked documentation for the expected format).

{{< callout type="info" >}}
Provide a key without pass phrase. Submodules are initialized during deployment unless you disable them with `CC_DISABLE_GIT_SUBMODULES`.
{{< /callout >}}

[Learn more: Private SSH key configuration](/doc/reference/common-configuration/#private-ssh-key) · [Environment variable reference](/doc/reference/reference-environment-variables/)
