---
weight: 1
title: Quickstart
shortdesc: quickstart guide on Clever Cloud
tags:
- getting-started
keywords:
- quickstart
type: "docs"
comments: false

---


## Create a Clever Cloud Account

{{% details title="🔑 Choose Your Authentication Method" closed="true" %}}

{{< readfile file="/content/partials/authentication.md" >}}

{{% /details %}}

## Deploy your code

{{% details title="🎓 What's an Application on Clever Cloud" closed="true" %}}


An application is defined on Clever Cloud by the following elements:

* a dedicated language/framework;
* a deployment method (FTP and/or Git);
* resources consumption (CPU, RAM, Disk…), depending on the language or framework used;
* an optional configuration file you may add to your project.

If one of these elements is missing, Clever Cloud can't deploy your application properly (except the configuration file, optional in some cases).

{{% /details %}}

### Supported platforms:

{{< cards >}}
  {{< card link="../deploy/application/docker/docker" title="Docker" icon="docker" >}}
  {{< card link="../deploy/application/golang/go" title="Go" icon="go" >}}
  {{< card link="../deploy/application/haskell/haskell" title="Haskell" icon= "haskell">}}
  {{< card link="../deploy/application/java/" title="Java" icon="java" >}}
  {{< card link="../deploy/application/javascript/by-framework/nodejs" title="Node.js" icon="node" >}}
  {{< card link="../deploy/application/ruby/ruby-rack" title="Ruby" icon="ruby" >}}
  {{< card link="../deploy/application/php/php-apps" title="PHP" icon="php" >}}
  {{< card link="../deploy/application/python/python_apps" title="Python" icon="python" >}}
  {{< card link="../deploy/application/rust/rust" title="Rust" icon="rust" >}}
  {{< card link="../deploy/application/scala/scala" title="Scala" icon="scala" >}}
  {{< card link="../deploy/application/elixir/elixir" title="Elixir" icon="elixir" >}}
  {{< card link="../deploy/application/dotnet/dotnet.md" title=".NET" icon="dotnet" >}}
  
{{< /cards >}}

{{% details title="📍 How it works" closed="true" %}}

When you push an application's code to git or via FTP, the platform receives it and checks the resource’s requirements. If they are complete, the deployment is launched. When finished and successful, the application is up and running.

The log system retrieves all output from the application and displays it in the logs tab of your application in the Clever Cloud console.

{{% /details %}}

## Create an application step by step

