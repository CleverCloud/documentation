---
type: docs
linkTitle: Ruby Rack
title: Ruby Rack
description: Deploy Ruby Rack web applications on Clever Cloud with detailed step-by-step tutorials and configuration examples
keywords:
- ruby
- rack
- web framework
- application server
- deployment guide
aliases:
- /doc/deploy/application/ruby/tutorials/ruby-rack-app
- /doc/ruby/ruby-rack
---

## Overview

Currently, Clever Cloud supports Rack-based applications.
Created in 2007, Rack has become the de-facto standard for ruby web applications and is used in many frameworks such as Ruby on Rails.

{{% content "create-application" %}}

 {{% content "set-env-vars" %}}

## Configure your Ruby and Rake application

### Mandatory configuration

Be sure that:

* Bundler is installed locally (`gem install bundler`)
* you have a `config.ru` file
* Git (for the deploy part)
* you have a `gems.rb` or `Gemfile` containing your dependencies

### Tutorial and sample app

- [An hello world tutorial of a Ruby and Rack application](/developers/guides/ruby-rack-app-tutorial)

 {{% content "new-relic" %}}

 {{% content "env-injection" %}}

To access environment variables from your code, just get them from the environment with `ENV["MY_VARIABLE"]`.

 {{% content "deploy-git" %}}

 {{% content "link-addon" %}}

{{% content "more-config" %}}
