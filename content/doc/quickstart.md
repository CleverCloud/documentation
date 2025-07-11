---
weight: 1
title: Quickstart
description: Follow this guide to get ready to deploy quickly as you learn the basics of Clever Cloud.
tags:
- getting-started
keywords:
- quickstart
aliases:
- /deploy
- /developers/doc/getting-started/quickstart
- /doc/getting-started/quickstart
- /getting-started/quickstart
type: "docs"
---
{{< hextra/hero-subtitle >}}
  Clever Cloud provides an automated hosting platform for developers. Deploy your app easily and launch dependencies without having to worry about the infrastructure set up. Follow this guide to get ready to deploy quickly as you learn the basics of Clever Cloud.
{{< /hextra/hero-subtitle >}}

## Create a Clever Cloud Account

The API of Clever Cloud uses OAuth 1 to perform authentication actions.
There are two ways to sign up for Clever Cloud: **email** or **GitHub login**.

{{< tabs items="Email Auth, GitHub Auth" >}}

  {{< tab >}}
  This kind of auth requires a valid and non-temporary disposable email, and a password having at least 6 characters.
  Do not forget to validate your email by clicking the link you will receive.
  {{< /tab >}}

  {{< tab >}}

  The GitHub sign up allows you to create an account or link your existing one to GitHub, in one click.
  This process asks the following permissions:

* Read your Public Key
* Read User Repositories

  The "repository permission" is used to deploy your GitHub apps directly to Clever Cloud, with a simple step.
  If you need to give access to Clever Cloud's API to a specific GitHub organisation, you can [do it here](https://GitHub.com/settings/connections/applications/d96bd8fd996d2ca783cc).
{{< /tab >}}

{{< /tabs >}}

