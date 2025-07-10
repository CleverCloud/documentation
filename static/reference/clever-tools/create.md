---
type: docs
title: Application creation with Clever Tools
position: 2
shortdesc: Create a new application using the Clever Cloud CLI tool
tags:
- cli
- reference
keywords:
- clever-tools
- create
- remove
- list
- application
- addon
- link
- unlink
- linked application
- dependency
- exposed configuration
---
## Apps creation process

`clever create` allows you to create a new application.

First of all, select the type of your application in the list below :

* docker (Docker)
* go (Go)
* gradle (Java or Groovy + Gradle)
* jar (Java + JAR)
* maven (Java + Maven)
* node (Node)
* php (PHP)
* play1 (Java + Play! 1)
* play2 (Java or Scala + Play! 2)
* python (Python)
* ruby (Ruby)
* rust (Rust)
* sbt (Scala + SBT)
* static-apache (Static)
* war (Java + WAR)

Then, in order to create your app in your personal space, use :

    clever create --type <type> <app-name>

    # Create an application for an organisation
    clever create --type <type> <app-name> --org <org>

    # Choose the region of your application (par, rbx, wsw, mtl, sgp, syd)
    clever create --type <type> <app-name> --region <zone>

### Alias

You might want to use an alias instead of the complete name.

    clever create --type <type> <app-name> --alias <alias>

When you want to make reference to this application using an other command, use `--alias ALIAS` instead of the name.

### GitHub

When creating your application, you can link it to GitHub for deployments.

    # Link an application to GitHub
    clever create --GitHub <owner>/<repository>

## Addon creation process

Using `clever addon`, you can add, rename or delete addon and list available addon providers

    # List existing addons
    clever addon

### Creating an addon

First, list addon providers and then create your addon.

    # List addon providers
    clever addon providers

    # Create your addon and link it to your application with --link <app-alias>
    clever addon create <provider-name> <addon-name> --link <app-alias>

    # Create an addon for an organisation
    clever addon create <provider-name> <addon-name> --link <app-alias> --org <org-name>

### Choosing provider's plan and region

You can choose your addon's plan when you create it using `--plan <plan-name>`. The plan is by default 'dev'. With the flag "--yes" you can skip confirmation even if the addon is not free. You can also select the region that will provision the addon in.

    # Show more informations about a provider(plans and available regions)
    clever addon providers show <provider-name>

    # Create your addon
    clever addon create <provider-name> --plan <plan> --region <region-name> <addon-name>

### Rename or delete an addon

Use `addon rename` and `addon delete` to respectively rename and delete an addon.
If you don't want any confirmation, use `--yes`.

    # Rename an addon
    clever addon rename <addon-name> <new-name>

    # Delete an addon
    clever addon delete <addon-name>

## Dependencies

### Link an application or an addon

You can make dependencies using `clever service link`

    # Link an application
    clever service link-app <app-name>

    # Link an addon
    clever service link-addon <addon-name>

You can unlink dependency using `unlink-app` and `unlink-addon`

## Exposed configuration

Clever-tools allows you to get and update the exposed configuration of your application that allows dependencies to get informations about your application.

### Get the whole configuration

Simply use the commmand down below to get all your variables.

    clever published-config

### Update a variable

Use `set` to add or update a  variable and `rm` to remove one.

    # Add or update a variable
    clever published-config set <variable-name> <variable-value>

    # Remove a variable
    clever published-config rm <variable-name>

### Import a configuration

Clever-tools allows you to load a configuration from STDIN.

    cat <configuration> | clever published-config import
