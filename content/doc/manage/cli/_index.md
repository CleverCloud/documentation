---
type: docs
weight: 100
linkTitle: Clever Tools (CLI)
title: Clever Tools (CLI)
description: Use Clever Tools CLI to manage applications, add-ons, and deployments from the command line with powerful automation and monitoring features
keywords:
- cli
- clever-tools
- command-line
- automation
- deployments
- applications
aliases:
- /clever-tools/getting_started
- /cli
- /doc/CLI
- /doc/administrate/clever-tools/getting_started
- /doc/administrate/cli
- /doc/clever-cloud-cli
- /doc/clever-tools/getting_started
- /doc/clever-tools/manage
- /doc/cli
- /doc/cli/getting_started
- /doc/getting-started/cli
- /doc/quickstartcli
- /doc/reference/clever-tools
- /doc/reference/clever-tools/getting_started
- /getting-started/cli
---

Clever Tools is the command line interface (CLI) of Clever Cloud. You can use it to create and manage multiple services of the platform as applications, databases or storage add-ons. It also provides easy authenticated access to Clever Cloud public APIv2 and APIv4 through the [`clever curl` command](#curl). It's an [easy to set up](install) multiplatform and open source tool, based on Node.js.

You can contribute to it through [issue](https://github.com/CleverCloud/clever-tools/issues) or [pull requests](https://github.com/CleverCloud/clever-tools/pulls). Ask for new features, enhancements or help us to provide them to our community.

- [How to install Clever Tools](install)
- [Create a Clever Cloud account](https://console.clever-cloud.com)

Use Clever Tools through `npx` or `npm exec` for one-off usage or in CI/CD pipelines for example:

```bash
# Set/Export CLEVER_TOKEN and CLEVER_SECRET to login with a given account
# --yes is used to skip the interactive prompts
npx --yes clever-tools@latest version
npm exec -- clever-tools@3.14 profile --format json
```

You'll find below the first commands to know to connect Clever Tools to your account, get its information and manage some options. Others are developed in dedicated pages:

{{< cards >}}
  {{< card link="/developers/doc/manage/cli/install" title="Install" icon="arrow-down-tray" >}}
  {{< card link="/developers/doc/manage/cli/addons" title="Create and manage add-ons" icon="wrench-screwdriver" >}}
  {{< card link="/developers/doc/manage/cli/applications" title="Create and manage applications" icon="code-bracket" >}}
  {{< card link="/developers/doc/manage/cli/kubernetes" title="Kubernetes" icon="kubernetes" >}}
  {{< card link="/developers/doc/manage/cli/kv-stores" title="Manage KV stores" icon="server-stack" >}}
  {{< card link="/developers/doc/manage/cli/logs-drains" title="Manage logs and drains" icon="command-line" >}}
  {{< card link="/developers/doc/manage/cli/network-groups" title="Network Groups" icon="tcp-ip-service" >}}
  {{< card link="/developers/doc/manage/cli/notifications-webhooks" title="Notifications and webhooks" icon="bell" >}}
  {{< card link="/developers/doc/manage/cli/operators" title="Operators (managed services)" icon="document-check" >}}
  {{< card link="/developers/doc/manage/cli/profiles" title="Profiles and overrides" icon="user" >}}
  {{< card link="/developers/doc/manage/cli/services-depedencies" title="Service dependencies" icon="endpoints" >}}
{{< /cards >}}

## basic commands

To show Clever tools available commands, use:

```console
clever
clever help
```

For each of them, you can add these parameters:

```console
[--help, -?]            Display help about this program (default: false)
[--version, -V]         Display the version of this program (default: false)
[--color]               Choose whether to print colors or not. You can also use --no-color (default: true)
[--update-notifier]     Choose whether to use update notifier or not. You can also use --no-update-notifier (default: true)
[--verbose, -v]         Verbose output (default: false)
```

> [!TIP]
> For commands returning a list of items, you can use `--format json` or `-F json` to get a JSON output.

## TLS certificates (corporate proxy / custom CA)

Clever Tools verifies the TLS certificate of every HTTPS connection it makes, both for API calls and for Git-based deployments. Behind a corporate proxy that intercepts HTTPS, or when your endpoint relies on a private or self-signed Certificate Authority (CA), this verification can fail with an error such as:

```text
Error: self signed certificate in certificate chain
```

The right fix is to make Clever Tools trust your CA, not to disable verification. There are two ways to do it, depending on whether your CA is installed system-wide or only available as a file.

### Trust your operating system's certificate store

If your corporate or proxy root CA is installed at the OS level (Windows Certificate Store, macOS Keychain, Linux `/etc/ssl/certs`), Clever Tools can rely on it. The binary already trusts the OS certificate store, there is nothing to do. The npm package runs on your own Node.js, so enable it explicitly:

```bash
NODE_OPTIONS=--use-system-ca clever profile
```

If the CA isn't in the OS store yet, ask your IT team to install it there: other tools relying on the OS certificate store then trust it too, not only Clever Tools.

### Trust a specific certificate

When the CA is only available as a file, set the `NODE_EXTRA_CA_CERTS` environment variable to its path. This works the same way for both the binary and npm installs. The file must be PEM-encoded and may contain several certificates:

{{< tabs >}}
  {{< tab name="Linux / macOS" >}}

  ```bash
  export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca.pem
  clever profile
  ```

  {{< /tab >}}
  {{< tab name="Windows (PowerShell)" >}}

  ```powershell
  $env:NODE_EXTRA_CA_CERTS = "C:\path\to\corporate-ca.pem"
  clever profile
  ```

  {{< /tab >}}
{{< /tabs >}}

Node.js reads `NODE_EXTRA_CA_CERTS` and `NODE_OPTIONS` at startup: set them in your shell, or inline before the command, not in a `.env` file.

### Git-based deployments

`clever deploy` pushes over HTTPS and verifies certificates too. By default, it delegates to your system `git` binary, which ignores `NODE_EXTRA_CA_CERTS` and follows its own TLS configuration: the OS certificate store (recommended), or an explicit CA file set with `git config --global http.sslCAInfo /path/to/corporate-ca.pem`, equivalent to the `GIT_SSL_CAINFO` environment variable.

If you fall back to the previous JavaScript Git implementation (`clever features disable system-git`), Clever Tools handles Git operations on Node.js instead. It then trusts the OS certificate store and `NODE_EXTRA_CA_CERTS` exactly like API calls.

Keep TLS verification enabled, and install your CA in the trust store each client uses: the OS certificate store for the binary, the same store with `NODE_OPTIONS=--use-system-ca` for npm installs, and the store or CA file configured for your system Git, depending on its TLS backend. Disabling TLS verification entirely, for example with `NODE_TLS_REJECT_UNAUTHORIZED=0`, exposes you to man-in-the-middle attacks, including the theft of your Clever Cloud credentials.

## HTTP proxy

On a network where outgoing traffic must go through an HTTP proxy, Clever Tools follows the `http_proxy` and `https_proxy` environment variables. Set them in your shell, and Clever Tools routes its API calls and update checks through the proxy:

{{< tabs >}}
  {{< tab name="Linux / macOS" >}}

  ```bash
  export http_proxy=http://proxy.example.com:3128
  export https_proxy=http://proxy.example.com:3128
  clever profile
  ```

  {{< /tab >}}
  {{< tab name="Windows (PowerShell)" >}}

  ```powershell
  $env:http_proxy = "http://proxy.example.com:3128"
  $env:https_proxy = "http://proxy.example.com:3128"
  clever profile
  ```

  {{< /tab >}}
{{< /tabs >}}

Clever Tools also recognizes the uppercase variants, `HTTP_PROXY` and `HTTPS_PROXY`. For a proxy that requires authentication, set credentials in the URL, such as `http://user:password@proxy.example.com:3128`. To bypass the proxy for some hosts, list them in the `no_proxy` (or `NO_PROXY`) variable:

```bash
export no_proxy=localhost,127.0.0.1,.internal.example.com
```

Like the TLS variables, Clever Tools reads proxy variables at startup: set them in your shell or inline before the command, not in a `.env` file. By default, `clever deploy` delegates to your system `git`, which follows its own proxy configuration: `git config --global http.proxy`, or the same `http_proxy` and `https_proxy` variables. The previous JavaScript Git implementation, used when you disable `system-git`, doesn't go through this proxy.

## features

Some features are available as experimental, before they're completely ready for prime time. They usually work well, but this testing phase allows us to get feedbacks, refine some details, documentation, and break things between two releases.

Experimental features can be (de)activated on-demand. To list them, use:

```console
clever features
```

To (de)activate an experimental feature, use:

```console
clever features enable theFeature
clever features disable theFeature
```

To get information about how to use an experimental feature, use:

```console
clever features info theFeature
```

A feature can also graduate to stable and become enabled by default, while you can still disable it. Since Clever Tools 5.0.0, it's the case of `system-git`, which makes Git operations use the `git` installed on your system instead of a pure JavaScript implementation. Disable it if `git` isn't available in your `PATH`:

```console
clever features disable system-git
```

## diag | version

To check the current version or get information about your setup, use:

```console
clever version
clever diag
clever diag --format json
```

> [!NOTE]
> Such information are nice to provide in your issues report or when you contact Clever Cloud technical support team.

## login | logout

To connect to your Clever Cloud account, use:

```console
clever login
```

It opens your default browser and starts an Open Authorization ([OAuth](https://en.wikipedia.org/wiki/OAuth)) process to get a `token` and `secret` pair added in your account if it succeeds. You can manage it from the [Console](https://console.clever-cloud.com/users/me/tokens). Clever Tools automatically stores these `token` and `secret` values in a hidden `clever-tools.json` config file in the current local user home folder. If Clever Tools can't open a browser, for example on a headless system, it prints a warning with the URL to open and keeps waiting for you to complete the login.

If you already know them, you can use:

```console
clever login --secret SECRET --token TOKEN
```

> [!TIP]
> If environment variables `CLEVER_SECRET` and `CLEVER_TOKEN` are set, Clever Tools will use them, `login` is not needed.

To log out, delete this file or use:

```console
clever logout
clever logout --alias ALIAS
```

## profile

To get information about the current logged-in user (ID, name, email, 2FA activation, etc.), use:

```console
clever profile
clever profile open
clever profile -F json
```

To manage multiple profiles or configure per-profile overrides, see: [Profiles and overrides](/doc/manage/cli/profiles/)

## emails

To list primary email and secondary emails associated with your Clever Cloud account, you can use:

```console
clever emails
clever emails -F json
```

To open the email management page in your browser, use:

```console
clever emails open
```

To add a secondary email, use:

```console
clever emails add email@example.com
```

To set a secondary email as primary, use:

```console
clever emails primary email@example.com
```

To remove one or all secondary emails, use:

```console
clever emails remove email@example.com
clever emails remove-all
clever emails remove-all --yes
```

## ssh-keys

To list public SSH keys associated with your Clever Cloud account, you can use:

```console
clever ssh-keys
clever ssh-keys -F json
```

To open the public SSH keys management page in your browser, use:

```console
clever ssh-keys open
```

To add a new public SSH key, use:

```console
clever ssh-keys add myPublicKey ~/.ssh/id_ecdsa.pub
```

To remove one or all public SSH keys, use:

```console
clever ssh-keys remove myPublicKey
clever ssh-keys remove-all
clever ssh-keys remove-all --yes
```

## curl

To use our public API, you need to be authenticated for most endpoints. If you're logged in through Clever Tools, there is a simple way to make any request you want: `clever curl`. It's `curl`, but in an authenticated context for Clever Cloud API.

- [Clever Cloud public APIv2 documentation](/api/v2/)
- [Clever Cloud public APIv4 documentation](/api/v4/)

## tokens

You can query [Clever Cloud public API](/api/) with a bearer token thanks to the Auth Bridge. To create a token, use:

```console
clever tokens create myTokenName
clever tokens create myTokenName --expiration 2w --format json
```

Once created, you can use it replacing the API endpoint with `https://api-bridge.clever-cloud.com`. For example:

```console
curl https://api-bridge.clever-cloud.com/v2/self -H "Authorization: Bearer myToken"
```

To list all your tokens, use:

```console
clever tokens
clever tokens -F json
```

To revoke a token, use:

```console
clever tokens revoke myTokenId
```
