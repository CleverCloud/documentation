---
type: docs
linkTitle: Quickstart
weight: 1
title: Quickstart
description: Deploy your first app on Clever Cloud in minutes. Learn how to create an account, push your code via Git or GitHub, and add databases or services to your application.
keywords:
- quickstart
- getting-started
- deploy
- account
- application
- git
- github
- clever-cloud
aliases:
- /deploy
- /doc/addons/add-an-addon
- /doc/clever-cloud-overview/add-application
- /doc/getting-started
- /doc/getting-started/quickstart
- /getting-started/authentication
- /getting-started/quickstart
- /quickstart
---
{{< hextra/hero-subtitle >}}
  Clever Cloud is an automated hosting platform that lets you deploy apps and launch dependencies without worrying about infrastructure setup. This guide shows you how to deploy your first app while learning the basics of Clever Cloud.
{{< /hextra/hero-subtitle >}}

## Clever Cloud applications

Every Clever Cloud application must have:

* A language or framework
* A deployment method (Git, GitHub, or FTP)
* Resource allocation (CPU, RAM, disk)
* A configuration file (optional)

Except for the optional configuration file, Clever Cloud can't deploy an application if any required element is missing.

> [!NOTE]
> Clever Cloud runtimes use immutable infrastructure and always start fresh with each deployment. This means local file storage is not persistent. For data that needs to persist between deployments, use [FS Bucket (file storage)](/doc/addons/fs-bucket/), [Cellar (object storage)](/doc/addons/cellar), or a [database service](/doc/addons/).

## Supported runtimes

{{< cards >}}
  {{< card link="/developers/doc/applications/dotnet" title=".NET" icon="dotnet" >}}
  {{< card link="/developers/doc/applications/docker" title="Docker" icon="docker" >}}
  {{< card link="/developers/doc/applications/elixir" title="Elixir" icon="elixir" >}}
  {{< card link="/developers/doc/applications/frankenphp" title="FrankenPHP" icon="frankenphp" >}}
  {{< card link="/developers/doc/applications/golang" title="Go" icon="go" >}}
  {{< card link="/developers/doc/applications/haskell" title="Haskell" icon="haskell">}}
  {{< card link="/developers/doc/applications/java" title="Java" icon="java" >}}
  {{< card link="/developers/doc/applications/linux" title="Linux" icon="linux" >}}
  {{< card link="/developers/doc/applications/meteor" title="Meteor.js" icon="meteor" >}}
  {{< card link="/developers/doc/applications/nodejs" title="Node.js & Bun" icon="node" >}}
  {{< card link="/developers/doc/applications/php" title="PHP with Apache" icon="php" >}}
  {{< card link="/developers/doc/applications/python" title="Python with uv support" icon="python" >}}
  {{< card link="/developers/doc/applications/ruby" title="Ruby" icon="ruby" >}}
  {{< card link="/developers/doc/applications/rust" title="Rust" icon="rust" >}}
  {{< card link="/developers/doc/applications/scala" title="Scala" icon="scala" >}}
  {{< card link="/developers/doc/applications/static" title="Static sites" icon="static" >}}
  {{< card link="/developers/doc/applications/static-apache" title="Static sites with Apache" icon="feather" >}}
  {{< card link="/developers/doc/applications/v" title="V (Vlang)" icon="v" >}}
{{< /cards >}}

## How Clever Cloud works

When you push your code via Git or FTP, Clever Cloud checks that all required elements are present and deploys automatically if they are. Once deployment completes, your application is live.

View application logs in the **Logs** tab of the Clever Cloud Console.

## Create a Clever Cloud account

You can sign up for Clever Cloud using your **email** or your **GitHub account**.

