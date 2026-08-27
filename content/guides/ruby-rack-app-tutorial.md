---
type: docs
linkTitle: Ruby Rack tutorial
title: Build and deploy a Ruby Rack application
description: Create a minimal Rack application and deploy it with Puma on the Clever Cloud Ruby runtime
keywords:
- ruby
- rack
- puma
- web framework
- tutorial
aliases:
- /doc/deploy/application/ruby/tutorials/ruby-rack-app-tutorial
---

[Rack](https://github.com/rack/rack) provides a standard interface between Ruby web applications and application servers. This tutorial creates a minimal Rack 3 application served by Puma and deploys it with the Clever Cloud Ruby runtime.

## Create the Rack application

Install a currently supported [Ruby release](https://www.ruby-lang.org/en/downloads/branches/), [Bundler](https://bundler.io/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), then initialize the project:

```bash
mkdir myRackApp
cd myRackApp
git init
```

Create a `Gemfile` with Rack and Puma. Declaring the Ruby branch keeps local and deployed environments consistent:

```ruby {filename="Gemfile"}
source "https://rubygems.org"

ruby "~> 3.4"

gem "puma", "~> 7.0"
gem "rack", "~> 3.2"
```

Create the Rack entry point:

```ruby {filename="config.ru"}
class HelloWorld
  def call(_env)
    [200, { "content-type" => "text/plain" }, ["Hello world!"]]
  end
end

run HelloWorld.new
```

Install the dependencies and generate the lockfile:

```bash
bundle install
bundle lock --add-platform x86_64-linux
```

You can check the application locally with `bundle exec puma config.ru`, then open `http://localhost:9292`.

## Deploy on Clever Cloud

Install [Clever Tools](/developers/doc/cli/), log in and create a Ruby application linked to the current directory:

```bash
npm i -g clever-tools
clever login

clever create -t ruby -a myRackApp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application's URL or add a [custom domain](/developers/doc/administrate/domain-names/). A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

Commit the files and deploy:

```bash
git add .
git commit -m "First deploy"

clever deploy
clever open
```

The Ruby runtime installs the locked gems and starts `config.ru` with Puma. It manages the listening socket and NGINX connection, so this application does not need a custom port or run command. Read application configuration with `ENV["VARIABLE_NAME"]`.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/ruby/" title="Ruby runtime" subtitle="Configure Ruby and Puma applications" icon="ruby" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://github.com/rack/rack" title="Rack documentation" subtitle="Learn the Rack interface" icon="github" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://puma.io/" title="Puma documentation" subtitle="Configure the Ruby application server" icon="server" >}}
{{< /cards >}}
