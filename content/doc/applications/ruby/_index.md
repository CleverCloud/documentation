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
- /developers/doc/ruby/ruby-on-rails
- /doc/deploy/application/ruby
- /doc/deploy/application/ruby/by-framework/ruby-on-rails
- /doc/deploy/application/ruby/ruby-rack
- /doc/getting-started/by-language/ruby
- /doc/partials/language-specific-deploy/ruby
- /doc/ruby/ruby-on-rails
comments: false
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

## Make sure to log on stdout

Since January 2024, your logs may no longer show in your Clever Cloud console.
In production.rb, you should find something like:

```ruby
if ENV['RAILS_LOG_TO_STDOUT'].present?
  logger           = ActiveSupport::Logger.new($stdout)
  logger.formatter = config.log_formatter
  config.logger    = ActiveSupport::TaggedLogging.new(logger)
end
```

It means you need to add `RAILS_LOG_TO_STDOUT=true` in your environment variables.

{{< content "deploy-git" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
