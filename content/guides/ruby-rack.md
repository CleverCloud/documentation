---
type: docs
linkTitle: Ruby Rack
title: Deploy a Ruby Rack application
description: Prepare Rack applications for the Clever Cloud Ruby runtime and its managed Puma server
keywords:
- ruby
- rack
- puma
- web framework
- application server
aliases:
- /doc/deploy/application/ruby/tutorials/ruby-rack-app
- /doc/deploy/application/ruby/tutorials/ruby-rack-app-tutorial
- /doc/ruby/ruby-rack
- /guides/ruby-rack-app-tutorial
---

Clever Cloud supports applications built on the [Rack interface](https://github.com/rack/rack) with its Ruby runtime. The runtime installs dependencies with Bundler and starts the application's `config.ru` through Puma.

A deployable Rack application needs:

- A `Gemfile` that includes `rack` and `puma`
- A committed `Gemfile.lock` with the `x86_64-linux` platform
- A `config.ru` entry point
- A supported Ruby version declared in the `Gemfile` or with `CC_RUBY_VERSION`

No custom run command or listening port is required: the runtime configures Puma and connects it to the managed NGINX server. Access [environment variables](/developers/doc/develop/common-configuration/environment-variables/) with `ENV["VARIABLE_NAME"]`.

Read the [Ruby runtime reference](/developers/doc/deploy/applications/ruby/) for build hooks, Rake tasks, Puma settings and static files.
