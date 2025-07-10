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

{{% details title="Empty repository git error" closed="true" %}}

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
…
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

{{% details title="'Not a git repository' error" closed="true" %}}

```text
fatal: Not a git repository (or any of the parent directories)
```

This means that the folder in which you are is not a git repository.
In your console, at the root of your project, type `$ git init`. This will create a new git repository for your folder locally. Link it to Clever Cloud by going under the Clever Cloud console. In your application's information menu you will find a deployment url. Add it to your local repository git remotes with `$ git remote add clever <your deployment url>`.
You can add all your files with `$ git add .`, then you need to commit the files with `$ git commit -m "<your commit message>"`.
You will finally push your code with `$ git push clever master`.
{{% /details %}}

{{% details title="'fatal: 'clever' does not appear to be a git repository'" closed="true" %}}

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

Contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice) to explain what your apps do.

Ensure all your pending invoices are paid.

{{% /details %}}

{{% details title="How to recover your data?" closed="true" %}}

In case of a pending invoice aged more than 30 days, Clever Cloud might delete your apps and add-ons. However, we keep backups for 30 days after deletion.

You have to pay all of your pending invoices to recover your data.

{{% /details %}}

## Network

{{% details title="Backend Timeout Limits" closed="true" %}}

Clever Cloud uses [Sōzu](https://www.sozu.io) as its load balancer and reverse proxy. Sōzu enforces a 180-second timeout for all backend operations to prevent resource exhaustion from hanging requests.

For operations that may exceed the 180-second limit, implement one of these approaches:

1. Use long polling to send periodic status checks from the client
2. Create an asynchronous worker system: move long-running tasks to a background [worker]({{< ref "doc/develop/workers/" >}} "workers")
3. [Purchase a custom load balancer from Clever Cloud](https://www.clever-cloud.com/fr/contact/) with different timeouts

##### Additional considerations:

- Design your application architecture to handle timeouts gracefully
- Break up long-running operations into smaller tasks

Use your embedded [Grafana]({{< ref "doc/metrics/">}} "Grafana on Clever Cloud") to monitor resource usage when implementing any of these solutions.

##### How can I diagnosing Network Issue with `curl`

To gather detailed timing information for each step of the connection process, run the following `curl` command:
``` bash
curl -o /dev/null -s -w "DNS resolution: %{time_namelookup}s\nTCP connection: %{time_connect}s\nTLS handshake: %{time_appconnect}s\nTime to first byte: %{time_starttransfer}s\nTotal time: %{time_total}s\n" https://<example.com>
```

{{% /details %}}

## Others issues

{{% details title="Missing GitHub organisation on the application creation page" closed="true" %}}

GitHub does not give us access to organisations created or joined *after* you've linked your GitHub account to Clever Cloud (which is a good thing). So you need to let the Clever Cloud API access it. You can do that on <https://GitHub.com/settings/applications>.

Feel free to reach to [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice) if this page wasn't helpful enough.

{{% /details %}}

{{% details title="My application is not accessible for an unknown reason" closed="true" %}}

Check the status of the services on [clevercloudstatus.com](https://www.clevercloudstatus.com/). The support team is also there to help you identify any potential errors or misconfiguration.
{{% /details %}}

{{% details title="There are a lot of open ports, according to a port scan." closed="true" %}}

If you tried to scan your domain, you may not only have scanned your app, but also several public load balancers.
Here is an explanation of the different port you may see.

- Port 9999 : [Zabbix](https://www.zabbix.com) uses this port to monitor the hypervisor.
- Ports 5000 to 6000 : The TCP redirection feature uses these ports to work. If you notice a port within this range open but haven't enabled the feature, it indicates that another app on the same hypervisor is using it. The load balancer assigns a unique port to each app, ensuring that your app is securely isolated. You can be assured that other users can't access your app through this port.
- Port 3000 : Juggernaut, the daemon torrent for the VM images use this port.
- Ports 1080 and 1081 : Those are necessary for the reverse-proxy Sōzu to be able to redirect traffic to your application. Port 1080 is for HTTP and 1081 for HTTPS
- Port 80 and 443 : Your app use these ports to receive HTTP and HTTPS traffic

{{% /details %}}
