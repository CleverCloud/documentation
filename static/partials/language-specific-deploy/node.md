## Configure your Node.js application
### Mandatory configuration

Be sure that:

* you listen on HTTP port **0.0.0.0:8080**
* you have a `package.json` file
* your `package.json` either has a **scripts.start** or **main** field
* the folder `/node_modules` is mentioned in your `.gitignore` file
* you enable production mode by setting the [environment variable](#setting-up-environment-variables-on-clever-cloud) `NODE_ENV=production`

### Select node version

You can use the `engines.node` field in `package.json` to define the wanted version, if not provided we will use the latest LTS version.

### About package.json

The `package.json` file should look like the following:

```json
{
  "name" : "myapp",
  "version" : "0.1.0",
  "main" : "myapp.js",
  "scripts" : {
    "start" : "node myapp.js"
  },
  "engines" : {
    "node" : "^20"
  }
}
```
#### The json fields

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
      <td class="cc-depusage" rowspan="2">
        <span class="label label-danger">At least one</span>
      </td>
      <td>scripts.start</td>
      <td>This field provides a command line to run. If defined, <code>npm start</code> will be launched. Otherwise we will use the <code>main</code> field. See below to know how and when to use the <code>scripts.start</code> field</td>
    </tr>
    <tr>
      <td>main</td>
      <td>This field allows you to specify the file you want to run. It should be the relative path of the file starting at the project's root. It's used to launch your application if <code>scripts.start</code> is not defined.</td>
    </tr>
    <tr>
      <td class="cc-depusage" ><span class="label label-default">Optional</span></td>
      <td>engines.node</td>
      <td>Sets the node engine version you app runs with. Any "A.B.x" or "^A.B.C" or "~A.B" version will lead to run the application with the latest "A.B" local version. If this field is missing, we use the latest LTS available. If you want to ensure that your app will always run, please put something of the form "^A.B.C" and avoid setting only ">=A.B.C".</td>
    </tr>
  </tbody>
</table>

### NPM modules dependencies

If you need some modules you can easily add some with the *dependencies* field in your `package.json`. Here is an example:

```json
{
  "name" : { ... },
  "engines": { ... },
  "dependencies": {
    "express": "4.x",
    "socket.io": "4.7.x",
    "underscore": "1.13.6"
  }
}
```

#### Private dependencies

If your application has private dependencies, you can add a [Private SSH Key]({{< ref "doc/reference/common-configuration.md#private-ssh-key" >}}).

### Supported package managers

We support [npm](https://www.npmjs.com) and [yarn](https://yarnpkg.com) as package managers.

The [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_NODE_BUILD_TOOL` allows you to define which build tool you want to use. The default value is set to `npm` but it can be any of these values:

* `npm-install`: uses [npm install](https://docs.npmjs.com/cli/install)
* `npm-ci`: uses [npm ci](https://docs.npmjs.com/cli/ci)
* `npm`: Defaults to `npm-install` for now
* `yarn`: uses [yarn](https://classic.yarnpkg.com/lang/en/)
* `yarn2`: uses [yarn@2](https://yarnpkg.com/)
* `custom`: uses the build tool set with `CC_CUSTOM_BUILD_TOOL`

If a `yarn.lock` file exists in your application's main folder, then the `yarn` package manager will be automatically used. To overwrite this behaviour, either delete the `yarn.lock` file or set the `CC_NODE_BUILD_TOOL` environment variable.

If none of the above package managers fit your needs, you can put your own using `CC_CUSTOM_BUILD_TOOL`.

## Automatic HTTPS redirection

You can use the [X-Forwarded-Proto header]({{< ref "doc/find-help/faq.md#how-to-know-if-a-user-comes-from-a-secure-connection" >}}) to enable it.

If you are using [Express.js](https://expressjs.com/), you can use [express-sslify](https://www.npmjs.com/package/express-sslify) by adding:

```javascript
app.use(enforce.HTTPS({
  trustProtoHeader: true
}));
```

### Custom build phase

The build phase installs the dependencies and executes the `scripts.install` you might have defined in your `package.json`.
It's meant to build the whole application including dependencies and / or assets (if there are any).

All the build part should be written into the `scripts.install` field of the `package.json` file. You can also add a custom bash script and execute it with: `"scripts.install": "./build.sh"`

For more information, see <a href="https://docs.npmjs.com/misc/scripts">the npm documentation</a>

## Development Dependencies

Development dependencies will not be automatically installed during the deployment. You can control their installation by using the `CC_NODE_DEV_DEPENDENCIES` environment variable which takes `install` or `ignore` as its value. This variable overrides the default behaviour of `NODE_ENV`.

Here are various scenarios:

- `CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies will be installed.
- `CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies will not be installed.
- `NODE_ENV=production, CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies will be installed.
- `NODE_ENV=production, CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies will not be installed.
- `NODE_ENV=production`: Package manager (NPM / Yarn) default behaviour. Development dependencies will not be installed.
- Neither `NODE_ENV` nor `CC_NODE_DEV_DEPENDENCIES` are defined: Package manager (NPM / Yarn) default behaviour. Development dependencies will be installed.

### Custom run command

If you need to run a custom command (or just pass options to the program), you can specify it through the `CC_RUN_COMMAND` [environment variable](#setting-up-environment-variables-on-clever-cloud).

For instance, for a meteor application, you can have `CC_RUN_COMMAND="node .build/bundle/main.js <options>"`.

### Custom run phase

The run phase is executed from `scripts.start` if defined. This phase is only meant to start your application and should not
contain any build task.

### Use private repositories with CC_NPM_REGISTRY and NPM_TOKEN

Since April 2015, npmjs.com allows you to have private repositories. If you want to use a private repository on npmjs.com (the default one), you only need to provide the *token* part. To register your auth token, you need to add to your application the `NPM_TOKEN` environment variable.

```bash
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

Then, the .npmrc file will be created automatically for your application, with the registry url and the token.

```txt
//registry.npmjs.org/:_authToken=00000000-0000-0000-0000-000000000000
```

To authenticate to another registry (like github), you can use the `CC_NPM_REGISTRY`  environment variable to define the registry's host.

```bash
CC_NPM_REGISTRY="npm.pkg.github.com"
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

```txt
//npm.pkg.github.com/:_authToken=00000000-0000-0000-0000-000000000000
```
