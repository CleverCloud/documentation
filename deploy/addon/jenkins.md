---
title: Jenkins
position: 4
shortdesc: This add-on provides a Jenkins master instance with a list of preinstalled plugins.
tags:
- addons
keywords:
- Jenkins
- continuous integration
- continuous deployment
- ci/cd
---

Jenkins is an an open source automation server which enables developers to build, test, and deploy their software.

## Clever Cloud Plugin

The Jenkins addon has a pre-installed Clever Cloud plugin allowing you to configure on demande Jenkins nodes.

It can be configured under `https://yourJenkins.services.clever-cloud.com/configureClouds/`. You will find a Cloud provider called `Clever Cloud` with which you can add new Agent Template. An Agent is defined by a label(the reference of your node in your Jobs), a display name, a Docker Image available from the Docker Hub and a machine size.

## Default plugin list

Jenkins comes with the following pre-installed plugins:

 - blueocean
 - git
 - artifactory
 - workflow-aggregator
 - git-client
 - ssh-credentials
 - saml
 - clevercloud

 ## Backup

By default, Clever Cloud perfoms a free backup every day, with a retention of three days. Retention and frequency can be customized for Premium customers. Each backup can be found in the add-on dashboard in the web console, along with the credentials.
