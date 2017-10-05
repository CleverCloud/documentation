---
title: Hello world tutorial
shortdesc: How to write a hello world web application using Rack and deploy it on Clever Cloud.
tags:
- ruby
---
# Hello World tutorial for Rack-based application

## Introduction

Currently, Clever Cloud supports Rack-based applications.
Created in 2007, Rack has become the de-facto standard for ruby
web applications.


## Dependencies

To follow this tutorial, you will need:

* Ruby >= 1.9.2 (w/ Rubygems)

* Bundler (`gem install bundler` and you're good to go!)

* Your preferred editor

* Git (for the deploy part)

<div class="alert">
To manage your gems and ruby versions, we recommend <a href="https://github.com/sstephenson/rbenv">rbenv</a>.
If you use a system-wide installation of ruby, You will have to use `sudo` with the `gem` and `bundle` commands,
or use arguments that will make gem and bundle install the gem in directories you have write-permissions in.
</div>


## Create and write your application

```bash
$ mkdir helloworld-rack
$ cd !$ # or 'helloworld-rack'.
$ touch hello.rb config.ru gems.rb ## or Gemfile
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
```

We don't need any more dependencies. The gems.rb or Gemfile is mandatory to deploy
on Clever Cloud.

## Test your application

To test your application, just fetch the dependencies using bundler:

```bash
$ bundle install
Fetching gem metadata from https://rubygems.org/..........
Resolving dependencies...
Using rack (1.5.2)
Using bundler (1.3.5)
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is installed.
$ bundle exec rackup # That will start your application
[2013-09-16 17:35:26] INFO  WEBrick 1.3.1
[2013-09-16 17:35:26] INFO  ruby 2.0.0 (2013-06-27) [x86_64-linux]
[2013-09-16 17:35:26] INFO  WEBrick::HTTPServer#start: pid=5656 port=9292
```

You can now test with your browser at <a href="http://localhost:9292/">localhost:9292</a>.

## Deploy your application

1. Using the Clever Cloud console, create a new Ruby application (<a href="https://console.clever-cloud.com/users/me/applications/new">https://console.clever-cloud.com/users/me/applications/new</a>).
2. Initialize and set up a the git repository for your application:

```bash
$ git init
Initialized empty Git repository in /*******/helloworld-rack/.git/
$ git add config.ru hello.rb gems.rb gems.locked # or Gemfile Gemfile.lock
$ git commit -m "Initial commit, ready for clever push"
[master (root-commit) eaadcfc] Initial commit, ready for clever push
 4 files changed, 20 insertions(+)
 create mode 100644 gems.rb
 create mode 100644 gems.locked
 create mode 100644 config.ru
 create mode 100644 hello.rb
$ git remote add cleverapps git+ssh://git@push.clever-cloud.com/app_xxxxx-xxxxx-xxxxx-xxxxx-xxxxxx.git
$ git push cleverapps master
Counting objects: 6, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 641 bytes | 0 bytes/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote: {"id":320,"message":"The application has successfully been queued for redeploy.","type":"success"}
To git+ssh://git@push.clever-cloud.com/app_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.git
 * [new branch]      master -> master
```


And now, wait till the end of the deployment. You can check the logs in the console.
Our demo for this tutorial is here: <a href="https://helloworld-rack-demo.cleverapps.io/">https://helloworld-rack-demo.cleverapps.io/</a>.
