---
type: docs
title: Fluentd
Description: How to deploy a fluentd using Docker on Clever Cloud.
tags:
- deploy
keywords:
- docker
- ruby
- fluentd
str_replace_dict:
  "@application-type@": "Docker"
type: docs
aliases:
- /doc/deploy/application/docker/tutorials/fluentd
---

## Overview

Since you deploy microservices on Clever Cloud, you may need some data pipes between your services to:

* collect data from your PostgreSQL to create Elasticsearch indexes for your website search engine
* collect application logs to analyze them with Elasticsearch, then archive them with S3
* collect Apache access logs to analyze them in MongoDB
* extract data from the database of your PHP/MySQL application to transform then load them in your other node.js/PostgreSQL application
* and many more …

Fluentd is an open source data collector written in Ruby, which lets you unify the data collection and consumption for a better use and understanding of data.

{{< callout type="info" >}}
  Ruby application on Clever Cloud requires **Puma** webserver but fluentd is using **excon**.
{{< /callout >}}

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

## Configure your Fluentd + Docker application

### Mandatory configuration

To follow this tutorial, you will need:

* Ruby >= 2.4.4 (w/ Rubygems)
* Bundler
* Docker
* Git
* curl
* a Ruby versions manager

{{< callout type="info" >}}
To manage your gems and ruby versions, we recommend [rbenv](https://GitHub.com/sstephenson/rbenv).
{{< /callout >}}

### My application does not exists already

#### Create a fluentd application locally

```bash
mkdir myFluentd
cd myFluentd
touch Gemfile Dockerfile go.sh td-agent.conf
chmod +x go.sh
```

Inside `Gemfile` put the following:

```ruby
source 'https://rubygems.org'

ruby '2.4.4'

gem 'fluentd'
gem 'fluent-plugin-td'
```

Then run bundler to install dependencies and generate your `Gemfile.lock`

```bash
bundle install
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

#### Test locally

Start you service

```bash
PORT=9292 ./go.sh
```

Verify that it responds to requests

```bash
curl 0.0.0.0:9292
```

You can now read [My application already exists](#my-application-already-exists)

#### Fine tune you application

You can [update your configuration](https://docs.fluentd.org/v1.0/articles/config-file) with all inputs, filters and outputs you need or check for a [community based plugin](https://www.fluentd.org/plugins).

### My application already exists

#### Prepare your application for deployment

Create a `Dockerfile` at the root of your project and put inside the following (assuming your start script is in `go.sh`):

```dockerfile
FROM ruby:2.4.4
EXPOSE 8080
COPY Gemfile Gemfile.lock td-agent.conf go.sh ./

RUN bundle config --global frozen 1
RUN bundle install
RUN chmod +x go.sh

CMD [ "/go.sh" ]
```

 {{< content "env-injection" >}}

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}
