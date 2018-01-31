---
title: Trace add-on (deprecated)
position: 9
shortdesc: Trace is a Node.js performance monitoring tool which helps you to understand how your application behaves and lets you to find performance bottlenecks with ease
tags:
- addons
keywords:
- node
- nodejs
- monitoring
- microservices
- microservice
---

Trace provides error detection, alerting, distributed tracing and process monitoring for your Clever Cloud applications. Install the Trace Trace Clever Cloud add-on by following these steps:

## Prerequisites

NPM version 2.7.0 or greater must be installed. To update simply use `npm install npm -g`.

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">npm version</h4>
  </div>
  <div class="panel-body">
    Be sure to use npm version greater than 2.7.0. - as Trace uses scoped packages. If you can't update to npm@2.7.0 for whatever reason, you can still install Trace using `npm i risingstack/trace-nodejs
  </div>
</div>

## Installation

1. Click the "Add an add-on" button on the Clever Cloud dashboard
2. Select the "Trace by RisingStack" add-on
3. Choose a plan that fits for your application
4. Select the applications that will use this add-on. Linking more applications with the same add-on helps to find issues in a distributed system (microservices or SOA architecture)

The add-on sets the `TRACE_API_KEY` environment variable for every linked application.

<div class="panel panel-success">
  <div class="panel-heading">
    <h4 class="panel-title">Link multiple applications</h4>
  </div>
  <div class="panel-body">
    With linking multiple applications to the same add-on you will be able to monitor and debug distributed systems and see how you applications communicate with each other. This is recommended for micro-services and SOA architectures.
  </div>
</div>

## Application configuration

To start monitoring your applications you must first add them and name them by setting up TRACE_SERVICE_NAME environment variables for them.

To add the environment variable follow these steps:

1. Select your application
2. Pick the "Environment variables" menu
4. Add a new variable with, Name: TRACE_SERVICE_NAME, Value: My Application 1
4. Click "Add"
5. Repeat for all linked applications

If you'd like to know more on how you should name your services, read the guideline on naming infrastructures and services on [trace's documentation](http://trace-docs.risingstack.com/docs/how-to-name-your-infrastructure-and-services).

## Installating the Trace collector agent

1. Install the Trace collector as a dependency of your Node.js application using the following command `npm install @risingstack/trace --save`
2. Import Trace in the main script of your application. It should be the first module you require.
3. Deploy your application!
4. Generate some traffic on your website.

```javascript
// index.js

require('@risingstack/trace') // trace should be on top

// your application code

var express = require('express')
var app = express()

// so on ...
```

<div class="panel panel-danger">
  <div class="panel-heading">
    <h4 class="panel-title">Don't see your data?</h4>
  </div>
  <div class="panel-body">
    I just integrated my service and installed Trace: Run your application and wait a few minutes.
    I integrated my service more than 5 minutes ago: Check out the Troubleshooting page.
    I don’t know: Contact us via the live chat and we’ll figure it out for you.
  </div>
</div>

## Linking trace with additional applications

1. Select your application
2. Pick the "Add-ons" menu
3. Click the "link" button in the list where you see your Trace add-on
4. Repeat the original integration steps from # 3 Name you application