In the [Clever Cloud Console](https://console.clever-cloud.com/):

{{% steps %}}

### Select the proper organization you want to add the application to

At this point you must only have the Personal Space but you can create one.

### Click on the "Create an application" button

Find it in the **Organization Manager** panel.

This starts the application creation wizard. If your account has been linked to GitHub, you can select a repository from your GitHub account.

If you want to deploy an application within a GitHub organisation, first [grant the Clever Cloud API access to it](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

### Select the language or the framework you need

**💡 Optional:** For PHP applications, you can choose between FTP and Git deployment.

### Fine-tune your scaling configuration

Horizontal scaling is the number of instances that can run at the same time. Vertical scaling sets the minimum and maximum size the instance can be.

### Enter the name and description of your application.

### Optional steps

- The wizard will offer you to [add an add-on]({{< ref "doc/deploy/addon" >}}) to your application

- The wizard will offer you to [add environment variables]({{< ref "doc/develop/env-variables.md" >}}) to your application


{{% /steps %}}

## Choose how to deploy

{{% details title="🌱 Deploy with Git Step by Step" closed="true" %}}

*To deploy via Git, you need it installed on your machine. You can find more information on Git website: [git-scm.com](https://git-scm.com)*

*Note:* During the deployment, the .git folder is automatically deleted to avoid security problems. If you need to know which version is used on the server please use the `COMMIT_ID` [environment variable]({{< ref "doc/develop/env-variables.md" >}}).

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
{{% /details %}}

{{< callout type="warning" >}}

You can only push to the **master** branch for deployment.

Trying to push to another branch will trigger an error.

You cannot push a tag (which refers to a commit) to the remote repository. If you do so, **no deployment** will be triggered.

In order to push to **master** from a non-master local branch, use this syntax:

```bash
git push <remote-name> <branch-name>:master
```

{{< /callout >}}

You can see your application **logs** in the dashboard to **monitor the deployment**.

{{< callout type="error" >}}

If the remote asks you for a password right after a git push attempt, this may be due to a SSH Key misconfiguration.

**Add your SSH key to your profile here:**

   https://console.clever-cloud.com/users/me/ssh-keys">https://console.clever-cloud.com/users/me/ssh-keys
   
   The full tutorial about adding SSH key is here: [Adding SSH keys](/account/ssh-keys-managment)

{{< /callout >}}

{{% details title= " Deploy automatically from GitHub" closed="true" icon="github" %}}

Once you have created your application with GitHub, each push on the `master` branch trigger a deployment. To deploy an other branch than `master`, go to the `information` panel of your application and select the default branch to use.

{{< image "/images/github-deployment-branch.png" "Github deployment branch select" >}}


If you don't find your repository in the list fetched from Github, a workaround is to unlink your account in your profile here : https://console.clever-cloud.com/users/me/information, remove **Clever Cloud API** from your Github [Authorized OAuth Apps](https://github.com/settings/applications) and link again your Github account to your Clever Cloud account.

**Private GitHub repositories are also supported.**

Caution: in GitHub, private repositories in an ordinary user account are an all-or-nothing deal: either someone has full read write access (i.e., they're a collaborator) or they have no access. 

However, if you set up an organization, create the repo under the aegis of the organization, and then add the collaborator, you have much more fine-grained control (including giving read-only access to a private repository).

{{% /details %}}

{{< callout type="warning" >}}

You can't directly push to an application created on Clever Cloud as a GitHub app: in this case, only the automatic deployment from GitHub is henceforth allowed.

If you try to push to Clever Cloud, as you would do for a non-GitHub app, you will get the following error :

```bash
fatal: '/data/repositories/<app_id>.git' does not
appear to be a git repository
```

Indeed, no git repository is created on Clever Cloud because the application is directly cloned from GitHub.

If you have to push directly to a repo in order to deploy an application (eg if you deploy from a CI), then create a non-GitHub app.

{{< /callout >}}

{{% details title="📂 FTP Deployment" closed="true" %}}

You can deploy via FTP with PHP applications.  

To deploy via FTP, you need an FTP software installed on your machine. [Filezilla](https://filezilla-project.org/) is one of them.

Deploy your application via FTP, create a [FS Bucket]({{< ref "doc/deploy/addon/fs-bucket.md" >}}) with an ID
matching your application's ID. You will find the FTP credentials in the configuration tab of this particular FS Bucket.

[More documentation about Filezilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29).

{{% /details %}}

{{< callout type="info" >}}

An FTP application is automatically started once the application is created, even if no code has been sent.

{{< /callout >}}

{{< callout type="warning" >}}
FTP deployment is ok for small websites but not for large ones. We strongly recommend you to use **Git** deployment for **large PHP websites**.

{{< /callout >}}

## Manage your stack

{{% details title="🌐 Manage your Application from the Dashboard" closed="true" %}}

There are many tabs available in the application's menu:

- **Information:** General information about your application
- **Scalability:** Set-up scalability options
- **Domain names:** Manage custom domain names
- **Environment variables:** Manage environment variables
- **Service dependencies:** Link add-ons and applications
- **Exposed configuration:** Manage exposed environment variables
- **Activity:** Track last deployments
- **Logs:** Visualize application's logs
- **Metrics:** Visualize application's metrics
- **Consumption:** Visualize your application's consumption.

{{% /details %}}

{{% details title="🔌 Create your first add-on" closed="true" %}}

Applications often requires one or more services in addition to the runtime itself. Add-ons are services you can use independently, or you can link them with your application(s). For instance, you may want to add a database or a caching system to your application or just have a database with no linked application.

An add-on can be shared by different applications to share data between them. It can be a database shared by two or three applications of your infrastructure for example, or they can be independent.

Most of the add-ons catalog is provided by Clever Cloud, but vendors are also allowed to provide services external to Clever Cloud ([See how to integrate your SaaS with Clever Cloud]({{< ref "doc/extend/cc-api.md" >}}))

{{% /details %}}

### Available add-ons

Clever Cloud provides multiple add-ons to work with your applications:

{{< cards >}}
  {{< card link="../deploy/addon/mysql/mysql" title="MySQL" icon="mysql" >}}
  {{< card link="../deploy/addon/postgresql" title="PostgreSQL" icon="pg" >}}
  {{< card link="../deploy/addon/mongodb" title="MongDB" subtitle="The NoSQL document-oriented database" icon= "mongo">}}
  {{< card link="../deploy/addon/fs-bucket" title="FS Bucket" subtitle="External File System for your apps" icon="fsbucket" >}}
  {{< card link="../deploy/addon/cellar" title="Cellar" subtitle="Object storage" icon="cellar" >}}
  {{< card link="../deploy/addon/redis" title="Redis" subtitle="In-memory database" icon="redis" >}}
  {{< card link="../deploy/addon/config-provider" title="Config Provider" subtitle="More freedom to manage, import and inject your credentials" icon="creds" >}}
  
{{< /cards >}}


{{% details title="💰 Add-on Billing" closed="true" %}}

There are two kinds of billing:

* Per-month billing: Add-ons with fixed resources (storage, CPU and RAM)
* Per-usage billing: Add-ons based on consumption, like [FS Bucket]({{< ref "doc/deploy/addon/fs-bucket.md" >}}) and [Cellar]({{< ref "doc/deploy/addon/cellar.md" >}})

{{% /details %}}

{{< callout type="warning" >}}

Add-ons having a free plan are meant for testing purposes, not production usage. These add-ons usually rely on shared resources, resulting in variable, non-guaranteed performances and stability.

Shared clusters may not be running the same version as dedicated instances.

{{< /callout >}}

{{< callout emoji="📊" >}}
**Note:** Per usage billing will be taken on runtime credits each day, while per-month add-ons will create a new line in the monthly invoice.
{{< /callout >}}

{{% details title=" 🪄 Create an add-on for an existing application" closed="true" %}}

Here we will assume you want to create a new add-on and link it to your application.

1. Go to the [Clever Cloud Console](https://console.clever-cloud.com/).
2. Go to the organization in which you want to create the add-on, for example your [personal space](https://console.clever-cloud.com/users/me).
3. Click on **Add an add-on**. This space let you create and configure the add-on according to your needs.
4. Choose which *type* of add-on you want to create. See above the list of available add-ons and their corresponding documentation pages for further information on how they work.
5. Select the plan you need for you add-on. You can find details about the pricing, the capacity of the add-on and other specifications on this page or in the corresponding documentation page.
6. Choose with which application you want to link you add-on. Linking an add-on to an application will provide configuration to the application through [environment variables]({{< ref "doc/develop/env-variables.md" >}}). The environment variables provided by the add-on are available for use in the linked application. If you want to use your add-on alone, just don't link it to any application.
7. Choose the name of the add-on and the region where the add-on will be hosted.
8. Click on the **Create** button.

The add-on will now be available in your organization, and corresponding environment variables will be available for the applications linked to the add-on you just created.

{{% /details %}}

{{% details title="🔗 Link an existing add-on to your application" closed="true" %}}

To link an already existing add-on with your application, just follow these steps:

1. Go in the organization of your application.
2. Click on the name of the application you want to link with your add-on.
3. Go in the **Service dependencies** section.
4. Select the add-on you want to link under the "Link addons" dropdown menu.
5. Click on the **Link** button of the add-on you want to link to your application.

{{% /details %}}

{{% details title="⚙️ Managing your add-on" closed="true" %}}

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

To delete an add-on:
1. Go to the *Configuration* page of the add-on.
2. Click on *Remove add-on*.

⚠️ Warning: After deletion of the add-on, all associated data will be removed.

{{% /details %}}