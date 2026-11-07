---
type: docs
linkTitle: Ruby
title: Ruby application runtime
description: Build and deploy Ruby applications on Clever Cloud with Bundler and Puma, from a Sinatra application to Ruby on Rails, with Sidekiq workers
keywords:
- bundler
- gem
- puma
- rack
- rails
- ruby app hosting
- ruby cloud
- ruby on rails
- sidekiq
- sinatra
aliases:
- /applications/ruby
- /doc/applications/ruby
- /doc/deploy/application/ruby
- /doc/deploy/application/ruby/by-framework
- /doc/deploy/application/ruby/by-framework/ruby-on-rails
- /doc/deploy/application/ruby/ruby-rack
- /doc/en/ruby-hosting
- /doc/getting-started/by-language/ruby
- /doc/partials/language-specific-deploy/ruby
- /doc/ruby
- /doc/ruby-hosting
- /doc/ruby/ruby
- /doc/ruby/ruby-on-rails
- /doc/applications/ruby/ruby/
- /getting-started/by-language/ruby
---

## Overview

[Ruby](https://www.ruby-lang.org) is a dynamic language focused on simplicity and productivity. Clever Cloud installs the gems of your project with [Bundler](https://bundler.io), and serves it with [Puma](https://puma.io) behind NGINX. It works with any [Rack](https://github.com/rack/rack) application, such as [Ruby on Rails](https://rubyonrails.org) or [Sinatra](https://sinatrarb.com).

## Create your Ruby application

To create a new Ruby application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type ruby
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Ruby application

### Mandatory needs

A Ruby application needs, at the root of the project or of the folder set in `APP_FOLDER`:

- A `Gemfile` with the `puma` gem, and its committed `Gemfile.lock`
- A `config.ru` file

The `Gemfile` lists the gems, the libraries your application uses. When you run `bundle install`, [Bundler](https://bundler.io) installs them and records their exact versions in `Gemfile.lock`: commit this file, so that Clever Cloud installs the same versions as your computer. Clever Cloud also accepts `gems.rb` and `gems.locked`, other names of these files.

Clever Cloud serves your application with [Puma](https://puma.io), a web server for [Rack](https://github.com/rack/rack) applications. Rack is the common interface between Ruby web frameworks and web servers, and `config.ru` is its entry point: it loads your application and tells Puma which object answers the requests. Ruby on Rails and most frameworks create this file with a new project. A Sinatra application started with `ruby app.rb` doesn't have one: add it, as in the example below. A [Clever Task](#ruby-scripts-as-clever-tasks) runs its own command, and doesn't need `config.ru`.

You don't set any port: Clever Cloud starts Puma, and NGINX forwards the requests to it. For instance, a minimal [Sinatra](https://sinatrarb.com) application:

```ruby {filename="Gemfile"}
source "https://rubygems.org"

gem "puma"
gem "sinatra"
```

```ruby {filename="config.ru"}
require "bundler"
Bundler.require

require "./app"
run Sinatra::Application
```

```ruby {filename="app.rb"}
require "sinatra"

get "/" do
  "Hello from Ruby #{RUBY_VERSION} on Clever Cloud"
end
```

In `config.ru`, `Bundler.require` loads the gems of the `Gemfile`, and `run` gives Puma the application to serve. To try it on your computer, run `bundle install`, then `bundle exec puma`, and open `http://localhost:9292`.

Your application reads its [environment variables](/doc/manage/environment-variables/) with `ENV`, such as `ENV["REDIS_URL"]` for the credentials of a linked add-on.

### Build phase

On a new build, Clever Cloud selects the [Ruby version](#ruby-version) and runs the pre-build [hook](/doc/manage/build-hooks/). It then installs your gems in the `vendor/bundle` folder, without the `development` and `test` groups:

```bash
bundle config set deployment true
bundle config set path vendor/bundle
bundle config set without development:test
bundle install
```

The installation fails if `Gemfile.lock` doesn't match the `Gemfile`, or if it doesn't list `puma`. If Bundler fails with an older project, set `CC_RUBY_LEGACY=true` to install the gems with the former Bundler options.

### Run Rake tasks during the build

[Rake](https://ruby.github.io/rake/) runs the tasks defined in a `Rakefile`, or by Rails, such as `db:migrate` for database migrations. To run some after the gems are installed, list them in `CC_RAKEGOALS`, separated by commas:

```bash
clever env set CC_RAKEGOALS "db:migrate, assets:precompile"
```

Clever Cloud runs them in this order with `bundle exec rake`, if your project has a `Rakefile`: `bundle exec` runs a command with the gems of your project. If one of them fails, the deployment fails. They run on each new build, not when an application restarts from its [build cache](#caches).

### Ruby version

Your `Gemfile` can require a Ruby version, such as any Ruby 3.4 release with this line:

```ruby {filename="Gemfile"}
ruby "~> 3.4.0"
```

Clever Cloud uses the Ruby version set in `CC_RUBY_VERSION`, or the most recent one installed that matches the `Gemfile`. Without any of them, it uses the most recent Ruby version installed. To use the latest Ruby 3.4 release, for instance:

```bash
clever env set CC_RUBY_VERSION 3.4
```

`CC_RUBY_VERSION` accepts a major version, such as `4`, a minor version, such as `4.0`, or an exact version, such as `4.0.1`. If no installed version matches, the deployment fails. Keep `CC_RUBY_VERSION` consistent with the `ruby` requirement of your `Gemfile`: when they disagree, the deployment either fails, or uses the version the `Gemfile` requires.

Clever Cloud doesn't read the `.ruby-version` file: to use it, add `ruby file: ".ruby-version"` to your `Gemfile`.

### Environment

Clever Cloud sets `RAILS_ENV` and `RACK_ENV` to `production`. To use another environment, such as `staging`, set `RAILS_ENV`: Clever Cloud gives `RACK_ENV` the same value. With `development`, Bundler also installs the `development` and `test` groups.

### Puma workers and threads

Clever Cloud starts Puma with `bundle exec puma`, behind NGINX, and reads `config/puma.rb`. Puma runs several processes, its workers, which each handle several requests at once, with threads.

By default, Clever Cloud starts one worker per vCPU of the instance, each with as many threads. To change them, set `CC_PUMA_WORKERS` and `CC_PUMA_THREADS`, which take precedence over `config/puma.rb`. `CC_PUMA_THREADS` accepts a number, or a minimum and a maximum:

```bash
clever env set CC_PUMA_WORKERS 2
clever env set CC_PUMA_THREADS 4:8
```

If `WEB_CONCURRENCY` and `RAILS_MAX_THREADS` aren't set, Clever Cloud sets them, for the Puma configuration that Rails generates. Puma is the only server Clever Cloud starts: `CC_RUN_COMMAND` only applies to [Clever Tasks](#ruby-scripts-as-clever-tasks).

### Manage your static files and assets

NGINX can serve the static files of your project without reaching Puma. Set their folder in `STATIC_FILES_PATH`, from the root of the repository:

```bash
clever env set STATIC_FILES_PATH public
```

NGINX then serves the files of this folder with a usual static extension, such as `.css`, `.js`, or `.png`, at the same path: `public/robots.txt` at `/robots.txt`. It forwards the other requests to your application. To serve the whole folder under a path instead, set this path in `STATIC_URL_PREFIX`: with `/static`, `public/logo.png` is at `/static/logo.png`.

### NGINX settings

NGINX waits up to 300 seconds for data from your application. To change this delay, set `NGINX_READ_TIMEOUT`, in seconds: if your application sends nothing for longer, before it starts its response, NGINX answers with a `504` error.

To protect your application with HTTP basic authentication, set `CC_HTTP_BASIC_AUTH` to a `login:password` pair. For more users, add `CC_HTTP_BASIC_AUTH_1`, `CC_HTTP_BASIC_AUTH_2`, and so on:

```bash
clever env set CC_HTTP_BASIC_AUTH "admin:$(openssl rand -base64 32)"
```

A `clevercloud/http.json` file sets NGINX redirections: `force_https` sends HTTP to HTTPS, `aliases` serves a path with another one:

```json {filename="clevercloud/http.json"}
{
  "force_https": true,
  "aliases": {
    "/old-page": "/new-page"
  }
}
```

### Sidekiq

[Sidekiq](https://sidekiq.org) runs jobs in the background, from queues stored in Redis®. To use it, add the `sidekiq` gem to your `Gemfile`, link a [Redis® add-on](/doc/deploy/databases/redis/), which provides `REDIS_URL`, then enable Sidekiq:

```bash
clever env set CC_ENABLE_SIDEKIQ true
```

Each instance of the application then starts a Sidekiq process next to Puma, and restarts it if it stops. To start one Sidekiq process per configuration file, list these files in `CC_SIDEKIQ_FILES` instead, separated by commas, from the root of your project:

```bash
clever env set CC_SIDEKIQ_FILES "config/sidekiq.yml,config/sidekiq_low.yml"
```

Outside of Rails, a Sidekiq configuration file loads the file that defines your jobs with `:require:`, here `worker.rb`:

```yaml {filename="config/sidekiq.yml"}
:concurrency: 2
:require: ./worker.rb
:queues:
  - default
```

### Ruby on Rails

A Rails application needs a few more settings in production:

- `SECRET_KEY_BASE`, a secret generated with `openssl rand -hex 64`
- A database: a linked [PostgreSQL add-on](/doc/deploy/databases/postgresql/) provides `POSTGRESQL_ADDON_URI`, to read in `config/database.yml`
- `CC_RAKEGOALS`, to prepare the database and compile the assets, and `STATIC_FILES_PATH=public`, so that NGINX serves them

```bash
clever env set SECRET_KEY_BASE "$(openssl rand -hex 64)"
clever env set CC_RAKEGOALS "db:prepare, assets:precompile"
clever env set STATIC_FILES_PATH public
```

Clever Cloud collects what your application writes to its standard output, and to the log file of its environment, such as `log/production.log`: Rails logs there by default. To store files with Active Storage, use [Cellar](/doc/deploy/storage/cellar/), the S3-compatible object storage of Clever Cloud.

The [Ruby on Rails guide](/guides/frameworks/ruby-on-rails/) deploys a complete application, from the database to the assets.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the gems between commits, in `vendor/bundle` at the repository root.

## Ruby scripts as Clever Tasks

A Ruby script can run as a [Clever Task](/doc/deploy/tasks/), such as a job: Clever Cloud installs the gems, then runs `CC_RUN_COMMAND` from the repository root.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `scripts/report.rb` script:

```bash
clever create --type ruby --task "bundle exec ruby scripts/report.rb"
clever deploy # or clever restart if there is no code change
```

A task doesn't need `config.ru`, but its `Gemfile` must still list the `puma` gem.

## Go Further

{{< cards >}}
  {{< card link="/developers/guides/frameworks/ruby-on-rails" title="Ruby on Rails" subtitle="Deploy a Rails application with PostgreSQL" icon="ruby" >}}
  {{< card link="/developers/guides/frameworks/ruby-rack" title="Ruby Rack" subtitle="Deploy a Rack application" icon="ruby" >}}
  {{< card link="/developers/doc/observability/new-relic" title="New Relic" subtitle="Monitor your application with New Relic" icon="chart-pie" >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
