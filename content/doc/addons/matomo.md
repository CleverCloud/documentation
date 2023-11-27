---
type: docs
title: Matomo
position: 10
shortdesc: This add-on provides a Matomo Analytics solution based on existing Clever Cloud services.
tags:
- addons
keywords:
- matomo
- web analytics
- google analytics
- privacy
- gdpr
aliases:
- /doc/deploy/addon/matomo
type: docs
---

Matomo is an open-source web analytics solution which gives you full ownership of your data. It's a [GDPR compliant](https://matomo.org/gdpr-analytics) alternative to Google Analytics. You can learn more about Matomo on [their website](https://matomo.org).

Matomo on Clever Cloud will allow your marketing team to effortlessly setup a tailored web analytics solution, that can be adjusted to your needs and workloads.

{{< image "/images/matomo/full-dashboard.png" "Matomo Dashboard" >}}

## How it works?

When you subscribe the Matomo add-on, we automatically setup a PHP instance based on the latest Matomo release. It comes with the required MySQL database and an optional Redis cache.

We have chosen to let you see and manage these companion add-ons in the Console so that you could adjust them to your needs. You can change their settings and use the Clever Cloud ability to migrate from an S flavored database or cache to an L or XL if required. You can also activate autoscalabity (horizontal and/or vertical scaling).

By default, Matomo on Clever Cloud comes with small sized add-ons: 
- PHP Nano
- MySQL XXS BigStorage
- Redis S

We've already integrated the Clever Cloud SSO, so you can login directly into your matomo instance from the Console, start to integrate your website, create different users. 

## Create Matomo add-on

### Web Console

1. Create a new add-on by clicking on the **Create...** dropdown in the sidebar and then **an add-on**.
2. Select the Matomo add-on.
3. You can skip linking the add-on to an application, it won't be needed.
4. Enter the name of your Matomo add-on and select the zone where you wish to deploy it.
5. It's done!

### CLI

1. Make sure you have clever-tools installed locally. Report to the [getting started]({{< ref `doc/cli/getting_started.md` >}}) guide if needed.
2. List the available plans and options for Matomo: `clever addon providers show Matomo`.
3. In your terminal, you can then run `clever addon create matomo <app-name> --region <region> --org <org>` where `app-name` is the name you want for your add-on, `region` deployment region, and `org` the organization ID the application will be created under.

Refer to the [documentation]({{< ref `doc/cli/create.md` >}}) for more details on application creation with Clever Tools

## Accessing the Matomo interface

Once you created your add-on, you should get to the dashboard and see a link named `Access Matomo`. Opening that link will redirect you to our SSO authentication.

{{< readfile file="single-sign-on.md" >}}

## Configure your Matomo instance

Once you accessed your Matomo interface, we can start configuring it. A custom Clever Cloud configuration is automatically installed on your instance during the provisioning.

This configuration helps you taking advantage of optimizations by using a Redis cache by default.

### Using your Matomo

If you're new with Matomo, you would probably want to read the Matomo's guides on [the official documentation](https://matomo.org/guides/).

## Matomo plugins

Your Matomo instance comes with a list of pre-installed plugins. As a managed instance, our Matomo addon won't let you bypass the installation process. Installed plugins already allows a quite advanced use of Matomo, but if you wish to install a specific plugin that's not in your instance, feel free to contact our suport team.

### When activating a deactivated plugin

Keep in mind that some plugins might consume more ressources than you have by default on your PHP instance, since some PHP processes can take a long time, depending on what you are doing.

If you activate a deactivated by default plugin (like [GoogleAnalyticsImporter](https://matomo.org/guide/installation-maintenance/import-google-analytics/)):

- Scale your PHP app
- Disable autoscalability for the PHP app
- Scale your Matomo MySQL addon

If you activate the plugin while enabling autoscalability, your PHP insatnce will restart with default settings when scaling, therefore disabling the plugin and killing the process.

Plugins can be browsed from [Matomo own plugin repository](https://plugins.matomo.org/).

{{< callout type="warning" >}}
Plugin files are removed everytime your instance reboots. **This means you have to reinstall them all again after every reboot.** This is temporary, and it is something we plan on improving as soon as we can.
{{< /callout >}}

## Security and updates

The Matomo add-on is a fully managed application, you don't have to select a particular version. Still its receives updates for both features and security, that we will managed for you with continuously upgraded version over time.

After being updated, you Matomo add-on could need to be restarted.

## Plans

Matomo on Clever Cloud is the easiest way to set it up, but you can go further and adjust the flavour of your instance, database or cache. We provide [different plans for PHP, MySQL and Redis](https://www.clever-cloud.com/pricing/).
