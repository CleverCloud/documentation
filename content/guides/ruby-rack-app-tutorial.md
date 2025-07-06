---
type: docs
title: Ruby Rack full tutorial
shortdesc: How to write a hello world web application using Rack and deploy it on Clever Cloud.
tags:
- deploy
keywords:
- ruby
- rack
str_replace_dict:
  "@application-type@": "Ruby"
type: docs
aliases:
- /doc/deploy/application/ruby/tutorials/ruby-rack-app-tutorial
---

## Overview Introduction

Currently, Clever Cloud supports Rack-based applications.
Created in 2007, Rack has become the de-facto standard for ruby web applications and is used in many frameworks such as Ruby on Rails.

## Configure your Rack based application

### Mandatory configuration

To follow this tutorial, you will need:

* Ruby >= 1.9.2 (w/ Rubygems)
* Bundler (`gem install bundler` and you're good to go!)
* Your preferred editor
* Git (for the deploy part)

{{< callout type="info">}}
To manage your gems and ruby versions, we recommend [rbenv](https://github.com/sstephenson/rbenv). If you use a system-wide installation of ruby, You will have to use `sudo` with the `gem` and `bundle` commands, or use arguments that will make gem and bundle install the gem in directories you have write-permissions in.
{{< /callout >}}

### My application does not exists already

#### Create a Ruby + Rake application locally

You can deploy a demo application by following these instructions:

```bash
mkdir helloworld-rack
cd helloworld-rack
touch hello.rb config.ru Gemfile ## or gems.rb
```

Inside `hello.rb` put the following:

```ruby
class HelloWorld
  def call(env)
   [200, {"Content-Type" => "text/plain"}, ["Hello world!"]]
  end
end
```

Inside the `config.ru` (That is, the main Rack entry-point) put:

```ruby
require './hello'
run HelloWorld.new
```

The `gems.rb` or `Gemfile` file will contain our dependencies:

```ruby
source 'https://rubygems.org'

gem 'rack', '~>1.5.1'


gem "puma", "~> 6.4"
```

We don't need any more dependencies. The `gems.rb` or `Gemfile` is mandatory to deploy
on Clever Cloud.

Do not forget to init an empty git repository with `$ git init`

#### Test your application locally

To test your application, just fetch the dependencies using bundler:

```shell
$ bundle install
Fetching gem metadata from https://rubygems.org/..........
Resolving dependencies...
Using rack (1.5.2)
Using puma (6.4.2)
Using bundler (1.3.5)
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is installed.
```

And start your application:

```bash
$ bundle exec rackup
[2013-09-16 17:35:26] INFO  WEBrick 1.3.1
[2013-09-16 17:35:26] INFO  ruby 2.0.0 (2013-06-27) [x86_64-linux]
[2013-09-16 17:35:26] INFO  WEBrick::HTTPServer#start: pid=5656 port=9292
```

You can now test with your browser at `http://localhost:9292`.

You can now read [My application already exists](#my-application-already-exists)

### My application already exists

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

 {{< content "env-injection" >}}

To access environment variables from your code, just get them from the environment with `ENV["MY_VARIABLE"]`.

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}
