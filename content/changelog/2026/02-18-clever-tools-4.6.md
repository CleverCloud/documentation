---
title: "Clever Tools 4.6: multi-profile, config providers, system Git and AI skill"
date: 2026-02-18
description: Clever Tools 4.6 adds multi-profile account management, config provider CLI commands, faster deploys with system Git and an AI coding skill
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
excludeSearch: true
---

[Clever Tools 4.6.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.6.0) is available. This release brings multi-profile support, config provider commands, add-on logs migration to the v4 API, optional system Git support and an AI assistant skill.

## Multi-profile support

You can now login to multiple Clever Cloud accounts, each with its own credentials and alias. New commands allow you to list and switch between profiles, making it easier to work across different accounts or environments from a single machine. Each profile can also have per-profile endpoint and OAuth overrides configured during login for custom Clever Cloud deployments.

```bash
# Create named profiles
clever login --alias personal
clever login --alias work

# Create a profile with custom API endpoint
clever login --alias staging --api-host https://clever-cloud-api.example.com

# List all profiles
clever profile list

# Switch to another profile
clever profile switch --alias work

# With exactly 2 profiles, switch to the other one
clever profile switch

# Display the current profile
clever profile
```

## Config providers

New `config-provider` commands are now available, giving you direct access to manage [config providers](/doc/addons/config-provider/) from the CLI. You can list, get, set, remove and import environment variables.

```bash
# List all config providers
clever config-provider list

# Get variables from a config provider (by name or ID)
clever config-provider get my-config-provider

# Export variables in shell format
clever config-provider get my-config-provider --format shell

# Set a variable
clever config-provider set my-config-provider MY_VAR "my-value"

# Remove a variable
clever config-provider rm my-config-provider MY_VAR

# Import variables from a .env file
cat my-vars.env | clever config-provider import my-config-provider

# Import variables from JSON
echo '[{"name":"FOO","value":"bar"}]' | clever config-provider import my-config-provider -F json
```

## AI assistant skill

Clever Tools is now available as a skill for AI coding assistants such as Claude Code, Codex, Cursor or GitHub Copilot. Once installed, the assistant gets knowledge of CLI commands, Clever Cloud concepts, available runtimes, add-on providers and common workflows.

```bash
# Install the skill for your AI coding assistant
npx skills add CleverCloud/clever-tools
```

## System Git support (beta)

By default, Clever Tools uses an embedded JavaScript Git implementation for deploy operations. While it works without requiring Git to be installed, it can be slow on large repositories or branches with rewritten history (rebases, squashes), and does not support SSH-based protocols.

You can now opt in to use your system's native `git` command instead, for faster and more reliable deployments. This feature is currently in beta and requires `git` to be available in your `PATH`.

```bash
# Enable system Git
clever features enable system-git

# Deploy as usual, now using your system's git
clever deploy

# Disable if not needed anymore
clever features disable system-git
```

## How to upgrade

To upgrade Clever Tools, [use your favorite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
