---
type: docs
title: Clever Grid
weight: 5
shortdesc: Clever Grid is the machine learning oriented platform by Clever Cloud. It provides a unified GPU ecosystem to run your scripts.
tags:
- dashboard-setup
keywords:
- ai
- artificial
- intelligence
- ml
- machine learning
- nvidia
- cuda
- tensorflow
- neural
- deep 
- learning
type: docs
draft: true
---

## Concepts in Clever Grid

Clever Grid is the machine learning oriented platform by Clever Cloud. It provides a unified GPU ecosystem to run your scripts.

### Organization, Application, Add-on

In Clever Grid you create some **applications** under one **organization**.
Organization is useful to manage roles and team collaboration.

An application is a **stateless** virtual machine which runs your code.

Additionally to an application, you can link one or more **stateful** virtual machine called **add-on** in Clever Grid. That lets
you keep your data

### Application as Runner, Application as Webapp

In some case, you may just need a one run of a script. To train a model or proceed a huge calculation for example. That the
interest of **Runner**. A Runner runs a script and then go away.

A **Webapp** keeps the application up and serve via HTTP.

## Create an application

{{< callout type="warning" >}}
    Remember that an application is **stateless**. To save your data, you need to use an add-on.
{{< /callout >}}

1. Go to https://dashboard.clevergrid.io, create a “brand new application”.
{{< image "/images/create-application.png" "Create application." >}}
2. Select the application type :
   * Docker (Runner | Webapp)
   {{< image "/images/docker.png" "Docker" >}}
   * Python (Runner | Webapp)
   {{< image "/images/python.png" "Python" >}}
   * Java (Runner | Webapp)
   {{< image "/images/java.png" "Java" >}}
3. Select the size of your instance(s) and the number of nodes
4. (optional) You can choose a Template for your application
  {{< callout type="info" >}}
    Template will set up for you a compete ecosystem for a specific application. It provides add-ons and environment 
   variables for you.
   <ul>
      <li>Jupyter Notebook</li>
      <li>R Notebook</li>
      <li>…</li>
   </ul>
  {{< /callout >}}

## Create an add-on

1. Go to https://dashboard.clevergrid.io, Add a “a storage service”.
{{< image "/images/addons.png" "Addons" >}}
2. Select the storage plan you need
3. Link it to your applications
  {{< callout type="info" >}}
    Add-ons's credentials will be automatically set up in your application. Yet it can be found on the "Add-on dashboard" tabs of your dashboard by the Clever Cloud console.
  {{< /callout >}}


## Set-up an application

You can pass some parameter to your application by **environments variables**.

  {{< callout type="warning" >}}
    If you deploy a Webapp, Clever Grid expects an exposed `PORT` as environment variable listening the port `8080`
  {{< /callout >}}


- Go to [dashboard.clevergrid.io](https://dashboard.clevergrid.io) and select your application
- Manage your environment variables by the tab "Environment variables" 
{{< image "/images/env-selection.png" "Environment selection" >}}

### Python applications

If there is a `requirements.txt` in the root folder of your application, dependencies will be installed during the deployment.

* Starting file
  * Clever Grid need to know  which file runs to start your application. That can be a python file, declare in the
 `CC_MLPYTHON_RUN_MAIN` environment variable or custom bash script in `CC_MLPYTHON_START_SCRIPT` environment variable.
  {{< callout type="warning" >}}
    It should contain the path of your main file. The path should be relative to the root of your repository.
  {{< /callout >}}

For example, “pytorch.py” and “./pytorch.py are both valid.
**Bash scripts are expected to be executable (via `chmod+x`)** 

* Python version : 
  * You can select the python version with the `PYTHON_VERSION` environment variable. Valid values are documented here: [www.clever-cloud.com/doc/python/python_apps/#choose-python-version](https://www.clever-cloud.com/doc/python/python_apps/#choose-python-version)

### Docker application

Refer to the Clever Cloud documentation : https://www.clever-cloud.com/doc/docker/

### Java application

Refer to the Clever Cloud documentation : https://www.clever-cloud.com/doc/java/java-jar/

### Hooking build steps

Between the build steps and before running the script, you can hook scripts. The hooks are documented here: https://www.clever-cloud.com/doc/clever-cloud-overview/hooks/
E.g. you can have a post build hook to initialize conda and stuff.

## Send your code

Your Clever Grid application is now set up to receive your code.

* Go to your project and add the Clever Grid repository to your repository :

      git remote add clever-grid git+ssh://git@push-clevergrid-clevercloud-customers.services.clever-cloud.com/<APP_ID>
  {{< callout type="info" >}}
    You can find the repository address on the overview page of your application
    {{< image "/images/git-url.png" "git-url" "width:100%" >}}
  {{< /callout >}}

* Push your code

## Command line management

In addition to the Clever Grid console, you can manage your add-ons and applications from the command line with Clever Tools.

see : https://www.clever-cloud.com/doc/clever-tools/getting_started/

## Billing

Clever Grid application are reports on the Clever Cloud platform to billing purpose

* 1 GPU cost 10 euros by day. Charged per minute.
* Storage add-ons are based on the Clever Cloud billing : https://www.clever-cloud.com/en/pricing

## Support

If you are having issues, please let us know support@clever-cloud.com
