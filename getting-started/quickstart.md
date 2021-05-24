---
weight: 1
title: Quickstart
shortdesc: quickstart guide on Clever Cloud
tags:
- getting-started
keywords:
- quickstart
---

{{< readfile "/content/partials/authentication.md" >}}

## Deploy your code

### What is an application

An application is defined on Clever Cloud by the following elements:

* a dedicated language/framework
* a deployment method (FTP and/or Git)
* RAM and CPU consumption, depending on the language or framework used
* an optional configuration file you may add to your project

If one of these elements is missing, Clever Cloud can't deploy your application properly (except the configuration file, optional in some cases).

Supported platforms:

* [Docker]({{< ref "/deploy/application/docker/docker" >}})
* [Go]({{< ref "/deploy/application/golang/go" >}})
* [Haskell]({{< ref "/deploy/application/haskell/haskell" >}})
* [Java]({{< ref "/deploy/application/java/" >}}) [Play Framework 1 & 2, Maven, War files… ]
* [Node.js]({{< ref "/deploy/application/javascript/by-framework/nodejs" >}})
* [PHP]({{< ref "/deploy/application/php/php-apps" >}})
* [Python]({{< ref "/deploy/application/python/python_apps" >}})
* [Ruby]({{< ref "/deploy/application/ruby/ruby-rack" >}})
* [Rust]({{< ref "/deploy/application/rust/rust" >}})
* [Scala]({{< ref "/deploy/application/scala/scala" >}})
* [Elixir]({{< ref "/deploy/application/elixir/elixir" >}})

### How it works

When an application's code is pushed to git or via FTP, the platform receives it. It then checks the resources’ requirements. If they are complete, the deployment is launched. When finished and successful, the application is up and running.

The log system retrieves all output from the application and displays it in the logs tab of your application in the Clever Cloud console.

### Create an application