Navigate to the [Clever Cloud Console](https://console.clever-cloud.com/), click **Create an account** at the bottom of the page, and select the sign-up method you prefer.

{{< tabs items="Email auth, GitHub auth" >}}

  {{< tab >}}
  You need a valid email address (not a temporary or disposable one) to sign up using email.

* Create a password with at least 6 characters.
* Validate your email address by clicking on the link in the confirmation email from Clever Cloud.
  {{< /tab >}}

  {{< tab >}}
  Use the GitHub sign up to create a Clever Cloud account or link an existing account to GitHub in one click.
  Signing up with GitHub requires permission to read your:

* Public key
* User repositories

  Repository permission lets you deploy GitHub apps to Clever Cloud in one step.
  
  Give the Clever Cloud API access to a specific GitHub organisation in your [GitHub account **Developer Settings**](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).
{{< /tab >}}

{{< /tabs >}}

### Enable two-factor authentication

Enable two-factor authentication (2FA) in your [**Authentication** settings](https://console.clever-cloud.com/users/me/authentication).

> [!NOTE]
> Save your recovery codes when Clever Cloud displays them. Without them, you won't be able to recover your account if you lose access to your 2FA device.

## Deploy your code

To deploy on Clever Cloud, you'll create an application in the console, then push your code via Git, GitHub, or FTP.

### Set up a Clever Cloud application

{{< youtube 9ww_t0o-GmA >}}

In the [Clever Cloud Console](https://console.clever-cloud.com/):

{{% steps %}}

#### Select the organization

From the left menu, choose the organization to deploy in. If you only have a **Personal space**, click **Add an organization** to create one.

#### Create an application

In the **Organization manager** panel at the top of the left menu, click **+ Create** and select **Application** to start the creation wizard.

If your account is linked to GitHub, you can select a repository in the wizard.

To deploy an application from a GitHub organization, first [grant the Clever Cloud API access to it](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

#### Select the application type

Choose your language or framework.

 {{< callout emoji="💡" >}}
  **Note:** PHP applications can use FTP or Git deployment.
  {{< /callout >}}

#### Configure scaling

**Horizontal scaling** is the number of instances that can run at the same time. **Vertical scaling** sets the minimum and maximum size the instance can be.

[Learn more about scaling and instance size](/doc/administrate/scalability).

#### Give the application a name

Enter a name and description for the application.

#### Optional steps

The wizard will prompt you to configure [add-ons](/doc/addons) and [environment variables](/doc/develop/env-variables), if needed.

{{% /steps %}}

### Choose a deployment method

Follow the steps for your preferred deployment method in the tabs below.

Monitor deployment progress in the **Logs** tab of the Clever Cloud Console.

{{< tabs items="Git, GitHub, FTP" >}}
  {{< tab >}}
  You'll need Git installed on your machine to deploy with it. Learn more at [git-scm.com](https://git-scm.com).

  To deploy with Git:

* Navigate to the application information page in the Clever Cloud Console and copy the Git deployment URL. It will look something like `git+ssh://git@push.<zone>.clever-cloud.com/<your_app_id>.git`.
* Open your terminal and go to your application directory. Initialize Git if you haven't already:

  ```bash
  git init
  git add .
  git commit -m "first commit"
  ```
* Link your local repository to Clever Cloud by providing the Git remote URL:

  ```bash
  git remote add <remote-name> <your-git-deployment-url>
  ```
* Push your application to Clever Cloud:

  ```bash
  git push <remote-name> <branch-name>:master
  ```

  **Note:** The `.git` folder is automatically deleted during deployment for security. To track which version is deployed, use the `COMMIT_ID` [environment variable](/doc/reference/reference-environment-variables/).
  {{< /tab >}}

  {{< tab >}}
  Once you have created an application with GitHub, each push to the `master` branch triggers a deployment. If your repository uses `main` or another branch, go to the application's information panel and select the default branch to use.

  ![Selecting the GitHub deployment branch](/images/github-deployment-branch.png "Selecting the GitHub deployment branch")

  If the repository doesn't appear in the list fetched from GitHub, you might need to relink your GitHub account to Clever Cloud. In GitHub, navigate to [Authorized OAuth Apps](https://github.com/settings/applications) (**Settings** > **Applications**) and revoke access for **Clever Cloud API**. Return to your [Clever Cloud profile](https://console.clever-cloud.com/users/me/information) and click **Link your GitHub account** in the **Information** tab.

  **Note:** You can use private GitHub repositories with Clever Cloud. However, personal GitHub accounts grant collaborators full access to private repositories. For granular permissions (like read-only access), use a GitHub organization.
  {{< /tab >}}

  {{< tab >}}
  Only PHP applications can be deployed with FTP.

  Ensure you have FTP software like [FileZilla](https://filezilla-project.org/) installed on your machine. For more information, see the [FileZilla Client Tutorial](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29).

  To deploy your application via FTP, create an [FS Bucket](/doc/addons/fs-bucket) with the same ID as your application ID. Find the FTP credentials in the FS Bucket **Configuration** tab.

  PHP applications with FTP deployment start automatically when created, even without any code.

  {{< callout type="warning" >}}
  FTP deployment is suitable for small websites. For large PHP websites, we strongly recommend using Git deployment.
  {{< /callout >}}
  {{< /tab >}}
{{< /tabs >}}

### Troubleshooting

{{% details title="Git ⋅ Prompted for a password when pushing" closed="true" %}}
If Git asks for a password when you push, check your SSH key configuration.

Add your SSH key to Clever Cloud in the [**SSH Keys** tab](https://console.clever-cloud.com/users/me/ssh-keys) of your profile. See the [SSH keys documentation](/doc/account/ssh-keys-management/) for more information.
{{% /details %}}

{{% details title= "Git ⋅ Unable to resolve the reference master" closed="true" %}}
This error means that Git can't find the branch reference you're trying to push.

* You can only push to the `master` branch for deployment. Pushing to another branch will trigger an error.
* You cannot push tags to trigger deployments. Only branch pushes will deploy your code.

To push to `master` from a different local branch, use this syntax:

```bash
git push <remote-name> <branch-name>:master
```
{{% /details %}}

{{% details title= "GitHub ⋅ fatal: does not appear to be a git repository" closed="true" %}}
If you try to push directly to an application created from a GitHub repository, you'll get this error:

```bash
fatal: '/data/repositories/<app_id>.git' does not
appear to be a git repository
```

Applications created from GitHub repositories are cloned directly from GitHub (no Git repository is created on Clever Cloud) and deploy automatically.

If you need to deploy by pushing directly to Clever Cloud (for example, from a CI/CD pipeline), create a non-GitHub application instead.
{{% /details %}}

## Manage Clever Cloud applications

The Clever Cloud application menu includes the following tabs:

* **Information:** General information about the application
* **Scalability:** Set up scalability options
* **Domain names:** Manage custom domain names
* **Environment variables:** Manage environment variables
* **Service dependencies:** Link add-ons and applications
* **Exposed configuration:** Manage exposed environment variables
* **Activity:** Track previous deployments
* **Logs:** View application logs
* **Metrics:** View application metrics
* **Consumption:** View application resource consumption

## Add-ons for Clever Cloud applications

Applications often need databases, storage, or other services in addition to the runtime. Clever Cloud add-ons provide these services.

An add-on can be used independently, linked to an application, or shared between applications. For example, a database can be used standalone without linking it to an application, or it can be linked to multiple applications that share the data.

Clever Cloud hosts and manages most add-ons in the catalog. External vendors can also integrate their services with the platform ([learn how](/api)).

Available add-ons:

### Databases

{{< cards >}}
  {{< card link="/developers/doc/addons/materia-kv" title="Materia KV" subtitle="Serverless distributed key-value database" icon="materia" tag="Alpha" >}}
  {{< card link="/developers/doc/addons/mongodb" title="MongoDB" subtitle="A NoSQL document-oriented database" icon= "mongo">}}
  {{< card link="/developers/doc/addons/mysql" title="MySQL" icon="mysql" subtitle="A managed relational database" >}}
  {{< card link="/developers/doc/addons/postgresql" title="PostgreSQL" icon="pg" subtitle="A not-only-SQL managed database" >}}
  {{< card link="/developers/doc/addons/elastic" title="Elastic Stack" subtitle="Deploy your Elastic Stack in one click" icon="elastic" >}}

  {{< card link="/developers/doc/addons/redis" title="Redis" subtitle="Managed key-value database" icon="redis" >}}
{{< /cards >}}

### Storage and messaging

{{< cards >}}
  {{< card link="/developers/doc/addons/cellar" title="Cellar" subtitle="Object storage, compatible with S3 API" icon="cellar" >}}
  {{< card link="/developers/doc/addons/fs-bucket" title="FS Bucket" subtitle="Persistent external file system" icon="fsbucket" >}}
  {{< card link="/developers/doc/addons/pulsar" title="Pulsar" subtitle="Open-source, cloud-native messaging and streaming platform" icon="pulsar" tag="Beta" >}}
{{< /cards >}}

### Services and tools

{{< cards >}}
  {{< card link="/developers/doc/addons/config-provider" title="Config Provider" subtitle="Manage, import, and inject configurations and credentials" icon="creds" >}}
  {{< card link="/developers/doc/addons/heptapod" title="Heptapod" subtitle="The friendly fork of GitLab Community Edition that adds support for Mercurial" icon="git" >}}
  {{< card link="/developers/doc/addons/jenkins" title="Jenkins" subtitle="The leading open-source automation server" icon="jenkins" >}}
  {{< card link="/developers/doc/addons/keycloak" title="Keycloak" subtitle="Identity and access management with single sign-on" icon="keycloak" >}}
  {{< card link="/developers/doc/addons/mailpace" title="MailPace" subtitle="Fast, reliable transactional email" icon="mail" >}}
  {{< card link="/developers/doc/addons/matomo" title="Matomo" subtitle="Open-source web analytics alternative to Google Analytics" icon="matomo" >}}
  {{< card link="/developers/doc/addons/metabase" title="Metabase" subtitle="An easy business intelligence tool to query and visualize data" icon="metabase" >}}
  {{< card link="/developers/doc/addons/otoroshi" title="Otoroshi with LLM" subtitle="Simple API management based on a modern reverse proxy with preconfigured plugins" icon="endpoints" >}}
{{< /cards >}}

### Create your first add-on

When you link an add-on to an application (either during creation or afterward), the add-on provides configuration through [environment variables](/doc/reference/reference-environment-variables/). These variables are automatically available in your application.

Select a tab below depending on whether you're creating a new add-on or linking an existing one.

{{< tabs items="Create new add-on, Link existing add-on" >}}
  {{< tab >}}
  * In the [Clever Cloud Console](https://console.clever-cloud.com/), navigate to the organization where you want to create the add-on (for example, your [personal space](https://console.clever-cloud.com/users/me)).
  * Click **Add an add-on**.
  * Select the type of add-on to create.
  * Select the pricing plan for the add-on. See the [add-on billing](#add-on-billing) section below or the [Clever Cloud pricing page](https://www.clever-cloud.com/pricing/) for more information.
  * Select the application to link the add-on to. To use the add-on alone, don't link it to an application.
  * Give the add-on a name and select a hosting region.
  * Click **Create**.
  {{< /tab >}}

  {{< tab >}}
  * In the [Clever Cloud Console](https://console.clever-cloud.com/), navigate to the organization, then select the application.
  * Go to **Service dependencies**.
  * Click **Link add-ons** and select the add-on from the dropdown menu.
  * Click **Link**.
  {{< /tab >}}
{{< /tabs >}}

### Add-on billing

Add-ons with fixed resources (storage, CPU, RAM) are billed monthly, and add-ons that scale with consumption (like [FS Bucket](/doc/addons/fs-bucket) and [Cellar](/doc/addons/cellar)) are billed based on usage.

{{< callout emoji="📊" >}}
**How you're invoiced:** Per-usage billing is deducted from daily runtime credits. Per-month billing appears as a line item on your monthly invoice.
{{< /callout >}}

{{< callout type="warning" >}}
**Free plans:** Some add-ons offer free plans for testing purposes. Free plans run on shared resources with variable, non-guaranteed performance, and may run different versions than dedicated instances. Free plans are not suitable for production use.
{{< /callout >}}

### Manage add-ons

Each add-on has a management interface and sidebar menu. The sidebar menu always includes:

* **Add-on dashboard:** Connection credentials and configuration tools

!["Add-on dashboard"](/images/addon-dashboard.png "Example of an add-on dashboard")

* **Information:** Overview of add-on details, plan, and environment variables

Other menu items may be available, depending on the add-on type.

### Delete add-ons

To delete an add-on, go to the add-on's **Information** view and click **Remove add-on**.

{{< callout type="warning" >}}
Deleting an add-on permanently removes all associated data.
{{< /callout >}}
