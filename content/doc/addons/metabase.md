---
type: docs
title: Metabase
description: This add-on provides a one-click Metabase (Business Intelligence, Dashboards, and Data Visualization) instance hosted by Clever Cloud
tags:
- addons
keywords:
- metabase
- business intelligence
- BI
- dashboard
- data visualization
- dataviz
type: docs
---

[Metabase](https://www.metabase.com/) is an open source Business Intelligence server that connects to MySQL, PostgreSQL, MongoDB, and more! Anyone can use it to build charts, dashboards, nightly emails or Slack reports. Thanks to this add-on, you can deploy Metabase in your organization in just one click. It leverages all Clever Cloud features such as monitoring, scalability, high availability SLA, etc.

{{< callout type="info" >}}
**Metabase is in Beta testing phase:** your insights and suggestions are crucial in shaping the future of this platform.
To share your feedback, please visit us at [our community page](https://github.com/CleverCloud/Community/discussions/categories/metabase).
Thank you for being a part of our journey towards innovation and improvement!
{{< /callout >}}


## Key Features

Metabase on Clever Cloud is a preconfigured set of resources, benefiting from all features the platform provides such as monitoring, scalability, up-to date systems, blue/green deployments, etc. It's easy to manage and allows you to make better sense of the business metrics produced by your application. Once deployed, Metabase takes form of a web application in which you can:

- Navigate and **explore data** in the connected databases
- Create **dashboards** that regroup multiple questions in a canva
- **Integrate** questions/dashboards in another application
- **Share** a questions/dashboard to anyone using an anonymous link
- **Periodically send** results of a question/dashboard by email/Slack
- Configure **data visualization** for questions results: table, line chart, pie chart, gauge, single number, etc.
- Connect **external databases**; it works with add-ons such as [MySQL](/doc/addons/mysql/), [PostgreSQL](/doc/addons/postgresql/), [MongoDB](/doc/addons/mongodb/) and [many other data sources](https://www.metabase.com/data_sources/)
- Create _questions_ either by typing in `SELECT` SQL queries or by using Metabase’s UI to build such queries **without using SQL**

You can also save questions and **organize** them in _collections_. When opening a saved question, fresh data is extracted from the source DB, so that questions always show fresh results. You get user management with **groups and permissions**: users can access to whole data sources so that they can explore and create questions, or they can have access only to collections containing already existing questions/dashboard.

## Create a Metabase add-on

### From the Console

1. [Create a new add-on](https://console.clever-cloud.com/users/me/addons/new) by clicking the **Create...** dropdown in the sidebar and then **an add-on**
2. Select the Metabase add-on
3. You can skip linking the add-on to an application, it won't be needed (connecting data sources to Metabase is done via Metabase's UI)
4. Enter a name for your Metabase add-on and select the zone where you want it to be deployed

### Using the CLI

1. Make sure you have `clever-tools` installed locally. Please refer to the [setup guide](https://github.com/CleverCloud/clever-tools/blob/master/docs/setup-systems.md) if needed
2. List the available plans and options for Metabase: `clever addon providers show metabase`
3. In your terminal, run `clever addon create metabase <name> --org <org>` (`--org` is optional)

Refer to the [Clever Tools documentation](https://github.com/CleverCloud/clever-tools/blob/master/docs/addons-backups.md) for more details on add-on management.

## Acessing the Metabase Interface

Once deployed, Metabase is accessible through an URL provided in the add-on's `Service dependencies` page. You can also go in the environment variables page of the Java application and look for `MB_SITE_URL` value. To get this URL with Clever Tools, use the add-on ID:

```
$ clever addon env ADDON_ID
METABASE_URL="https://an_id-metabase.services.clever-cloud.com"
````

## Underlying Resources

When you create the Metabase add-on, Clever Cloud automatically deploys:

- A [Java](/doc/applications/java/java-jar/) instance with Metabase pre-loaded
- A [PostgreSQL](/doc/addons/postgresql/) database (for internal Metabase use)

When you first connect to your Metabase instance, you will be taken to a wizard to create the first user, data sources, etc. Then you can configure and use it.

* [Learn how to use Metabase](https://www.metabase.com/learn/metabase-basics/getting-started/find-data)

## Plan sizing

By default, Metabase on Clever Cloud uses small-size resources, i.e:

- XS Java
- XXS Small Space PostgreSQL

They are dimensioned to suit a majority of needs. You can however manage and adjust them directly [in the Console](https://console.clever-cloud.com/). For example when you have multiple users loading large dashboards concurrently or if your instance experiences crashes due to Out of Memory (OOM) issues, you should use a larger flavor for the Java application or activate auto-scalability. The PostgreSQL database is not likely to be needed a larger plan, but should this happen you can migrate it using Clever Cloud's Console.

## Version management, Security and Updates

The Metabase add-on is a fully managed application, so you don't have to do anything to update it: by default **it is automatically updated** to match the latest Community Edition release. Your add-on will be automatically restarted when a new Metabase release is available, but thanks to Clever Cloud this will be done without downtime. All deployed versions are reviewed and tested before being released.

Of course, you have full control other this. The Java application of your Metabase add-on contains a `CC_METABASE_VERSION` environment variable.
This variable can be modified to specify which version of Metabase you want. This variable must contain a value that is either a special keyword or a [SemVer](https://semver.org/) version requirement (the only difference with SemVer is that `x.y.z` is interpreted as `=x.y.z` instead of `^x.y.z`.):

- `CC_METABASE_VERSION=community-latest` (_default_): use the latest version of the Community Edition _(same as `0`, `0.*`, `^0` or empty)
- `CC_METABASE_VERSION=0.50.3`: use the `0.50.3` version _(same as `=0.50.3`)
- `CC_METABASE_VERSION=0.50`: use the latest available version starting with `0.50` _(same as `^0.50.0`, `~0.50.0`)

To update Metabase manually, you **should** restart the Java application without the build cache, using the `re-build and restart` button in the [Console](https://console.clever-cloud.com/) or the `clever restart --without-cache` command of [Clever Tools](https://github.com/CleverCloud/clever-tools/blob/master/docs/applications-deployment-lifecycle.md#restart).
The Metabase JAR is stored in the build cache so that no time is wasted re-downloading it every time you restart the application (or it is restarting as part of a scaling event). This also makes the service more resilient: should the download be temporarily failing for any reason, this would not prevent restarting/scaling your add-on.

{{< callout type="warning" >}}
**With great power comes great responsibility.** If you choose to fix your add-on to a specific version (for example, `0.50.3`) or a specific "branch" (for example, `0.50`), you must make sure that this version/branch does not become obsolete (new Metabase versions that patch critical security issues may be released but not used in your add-on because you specified otherwise).
{{< /callout >}}

- [The Atom feed (XML) of latest versions and their changelog](https://cc-metabase.cellar-c2.services.clever-cloud.com/metabase_releases.xml)
- [The TOML list of all available versions and their changelog](https://cc-metabase.cellar-c2.services.clever-cloud.com/metabase_releases.toml)

### Using Metabase Enterprise Edition

Metabase provides an Enterprise Edition (EE) that offers [more features](https://www.metabase.com/docs/latest/paid-features/overview) but requires a license key that must be purchased through their website (see the [pricing page](https://www.metabase.com/pricing/)) EE versions are usually released at the same time as Community Edition (CE) versions, starting with a `1` instead of a `0`.

If you wish to deploy an EE version on your Clever Cloud add-on, `CC_METABASE_VERSION` environment variable to either use a fixed version/branch that starts with `1` (for example: `CC_METABASE_VERSION=1.50`) or `CC_METABASE_VERSION=enterprise-latest`.

You must then add your license key in Metabase's settings (see [documentation](https://www.metabase.com/docs/latest/paid-features/activating-the-enterprise-edition#how-to-activate-your-token-when-self-hosting)).

### Version Rollbacks

There is nothing stopping you from rolling back your Metabase instance to an older version (using the `CC_METABASE_VERSION` environment variable), but **this may break things**. When starting, Metabase checks its attached internal PostgreSQL database and may apply database migrations to evolves its structure. But not all new versions of Metabase add new migrations (patch versions may not, thus this is not a contract).

There are two cases:

1. A version does not add migrations: rolling-back to the previous version can be done without complications
2. A version adds migrations: rolling-back may or may not work. An older Metabase software is not guaranteed to work with a new database structure, so this could break the whole instance, some features or cause data loss.

{{< callout type="info" >}}
**Rollbacks are not officially supported.**
If you need to rollback to an older version (for example, because a new version introduced a blocking regression), it is your responsibility to check if this can be done safely.
{{< /callout >}}

## Credentials At-Rest Encryption

When you add a new data source to Metabase, its credentials are stored into Metabase internal database. Metabase offers an [optional feature](https://www.metabase.com/docs/latest/databases/encrypting-details-at-rest) that allows you to encrypt such credentials before storing them in the database.

When you deploy a Metabase add-on, this **at-rest encryption is enabled by default**.
This is why the Java app of your add-on has a `MB_ENCRYPTION_SECRET_KEY` environment variable that contains a randomly generated value.

## Configuring a SMTP Server

While this is not strictly required to successfully operate Metabase, it might be useful to configure a SMTP server.
There are two main usages:

1. Sending user management/security emails (new user connections, account recoveries, invitations, …)
2. Sending questions/dashboards emails (when users created subscriptions to them)

Clever Cloud does not provide a SMTP server for your Metabase add-on.
You can use a [MailPace](/doc/addons/mailpace/) add-on or any other SMTP server.

The SMTP server can be configured (and tested) in Metabase administration interface.
See [documentation](https://www.metabase.com/docs/latest/configuring-metabase/email) for more details.

### Using a MailPace Add-On

If you have a [MailPace](/doc/addons/mailpace/) add-on, you can link it to the Java application of your Metabase add-on using [Clever Cloud's console](https://console.clever-cloud.com/):

- Go to the Java application of the Metabase add-on
- Open the "Service dependencies" page
- In the "Linked add-ons" section, select your MailPace add-on and click "Add"
- Restart the Java application of your Metabase add-on

When a MailPace add-on is linked, Metabase will automatically get the SMTP server and credentials using (hidden) environment variables. In this case, SMTP settings will **not** be editable from Metabase interface; just unlink the MailPace add-on if you prefer to edit them manually.

You still need to specify the email address which Metabase must use as sender (use Metabase administration interface or set the `MB_EMAIL_FROM_ADDRESS` environment variable). Make sure you MailPace account is able to send email from this address/domain.

## Migrating From a Self-Hosted Instance

Even if you already have a self-hosted Metabase instance, you might want to migrate to the Metabase add-on in order to benefit from automatic upgrades. This is possible if your self-hosted instance uses PostgreSQL as its internal database.

Here is how you can do it:

1. Create an instance of the Metabase add-on in your Clever Cloud organization
2. In the add-on Java application, set `CC_METABASE_VERSION` to the same version as your existing self-hosted instance
3. In the add-on Java application, set `MB_ENCRYPTION_SECRET_KEY` to the same value as it is in your existing self-hosted instance (or let it to its current random value if you did not enable credentials encryption in your existing self-hosted instance)
4. Stop the Java application of your Clever Cloud add-on
5. Stop your self-hosted instance (but let its database up!)
6. Use `pg_dump` to export the whole internal database of your self-hosted instance: `pg_dump -d postgresql://[your-self-hosted-instance-connection-URI] --format c --compress 7 --schema public --verbose > metabase.backup`
7. Use `pg_restore` to restore the dump to the PostgreSQL database of your Clever Cloud add-on: `pg_restore -d postgresql://[your-addon-database-connection-URI] --no-owner --clean --if-exists --schema public --verbose metabase.backup`
8. _(optional)_ Configure the Java application domain and update your DNS record accordingly; if you use a custom domain, you should also update the `MB_SITE_URL` environment variable (it defines the base URL used by links in Metabase emails, among other things)
9. Start the Java application of your Clever Cloud add-on (without build cache)

If everything seems OK, set `CC_METABASE_VERSION` to the value you wish (for example, `community-latest`) in the Java application of your Clever Cloud add-on and restart it. [Contact the Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) if you need advice or help doing that.
