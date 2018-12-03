---
title: Deploy a fluentd
shortdesc: How to deploy a fluentd using Docker on Clever Cloud.
tags:
- docker
- ruby
- fluentd
---

## Introduction

Since you deploy microservices on Clever Cloud, you may need some data pipes between your services to:

* collect data from your PostgreSQL to create Elasticsearch indexes for your website search engine
* collect application logs to analyze them with Elasticsearch, then archive them with S3
* collect Apache access logs to analyze them in MongoDB
* extract data from the database of your PHP/MySQL application to transform then load them in your other node.js/PostgreSQL application
* and many more ...

Fluentd is an open source data collector, which lets you unify the data collection and consumption for a better use and understanding of data.

## Dependencies

To follow this tutorial, you will need:

* Ruby >= 2.4.4 (w/ Rubygems)

* Bundler

* Docker

* Git

* curl

<div class="alert">
To manage your gems and ruby versions, we recommend <a href="https://github.com/sstephenson/rbenv">rbenv</a>.
</div>

## Create a fluentd application locally

```bash
$ mkdir myFluentd
$ cd myFluentd
$ touch Gemfile Dockerfile go.sh td-agent.conf
$ chmod +x go.sh
```

Inside `Gemfile` put the following:

```ruby
source 'http://rubygems.org'

ruby '2.4.4'

gem 'fluentd'
gem 'fluent-plugin-td'
```

Then run bundler to install dependencies and generate your `Gemfile.lock`

```bash
$ bundle install
```

Clever Cloud needs that your application answers on requests made on `0.0.0.0:8080`, we'll use a PORT environment variable for local test purposes (this variable is automatically setup on each application).
Inside `td-agent.conf` put the following:

```yaml
<source>
  @type monitor_agent
  bind 0.0.0.0
  port "#{ENV['PORT']}"
</source>
```

Inside `go.sh` put the following:

```bash
#!/bin/sh
bundle exec fluentd --use-v1-config -c td-agent.conf
echo "🌍 Fluentd server started"
```

## Test locally

Start you service

```bash
$ PORT=9292 ./go.sh
```

Verify that it responds to requests

```bash
$ curl 0.0.0.0:9292
```

## Create a Docker application in the console

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Why I can't just use ruby runtime</h4>
  </div>
  <div class="panel-body">
    Ruby runtime on Clever Cloud requires **Puma** or **uWSGI** webserver but fluentd is using **excon**.
  </div>
</div>

First create a [Docker application](./docker.md)

Then inside `Dockerfile` put the following:

```docker
FROM ruby:2.4.4
EXPOSE 8080
COPY Gemfile Gemfile.lock td-agent.conf go.sh ./

RUN bundle config --global frozen 1
RUN bundle install
RUN chmod +x go.sh

CMD [ "/go.sh" ]
```

Now you can deploy your application.

Finally, you can [update your configuration](https://docs.fluentd.org/v1.0/articles/config-file) with all inputs, filters and outputs you need or check for a [community based plugin](https://www.fluentd.org/plugins).