Go to the [Clever Cloud Console](https://console.clever-cloud.com/) and select the method you prefer.

### Two Factor Authentication (2FA)

Clever Cloud supports 2FA. You can enable it here: <https://console.clever-cloud.com/users/me/authentication>

Please, backup your recovery codes, we won't be able to restore access to your account if you lose access to your regular codes.

## Deploy your code

### What's an Application on Clever Cloud

An application is defined on Clever Cloud by the following elements:

* a dedicated language/framework;
* a deployment method (FTP and/or Git);
* resources consumption (CPU, RAM, Disk…), depending on the language or framework used;
* an optional configuration file you may add to your project.

If one of these elements is missing, Clever Cloud can't deploy your application properly (except the configuration file, optional in some cases).

### How it Works

When you push an application's code to git or via FTP, the platform receives it and checks the resource's requirements. If they are complete, the deployment is launched. When finished and successful, the application is up and running.

The log system retrieves all output from the application and displays it in the logs tab of your application in the Clever Cloud console.

### Supported Platforms

{{< cards >}}
  {{< card link="/developers/doc/applications/dotnet" title=".Net" icon="dotnet" >}}
  {{< card link="/developers/doc/applications/docker" title="Docker" icon="docker" >}}
  {{< card link="/developers/doc/applications/elixir" title="Elixir" icon="elixir" >}}
  {{< card link="/developers/doc/applications/frankenphp" title="Franken PHP" icon="frankenphp" >}}
  {{< card link="/developers/doc/applications/golang" title="Go" icon="go" >}}
  {{< card link="/developers/doc/applications/haskell" title="Haskell" icon="haskell">}}
  {{< card link="/developers/doc/applications/java" title="Java (Gradle, Jar, Maven, War/Ear)" icon="java" >}}
  {{< card link="/developers/doc/applications/linux" title="Linux" icon="linux" >}}
  {{< card link="/developers/doc/applications/meteor" title="Meteor.js" icon="meteor" >}}
  {{< card link="/developers/doc/applications/nodejs" title="Node.js & Bun" icon="node" >}}
  {{< card link="/developers/doc/applications/php" title="PHP with Apache" icon="php" >}}
  {{< card link="/developers/doc/applications/python" title="Python with uv support" icon="python" >}}
  {{< card link="/developers/doc/applications/ruby" title="Ruby" icon="ruby" >}}
  {{< card link="/developers/doc/applications/rust" title="Rust" icon="rust" >}}
  {{< card link="/developers/doc/applications/scala" title="Scala" icon="scala" >}}
  {{< card link="/developers/doc/applications/static" title="Static" icon="static" >}}
  {{< card link="/developers/doc/applications/static-apache" title="Static with Apache" icon="feather" >}}
  {{< card link="/developers/doc/applications/v" title="V (Vlang)" icon="v" >}}
{{< /cards >}}

### Create an Application Step by Step

{{< youtube 9ww_t0o-GmA >}}

In the [Clever Cloud Console](https://console.clever-cloud.com/):

{{% steps %}}

#### Select the organisation

Choose the organisation you want to deploy in from the left menu. At this point you must only have the Personal Space but you can create one.

#### Click on "Create an application"

Find it in the **organisation Manager** panel, at the top left of the left menu.

This starts the application creation wizard. If your account has been linked to GitHub, you can select a repository from your GitHub account.
If you want to deploy an application within a GitHub organisation, first [grant the Clever Cloud API access to it](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

#### Select the language

Choose the language or the framework you want to deploy.

 {{< callout emoji="💡" >}}
  **Optional:** for PHP applications, you can choose between FTP and Git deployment.
  {{< /callout >}}

#### Fine-tune your scaling configuration

Horizontal scaling is the number of instances that can run at the same time. Vertical scaling sets the minimum and maximum size the instance can be.

- [Learn more about scaling & instances size](/developers/doc/administrate/scalability)

#### Name your application

Enter the name and the description of your application.

#### Optional steps

* The wizard will offer you to [add an add-on]({{< ref "doc/addons" >}}) to your application
* The wizard will offer you to [add environment variables]({{< ref "doc/develop/env-variables.md" >}}) to your application

{{% /steps %}}

#### Choose How to Deploy

{{< tabs items="Git,GitHub, FTP" >}}
  {{< tab >}}
  *To deploy via Git, you need it installed on your machine. You can find more information on Git website: [git-scm.com](https://git-scm.com)*

  *Note:* during the deployment, the .git folder is automatically deleted to avoid security problems. If you need to know which version is used on the server please use the `COMMIT_ID` [environment variable](/developers/doc/reference/reference-environment-variables/).

  Follow these steps to deploy your application:

1. Get the git deployment URL in the application information page, which looks like: `git+ssh://git@push.<zone>.clever-cloud.com/<your_app_id>.git`.

2. In your terminal, go to your application repository. If you do not already track your app with git, start by typing:

  ```bash
  git init
  git add .
  git commit -m "first commit"
```

3. Then, link your local repository to Clever Cloud by providing the Git remote URL:

```bash
git remote add <remote-name> <your-git-deployment-url>
```

4. Push your application to Clever Cloud:

```bash
git push <remote-name> <branch-name>:master
```

  You can see your application **logs** in the dashboard to **monitor the deployment**.

  {{< /tab >}}

  {{< tab >}}
  Once you have created your application with GitHub, each push on the `master` branch trigger a deployment. To deploy an other branch than `master`, go to the `information` panel of your application and select the default branch to use.

  {{< image "/developers/images/doc/github-deployment-branch.png" "Github deployment branch select" >}}

  If you don't find your repository in the list fetched from GitHub, a workaround is to unlink your account in your profile here : <https://console.clever-cloud.com/users/me/information>, remove **Clever Cloud API** from your GitHub [Authorized OAuth Apps](https://github.com/settings/applications) and link again your GitHub account to your Clever Cloud account.

  **Private GitHub repositories are also supported.**

  Caution: in GitHub, private repositories in an ordinary user account are an all-or-nothing deal: that is, either someone has full read write access (because they're a collaborator) or they have no access.

  However, if you set up an organisation, create the repository under the aegis of the organisation, and then add the collaborator, you have much more fine-grained control (including giving read-only access to a private repository).
  {{< /tab >}}

  {{< tab >}}
  You can deploy via FTP with PHP applications.

  To deploy via FTP, you need an FTP software installed on your machine. [Filezilla](https://filezilla-project.org/) is one of them.

  Deploy your application via FTP, create a [FS Bucket]({{< ref "doc/addons/fs-bucket" >}}) with an ID matching your application's ID. You will find the FTP credentials in the configuration tab of this particular FS Bucket.

  [More documentation about Filezilla](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29).

  {{< icon "exclamation-circle" >}} An FTP application is automatically started once the application is created, even if no code has been sent.

  {{< callout type="warning" >}}
  FTP deployment is ok for small websites but not for large ones. We strongly recommend you to use **Git** deployment for **large PHP websites**.
  {{< /callout >}}
  {{< /tab >}}
{{< /tabs >}}

### Troubleshooting

{{% details title="Git ⋅ Remote is asking for a password" closed="true" %}}

If the remote asks you for a password right after a git push attempt, this may be due to a SSH Key configuration error.

**Add your SSH key to your profile here:**
<https://console.clever-cloud.com/users/me/ssh-keys>

The full tutorial about adding SSH key is here: [adding SSH keys](/developers/doc/account/ssh-keys-management/)

{{% /details %}}
{{% details title= "Git ⋅ Unable to resolve the reference master" closed="true" %}}
You are probably trying to push from another branch. Keep in mind that:

* You can only push to the **master** branch for deployment. Trying to push to another branch will trigger an error.
* You cannot push a tag (which refers to a commit) to the remote repository. If you do so, **no deployment** will be triggered.
* In order to push to **master** from a non-master local branch, use this syntax:

```bash
git push <remote-name> <branch-name>:master
```

{{% /details %}}

{{% details title= "GitHub ⋅ Does not appear to be a git repository" closed="true" %}}
You can't directly push to an application created on Clever Cloud as a GitHub app: in this case, only the automatic deployment from GitHub is henceforth allowed.

If you try to push to Clever Cloud, as you would do for a non-GitHub app, you will get the following error :

```bash
fatal: '/data/repositories/<app_id>.git' does not
appear to be a git repository
```

Indeed, no git repository is created on Clever Cloud because the application is directly cloned from GitHub.

If you have to push directly to a repository to deploy an application (eg if you deploy from a CI), then create a non-GitHub app.

{{% /details %}}

## Manage your Application

There are many tabs available in the application's menu on Clever Console:

* **Information:** General information about your application
* **Scalability:** Set-up scalability options
* **Domain names:** Manage custom domain names
* **Environment variables:** Manage environment variables
* **Service dependencies:** Link add-ons and applications
* **Exposed configuration:** Manage exposed environment variables
* **Activity:** Track last deployments
* **Logs:** Visualize application's logs
* **Metrics:** Visualize application's metrics
* **Consumption:** Visualize your application's consumption.

### Create your first add-on

Applications often requires one or more services in addition to the runtime itself. Add-ons are services you can use independently, or you can link them with your application(s). For instance, you may want to add a database or a caching system to your application or just have a database with no linked application.

An add-on can be shared by different applications to share data between them. It can be a database shared by two or three applications of your infrastructure for example, or they can be independent.

Most of the add-ons catalog is provided by Clever Cloud, but vendors are also allowed to provide services external to Clever Cloud ([See how to integrate your SaaS with Clever Cloud](/developers/api))

#### Available add-ons

Clever Cloud provides multiple add-ons to work with your applications:

{{< cards >}}
  {{< card link="../addons/mysql" title="MySQL" icon="mysql" subtitle="Your self-hosted managed relational database" >}}
  {{< card link="../addons/postgresql" title="PostgreSQL" icon="pg" subtitle="The not-only-SQL database, self hosted and managed" >}}
  {{< card link="../addons/mongodb" title="MongoDB" subtitle="The NoSQL document-oriented database" icon= "mongo">}}
  {{< card link="../addons/elastic" title="Elastic Stack" subtitle="Deploy your Elastic Stack in one click" icon="elastic" >}}
  {{< card link="../addons/fs-bucket" title="FS Bucket" subtitle="External File System for your apps" icon="fsbucket" >}}
  {{< card link="../addons/cellar" title="Cellar" subtitle="Object storage" icon="cellar" >}}
  {{< card link="../addons/redis" title="Redis" subtitle="Managed in-memory database" icon="redis" >}}
  {{< card link="../addons/config-provider" title="Config Provider" subtitle="More freedom to manage, import and inject your credentials" icon="creds" >}}
  {{< card link="../addons/pulsar" title="Pulsar" subtitle="Open-source, distributed messaging and streaming platform built for the cloud." icon="pulsar" >}}
   {{< card link="../addons/jenkins" title="Jenkins" subtitle="The leading open source automation server" icon="jenkins" >}}
   {{< card link="../addons/matomo" title="Matomo" subtitle="Best Google Analytics alternative" icon="matomo" >}}
{{< /cards >}}

**If your add-on:**

{{< tabs items="Doesn't exist yet,Already exists" >}}
  {{< tab >}}
  Here we will assume you want to create a new add-on and link it to your application.

  1. Go to the [Clever Cloud Console](https://console.clever-cloud.com/).
  2. Go to the organisation in which you want to create the add-on, for example your [personal space](https://console.clever-cloud.com/users/me).
  3. Click on **Add an add-on**. This space let you create and configure the add-on according to your needs.
  4. Choose which *type* of add-on you want to create. See preceding the list of available add-ons and their corresponding documentation pages for further information on how they work.
  5. Select the plan you need for you add-on. You can find details about the pricing, the capacity of the add-on and other specifications on this page or in the corresponding documentation page.
  6. Choose with which application you want to link you add-on. Linking an add-on to an application will provide configuration to the application through [environment variables](/developers/doc/reference/reference-environment-variables/). The environment variables provided by the add-on are available for use in the linked application. If you want to use your add-on alone, just don't link it to any application.
  7. Choose the name of the add-on and the region where the add-on will be hosted.
  8. Click on the **Create** button.

  The add-on will now be available in your organisation, and corresponding environment variables will be available for the applications linked to the add-on you just created.
  {{< /tab >}}

  {{< tab >}}
  To link an already existing add-on with your application, just follow these steps:

  1. Go in the organisation of your application.
  2. Click on the name of the application you want to link with your add-on.
  3. Go in the **Service dependencies** section.
  4. Select the add-on you want to link under the "Link add-ons" dropdown menu.
  5. Click on the **Link** button of the add-on you want to link to your application.
  {{< /tab >}}
{{< /tabs >}}

##### Add-on Billing

There are two kinds of billing:

* Per-month billing: Add-ons with fixed resources (storage, CPU and RAM)
* Per-usage billing: Add-ons based on consumption, like [FS Bucket]({{< ref "doc/addons/fs-bucket" >}}) and [Cellar]({{< ref "doc/addons/cellar.md" >}})

{{< callout type="warning" >}}
**Free Plan:** add-ons having a free plan are meant for testing purposes, not production usage. These add-ons usually rely on shared resources, resulting in variable, non-guaranteed performances and stability. Shared clusters may not be running the same version as dedicated instances.
{{< /callout >}}

{{< callout emoji="📊" >}}
**Your invoice:** per usage billing will be taken on runtime credits each day, while per-month add-ons will create a new line in the monthly invoice.
{{< /callout >}}

### Manage your Add-on

Once an add-on is created, at least two tabs are available in the Clever Cloud console:

* **Add-on dashboard:** This screen provides and overview of your add-on and its options, depending on the type of add-on it is.

{{< image "/developers/images/addon-dashboard.png" "Example of the dashoard tab of an add-on" >}}

* **Information tab:** This screen sums-up the characteristics of the selected add-on.
The system shows features and environment variables (if applicable).

Other tabs may be available, depending on the add-on type.

### Delete an add-on

To delete an add-on:

1. Go to the **Information** tab of the add-on.
2. Click on *Remove add-on*.

{{< callout type="warning" >}}
The system removes all associated data after you delete the add-on.
{{< /callout >}}
