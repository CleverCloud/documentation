---
type: docs
title: Troubleshooting
position: 4
shortdesc: Common issues and errors you may have
tags:
- help
keywords:
- support
- git issues
- troubleshoot
type: docs
---

## TROUBLESHOOT Mode

Sometimes, when something goes wrong during the deployment, it can be hard to find out what happens. The troubleshoot mode allows you to keep the instances up while you find out what has happened.
Additionally, the troubleshoot modes increases the overall verbosity of the deployment process.

To enable the troubleshoot mode, simply add `CC_TROUBLESHOOT=true` to your environment variables.


In addition to this, here are some common issues and how to fix them.

## File Persistence issues

> "Why are my files disappearing after an application restart?”

Clever Cloud use Git to transfer your code and application's assets from your local host to your scaler. If your application writes files on the local file system, those files are not committed: so you can't save these files from a instance to an other.

For most of Cloud providers, the use of the file system is not a good practice. But we know it could be sometimes pretty useful. That's why we provide an on-demand file system, easily pluggable to your app. In that case, your files will not be stored on the Git file system, but on a clustered file system, dedicated to it, accessible via FTP. This is the FS Bucket add-on.

Follow the [File System buckets documentation page]({{< ref "doc/addons/fs-bucket" >}}) to set up an FS Bucket for your application.

## Git issues

### warning: You appear to have cloned an empty repository

> “Logs are telling me \"warning: You appear to have cloned an empty repository\"”

This usually means that you created an application and asked to start it in the console without having pushed any source code to it before.

Under the Clever Cloud console, in your application's information menu you will find a deployment url. Add it to your local repository git remotes with `$ git remote add clever <your deployment url>`.
You can now push your commits to the new remote with `$ git push clever master`.

It may also be because you are working on another branch than master and pushed this specific branch to Clever Cloud and you encountered this error:

```bash
remote: You tried to push to a custom branch.
remote: This is not allowed.
remote: error: hook declined to update refs/heads/<yourSpecificBranchName>
...
error: failed to push some refs to '<yourSpecificBranchName>'
```

Clever Cloud uses the master branch to deploy your application but this does not mean that you cannot use another one on your computer.
What differs if you use another branch than master on your computer is that you need to explicitly tell Clever to consider the specific branch as the master one.

```bash
$ git push <cleverRemote> <yourSpecificBranchName>:master
```

If you called the Clever Cloud remote `clever` and your local branch is `production`, this becomes

```bash
$ git push clever production:master
```

### fatal: Not a git repository (or any of the parent directories)

This means that the folder in which you are is not a git repository.
In your console, at the root of your project, type `$ git init`. This will create a new git repository for your folder locally. Link it to Clever Cloud by going under the Clever Cloud console. In your application's information menu you will find a deployment url. Add it to your local repository git remotes with `$ git remote add clever <your deployment url>`.
You can add all your files with `$ git add .`, then you need to commit the files with `$ git commit -m "<your commit message>"`.
You will finally push your code with `$ git push clever master`.

### fatal: 'clever' does not appear to be a git repository

"clever" is a name used in our examples to represent the Clever Cloud servers.
In order to be able to use the same name for yourself, you will need to create a git remote named clever like this:

```bash
$ git remote add clever <your-git-deployment-url>
```

You can find your deployment url under the Clever Cloud console in your application's information menu.

### Fail to push to a repository

It might be because your SSH agent is not properly configured. Please check [the SSH documentation page]({{< ref "doc/account/ssh-keys-management#i-maybe-have-ssh-keys-i-want-to-check" >}}).

## Node application failed to deploy silently

> “My Node.js application is unable to start. Logs are not helping”

This kind of silent error may be due to the server port your have setup in your application. Make sure your application is listening on port 8080.
Most of the time, this simple line could do the trick in your main JS file:

```javascript
// Listen on port 8080
server.listen(8080);
```

## My GitHub organization is not listed on the application creation page

GitHub does not give us access to organizations created or joined *after* you've linked your GitHub account to Clever Cloud (which is a good thing). So you need to let the Clever Cloud API access it. You can do that on <https://GitHub.com/settings/applications>.

You can of course reach to support@clever-cloud.com if this page was not helpful enough.

## Websites are not accessible

Check the status of the services on [clevercloudstatus.com](https://www.clevercloudstatus.com/).
