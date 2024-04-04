---
type: docs
title: Keycloak
draft: true
shortdesc: This add-on provides a Keycloak single sign-on and indentity and access management solution based on existing Clever Cloud services and taking the adventage of the Please open-it experiences, our Keycloak expert parner.
tags:
- addons
keywords:
- Keycloak
- Security
- Autentication
- Identity
- OAuth
- OpenID
aliases:
- /doc/deploy/addon/Keycloak
type: docs
---

**This service is currently released as a technical preview for a few months. It aims to be adjust to needs according to users feedbacks**

Keycloak is an open-source identity and access management solution that gives you powerful features to secure applications and services.
Based on Clever Cloud services, the Keycloak add-on takes advantage of all Clever Cloud features such as monitoring, scalability, high level of SLA, and simplicity.

We have thought of the Keyclaok add-on as the most convenient and ready-to-use for the most classic needs.

To build the best product, we work with Please Open-it (https://please-open.it/). They have been recognized experts in authentication and Keycloak solutions for years. Together, we built the most efficient and straightforward  Keycloak service.


## Key features
With the Keycloak add-on, you have access to a wide panel of services such as:
- Secure Identity Management
- Single Sign-On (SSO)
- Centralized Administration
- Customizable Authentication (OAuth 2.0, LDAP, SAML, OpenID Connect, and more...)
- Easily load your pluggins and themes
- Multi Realms
- Monitoring and Logging
- Export and Import
- Support and Maintenance

Keyclaok on Clever Cloud will allow your team to effortlessly set up a tailored authentication and access management solution, that can be adjusted to your needs and workloads. We also provide expertizing with our partner Please Open-it in case of needs.

## A specific use? Going further with Please Open-it!

"Please open-it" is not only an expertized company helping us to build a great add-on. They have years of experience in authentication and access management, and they are used to help companies configure and architect their tools.

Realizing how central such tooling needs for companies. We decided to tackle the need and provide expert advice and help as demand for the most complex and loaded systems.

With Please Open-it, we are proud to provide an efficient and affordable service to fit the most common needs.

However, you may need to address the most complex and specific use case!
Please Open-it provide Keycloak expertise on demand. [Reach us for more information](mailto:sales@clever-cloud.com).


## How it works?

When you subscribe to the Keyckloak add-on, we automatically set a Java instance based on a preconfigured Keycloak release built-in with our partner Please Open-it. It comes with the required PostgreSQL database and an FSBucket used for themes, plugging, and import or export.

We have chosen to let you see and manage these companion add-ons in the Console so that you can adjust them to your needs. You can change their settings and use the Clever Cloud ability to migrate from an XS-flavored database to another one if required. 

However, we thought the basic setup to power the most common usage. It should be able to handle millions of simultaneous connections. It suits a majority of needs.

> You can also activate auto-scalability (horizontal and/or vertical scaling)

By default, Keycloak on Clever Cloud comes with small-sized add-ons:

- Java 17: XS
- PostgreSQL: XS Tiny Space
- FSBucket

## Create Keycloak add-on

### Web Console

1. Create a new add-on by clicking on the **Create...** dropdown in the sidebar and then **an add-on**.
2. Select the Keycloak add-on.
3. You can skip linking the add-on to an application, it won't be needed.
4. Enter the name of your Keycloak add-on and select the zone where you wish to deploy it.
5. It's done!

### CLI

1. Make sure you have clever-tools installed locally. Report to the [getting started]({{< ref `doc/cli/getting_started.md` >}}) guide if needed.
2. List the available plans and options for Matomo: `clever addon providers show Keycloak`.
3. In your terminal, you can then run `clever addon create Keyclaok <app-name> --region <region> --org <org>` where `app-name` is the name you want for your add-on, `region` deployment region, and `org` the organization ID the application will be created under.

Refer to the [documentation]({{< ref `doc/cli/create.md` >}}) for more details on application creation with Clever Tools

## Accessing the Keycloak interface

Once you created your add-on, you can go to your Java application page in the console and click on "Open the application" 

![Open the application button](LIEN VERS L'IMAGE DU BOUTON DE LA CONSOLE)

You also can get the Keycloak URL from the information panel of your Keyckoak add-on in your Clever Cloud console.

### admin interface
The admin interface is accessible on the `/admin` endpoint:
- `iffslonattslbta6eilb-keycloak.services.clever-cloud.com/admin`
> Here, the URL comes from the information panel in the console and we add `/admin`

### Admin User and Password
At your first connection, you will have to change your password

### Realms management
We recommend using as few Realm as possible. That is a cost factor in Keycloak by impacting the performances significantly.

Realms can be managed in two way

1. RECOMMENDED using Clever Cloud's environment variables
- In your Keycloak java application, go to the `Environment variables` panel and set as many Realms you need, separate by `,`.
- Rebuild and redeploy your java application after the change

> to deploy two realm `realm_1`, `realm_2` just set `REALMS=realm_1,realm_2`


2. Create a Realm from the Keycloak admin console
- On the dropdown menu from the top left corner in the Keycloak admin consol, click on `create realm`.

> A Realm created by Clever Cloud's environment variables is set-up with an optimized configuration.


### Custome Themes and Plugins
We used FSBucket to install themes or plugins. To deploy a custom theme or custom plugins. Download them into the respective `Theme` or `providers` folder in your FSBucket. 

### Export and Import
If you export your Keycloak. An export file will be created in your FSBuckeet, under the `Export` folder.

To import data from another Keycloak. You can download your data in the `Import`folder in your FSBucket.


## Security and updates

The Keyclaok add-on is a fully managed application, you don't have to select a particular version. Still, it receives updates for both features and security, that we will manage for you with continuously upgraded versions over time.

After being updated, your Keycloak add-on could need to be restarted.

## Plans

### Base price
Keycloak on Clever Cloud is the easiest way to set it up, but you can go further and adjust the flavor of your instance, database, or cache. We provide [different plans for Java and MySQL](https://www.clever-cloud.com/pricing/).

### Software management and set-up

Additionally to the base plan, we add an extra cost for maintenance, configuration, and platform cost. **It is free during the BETA deployment, time for us to adjust the cost**