In the [Clever Cloud Console](https://console.clever-cloud.com/):

1. Select the proper organization you want to add the application to. At this point you must only have the Personal Space but you can create one. Then, click on the **Add an application** button in the **Organization Manager** panel.

This starts the application creation wizard. If your account has been linked to GitHub, you can select a repository from your GitHub account.

If you want to deploy an application within a GitHub organisation, first [grant the Clever Cloud API access to it](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

2. Select the language or the framework you need
3. *Optional:* For PHP applications, you can choose between FTP and Git deployment.
4. You will be able to fine-tune your scaling configuration. Horizontal scaling is the number of instances that can run at the same time. Vertical scaling sets the minimum and maximum size the instance can be.
5. Enter the name and description of your application.
6. *Optional*: The wizard will offer you to [add an add-on]({{< ref "deploy/addon" >}}) to your application.
7. *Optional*: The wizard will offer you to [add environment variables]({{< ref "develop/env-variables.md" >}}) to your application.

### Git Deployment

*To deploy via Git, you need it installed on your machine. You can find more information on Git website: [git-scm.com](https://git-scm.com)*

*Note:* During the deployment, the .git folder is automatically deleted to avoid security problems. If you need to know which version is used on the server please use the `COMMIT_ID` [environment variable]({{< ref "develop/env-variables.md" >}}).

Follow these steps to deploy your application:

1. Get the git deployment url in the application information page, which looks like: `git+ssh://git@push.<zone>.clever-cloud.com/<your_app_id>.git`.

2. In your terminal, go to your application repository. If you do not already track your app with git, start by typing:

```bash
git init
git add .
git commit -m "first commit"
```

3. Then, link your local repository to Clever Cloud by providing the Git remote url:

```bash
git remote add <remote-name> <your-git-deployment-url>
```

4. Push your application to Clever Cloud:

```bash
git push <remote-name> <branch-name>:master
```

{{< alert "warning" "Warning:" >}}
   <p>You can only push to the <strong>master</strong> branch for deployment.
   Trying to push to another branch will trigger an error.</p>
   <p>In order to push to <strong>master</strong> from a non-master local branch, use this syntax:</p>
   <pre>git push &lt;remote&gt; &lt;your branch&gt;:master</pre>
{{< /alert >}}

You can see your application **logs** in the dashboard to **monitor the deployment**.

{{< alert "warning" "Troubleshooting:" >}}
   <p>If the remote asks you for a password right after a git push attempt, this may be due to a SSH Key misconfiguration.
   <br>Add your SSH key to your profile here:
   <a href="https://console.clever-cloud.com/users/me/ssh-keys">https://console.clever-cloud.com/users/me/ssh-keys</a></p>
   <p>The full tutorial about adding SSH key is here: <a href="/account/ssh-keys-managment/">Adding SSH keys</a> </p>
{{< /alert >}}

#### Automated Deployment with GitHub

Once you have created your application with GitHub, each push on the `master` branch will trigger a deployment. If you want to deploy an other branch than `master`, you can go to the `information` panel of your application and select the default branch to use.

{{< image "/images/github-deployment-branch.png" "Github deployment branch select" >}}

{{< alert "warning" "Warning:" >}}
   <p>You can't directly push to an application created on Clever Cloud as a GitHub app: in this case, only the automatic deployment from GitHub is henceforth allowed.</p>
   <p>If you try to push to Clever Cloud, as you would do for a non-GitHub app, you will get the following error :</p>
   <pre>fatal: '/data/repositories/&lt;app_id&gt;.git' does not appear to be a git repository</pre>
   <p>Indeed, no git repository is created on Clever Cloud because the application is directly cloned from GitHub.</p>
   <p>If you have to push directly to a repo in order to deploy an application (eg if you deploy from a CI), then create a non-GitHub app.</p>
{{< /alert >}}

If you don't find your repository in the list fetched from Github, a workaround is to unlink your account in your profile here : https://console.clever-cloud.com/users/me/information, remove **Clever Cloud API** from your Github [Authorized OAuth Apps](https://github.com/settings/applications) and link again your Github account to your Clever Cloud account.

**Private GitHub repositories are also supported.**

Caution: in GitHub, private repositories in an ordinary user account are an all-or-nothing deal: either someone has full read write access (i.e., they're a collaborator) or they have no access. 

However, if you set up an organization, create the repo under the aegis of the organization, and then add the collaborator, you have much more fine-grained control (including giving read-only access to a private repository).

### FTP Deployment

It is possible to deploy via FTP with PHP applications.  

To deploy via FTP, you need an FTP software installed on your machine. [Filezilla](https://filezilla-project.org/) is one of them.

When you have chosen to deploy your application via FTP, a [FS Bucket]({{< ref "/deploy/addon/fs-bucket.md" >}}) has been created with an ID
matching your application's ID. You will find the FTP credentials in the configuration tab of this particular FS Bucket.

[More documentation about Filezilla.](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29)

{{< alert "warning" "Warning:" >}}
<p>An FTP application is automatically started once the application is created, even if no code has been sent.</p>
{{< /alert >}}

{{< alert "warning" "Our advice:" >}}
<p>FTP deployment is ok for small websites but not for large ones. We strongly recommend you to use <b>Git</b> deployment for <b>large PHP websites</b>.</p>
{{< /alert >}}

### Application management generalities

There are many tabs available in the application's menu:

- Information: General information about your application
- Scalability: Set-up scalability options
- Domain names: Manage custom domain names
- Environment variables: Manage environment variables
- Service dependencies: Link add-ons and applications
- Exposed configuration: Manage exposed environment variables
- Activity: Track last deployments
- Logs: Visualize application's logs
- Metrics: Visualize application's metrics
- Consumption: Visualize your application's consumption.

## Create your first add-on

Applications often requires one or more services in addition to the runtime itself. Add-ons are services you can use independently, or you can link them with your application(s). For instance, you may want to add a database or a caching system to your application or just have a database with no linked application.

An add-on can be shared by different applications to share data between them. It can be a database shared by two or three applications of your infrastructure for example, or they can be independent.

Most of the add-ons catalog is provided by Clever Cloud, but vendors are also allowed to provide services external to Clever Cloud ([See how to integrate your SaaS with Clever Cloud]({{< ref "extend/cc-api.md" >}}))

### Available add-ons

Clever Cloud provides multiple add-ons to work with your applications:

* [MySQL]({{< ref "/deploy/addon/mysql/mysql" >}})
* [PostgreSQL]({{< ref "/deploy/addon/postgresql" >}})
* [MongoDB]({{< ref "/deploy/addon/mongodb" >}})
* [FS Bucket]({{< ref "/deploy/addon/fs-bucket" >}})
* [Cellar]({{< ref "/deploy/addon/cellar" >}})
* [Redis]({{< ref "/deploy/addon/redis" >}})
* [Config Provider]({{< ref "/deploy/addon/config-provider" >}})

### Add-on Billing

There are two kinds of billing:

* Per-month billing: Add-ons with fixed resources (storage, CPU and RAM)
* Per-usage billing: Add-ons based on consumption, like [FS-Buckets]({{< ref "/deploy/addon/fs-bucket.md" >}}) and [Cellar]({{< ref "/deploy/addon/cellar.md" >}})

{{< alert "warning" "Warning on SHARED plans" >}}
  <p>
    Add-ons having a free plan are meant for testing purposes, not production usage. These add-ons usually rely on shared resources, resulting in variable, non-guaranteed performances and stability.<hr>
    Shared clusters may not be running the same version as dedicated instances.
  </p>
{{< /alert >}}

**Note:** Per usage billing will be taken on runtime credits each day, while per-month add-ons will create a new line in the monthly invoice.

### Create an add-on for an existing application

Here we will assume you want to create a new add-on and link it to your application.

In order to create it, go to the [Clever Cloud Console](https://console.clever-cloud.com/).
Go to the organization in which you wan to create the add-on, for example your [personal space](https://console.clever-cloud.com/users/me).

1. When you are in the organization, click on **Add an add-on**. This space let you create and configure the add-on according to your needs.

2. Choose which *type* of add-on you want to create. See above the list of available add-ons and their corresponding documentation pages for further information on how they work.

3. Select the plan you need for you add-on. You can find details about the pricing, the capacity of the add-on, ... on this page or in the corresponding documentation page.

4. You will be able to choose with which application you want to link you add-on.

Linking an add-on to an application will provide configuration to the application through [environment variables]({{< ref "/develop/env-variables.md" >}}).
The environment variables provided by the add-on are available for use in the linked application.

If you want to use your add-on alone, just don't link it to any application.

1. Choose the name of the add-on and the region where the add-on will be hosted.

2. Click on the **Create** button and the add-on will now be available in your organization, and corresponding
environment variables will be available for the applications linked to the add-on you just created.

### Link an existing add-on to your application

To link an already existing add-on with your application, just follow these steps:

1. Go in the organization of your application and click on the name of the application you want to link with your add-on.
2. Go in the **Service dependencies** section.
3. Select the add-on you want to link under the "Link addons" dropdown menu.
4. Click on the **Link** button of the add-on you want to link to your application.

### Managing your add-on

Once an add-on is created, at least two management tabs are available in the Clever Cloud console:

* the Information tab
* the Configuration tab

Other tabs may be available, depending on the add-on type.

#### Information screen

This screen sums-up the characteristics of the selected add-on.
Features and environment variables (if applicable) are shown.

{{< image "/images/managing-addons-info.png" "Example of the information tab of an add-on" >}}

#### Configuration screen

Add-ons can be managed from the Configuration tab.
This screen is managed directly by the provider of the add-on.

{{< image "/images/managing-addons-config.png" "Example of the configuration tab of an add-on" >}}

### Delete an add-on

To delete an add-on, go to the *Configuration* page of the add-on, and click on *Remove add-on*.
Warning: After deletion of the add-on, all associated data will be removed.
