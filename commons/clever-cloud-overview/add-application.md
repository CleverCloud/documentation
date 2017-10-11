---
title: Deploying an application
position: 4
shortdesc: Step by step guide to deploy an application on Clever Cloud.
tags:
- dashboard-setup
---

# Deploying an application

There are two steps in this section: application creation (requiring actions from
dashboard) and application deployment (requiring actions from Git / or your FTP access).

## Create an application

 1. First, select the proper organization you want to add the application to. Then,
 click on the **Add an application** button in the **Organization Manager** panel.
 This starts the application creation wizard. If your account has been linked to
 GitHub, you can select a repository from your GitHub account. 
 
 If you want to deploy an application within a GitHub organisation, first [grant the Clever Cloud API access to it](https://github.com/settings/connections/applications/d96bd8fd996d2ca783cc).

 2. Then select the language or the framework you need

 3. *Optional:* For PHP applications, you can choose between FTP
 and Git deployment.

 4. In the next step, you will be prompted to select your scaling configuration.
 If you need help to configure your scaling options, please refer to
 [the dedicated section](/doc/clever-cloud-overview/scaling/).

 5. Enter the name and description of your application.

 6. *Optional*: The wizard will offer you to [add an
 add-on](/doc/addons/clever-cloud-addons/) to your application.

 7. *Optional*: The wizard will offer you to [add environment
 variables](/doc/admin-console/environment-variables/) to your application.

## Git Deployment

*To deploy via Git, you need it installed on your machine. You can find more
information on Git website: [git-scm.com](http://git-scm.com)*

*Note:* During the deployment, the .git folder is automatically deleted to avoid security problems. If you need to know
which version is used on the server please use the `COMMIT_ID` [environment variable](/doc/admin-console/environment-variables/).

Follow these steps to deploy your application:

 1. Get the git deployment url in the application information page, which looks like:
 ``git+ssh://git@push.<zone>.clever-cloud.com/<your_app_id>.git``.

 2. In your terminal, go to your application repository. If you do not already track your app with git, start by typing:

	```bash
	$ git init
	$ git add .
	$ git commit -m "first commit"
	```

 3. Then, link your local repository to Clever Cloud by providing the Git remote url:

	```bash
	$ git remote add <remote-name> <your-git-deployment-url>
	```

 4. Push your application to Clever Cloud:

	```bash
	$ git push <remote-name> <branch-name>:master
	```

 <div class="alert alert-hot-problems">
   <h4>Warning:</h4>
   <p>You can only push to the <strong>master</strong> branch for deployment.
   Trying to push to another branch will trigger an error.</p>
   <p>In order to push to <strong>master</strong> from a non-master local branch, use this syntax:</p>
   <pre>git push &lt;remote&gt; &lt;your branch&gt;:master</pre>
 </div>

 Checkout your application **logs** in the dashboard to **monitor the deployment**.

 <div class="alert alert-hot-problems">
   <h4>Troubleshooting:</h4>
   <p>If the remote asks you for a password right after a git push attempt, this may be due to a SSH Key misconfiguration.
   <br>Add your SSH key to your profile here:
   <a href="https://console.clever-cloud.com/users/me/ssh-keys">https://console.clever-cloud.com/users/me/ssh-keys</a></p>
   <p>The full tutorial about adding SSH key is here: <a href="/doc/admin-console/ssh-keys/">Adding SSH keys</a> </p>
 </div>

### Automatic Deployment with GitHub

Once you have created your application with Github, each push on the `master` branch will trigger
a deployment. If you want to deploy an other branch than `master`, you can go to the `information`
panel of your application and select the default branch to use.

 <div class="alert alert-hot-problems">
   <h4>Warning:</h4>
   <p>You can't directly push to an application created on Clever Cloud as a Github app: in this case, only the automatic deployment from Github is henceforth allowed.</p>
   <p>If you try to push to Clever Cloud, as you would do for a non-github app, you will get the following error :</p>
   <pre>fatal: '/data/repositories/&lt;app_id&gt;.git' does not appear to be a git repository</pre>
   <p>Indeed, no git repository is created on Clever Cloud because the application is directly cloned from Github.</p>
   <p>If you have to push directly to a repo in order to deploy an application (eg if you deploy from a CI), then create a non-github app.</p>
 </div>

<strong>Private GitHub repositories are also supported.</strong>

Caution: in Github, private repositories in an ordinary user account are an all-or-nothing deal: either someone has full read/write access (i.e., they're a collaborator) or they have no access. However, if you set up an organization, create the repo under the aegis of the organization, and then add the collaborator, you have much more fine-grained control (including giving read-only access to a private repository).

## FTP Deployment

It is possible to deploy via FTP with PHP applications.  

To deploy via FTP, you need an FTP software installed on your machine. [Filezilla](https://filezilla-project.org/) is
one of them.

When you have chosen to deploy your application via FTP, a [FS Bucket](/doc/addons/fs_buckets/) has been created with an ID
matching your application's ID. You will find the FTP credentials in the configuration tab of this particular FS Bucket.

[More documentation about Filezilla.](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29)


<div class="alert alert-hot-problems">
<h4>Warning:</h4>
<p>An FTP application is automatically started once the application is created, even if no code has been sent.</p>
</div>


<div class="alert alert-hot-problems">
<h4>Our advice</h4>
<p>FTP deployment is ok for small websites but not for large ones. We strongly
recommend you to use <b>Git</b> deployment for <b>large PHP websites</b>.</p>
</div>
