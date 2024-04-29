---
type: docs
title: Keycloak
description: This add-on provides a one-click Keycloak single sign-on and identity and access management (IAM) solution based on existing Clever Cloud services and taking advantage of the *Please open-it* experiences, our Keycloak expert partner.
tags:
- addons
keywords:
- Keycloak
- IAM
- Security
- Autentication
- Identity
- OAuth
- OpenID
aliases:
- /doc/deploy/addon/Keycloak
type: docs
---

Keycloak is an open source identity and access management (IAM) solution that offers powerful authentication features for services and secure applications. Thanks to this add-on, you can deploy Keycloak in your organization in just one click. It leverages all Clever Cloud features such as monitoring, scalability, high availability SLA, etc.

To fit the most common needs, the Keycloak add-on comes with batteries included: sensible defaults, easy migration with realms import/export, Keycloak Metrics, default theme, etc.


## Technical preview? What does that mean?

Clever Cloud uses your [feedback](https://www.clever-cloud.com/fr/contact-sales/) to release products fit for the industry and easy to use. A technical preview enables our users to fire-test the product.  Hence, the Keycloak add-on is first **offered as a Tech Preview**, before releasing it for production use.

During the Tech Preview period:
- Features consistencies are battle-tested and may evolve; 
- UX and interface aren't final and may also evolve;
- Bugs and potential issues feedback are deeply sought;
- Features and pricing may evolve;
- 0 € service & maintenance fees.

## Key features
Keycloak on Clever Cloud allows you to effortlessly set up a tailored authentication and access management solution, that you can adjust to your needs and workloads. It offers a wide panel of services such as:
- Secure Identity Management;
- Single Sign-On (SSO);
- Centralized Administration;
- Customizable Authentication (OAuth 2.0, LDAP, SAML, OpenID Connect, and more...);
- Easily load plugins and themes;
- Multi Realms;
- Monitoring and Logging;
- Export and Import;
- Support and Maintenance.

## Need expert advice?
The Clever Cloud Keycloak add-on is designed to meet the most common needs. For the most complex and loaded systems, [*Please Open-it*](https://please-open.it/), our partners and Keycloak experts behind this add-on, can provide assistance: [Contact us for more information](mailto:sales@clever-cloud.com).

## How it works?
When you create the Keycloak add-on, Clever Cloud automatically deploys:

-  A [Java](https://developers.clever-cloud.com/doc/applications/java/java-jar/) instance with Keycloak pre-loaded and configured
- A [PostgreSQL](https://developers.clever-cloud.com/doc/addons/postgresql/) database
- An [FSBucket](https://developers.clever-cloud.com/doc/addons/fs-bucket/) used for themes, plugins, and import/export storage needs. 

By default, Keycloak on Clever Cloud uses small-size resources, i.e:
- XS Java 17;
- XS Tiny Space PostgreSQL;
- Less than 100 MB FSBucket.

Those resources are dimensioned to suit a majority of needs. You can however manage and adjust them directly in the Console to fit your needs. You can for example change their settings, migrate to a larger storage database, etc. 

> Vertical auto-scalability can be activated now, with horizontal auto-scalability set to arrive soon!

Note: The setting of resource sizes manually is a Tech Preview feature that may change in the future.


## Create a Keycloak add-on
### From the Web Console
1. Create a new add-on by clicking the **Create...** dropdown in the sidebar and then **an add-on**.
2. Select the Keycloak add-on.
3. You can skip linking the add-on to an application, it won't be needed.
4. Enter a name for your Keycloak add-on and select the zone where you want it to be deployed.
### Using the CLI
1. Make sure you have `clever-tools` installed locally. Please refer to the [getting started]({{< ref `doc/cli/getting_started.md` >}}) guide if needed.
2.  List the available plans and options for Keycloak: `clever addon providers show addon-keycloak`.
3. In your terminal, run `clever addon create addon-keycloak <app-name> --region <region> --org <org>` where `app-name` is the name you want for your add-on, `region` deployment region, and `org` the organization ID where to create it.
Refer to the [documentation]({{< ref `doc/cli/create.md` >}}) for more details on add-on creation with Clever Tools.

## Accessing the Keycloak interface
Once you have created your add-on, go to the Console Keycloak Java runtime page and __click on "Open the application"__ 

![Open the application button](/images/doc/open_the_app_ico.png )

You also can get the Keycloak add-on URL from the Clever Cloud console, in the information panel of your Keycloak add-on.

### Keycloak admin interface
The admin interface is accessible on the `/admin` endpoint:

- `iffslonattslbta6eilb-keycloak.services.clever-cloud.com/admin`
> Here, the URL comes from the information panel in the console and we add `/admin` at the end.

### Admin User and Password
- A default user and password are provided in the Java application by the environment variables `CC_KEYCLOAK_ADMIN` and `CC_KEYCLOAK_ADMIN_PASSWORD`.
- You will be asked to __change the password at your first connection__

### Realms management
We recommend using __as few realms as possible__: they may significantly impact the overall performances.

Realms can be managed in two ways
1. __RECOMMENDED:__ by using the environment variables of the Clever Cloud Java application associated with the Keycloak add-on.

- In your Keycloak java application, go to the `Environment variables` panel and declare as many realms as you need, separating each of them by `,`.

>  `REALMS=realm_1,realm_2` will declare two realms : `realm_1`, `realm_2`.

> Don't forget to apply change at the bottom of the environment variable page if you use the console.

- `Restart` your Java application after the change.

2. Create a realm from the Keycloak admin console.

- On the dropdown menu from the top left corner in the Keycloak admin console, click `create realm`.

> A Realm __created by Clever Cloud's environment variables is set up with an optimized configuration__ such as brute-force detection and specific metrics.

### Custom Themes and Plugins
We use [FSBucket](https://developers.clever-cloud.com/doc/addons/fs-bucket/) to install themes and plugins. To deploy a custom theme or custom plugin, simply download them into the respective `themes` or `providers` folder in your FSBucket.

### Exporting data
There are two ways to export Keycloak data:
1. A partial export using the Keycloak console.
     - from the `Realm Settings` panel;
     - On the top right, click on the dropdown`action` menu;
     - Select `partial Export`;
     - A cold export can be done at the start.

> This is a total export, including the client's secrets and hashed password

2. Set in the environment variables tab of the Keycloak Java application from the Clever Cloud console.
    - In the Java application, you can explicit Realm you want to export as arguments to  the `CC_EXPORT_REALM` environment variable;

    > For instance, the following values will export `my_realm` after a restart:
    `CC_EXPORT_REALM=my_realm`
    - restart the Java application from the Clever Cloud console.

> Don't forget to apply change at the bottom of the environment variable page if you use the console.

### Importing realms data
Importing realms data is done by uploading previously exported data in the `Import` folder in the associated FSBucket. The realms data will be imported after restarting the Java application.

## Security and updates
Since the Keycloak add-on is a fully managed application, you don't have to select a particular version. It is automatically upgraded and updated both for features and security.
After being updated, your Keycloak add-on may need to be restarted.

> We will warn you when a restart is required.

## Pricing plans
### Technical Review price plan
The Tech Preview pricing is simple: it only consists of the sum of the deployed resources. In details, [as per the pricing plan](https://www.clever-cloud.com/pricing/), the default configuration is priced as such:

| Resource                 | Price / 30 days |
| :----------------------- | --------------: |
| XS Java                  |             16€ |
| XS Tiny Space PostgreSQL |             15€ |
| FS Bucket < 100 MB       |              0€ |
| Service and Management   |              0€ |
| **Total**                    |             **31€** |
Note: During the Technical Preview, no extra service management fees are applied.


> You can go further and adjust the flavor of your JAVA instance or database to fit your needs. We provide [different plans for Java and PostgreSQL](https://www.clever-cloud.com/pricing/).

#### Technical Review plan sizing

Even if this Keycloak add-on might handle heavy traffic and an important number of simultaneous connections, the default configuration should handle the following load (based on [Keycloak](https://www.keycloak.org/high-availability/concepts-memory-and-cpu-sizing) sizing recommendation)
- 5 login by second;
- 90 credential grants by the second;
- 70 refresh tokens by second.


### Known issues
#### Java application deployment may fail

> Sometimes, application dependencies such as PostgreSQL may take a longer time to be start. Wait and relaunch the deployment to fix this issue

- On the `Overview` tab from the Java application page;
- Click `RE-BUILD AND RESTART`.
