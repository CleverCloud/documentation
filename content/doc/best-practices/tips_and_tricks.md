---
title: Tips & Tricks
shortdesc: Discover some useful tips and tricks to improve your experience with Clever Cloud tools
tags:
- reference
- tips
- tricks
keywords:
- tips
- tricks
type: docs
draft: false
---
{{< hextra/hero-subtitle >}}
  Clever Cloud offers many powerful features designed to make your development work easier. This guide reveals useful capabilities you might not know about, from shortcuts to time-saving tools.
{{< /hextra/hero-subtitle >}}

## Web Console Features

The Clever Cloud Console (<https://console.clever-cloud.com>) is your control center for managing applications, add-ons, and organisations. Here are features that can enhance your workflow:

### Advanced Menu Filtering

The left sidebar menu includes a powerful search function. Beyond simple name searches, you can use special keywords to filter your resources:

| Keyword        | What it Shows |
| -------        | ----------- |
| `is:addon`     | Lists all your add-ons |
| `is:app`       | Shows only applications |
| `is:[addon]`   | Filters specific add-on types (Examples: `is:postgresql`, `is:redis`, `is:mysql`) |
| `is:[runtime]` | Shows applications by runtime (Examples: `is:node`, `is:php`, `is:java`) |

### Multi-line Environment Variables

Environment variables support more than just single-line values. When editing variables in simple mode:

1. Click in any variable's value field
2. Press `Enter` to create multiple lines
3. Add configuration files, long texts, or structured data

This works across all input modes (simple, expert, and JSON) as well as through Clever Tools and the API.

[Learn more about environment variables](/developers/doc/reference/reference-environment-variables)

### Quick Variable Creation

Speed up environment variable creation with these shortcuts:

- Use the `Add` button or press `CTRL+Enter` to create new variables
- Switch between simple, expert, and JSON modes for different input styles

{{< callout type="info" >}}
Always select `UPDATE CHANGES` before leaving the environment variables page to save your modifications
{{< /callout >}}

### Enhanced Logging System

The Console includes a sophisticated logging interface with features for debugging and monitoring:

- Filter logs by:
  - Date and time ranges
  - Text content
  - Regular expressions
  - Specific instances
- Customize your view with:
  - Multiple color themes
  - ANSI code stripping
  - Line wrapping
  - Configurable date formats and time zones
- Share logs easily by selecting and copying lines

Clever Cloud retains your logs for 7 days as part of the standard service.

[Explore logging features](/developers/doc/administrate/log-management/)

### Universal Resource Access

Navigate quickly to any resource using these features:

#### Quick Access Link

Access any application or add-on directly using its ID:

```shell
https://console.clever-cloud.com/goto/id
```

#### Global Search

Press the `/` key anywhere in the Console to search for applications, add-ons, or organisations by name or ID.

#### Keyboard Navigation

Use these shortcuts when viewing applications or add-ons:

| Key | Takes You To |
| --- | ----------- |
| `?` | Keyboard shortcuts help |
| `a` | Application activity |
| `d` | Domain settings |
| `e` | Environment variables |
| `i` | Resource information |
| `l` | Logs view |
| `m` | Application metrics |
| `o` | Overview page |
| `s` | Scalability settings |

### Running One-Time Tasks

While Clever Cloud primarily runs continuous services, you can also execute one-time tasks:

1. Define an application as a task in the `Information` panel, or
2. Create it through Clever Tools: `clever create --type TYPE --task "command to execute"`

After pushing your code, the application:

1. Starts normally
2. Installs dependencies
3. Completes the build process
4. Executes your specified command
5. Stops automatically when finished

[Learn more about task execution](/developers/doc/develop/tasks/)

### Database Management Tips

Need to update your database? The Console's migration tool offers several options:

- Upgrade to new major/minor versions without downtime
- Move databases between zones
- Apply patch updates
- Redeploy existing databases

To get the latest patch version or redeploy, simply migrate to the same version, plan, and zone.

[Database add-ons documentation](/developers/doc/addons/)
[Migration guide](/developers/doc/administrate/database-migration/)

## Clever Tools Features

The Clever Cloud CLI provides powerful command-line capabilities. Install it with:

```bash
npm i -g clever-tools
```

Then run `clever login` to get started.

### SSH Access Made Simple

While the platform uses immutable infrastructure, sometimes you need SSH access for debugging. Use these commands:

```bash
clever ssh                                         # Connect to default app
clever ssh --app app_id_or_name                    # Connect to specific app
clever ssh -a app_id_or_name -i ~/.ssh/id_ed25519  # Use specific key
```

For extended debugging sessions, set `CC_TROUBLESHOOT=true` as an environment variable. This keeps your application running for up to 1 hour, even if errors occur.

[SSH key management guide](/developers/doc/account/ssh-keys-management/)

### Domain Configuration Diagnostics

Check your domain setup with the built-in diagnostic tool:

```bash
clever domain diag                           # Check current application
clever domain diag -a app_id_or_name        # Check specific application
clever domain diag --app app_id_or_name --filter keyword  # Filter results
```

{{< callout type="info" >}}
  This tool may not catch all scenarios involving CDNs or private load balancers.
{{< /callout >}}

### Application Management

View all your applications with:

```bash
clever applications list
```

This command groups applications by organisation for easy reference.

### JSON Output Support

Add `--format json` or `-f json` to most commands for machine-readable output:

```bash
clever applications list --format json
```

This works well with tools like `jq`, `jless`, or `jql` for further processing.

### The Power of `clever curl`

Access the Clever Cloud API without managing authentication tokens using `clever curl`. It automatically handles credentials for you:

```bash
# Get your account details
clever curl https://api.clever-cloud.com/v2/self

# View all resources with JSON viewer
clever curl https://api.clever-cloud.com/v2/summary | jless
```

This tool helps you:

- Test API endpoints quickly
- Create automation scripts
- Set up CI/CD pipelines
- Explore available resources

[Explore the API documentation](/developers/api/)

### Browser Integration

Open your applications directly from the command line:

```bash
# Open default application
clever open
clever open --app app_id_or_name

# Access Console
clever console
clever console --app app_id_or_name
```

### Authentication Options

Multiple ways to authenticate with Clever Tools:

```bash
# Use environment variables for login
export CLEVER_TOKEN=TOKEN
export CLEVER_SECRET=SECRET
clever login

# Direct login with credentials
clever login --token TOKEN --secret SECRET

# One-time use without saving credentials
CLEVER_TOKEN=TOKEN CLEVER_SECRET=SECRET clever profile
```

### Contributing to Clever Tools

Clever Tools is open source and built with Node.js. You can:

- Report issues
- Suggest new features
- Submit pull requests
- Join the development community

[Clever Tools documentation](https://github.com/CleverCloud/clever-tools/tree/master/docs#readme)

## Did You Know?

### Stay Updated with Clever Cloud

Track platform improvements through:

- [Technical Changelog](/developers/changelog/)
- [RSS Feed](/developers/changelog/index.xml)
- [Blog Updates](https://www.clever-cloud.com/blog/)

### Built-in Runtime Tools

Every runtime includes useful tools:

- Node.js (customize version with `CC_NODE_VERSION`)
- Python
- Ruby
- Development tools (`jq`, `tmux`)
- Local Redis server (`redis-server`)

### Path Routing Capabilities

Thanks to the [open source load-balancer Sōzu](https://github.com/sozu-proxy/sozu), you can host multiple applications under one domain:

```bash
mydomain.com/blog  → Blog application
mydomain.com/api   → API application
```

Each application maintains:

- Independent scaling
- Separate logs
- Individual environment variables
- Automatic TLS certificate generation


[Path routing documentation](/developers/doc/administrate/domain-names/#path-routing)

### Create Custom Add-ons

Distribute your services through Clever Cloud:

1. Create an add-on provider
2. Make it available in your organisations
3. Optionally list it in the Clever Cloud Marketplace

[Marketplace API documentation](/developers/doc/marketplace/)

### Domain Management

The `cleverapps.io` domain system offers:

- Automatic `app_id.cleverapps.io` domains for new applications
- Custom subdomain creation
- Perfect for testing and staging environments

Remove these domains when moving to production with your custom domain.


### API-First Platform

Clever Cloud's entire platform runs on its public API:

- Console interface
- Clever Tools
- SDK features
- Custom integrations

This ensures API reliability and continuous improvement.

[API documentation](/developers/api)

### Web Components

Build custom Clever Cloud interfaces using :

- Open source Web Components
- Standard-based architecture
- Accessibility-focused design

Available through:

- [npm package](https://www.npmjs.com/package/@clevercloud/components)
- [Public repository](https://github.com/CleverCloud/clever-components)
- [Storybook documentation](https://www.clever-cloud.com/doc/clever-components)

### Custom Solutions

Clever Cloud offers:

- Public cloud hosting
- On-premise deployments
- Edge computing solutions
- Custom service integration
- Dedicated support

[Contact the sales team](https://www.clever-cloud.com/contact/) to discuss your specific needs.
