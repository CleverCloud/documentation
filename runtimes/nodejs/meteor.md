---
title: Deploying Meteor.js apps
shortdesc: Meteor is an open source platform for web, mobile, and desktop.
tags:
- meteor
- meteorjs
- nodejs
---

Clever Cloud allows you to deploy any Meteor.js application. This page will explain how to set up your application to run it on our services.

Be sure your `.meteor` folder is in your git repository.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/) and choose the Meteor.js type.

## Create a MongoDB add-on

Usually, your meteor.js application will need a MongoDB database. You can create one by following [this page](/doc/addons/clever-cloud-addons/)

## Create the environment variables

To run, your Meteor.js application needs a few mandatory [environment variables](https://www.clever-cloud.com/doc/admin-console/environment-variables/):

- `MONGO_URL`: this is the mongo uri you can find in your mongodb's dashboard, it has to start with `mongodb://`
- `ROOT_URL`: this is your application's root url. It has to start with `http://` or `https://`
- `PORT`: keep the current value of 8080

## Activate the dedicated build

Meteor.js eats a lot of memory during the build. You most likely will need to activate the [dedicated build feature](https://www.clever-cloud.com/doc/admin-console/apps-management/#dedicated-build).

If your build still fails after you enabled the feature, please contact us on the support so we can set a bigger scaler for the build (M scalers don't always have enough memory).

## Deployment

From there, your application should be fully configured to deploy. At each deployment, the needed Meteor.js version will be read from `.meteor/release` and installed.

You can now push ([using clever tools](https://www.clever-cloud.com/doc/clever-tools/manage/) or [using git](https://www.clever-cloud.com/doc/clever-cloud-overview/add-application/#git-deployment)) your code.

Your application will then be built using `meteor build --server-only` and deployed from the files created by this command.

If you want to set custom start parameters, the main entry point of built meteor applications is: `.build/bundle/main.js`.
Add in the `scripts.start` field of the package.json: `node .build/bundle/main.js <parameters>`

## Migrate from a Node.js instance

If you want to migrate from your classic node.js app to a meteor application, contact our support in the console or at
support@clever-cloud.com with the application id.

## Automatic HTTPS redirection

You can use this atmosphere package to redirect your users to the HTTPS version of your application:
[force-ssl](https://atmospherejs.com/meteor/force-ssl)

## Oplog Tailing
Oplog tailing is supported on dedicated databases (starting from Hazelnut). Contact the support to enable oplog. Once enabled, set the following environment variable:
- `MONGO_OPLOG_URL`: `mongodb://[…]mongodb.services.clever-cloud.com:{DB_PORT}/local?authSource={DB_NAME}`
