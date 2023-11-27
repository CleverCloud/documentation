---
type: docs
title: Rack setup
shortdesc: How to deploy a web application using Rack on Clever Cloud.
tags:
- deploy
keywords:
- ruby
- rack
str_replace_dict:
  "@application-type@": "Ruby"
type: docs
aliases:
- /doc/deploy/application/ruby/tutorials/ruby-rack-app
---

## Overview

Currently, Clever Cloud supports Rack-based applications.
Created in 2007, Rack has become the de-facto standard for ruby web applications and is used in many frameworks such as Ruby on Rails.

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

## Configure your Ruby and Rake application

### Mandatory configuration

Be sure that:

* Bundler is installed locally (`gem install bundler`)
* you have a `config.ru` file
* Git (for the deploy part)
* you have a `gems.rb` or `Gemfile` containing your dependencies

### Tutorial and sample app

You can find an hello world tutorial of a Ruby and Rack application [here]({{< ref "//guides/ruby-rack-app-tutorial" >}}) and find the source code of the demo [here](https://helloworld-rack-demo.cleverapps.io).

{{< readfile file="new-relic.md" >}}

{{< readfile file="env-injection.md" >}}

To access environment variables from your code, just get them from the environment with `ENV["MY_VARIABLE"]`.

{{< readfile file="deploy-git.md" >}}

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}