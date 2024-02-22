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

{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  If you're having trouble deploying applications or with with git, this section is for you. From git issues to configuration errors, problems can arise at different stages of your deployments.
{{< /hextra/hero-subtitle >}}

## Git-related issues

{{% details title="Some files disappear after an application restart" closed="true" %}}

Clever Cloud use Git to transfer your code and application's assets from your local host to your scaler. If your application writes files on the local file system, those files are not committed: so you can't save these files from a instance to an other.

For most of Cloud providers, the use of the file system is not a good practice. But we know it could be sometimes pretty useful. That's why we provide an on-demand file system, easily pluggable to your app. In that case, your files will not be stored on the Git file system, but on a clustered file system, dedicated to it, accessible via FTP. This is the FS Bucket add-on.

Follow the [File System buckets documentation page]({{< ref "doc/addons/fs-bucket" >}}) to set up an FS Bucket for your application.
{{% /details %}}

{{% details title="Troubleshooting empty repository git error" closed="true" %}}

In some cases, git may display this type of error message:

```text
Cloning into 'project'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
```

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
git push <cleverRemote> <yourSpecificBranchName>:master
```

If you called the Clever Cloud remote `clever` and your local branch is `production`, this becomes

```bash
git push clever production:master
```

{{% /details %}}

{{% details title="Troubleshooting 'Not a git repository' error" closed="true" %}}

```text
fatal: Not a git repository (or any of the parent directories)
```

This means that the folder in which you are is not a git repository.
In your console, at the root of your project, type `$ git init`. This will create a new git repository for your folder locally. Link it to Clever Cloud by going under the Clever Cloud console. In your application's information menu you will find a deployment url. Add it to your local repository git remotes with `$ git remote add clever <your deployment url>`.
You can add all your files with `$ git add .`, then you need to commit the files with `$ git commit -m "<your commit message>"`.
You will finally push your code with `$ git push clever master`.
{{% /details %}}

{{% details title="Troubleshooting 'fatal: 'clever' does not appear to be a git repository'" closed="true" %}}

"clever" is a name used in our examples to represent the Clever Cloud servers.
In order to be able to use the same name for yourself, you will need to create a git remote named clever like this:

```shell
git remote add clever <your-git-deployment-url>
```

You can find your deployment url under the Clever Cloud console in your application's information menu.
{{% /details %}}

{{% details title="Fail to push to a repository" closed="true" %}}

It might be because your SSH agent is not properly configured. Please check [the SSH documentation page]({{< ref "doc/account/ssh-keys-management#i-maybe-have-ssh-keys-i-want-to-check" >}}).
{{% /details %}}

## Deployments issues

{{% details title="Activating the troubleshooting mode" closed="true" %}}

Sometimes, when something goes wrong during the deployment, it can be hard to find out what happens. The troubleshoot mode allows you to keep the instances up while you find out what has happened.
Additionally, the troubleshoot mode increases the overall verbosity of the deployment process.

To enable this mode, simply add `CC_TROUBLESHOOT=true` to your environment variables.

{{% /details %}}

{{% details title="Node application failed to deploy silently" closed="true" %}}

This kind of silent error may be due to the server port your have setup in your application. Make sure your application is listening on port 8080.
Most of the time, this simple line could do the trick in your main JS file:

```javascript
// Listen on port 8080
server.listen(8080);
```

{{% /details %}}

## Moderation

{{% details title="What is moderation?" closed="true" %}}

Moderation means your account is not accessible anymore. You might have broken some important rules of Clever Cloud's General Terms of Use.

You are not allowed to create apps and add-ons, and run your current apps.

{{% /details %}}

{{% details title="Possible reasons why your app has been moderated" closed="true" %}}

The main reasons why your account has been moderated are:
- You run some forbidden apps such as those described on [this page](https://www.clever-cloud.com/acceptable-use-policy/)
- You have not paid your pending invoices older than 30 days
-  Clever Cloud system considers the lack of personal information or missing payment information as suspicious
- Our payment platform has spotted you as emitting fraudulent payments.

{{% /details %}}

{{% details title="How to recover your application online?" closed="true" %}}

Contact Clever Cloud's Support team at [support@clever-cloud.com](mailto:support@clever-cloud.com) to explain what your apps do.

Ensure all your pending invoices are paid.

{{% /details %}}

{{% details title="How to recover your data?" closed="true" %}}

In case of a pending invoice aged more than 30 days, Clever Cloud might delete your apps and add-ons. However, we keep backups for 30 days after deletion.

You have to pay all of your pending invoices to recover your data.

{{% /details %}}

## Others issues

{{% details title="Missing GitHub organization on the application creation page" closed="true" %}}

GitHub does not give us access to organizations created or joined *after* you've linked your GitHub account to Clever Cloud (which is a good thing). So you need to let the Clever Cloud API access it. You can do that on <https://GitHub.com/settings/applications>.

You can of course reach to <support@clever-cloud.com> if this page was not helpful enough.

{{% /details %}}

{{% details title="My application is not accessible for an unknown reason" closed="true" %}}

Check the status of the services on [clevercloudstatus.com](https://www.clevercloudstatus.com/). The support team is also there to help you identify any potential errors or misconfiguration.
{{% /details %}}
