---
type: docs
title: Keycloak
description: This add-on provides a one-click Keycloak single sign-on and identity and access management (IAM) solution hosted by Clever Cloud, built with *Please open-it*.
tags:
- addons
keywords:
- Keycloak
- IAM
- Security
- Authentication
- Identity
- OAuth
- OpenID
aliases:
- /doc/deploy/addon/Keycloak
type: docs
---

Keycloak is an open source identity and access management (IAM) solution that offers powerful authentication features for services and secure applications. Thanks to this add-on, you can deploy Keycloak in your organisation in just one click. It leverages all Clever Cloud features such as monitoring, scalability, high availability SLA, etc.

To fit the most common needs, the Keycloak add-on comes with batteries included: sensible defaults, easy migration with realms import/export, Keycloak Metrics, default theme, etc.

{{< callout type="info" >}}Share your feedback on Keycloak operator through [our community page](https://github.com/CleverCloud/Community/discussions/categories/keycloak){{< /callout >}}

## Key features
Keycloak on Clever Cloud allows you to effortlessly set up a tailored authentication and access management solution, that you can adjust to your needs and workloads. It offers a wide panel of services such as:
- Secure Identity Management
- Single Sign-On (SSO)
- Centralized Administration
- Customizable Authentication (OAuth 2.0, LDAP, SAML, OpenID Connect, and more…)
- Easily load plugins and themes
- Multi Realms
- Monitoring and Logging
- Export and Import
- Support and Maintenance

## Need expert advice?

The Clever Cloud Keycloak add-on is designed to meet the most common needs, built with [Please Open-it](https://please-open.it/) and hosted on our services. For the most complex and loaded systems, our partner and Keycloak experts behind this add-on, can provide assistance: [contact us](mailto:sales@clever-cloud.com).

## How it works?
When you create the Keycloak add-on, Clever Cloud automatically deploys:

- A [Java](/developers/doc/applications/java/java-jar) instance with Keycloak pre-loaded and configured
- A [PostgreSQL](../postgresql) database
- A [FS Bucket](../fs-bucket) used for themes, plugins, and import/export storage needs

## Security and updates
Since the Keycloak add-on is a fully managed application, you don't have to select a particular version. It's automatically upgraded and updated both for features and security.

An add-on update might require a rebuild.

> Required actions are notified by email

## Plan sizing

By default, Keycloak on Clever Cloud uses small-size resources, i.e:

- S Java
- XXS Small Space PostgreSQL
- Less than 100 MB in FS Bucket

They are dimensioned to suit a majority of needs. Even if this Keycloak add-on might handle heavy traffic and an important number of simultaneous connections, the default configuration should handle the following load (based on [Keycloak](https://www.keycloak.org/high-availability/concepts-memory-and-cpu-sizing) sizing recommendation):
- 5 logins by second
- 90 credential grants by the second
- 70 refresh tokens by second

You can however manage and adjust them directly in the Console to fit your needs. You can for example change their settings, migrate to a larger storage database, etc. Vertical auto-scalability is available for this service. [Different plans for Java and PostgreSQL](https://www.clever-cloud.com/pricing/) are available on Clever Cloud.

## Create a Keycloak add-on

### From the Console
1. [Create a new add-on](https://console.clever-cloud.com/users/me/addons/new) by clicking the **Create…** dropdown in the sidebar and then **an add-on**
2. Select the Keycloak add-on
3. You can skip linking the add-on to an application, it won't be needed
4. Enter a name for your Keycloak add-on and select the zone where you want it to be deployed

### Using the CLI

Make sure you have `clever-tools` installed locally. Please refer to the [setup guide](/developers/doc/cli/install/) if needed. In your terminal, run `clever addon create keycloak <name> --org <org>` (`--org` is optional). You'll get URLs to manage your Keycloak instance and the temporary credentials:

```
$ clever addon create keycloak myKeycloak
Add-on created successfully!
ID: addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Real ID: keycloak_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Name: mykeycloak

Your Keycloak is starting:
 - Access it: https://xxxxxxxxxxxxxxxxxxxx-keycloak.services.clever-cloud.com
 - Manage it: https://console.clever-cloud.com/addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

An initial account has been created, you'll be invited to change the password at first login:
 - Admin user name: cc-account-admin
 - Temporary password: xxxxxxxxxxxxxxxx

/!\ The keycloak provider is in beta testing phase
```

Refer to the [Clever Tools documentation](https://github.com/CleverCloud/clever-tools/tree/master/docs) for more details on add-on creation.

## Accessing the Keycloak interface

Once you have created your add-on, go to the Console Keycloak Java runtime page and click "Open the application". You also can get the Keycloak add-on URL from the Clever Cloud console, in the information panel of your Keycloak add-on.

The admin interface is accessible on the `/admin` endpoint. The default user and password are provided in the Java application by the environment variables `CC_KEYCLOAK_ADMIN` and `CC_KEYCLOAK_ADMIN_DEFAULT_PASSWORD`.

A password change is requested at the first connection.

### Bootstrap admin client

You can set up a new client with the `admin` role for `master` realm during build time using `CC_KEYCLOAK_BOOTSTRAP_ADMIN_CLIENT_ID` and `CC_KEYCLOAK_BOOTSTRAP_ADMIN_CLIENT_SECRET` environment variables of the Java application. Once created, delete the environment variables from your application.

Bootstrap client [should be temporary](https://www.keycloak.org/server/bootstrap-admin-recovery) and is mostly necessary for provisioning.

## Realms management

The number of realms significantly impacts the overall performances. **Use as few realms as possible.**

**The recommended way** to create realms is by using the environment variables of the Java application of the Keycloak add-on. Thus, it comes with an optimized configuration such as brute-force detection and specific metrics:

- In the Java application, go to the `Environment variables` panel and in the `CC_KEYCLOAK_REALMS` environment variable, declare as many realms as you need, separated by a `,`. For example `CC_KEYCLOAK_REALMS=realm_1,realm_2` declares `realm_1` and `realm_2`.
- Restart the application after the change.

You can also create a realm from the Keycloak administrator console. On the dropdown menu from the top left corner, click `create realm`.

>[!NOTE]
Starting with `26.2` release, Keycloak add-ons on Clever Cloud come with `admin-cli` client disabled by default. If you need it for provisioning through a `direct access grant`, you must enable it first.

### Exporting realms data

You can create a partial export using the Keycloak console:

- From the `Realm Settings` panel
- On the top right, click the dropdown`action` menu
- Select `partial Export`
- A cold export can be done at the build

You can create a full export using the environment variables of the Keycloak Java application:

- Go to the Keycloak Java application in the Clever Cloud Console
- In the Java application, create the `CC_KEYCLOAK_EXPORT_REALMS` environment variable
- Set the realms you want to export, separated by a `,`
- Rebuild the Java application from the Clever Cloud console

It's a total export, including the client's secrets and hashed password. Exported realms are available in `realms/export` folder of the FS Bucket.

### Importing realms data

Uploading previously exported data in `realms/import` folder in the associated FS Bucket enables importing realms data. The import process starts after rebuilding the Java application.

## Custom Themes and Plugins

Keycloak uses an [FSBucket](../fs-bucket) to install themes and plugins. To deploy a custom theme or custom plugin, simply download them into the respective `themes` or `providers` folder in your FSBucket.

## Add IP filtering in Keycloak for admin console

Two specific authentication flows with an IP addresses based filter are especially created and affected as default to clients `security-admin-console` and `admin-cli`. To use them (do not forget to make the same on each realm you want to protect):

- Enable "PLEASE-OPEN.IT Authenticator IP Range" to "Required"
- Click on the crank to access parameters
- Set IPs with authorized access

Those flows could be affected to your own clients if you need.

## Grafana dashboard & Metrics

Since version `25.06`, Keycloak add-on exposes [Prometheus](https://prometheus.io/) metrics on port `9000`. Use Clever Cloud's [Grafana integration](../../metrics/#publish-your-own-metrics) to visualize them.

You can also use a Grafana dashboard ready to import, available starting with Keycloak `26.2` release:
- Go to the `Metrics in Grafana` section of your organisation or personal space in [Console](https://console.clever-cloud.com/)
- Open Grafana, click on the `+` icon in the upper right corner and select `Import` dashboard
- Import this [JSON file](https://cc-keycloak.cellar-c2.services.clever-cloud.com/keycloak-grafana-dashboard.json)

Then you'll have a `Keycloak dashboard` in your Grafana folders. Just select your Keycloak add-on in the `runtime section`, you'll automatically get instance information, metrics, cache and performance data, etc.

## Hostnames

By default, your Keycloak instance is exposed through a Clever Cloud domain, as mentioned in the `Service dependencies` tab of your add-on.

### Custom hostname

You can use your own domain. [Just set it](../../administrate/domain-names) in the `Domains` section of the Java application of the Keycloak add-on. Then, edit the `CC_KEYCLOAK_HOSTNAME` environment variable, apply this change and restart the application.

### Admin hostname

By default, Keycloak expose administration console on the same hostname, but [you can use another one](https://www.keycloak.org/server/hostname#_exposing_the_administration_console_on_a_separate_hostname). Add its domain to the application and set it through the `CC_KEYCLOAK_HOSTNAME_ADMIN` environment variable. Then apply this change and restart the application.

## Known issues

### Java application deployment may fail

> Sometimes, application dependencies such as PostgreSQL may take a longer time to start. Wait and relaunch the deployment to fix this issue

- On the `Overview` tab from the Java application page
- Click `RE-BUILD AND RESTART`
