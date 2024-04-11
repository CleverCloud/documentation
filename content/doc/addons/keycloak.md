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

Keycloak is an open-source identity and access management (IAM) solution that offers powerful authentication features for services and secure applications. Thanks to this add-on, you can deploy Keycloak in your organization in just one click. And it obviously leverages all Clever Cloud features such as monitoring, scalability, high availability SLA, etc.
To fit the most common needs, the Keycloak add-on comes with batteries included : sensible defaults, realms import/export for easy migration, Clever Cloud SSO, Keycloak Metrics, default theme, etc.
We have partnered with [*Please Open-it*](https://please-open.it/) to offer the most efficient and straightforward Keycloak service. They have been recognized experts for years and are a go-to reference for advanced deployments and consulting.

## Technical preview. What does that mean?

We are proud to release a great product, fit for the industry, and the easiest to use we can do.

To do that, we need feedback. We also want to be sure we have worked in a good direction. Hence, we have to fire-test the product.

During that time:
- Feature consistency is battle-tested
- UX and interface may evolve
- Bug and potential issues are deeply sought
- Features and pricing may evolve
- Free of charge service management fees

Suggestions are welcome!

## Key features
With the Keycloak add-on, you have access to a wide panel of services such as:
- Secure Identity Management
- Single Sign-On (SSO)
- Centralized Administration
- Customizable Authentication (OAuth 2.0, LDAP, SAML, OpenID Connect, and more...)
- Easily load your plugins and themes
- Multi Realms
- Monitoring and Logging
- Export and Import
- Support and Maintenance

Keycloak on Clever Cloud will allow your team to effortlessly set up a tailored authentication and access management solution, that can be adjusted to your needs and workloads. We also provide expertizing with our partner [*Please Open-it*](https://please-open.it/) in case of needs.

## A specific use? Going further with Please Open-it!
The Clever Cloud Keycloak add-on is an efficient and affordable service to fit the most common needs. However, realizing how central and criticial authentication needs are for companies, we decided to tackle the issue and recommend expert advice for the most complex and loaded systems.

[*Please Open-it*](https://please-open.it/) are not only the Keycloak experts who helped us building a great add-on. They have years of experience in authentication and access management, and are here to help architect and configure complex authentication projects. [Contact them directly for more information](mailto:sales@clever-cloud.com)__.

## How it works?
When you subscribe to the Keycloak add-on, we automatically deploy a Java instance with Keycloak pre-loaded and configured. We also deploy the required PostgreSQL database and an FSBucket used for themes, pluggins and import/export storage needs. 

By default, Keycloak on Clever Cloud comes with small-sized add-ons:
- Java 17: XS
- PostgreSQL: XS Tiny Space
- FSBucket

We have sized those resources to power the most common usage. It should suit a majority of needs. You can manage and adjust these resources directly in the Console to fit your them. You can for example change their settings, migrate from an XS-flavored database to another if required, etc. Please note that this is a feature available in the Tech Preview and may change in the future.


> You can also activate auto-scalability (horizontal and/or vertical scaling)


## Create Keycloak add-on
### Web Console
1. Create a new add-on by clicking on the **Create...** dropdown in the sidebar and then **an add-on**.
2. Select the Keycloak add-on.
3. You can skip linking the add-on to an application, it won't be needed.
4. Enter the name of your Keycloak add-on and select the zone where you wish to deploy it.
5. That's it !
### CLI
1. Make sure you have `clever-tools` installed locally. Report to the [getting started]({{< ref `doc/cli/getting_started.md` >}}) guide if needed.
2. List the available plans and options for Matomo: `clever addon providers show Keycloak`.
3. In your terminal, you can then run `clever addon create Keycloak <app-name> --region <region> --org <org>` where `app-name` is the name you want for your add-on, `region` deployment region, and `org` the organization ID the application will be created under.
Refer to the [documentation]({{< ref `doc/cli/create.md` >}}) for more details on application creation with Clever Tools

## Accessing the Keycloak interface
Once you have created your add-on, you can go to the Keycloak Java runtime page in the console and __click on "Open the application"__ 

![Open the application button]({{< ref `assets/images/open_the_app_ico.png` >}})

You also can get the Keycloak URL from the Clever Cloud console, in the information panel of your Keyckoak add-on.

### Keycloak admin interface
The admin interface is accessible on the `/admin` endpoint:

- `iffslonattslbta6eilb-keycloak.services.clever-cloud.com/admin`
> Here, the URL comes from the information panel in the console and we add `/admin` at the end.

### Admin User and Password
- A default user and password is provided in the Java application's environment variables
- __At your first connection, you will have to change the password__

### Realms management
We recommend using __as few Realm as possible__ : they may significantly impact the overall performances.

Realms can be managed in two way
1. __RECOMMENDED:__ using Clever Cloud's Keycloak add-on environment variables
- In your Keycloak java application, go to the `Environment variables` panel and set as many Realms you need, separate by `,`.
- Rebuild and redeploy your Java application after the change

> to deploy two realms `realm_1`, `realm_2` just set `REALMS=realm_1,realm_2`

2. Create a Realm from the Keycloak admin console
- On the dropdown menu from the top left corner in the Keycloak admin console, click on `create realm`.

> A Realm __created by Clever Cloud's environment variables is set up with an optimized configuration__.

### Custom Themes and Plugins
We used FSBucket to install themes or plugins. To deploy a custom theme or custom plugins. Download them into the respective `Theme` or `providers` folder in your FSBucket.

### Exporting data
There are two ways to export in Keycloak:
- A partial export using the Keycloak console
     - from the `Realm Settings` panel
     - On the top right, click on the dropdown`action` menu
     - Select `partial Export`
- A cold export can be done at the start

> This is a total export, including the client's secrets and hashed password

- Set in the environment variables tab of the Keycloak Java application from the Clever Cloud console:
    - `CC_EXPORT_REALM`
- restart the Java application from the Clever Cloud console

### Importing data
Importing Realm is done by adding priory exported in the `Import` folder in the associated FSBucket. After restarting the Java application, they would be imported.

## Security and updates
The Keycloak add-on is a fully managed application, you don't have to select a particular version. Still, it receives updates for both features and security, that we will manage for you with continuously upgraded versions over time.
After being updated, your Keycloak add-on could need to be restarted.

## Pricing plans
### Technical Review price plan
Keycloak on Clever Cloud is the easiest way to set up a ready-to-use Keycloak.

It starts with
- Java 17: XS
- PostgreSQL: XS Tiny Space
- FSBucket

We add services management fees for maintenance, configuration, platform costs, and support. During the technical review, this service management is free.

Hence, the total price for 30 days for the base plan is (according to the [pricing page](https://www.clever-cloud.com/pricing/)):
- `JAVA XS` (16€) + `PostgreSQL XS Tiny Space` (15€) + `< 100MB FSBucket` (0€) + `add-on management fees` (O€) = 31€/30 days

> You can go further and adjust the flavor of your JAVA instance or database to fit your needs. We provide [different plans for Java and PostgreSQL](https://www.clever-cloud.com/pricing/).

#### Technical Review plan sizing

Even if this Keycloak add-on might handle heavy traffic and an important number of simultaneous connections, we base the following estimate on the maximum load handle on [Keycloak](https://www.keycloak.org/high-availability/concepts-memory-and-cpu-sizing) sizing recommendation:
- 5 login by second
- 90 credential grants by the second
- 70 refresh tokens by second

We are benchmarking for more precise limitations.


### Known issues
#### Java application deployment may fail.

> Sometimes, application dependencies such as PostgreSQL may take a longer time to be started. Wait and relaunch the deployment to fix this issue

- On the `Overview` tab from the Java application page
- Click on `RE-BUILD AND RESTART`


