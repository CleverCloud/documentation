---
title: Deploy Node.js apps
shortdesc: Node.js is a platform built on Chrome's JavaScript runtime for building fast, scalable network applications.
tags:
- nodejs
---

# Deploy Node.js apps

Clever Cloud allows you to deploy any Node.js application. This page will
explain you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will help you to configure your apps with some
mandatory files to add, and properties to setup.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Requirements

Be sure that:

* you have pushed in <b>master branch</b>
* you listen on <b>0.0.0.0:8080</b>
* your packages.json either has a <b>scripts.start</b> or <b>main</b> field

The following code describes a Hello world application listening on port 8080:

```javascript
// Load the http module to create an http server.
const http = require('http');

// Configure our HTTP server to respond with Hello World to all requests.
const server = http.createServer((request, response) => {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Hello World\n");
});

// Last, but not least, listen on port 8080
// The environment variable PORT is automatically defined and equals to 8080
server.listen(process.env.PORT, '0.0.0.0');
```
Then, a *package.json* file is mandatory to initiate your app deployment on Clever Cloud. The next section will detail this point.

### Describing package.json

Even if you have no dependencies, you have to provide a `package.json` file at the root of your project’s directory.

<div class="alert">
  <h5>About dependencies:</h5>
  <ul>
  <li>For every Node.js project you **HAVE TO** provide a package.json file at the root of your project’s
directory.</li>
  <li>Additionally, make sure that the folder "/node_modules" is in your .gitignore file before pushing your app.</li>
  </ul>
</div>

If you already are a Node.js guru, you probably won't have to change anything to that
file. Just check the required fields below.

The `package.json` file should look like the following:

```javascript
{
  "name" : "myapp",
  "version" : "0.1.0",
  "main" : "myapp.js",
  "scripts" : {
    "start" : "node myapp.js"
  },
  "engines" : {
    "node" : "~4.0"
  }
}
```

### The json fields

The following table describes each of the fields formerly mentioned.

<table id="nodedeps" class="table table-bordered table-striped">
<thead>
<tr>
<th>Usage</th>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="cc-depusage" rowspan="2"><span class="label label-danger">At least one</span></td>
<td>scripts.start</td>
<td>This field provides a command line to run. If defined, <code>npm start</code> will be launched. Otherwise
we will use the <code>main</code> field. See below to know how and when to use the `scripts.start` field</td>
</tr>
<tr>
<td>main</td>
<td>This field allows you to specify the file you want to run. It should
be the relative path of the file starting at the project's root. It's used to launch your application if <code>scripts.start</code> is not defined.</td>
</tr>
<tr>
<td class="cc-depusage" ><span class="label label-default">Optional</span></td>
<td>engines.node</td>
<td>Sets the node engine version you app runs with. Any "A.B.x" or "^A.B.C" or "~A.B" version will lead
to run the application with the latest "A.B" local version. If this field is
missing, we use the latest LTS available. If you want to ensure that your app will always run,
please put something of the form "^A.B.C" and avoid setting only ">=A.B.C".</td>
</tr>
</tbody>
</table>

### Build and start

When deploying an application, there are two phases: build and run.

* The build phase installs the dependencies and executes the `scripts.install` in your `package.json` (if defined).
It's meant to build the whole application including dependencies and / or assets (if there are any).

* The run phase is executed from `scripts.start` if defined. This phase is only meant to start your application and should not
contain any build task.

All the build part should be written into the `scripts.install` field of the `package.json`. You can also add a custom bash script and
execute it with: `"scripts.install": "./build.sh"`

For more information, see <a href="https://docs.npmjs.com/misc/scripts">the npm documentation</a>

### NPM modules dependencies

If you need some modules you can easily add some with the *dependencies* field.

Here is an example :

```javascript
{
  "name" : "myapp",
  "version" : "0.1.0",
  "main" : "myapp.js",
  "scripts" : {
    "start" : "node myapp.js"
  },
  "engines": {
    "node": "0.8.15"
 },
"dependencies": {
  "express": "3.x",
  "socket.io": "0.9.x",
  "underscore": "1.4.3"
  }
}
```

#### Deploy with privates dependencies

If your application got privates dependencies, you can add a [Private SSH Key](https://www.clever-cloud.com/doc/clever-cloud-overview/common-application-configuration/#private-ssh-key).


## Node.js supported versions

Clever Cloud can virtually run any version of node >= 0.6 and any
module. Lesser (pre-npm) versions are not officially supported. Unstable
versions are not supported either. You can use the `engines.node` field
in `package.json` to define the wanted version.

## Supported package managers

We support [npm](https://www.npmjs.com) and [yarn](https://yarnpkg.com) as package managers.
You can define the environment variable `NODE_BUILD_TOOL` to `npm` or `yarn` to select the
one you want. If not specified, `npm` will be used.

`yarn` is only available on `node.js` instances for now.

If you want to use `yarn`, please note that it's only installed for pre-installed node versions.
Use `^6` or `^7` in your `engines.node` if you need to target the pre-installed version for a given
release.

## Pre-installed modules

We currently provide these pre-installed modules:

**You can use any version of node you need and any modules you need. Preinstall version is only for faster deployment process.**

* phantomjs

New versions will be added as they are released and are only available with pre-installed versions of node.

## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

To access your variable in your application, nothing simpler! Just get
it from your environment: `process.env.MY_VARIABLE`.

You can (and should) define the `NODE_ENV=production` environment variable as many frameworks
rely on it for production mode.

### Special env NPM_TOKEN

Since April 2015, npmjs.com allows you to have private repositories. The bad news is,
you have to write a specific line in your `.npmrc` for that. The good news is, on Clever
Cloud, you only need to provide the *token* part, and we set up everything for you!

So to register your npm auth token, you need to add to your application the `NPM_TOKEN`
environment variable.

``` javascript
Example:
NPM_TOKEN=00000000-0000-0000-0000-000000000000
```

As you can see, only the `authToken` value is needed, not the full url you can find in
your .npmrc.

## Custom run command

If you need to run a custom command (or just pass options to the program),
you can specify it through the `CC_RUN_COMMAND` environment variable.

For instance, for a meteor application, you can put

```
CC_RUN_COMMAND=node .build/bundle/main.js <options>
```

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these steps](/doc/clever-cloud-overview/add-application/) to deploy your application.

## Deployment video

<iframe width="853" height="480" src="https://www.youtube.com/embed/dxhSjHnrrhA?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>

More info on <a target="_blank" href="http://nodejs.org/">nodejs.org</a>.
