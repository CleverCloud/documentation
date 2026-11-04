---
type: docs
weight: 14
linkTitle: Tips & Tricks
title: Tips & Tricks
description: Discover useful Console features, CLI shortcuts, deployment tricks, and time-saving tools to improve your Clever Cloud experience
keywords:
- tips
- tricks
- console
- cli
- shortcuts
- tools
aliases:
- /doc/best-practices/tips-and-tricks
- /doc/best-practices/tips_and_tricks
- /doc/getting-started/tips-and-tricks
---
{{< hextra/hero-subtitle >}}
  The Console, Clever Tools, and the platform hide many small features that save you time. Here are the ones worth knowing from day one, whether you deploy your first application or manage hundreds.
{{< /hextra/hero-subtitle >}}

## Web Console

The [Clever Cloud Console](https://console.clever-cloud.com) is where you manage your applications, add-ons, and organisations. A few tricks help you get around faster.

### Group your resources by project

Working on several projects in the same organisation? Add a `project:` tag to your applications and add-ons, such as `project:billing`, and they move to a sidebar section named after the project. You edit the tags of an application from its information page, and those of an add-on from its settings. Hover a project section and click its star to pin it to the top of the sidebar. The Console saves your filter, collapsed sections, and starred projects in your account, so you find your sidebar as you left it on any device.

### Filter the sidebar like a pro

The filter at the top of the sidebar matches the names and IDs of your resources as you type. It also understands keywords, which you can combine: `is:app is:running` lists the running applications of your organisation.

| Keyword          | Shows                                                                      |
| ---------------- | -------------------------------------------------------------------------- |
| `is:addon`       | Add-ons                                                                    |
| `is:app`         | Applications                                                               |
| `is:cke`         | Kubernetes clusters                                                        |
| `is:ng`          | Network Groups                                                             |
| `is:[product]`   | Add-ons or applications of a product, such as `is:postgresql` or `is:node` |
| `is:[status]`    | Resources in a given state, such as `is:running` or `is:stopped`           |
| `project:[name]` | Resources of a project, such as `project:billing`                          |

### Jump anywhere with search and links

Press `/` to open the search bar, wherever you are, as long as you're not typing in a field. It finds applications, add-ons, organisations, and Console pages by name or ID, and understands the same `is:` keywords as the sidebar filter.

Know the ID of an application or an add-on, but not the organisation it lives in? Open the `goto` link with it, the Console takes you there:

```text
https://console.clever-cloud.com/goto/app_xxxxxxxx
```

Add the Console as a search engine in your browser. Search your resources from the address bar with this configuration:

```yaml
name: Clever Cloud
shortcut: cc
search URL: https://console.clever-cloud.com/?search=%s
```

### Keep your hands on the keyboard

When you look at an application or an add-on, a single key takes you to one of its pages, when the resource has it. Press `?` to list them all:

| Key | Takes you to                       |
| --- | ---------------------------------- |
| `a` | Activity of the application        |
| `d` | Domain names                       |
| `e` | Environment variables              |
| `i` | Information                        |
| `l` | Logs                               |
| `m` | Metrics of the application         |
| `o` | Overview of the application        |
| `O` | The application, in a new tab      |
| `s` | Scalability                        |

Press `<` or `>` to collapse or expand the sidebar.

### Pick your colors

The Console comes with several color themes. Choose yours from the [Labs](https://console.clever-cloud.com/users/me/feature-list) page of your profile menu, or press `Alt+T` to cycle through them and `Alt+Shift+T` to go backwards. On macOS, use `Option+T` and `Option+Shift+T`.

The [Labs](https://console.clever-cloud.com/users/me/feature-list) page is also where you try features in beta before everyone else.

### Close a session left open elsewhere

Logged in to the Console from a shared or lost computer? The [Console sessions](https://console.clever-cloud.com/users/me/session-tokens) page of your profile lists every active session, with its last activity. Revoke the ones you don't recognize, or all the others at once. To end the current session, log out.

### Let the Console teach you the CLI

Many blocks of the Console, such as domain names, environment variables, TCP redirections, or add-on backups, have a `Command line` panel at the bottom. It shows the matching Clever Tools commands, already filled with the ID of your application or add-on. Do it once in the Console, then copy the command as a starting point for your scripts.

### Environment variables are multi-line

When you edit an environment variable in simple mode, its value looks like a single-line field. Press `Enter` in it: the value splits into several lines. You can paste the full content of a configuration file, a certificate, or any structured data. Expert and JSON modes, Clever Tools, and the API handle multi-line values too.

To add a new variable without reaching for the mouse, press `Ctrl+Enter`, or `Cmd+Enter` on macOS, in its value field. Then click `Update changes` before you leave the page, or your edits stay unsaved.

- [Learn more about environment variables](/doc/develop/common-configuration/environment-variables/reference/)

### Logs come supercharged

The logs interface of the Console follows your application live, or shows a time window you choose. Filter by text, exact string, regular expression, or instance. Its settings change colors, wrap lines, strip ANSI codes, and switch the date format and time zone.

Found the line you were looking for? Select it and click `Inspect`: the filter goes away, and the view centers on this line among the logs around it. To share what you see, copy the selected lines, or send the URL of the page, which keeps your filter. The platform keeps your logs for 7 days.

- [Learn more about logs on Clever Cloud](/doc/develop/observability/logs/)

### Explore your data without a client

No need to install a database or S3 client to peek at your data. The KV Explorer of Redis® and Materia KV add-ons lists your keys and edits the values of the supported types. Its terminal sends any command the service supports. For Materia KV, the editor handles strings only. The Cellar Explorer lists the buckets of your Cellar add-on, browses objects as folders, uploads and downloads files, and shows their metadata.

Prefer the terminal? `clever kv` sends a command to a Redis® or Materia KV add-on:

```bash
clever kv my-cache GET session-status
```

- [Learn more about the KV Explorer](/doc/deploy/databases/redis/#clever-cloud-kv-explorer)
- [Learn more about the Cellar Explorer](/doc/deploy/storage/cellar/)

### Run an application as a one-time task

Most applications on Clever Cloud run continuously, with logs, metrics, and scaling. But sometimes, you only need to run a script once: a data import, a migration, a report. In the Console, enable the `Task` option in the information page of the application, and set the `CC_RUN_COMMAND` environment variable to the command to run. Clever Tools does both at creation.

For example, from a Node.js project whose `package.json` declares an `import` script:

```bash
clever create --type node --task "npm run import"
clever deploy
```

The application follows the usual deployment process, then runs your command and stops when it finishes.

- [Learn more about Clever Tasks](/doc/develop/tasks/)

### Patch or redeploy a database

The migration tool of database add-ons, in their `Migrate / Upgrade` tab, isn't only for major upgrades or a bigger plan. Migrate to the exact same version, plan, and zone, and you get a fresh virtual machine with the latest patches and system updates. The database stays readable but not writable during the migration, and its hostname and database name change.

Use the environment variables of the add-on in your applications, and they follow automatically. Your framework expects `DATABASE_URL` rather than `POSTGRESQL_ADDON_URI`? Don't copy the value into a new variable, it would break at the next migration. On the Linux runtime, let a Mise `run` task start your application, and map the variable in the `[env]` section of `mise.toml` instead. Mise reads the add-on variable each time it runs the task. A `CC_RUN_COMMAND` takes precedence over this task, and its process doesn't get these variables.

```toml {filename="mise.toml"}
[env]
DATABASE_URL = "{{ env.POSTGRESQL_ADDON_URI }}"

[tasks.run]
run = "node server.js"
```

- [Learn more about database migrations](/doc/manage/database-migration/)
- [Learn more about shaping the environment with Mise](/doc/develop/mise/#shape-the-environment)

## Clever Tools

Clever Tools, the Clever Cloud CLI, drives the whole platform from your terminal. Install it with npm, then log in:

```bash
npm install -g clever-tools
clever login
```

Prefer another way? Many package managers also provide Clever Tools, such as pnpm, Bun, Homebrew, or WinGet. You can also download it as a standalone binary for Linux, macOS, or Windows.

- [Learn more about installing Clever Tools](/doc/manage/cli/install/)
- [Learn more about Clever Tools](/doc/manage/cli/)

### SSH into any application

The instances of your applications are immutable, so you shouldn't need to change anything on them. But to debug, nothing beats a look inside. `clever ssh` connects you to an instance, with the SSH key of your choice if needed:

```bash
clever ssh
clever ssh --app my-api
clever ssh --app my-api -i ~/.ssh/id_ed25519
```

Need a quick answer rather than a shell? Add `--command`, or `-c`, to run a command on the instance and exit. With `--instance any`, Clever Tools doesn't even ask which instance to pick:

```bash
clever ssh --app my-api --instance any -c "df -h"
```

`clever instances` lists the running instances of an application, including the build instance during a deployment, with their number and ID. `clever activity --follow` watches the deployments as they happen:

```bash
clever instances --app my-api
clever activity --app my-api --follow
```

If a deployment fails and you want to understand why, set the `CC_TROUBLESHOOT` environment variable to `true`. The instance can then stay available for up to one hour after the failure, and some runtimes add extra build diagnostics.

- [Learn more about SSH access](/doc/develop/ssh-access/)

### Diagnose the DNS of your domains

Your domain doesn't answer? `clever domain diag` checks the DNS records of the domains linked to an application, and tells you what to fix:

```bash
clever domain diag
clever domain diag --app my-api
clever domain diag --app my-api --filter example.com
```

{{< callout type="info" >}}
  This tool can't see through a CDN or a private load balancer in front of your application
{{< /callout >}}

### Redeploy without a new commit

Changed an environment variable, or want a fresh start? No need for an empty commit. `clever restart` starts your application again, reusing the build cache when it can, and `--without-cache` rebuilds it from scratch. When you deploy a commit already on Clever Cloud, `--same-commit-policy` tells `clever deploy` to restart or rebuild instead of failing:

```bash
clever restart --without-cache
clever deploy --same-commit-policy rebuild
```

- [Learn more about the deployment lifecycle](/doc/manage/cli/applications/deployment-lifecycle/)

### Get everything in JSON

`clever applications list` lists all your applications, grouped by organisation. Like most Clever Tools commands, it outputs JSON with `--format json`, or `-F json`. Pipe it to `jq` or `jless`, and you've got a script or a CI/CD step ready:

```bash
clever applications list --format json | jq '.[].applications[].name'
```

### The power of `clever curl`

Want to explore the Clever Cloud API without handling authentication? `clever curl` is a `curl` wrapper that signs your requests with your Clever Tools credentials:

```bash
clever curl https://api.clever-cloud.com/v2/self
clever curl https://api.clever-cloud.com/v2/summary | jless
```

The first command returns the details of your account. The second one returns everything your account can reach: organisations, applications, add-ons. Browse it in `jless`, and you've got a map of your resources.

- [Explore the Clever Cloud API](/api/)

### Send your logs where you want

The Console keeps your logs for 7 days. To keep them longer, or to search them with the tools your team already uses, add a drain. It forwards the logs of an application or an add-on to Datadog, Elasticsearch, New Relic, Splunk, a syslog server, or any HTTP endpoint. `clever drain list` then lists the drains of all your organisations. For example, for a Datadog account on the EU site, with your API key in `DATADOG_API_KEY`:

```bash
clever drain create datadog "https://http-intake.logs.datadoghq.eu/v1/input/$DATADOG_API_KEY?ddsource=clevercloud&service=my-api"
clever drain list
```

- [Learn more about drains](/doc/develop/observability/drains/)

### Open the Console or your application from the terminal

`clever open` opens your application in your browser, through its favorite domain, or another linked domain if it has no favorite. `clever console` opens it in the Console:

```bash
clever open
clever console --app my-api
```

Keycloak, Matomo, Metabase, and Otoroshi add-ons get their own shortcuts. Open the admin interface of the service, its logs, or its dashboard in the Console, without looking for the underlying application. Otoroshi also opens its Swagger UI. These commands are in beta, so enable them first:

```bash
clever features enable operators

clever matomo open my-matomo
clever metabase open logs my-metabase
clever keycloak open webui my-keycloak
clever otoroshi open swaggerui my-otoroshi
```

- [Learn more about operators in Clever Tools](/doc/manage/cli/operators/)

### Pass your credentials to Clever Tools

`clever login` opens your browser to authenticate you. On a server or in a CI/CD pipeline, use an existing token with its secret instead. Give them to the login command, or set them as environment variables for a one-time use:

```bash
# Log in with an existing token
clever login --token TOKEN --secret SECRET

# Use the credentials for a single command, without saving them
CLEVER_TOKEN=TOKEN CLEVER_SECRET=SECRET clever profile
```

### Run Clever Tools in a container

In a CI/CD job or any container, use the Clever Tools image instead of installing it. Export your token and secret, pass them to the container, and pin a version tag for reproducible jobs:

```bash
docker run --rm -e CLEVER_TOKEN -e CLEVER_SECRET clevercloud/clever-tools:5.3.0 status --app my-api
```

### Juggle several accounts

A personal account and a work one, or a test account next to the real one? Clever Tools keeps several profiles side by side. Log in once per account with an alias, then switch between them when you need to:

```bash
clever login --alias personal
clever login --alias work
clever profile list
clever profile switch --alias work
```

With two profiles, `clever profile switch` alone toggles to the other one. Before running anything that creates resources, `clever profile` tells you which account is active.

- [Learn more about Clever Tools profiles](/doc/manage/cli/profiles/)

### Ask for something, or contribute

Clever Tools is an [open-source project](https://github.com/CleverCloud/clever-tools), built with Node.js, and developed in the open. Ideas, issues, and pull requests [are welcome](https://github.com/CleverCloud/clever-tools/blob/master/CONTRIBUTING.md).

- [Learn more about Clever Tools](/doc/manage/cli/)

## Did you know?

### Give the docs and the CLI to your AI assistant

Every documentation page has a `Copy Page` menu. Copy the page as Markdown, view its Markdown source, or open it in ChatGPT, Claude, Le Chat, or Perplexity, ready to ask your questions. To teach your coding assistant the Clever Tools commands, add the Clever Tools skill:

```bash
npx skills add CleverCloud/clever-tools
```

- [Learn more about driving Clever Cloud from an AI agent](/doc/ai-llms/)

### Follow what's new

The [changelog](/changelog/) lists the technical updates of the platform: new versions, features, deprecations. Subscribe to [its RSS feed](/changelog/index.xml) to never miss one, and read the [Clever Cloud blog](https://www.clever.cloud/blog/) for the bigger stories.

### Runtimes come with batteries included

Runtimes other than Docker come with many tools you can use in your applications, scripts, or SSH sessions, whatever their language.

A few examples:

- **Command line:** `jq`, ripgrep (`rg`), `fd`, `htop`, `tmux`, Zellij, Vim, and nano
- **Data:** PostgreSQL and MySQL clients, MongoDB tools, Redis, SQLite, and `s3cmd`
- **Documents and media:** Chromium, FFmpeg, ImageMagick, LibreOffice, and Tesseract
- **Platform:** Clever Tools, Git, Mise, and `uv`

All non-Docker applications share the same image. It holds every language of the platform: .NET, Elixir, Go, Java, Node.js and Bun, PHP, Python, Ruby, Rust, and more. A PHP application can run a Node.js build step without any setup.

To pick a version, whatever the runtime of your application, set the matching variable, such as `CC_NODE_VERSION`, `CC_PHP_VERSION`, `CC_PYTHON_VERSION`, `CC_COMPOSER_VERSION`, or `CC_HUGO_VERSION`. For anything else, [Mise](/doc/develop/mise/) installs the tools your project declares in a `mise.toml` file. In a Docker application, the tools come from your image.

- [Follow the tools updates in the changelog](/changelog/)
- [List all the environment variables](/doc/develop/common-configuration/environment-variables/reference/)

### Share variables across applications

Several applications need the same API endpoint, feature flags, or settings? Store them once in a Configuration provider add-on, and link it to each application of the same organisation. Variables set on an application still win over the shared ones, and updating the provider restarts the linked applications.

- [Learn more about the Configuration provider](/doc/deploy/services/config-provider/)

### Check that your application is really ready

By default, a deployment succeeds once your application answers on `/`, even with a `404`. Point `CC_HEALTH_CHECK_PATH` to a route that checks what matters, such as the database connection, and the deployment only succeeds once it returns a `2xx` code:

```bash
clever env set CC_HEALTH_CHECK_PATH /health
```

- [Learn more about health checks](/doc/develop/common-configuration/healthcheck/)

### Put services in front of your application

On runtimes other than Docker, Request Flow chains services between the public port and your application, without touching your code. Add a `clevercloud/varnish.vcl` file for an HTTP cache, or a Redirection.io project key for redirects and search engine rules. The Otoroshi challenge accepts only the traffic coming from your API gateway. With `CC_REQUEST_FLOW` and its settings, `oauth2-proxy` puts a login screen in front of a staging application, `block` closes public access, and `custom` runs your own reverse proxy.

The services take over the public port `8080` and forward the requests to your application on `9000`, except `block`, which answers on its own. If your application runs its own HTTP server, set `PORT` to `9000`.

- [Learn more about Request Flow](/doc/develop/request-flow/)

### A preview for each pull request

Once configured in your repository, the Clever Cloud review app GitHub Action deploys each pull request to its own application, with its own URL. It removes the application when the pull request closes. Your colleagues test the change without installing anything.

- [Learn more about review apps](/doc/tools/github/#deploy-review-apps-from-a-pr-on-github)

### Schedule recurring scripts

Need to clean a cache every night or send a weekly report? On applications other than Docker and tasks, add a `clevercloud/cron.json` file to your project. Times are in UTC, commands use absolute paths, and `$ROOT` stands for the root of your application:

For example, to run a PHP script at `scripts/clean-cache.php` every night:

```json {filename="clevercloud/cron.json"}
[
  "0 3 * * * /usr/bin/php $ROOT/scripts/clean-cache.php"
]
```

Each running instance of your application runs these scheduled commands, so handle concurrency yourself if your application has several instances.

- [Learn more about scheduled tasks](/doc/develop/cron/)

### Start from a blank Linux runtime

Your project doesn't fit a language ecosystem, or mixes several? The Linux runtime expects nothing but a command to start your application. Install what you need with Mise, a script, or your build step, without the conventions of a specific ecosystem. Unless it's a task, your application listens on `0.0.0.0:$PORT`. `PORT` defaults to `8080`: set it to `9000` when you put [Request Flow](/doc/develop/request-flow/) services in front of it. Set the start command with `CC_RUN_COMMAND`, or declare `build` and `run` targets in a Makefile, or Mise tasks, in a `mise.toml` file or as task files.

- [Learn more about the Linux runtime](/doc/deploy/applications/linux/)

### One domain, several applications

Linking a domain to an application takes a few clicks, and Clever Cloud generates its TLS certificate for you. [Sōzu](https://github.com/sozu-proxy/sozu/), the open-source load balancer of Clever Cloud, does the routing. But a domain can also serve several applications, one per path: your blog on `example.com/blog`, your API on `example.com/api`. Each one keeps its own scaling, logs, and environment variables.

- [Learn more about path routing](/doc/develop/common-configuration/domain-names/#path-routing)

### Pick the `cleverapps.io` subdomain you want

Each new application gets an `app_id.cleverapps.io` domain, but you can pick any free subdomain instead, such as `my-demo.cleverapps.io`. It's handy for demos and testing. `cleverapps.io` is a shared domain, though, not made for production. Link your own domain when you go live, and remove the `cleverapps.io` one if you don't need it anymore.

- [Learn more about domain names](/doc/develop/common-configuration/domain-names/)

### Distribute your own add-ons

You provide a service? Make it an add-on provider: your applications and organisations can then link it like any Clever Cloud add-on. It can even join the Clever Cloud Marketplace and reach other customers.

- [Learn more about the Marketplace API](/doc/develop/marketplace/)

### Clever Cloud runs on its own public API

The Console and Clever Tools use the same public API you can use. Everything they do, your scripts and integrations can do too, which keeps the API complete and well-tested.

- [Learn more about the Clever Cloud API](/api/)

### Build your own interface with Clever Cloud Web Components

The Console uses open-source Web Components, designed for accessibility. Built on web standards, they work without a specific framework. Use them in your own tools: they're available [as an npm package](https://www.npmjs.com/package/@clevercloud/components), developed [on a public repository](https://github.com/CleverCloud/clever-components/), and documented in [their Storybook](https://www.clever.cloud/developers/clever-components/).

### Need something specific? Ask

Clever Cloud runs on its own infrastructure and on partners' clouds, and can run on-premises for specific needs, all with the same control plane technology. If you need a dedicated setup or a service off the catalog, [contact the sales team](https://www.clever.cloud/contact/).
