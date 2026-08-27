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
- /doc/ruby/ruby-rack
---

Clever Cloud supports applications built on the [Rack interface](https://github.com/rack/rack) with its Ruby runtime. The runtime installs dependencies with Bundler and starts the application's `config.ru` through Puma.

A deployable Rack application needs:

- A `Gemfile` that includes `rack` and `puma`
- A committed `Gemfile.lock` with the `x86_64-linux` platform
- A `config.ru` entry point
- A supported Ruby version declared in the `Gemfile` or with `CC_RUBY_VERSION`

No custom run command or listening port is required: the runtime configures Puma and connects it to the managed NGINX server. Access [environment variables](/developers/doc/develop/env-variables/) with `ENV["VARIABLE_NAME"]`.

Follow the [complete Ruby Rack tutorial](/guides/ruby-rack-app-tutorial/) to create, test and deploy a minimal current application, or read the [Ruby runtime reference](/developers/doc/applications/ruby/) for build hooks, Rake tasks, Puma settings and static files.
