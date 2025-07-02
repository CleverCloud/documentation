---
type: docs
title: Ruby on Rails
shortdesc: Ruby on Rails is an open source web application framework which runs on the Ruby programming language.
tags:
- deploy
keywords:
- ruby
- rails
str_replace_dict:
  "@application-type@": "Ruby"
type: docs
aliases:
- /doc/deploy/application/ruby/ruby-on-rails
---

## Overview

Ruby on Rails is an open source web application framework which runs on the Ruby programming language. It is a full-stack framework: it allows creating pages and applications that gather information from the web server, talk to or query the database, and render templates out of the box. As a result, Rails features a routing system that is independent of the web server.

Clever Cloud allows you to deploy any Ruby on Rails application. This page will explain you how to set up your application to run it on our service.
You do not need to change a lot in your application, the *requirements* will help you configure your applications with some mandatory files to add, and properties to setup.

- [An example of Ruby on Rails application on Clever Cloud](https://GitHub.com/CleverCloudDemos/demo-rubyonrails-pg-rest)

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

{{< content "language-specific-deploy/ruby" >}}

 {{< content "new-relic" >}}

 {{< content "env-injection" >}}

To access environment variables from your code, just get them from the environment with `ENV["MY_VARIABLE"]`.

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}
