---
title: Common apps configuration
position: 5
shortdesc: Learn how to do some basic steup configuration to get started
tags:
- apps
- dashboard-setup
---

#  Configuration items available on every instance type.

Each instance type (php,java,python,go,ruby…) has its own configuration. However, some of
these configuration items can be applied to any instance.

## Private SSH key

If your company manages its own artifacts in a private repository (like, you can only
access them via git+ssh or sftp), and you need a private key to connect to the server, you
can commit them in your application's Clever Cloud repository and then add the
`clevercloud/ssh.json`.

The content of this file is pretty straight-forward:

```javascript
{
    "privateKeyFile": "path/to/file"
}
```

The `privateKeyFile` field must be a path to a SSH private key. The path must be relative
to the root of your repository. e.g. if your private key file is in the `clevercloud`
folder and is named `my_key`, the `privateKeyFile` field will be `"clevercloud/my_key"`.

That key will be installed as `~/.ssh/id_rsa` before the start of the build. So the
dependency manager will use it to fetch libs only accessible by ssh.

*NB: Please provide a key without pass phrase, or the system will be unable to unlock it*

## Hooks

You can run specific tasks during the deployment of your application. Please
refer to the [hooks documentation](/doc/clever-cloud-overview/hooks/) to learn
more about them.

### Post deploy hook

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Post deploy hooks are being deprecated</h4>
  </div>
  <div class="panel-body">
    Please refer to the <a href="/doc/clever-cloud-overview/hooks/">hooks documentation</a> to replace them.
  </div>
</div>

If you need to perform additional actions after your app is started, you can define a
"postDeploy" hook in your `<instance_type>.json` file (e.g. if you are deploying a ruby app,
put it in your `ruby.json` file):

```javascript
{
  "hooks": {
    "postDeploy": "./clevercloud/myScript"
  }
}
```

The `postDeploy` field must contain the path to a script, relative to the root of your
repository. The script file **MUST** have execution right set.

In the example above, the script is a file named `myScript` in the `clevercloud` folder.
That is, right beside the `<instance_type>.json` file.

## Workers

You can run background tasks during in parallel of your application. They will be restarted automatically on error.

The workers automatically inherit your application's environment and are launch in the directory in which the
application is located.

All you need to do is add one (or several) envrionment variables as such:

```
CC_WORKER_COMMAND=my-awesome-worker
```

Or

```
CC_WORKER_COMMAND_0=my-awesome-worker
CC_WORKER_COMMAND_1=my-other-worker
```
