---
title: Introduction to Add-ons
position: 2
shortdesc: 'This article introduces the add-ons: a way to add services to your application on Clever Cloud.'
tags:
- addons
keywords:
- addons
- addon
---

Add-ons are a way to add services to your application, for example a database or a caching system, to enrich its
features.

An add-on can be shared by different applications to share data between them. It can be a database shared by two or
three applications of your infrastructure for example, or they can be independent.

The add-ons offer different plan to adapt to your needs. You can find details about them on the documentation page of
the add-on.

## Available add-ons

Clever Cloud provides multiple add-ons to work with your applications:

* [MySQL](/doc/addons/mysql)
* [PostgreSQL](/doc/addons/postgresql)
* [MongoDB](/doc/addons/mongodb)
* [FS buckets](/doc/addons/fs_buckets)
* [Cellar](/doc/addons/cellar)
* [Redis](/doc/addons/redis)

## Create an add-on for your application

In order to create an add-on for your application, go to the [Clever Cloud Console](https://console.clever-cloud.com/).
When you are in the main page of the console, go to the organization in which you wan to create the add-on,
for example your [personal space](https://console.clever-cloud.com/users/me).

When you are in the organization, click on **Add an add-on**. This space let you create and configure the
add-on to follow your needs.

First, choose which *type* of add-on you want to create. See above to have a list of available add-ons and the
corresponding pages for a description and information.

Now, select the plan you need for you add-on. You can find details about the pricing, the capacity of the add-on, ...
on this page or in the corresponding documentation page.

The third step offers you to choose with which application you want to link you add-on. Linking an add-on to an
application will provide configuration to the application through [environment variables](/admin-console/environment-variables).
This environment variables must be used in your application to, for example, provide the credentials and the
localization of the database provided by the add-on.

The last step lets you choose the name of the add-on (for example "My database") and the region where the add-on is
hosted. Click on the **Create** button and the add-on will now be available in your organization, and corresponding
environment variables will be available for the applications linked to the add-on you just created.

## Managing your add-on

Once an add-on is created, two tabs are available:

* the Information tab
* the Configuration tab


### Link an add-on to your application

To link an add-on with your application, just follow the following steps:

1. Go in the organization of your application and click on the name of the application you want to link with your add-on.
2. Go in the **Add-ons** section.
3. Click on the **Link** button of the add-on you want to link to your application.


### Information screen

This screen sums-up the characteristics of the selected add-on.
Features and environment variables (if applicable) are shown.

<figure class="cc-content-img">
  <a class="cc-content-img" href="/doc//assets/images/managing-addons-info.png">
    <img src="/doc/assets/images/managing-addons-info.png">
  </a>
  <figcaption>
    Example of the information tab of an add-on
  </figcaption>
</figure>


### Configuration screen

Add-ons can be managed from the Configuration tab.
This screen is managed directly by the provider of the add-on.

<figure class="cc-content-img">
  <a class="cc-content-img" href="/doc/assets/images/managing-addons-config.png">
    <img src="/doc/assets/images/managing-addons-config.png">
  </a>
  <figcaption>
    Example of the configuration tab of an add-on
  </figcaption>
</figure>


## Delete an add-on

To delete an add-on, go to the *Configuration* page of the add-on, and click on *Remove add-on*.
Warning: After deletion of the add-on, all associated data will be removed.
