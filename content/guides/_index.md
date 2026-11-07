---
type: docs
linkTitle: Guides
title: Guides
description: Step-by-step guides to deploy frameworks, static sites, and self-hosted software on Clever Cloud, and to set up database and observability tools
keywords:
- guides
- tutorials
- deployment
- frameworks
- applications
- configuration
aliases:
- /doc/deploy/application/docker/tutorials
- /doc/deploy/application/haskell/tutorials
- /doc/deploy/application/javascript/tutorials
- /doc/deploy/application/php/tutorials
- /doc/deploy/application/python/tutorials
- /doc/deploy/application/ruby/tutorials
- /doc/deploy/application/scala/tutorials
- /doc/tutorials/
llmsTxtOptional: true
---

{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Step-by-step guides to deploy and use your favorite stack on Clever Cloud
{{< /hextra/hero-subtitle >}}

Guides deploy a framework, a static site, or ready-to-use software, and set up tools around your add-ons and your observability. To manage Clever Cloud add-ons from a Kubernetes cluster, see the [Kubernetes Operator](/doc/deploy/kubernetes/operator/).

## Database Tools

{{< cards >}}
  {{< card link="/developers/guides/databases/pgpool" title="Pgpool-II" subtitle="Configure Pgpool-II for PostgreSQL add-ons" icon="simple:postgresql" >}}
  {{< card link="/developers/guides/databases/proxysql" title="ProxySQL" subtitle="Configure ProxySQL for MySQL add-ons" icon="mysql" >}}
{{< /cards >}}

## Frameworks

{{< cards >}}
  {{< card link="/developers/guides/frameworks/astro" title="Astro" subtitle="Deploy an Astro application as a static site or with Node.js" icon="simple:astro" >}}
  {{< card link="/developers/guides/frameworks/django" title="Django" subtitle="Deploy a Django application" icon="simple:django" >}}
  {{< card link="/developers/guides/frameworks/hono" title="Hono" subtitle="Deploy a Hono application with Node.js" icon="simple:hono" >}}
  {{< card link="/developers/guides/frameworks/laravel" title="Laravel" subtitle="Deploy a Laravel application" icon="simple:laravel" >}}
  {{< card link="/developers/guides/frameworks/nodejs-mongodb" title="Node.js & MongoDB" subtitle="Deploy a Node.js application with MongoDB" icon="simple:nodedotjs" >}}
  {{< card link="/developers/guides/frameworks/nuxt" title="Nuxt" subtitle="Deploy a Nuxt application as a static site or with Node.js" icon="simple:nuxt" >}}
  {{< card link="/developers/guides/frameworks/otree" title="oTree" subtitle="Deploy an oTree application" icon="simple:django" >}}
  {{< card link="/developers/guides/frameworks/ruby-on-rails" title="Ruby on Rails" subtitle="Deploy a Ruby on Rails application" icon="ruby" >}}
  {{< card link="/developers/guides/frameworks/ruby-rack" title="Ruby Rack" subtitle="Deploy a Ruby Rack application" icon="ruby" >}}
  {{< card link="/developers/guides/frameworks/sveltekit" title="SvelteKit" subtitle="Deploy a SvelteKit application with static or server-side rendering" icon="simple:svelte" >}}
  {{< card link="/developers/guides/frameworks/symfony" title="Symfony" subtitle="Deploy a Symfony application" icon="simple:symfony" >}}
{{< /cards >}}

## Observability

{{< cards >}}
  {{< card link="/developers/guides/observability/haskell-ekg-statsd" title="Ekg-statsd" subtitle="Export Haskell metrics with ekg-statsd" icon="simple:haskell" >}}
  {{< card link="/developers/guides/observability/fluentd" title="Fluentd" subtitle="Deploy a Fluentd data collector" icon="simple:fluentd" >}}
  {{< card link="/developers/guides/observability/kibana" title="Kibana" subtitle="Enable Kibana for an Elastic Stack add-on" icon="simple:kibana" >}}
  {{< card link="/developers/guides/observability/nodejs-statsd" title="Node.js StatsD" subtitle="Export Node.js metrics with hot-shots" icon="simple:nodedotjs" >}}
{{< /cards >}}

## Self-Hosted Software

{{< cards >}}
  {{< card link="/developers/guides/self-hosted/docs" title="Docs" subtitle="Deploy the Docs collaborative editor" icon="docs-suite" >}}
  {{< card link="/developers/guides/self-hosted/drupal" title="Drupal" subtitle="Deploy a Drupal website" icon="drupal" >}}
  {{< card link="/developers/guides/self-hosted/echoip" title="EchoIP" subtitle="Deploy EchoIP as a Go application" icon="simple:go" >}}
  {{< card link="/developers/guides/self-hosted/ghost" title="Ghost" subtitle="Deploy a publishing platform with MySQL and object storage" icon="simple:ghost" >}}
  {{< card link="/developers/guides/self-hosted/moodle" title="Moodle" subtitle="Deploy and configure a Moodle learning platform" icon="moodle" >}}
  {{< card link="/developers/guides/self-hosted/outline" title="Outline" subtitle="Deploy the Outline knowledge base" icon="simple:outline" >}}
  {{< card link="/developers/guides/self-hosted/sftpgo" title="SFTPGo" subtitle="Deploy an SFTP server with PostgreSQL and Cellar object storage" icon="server-stack" >}}
  {{< card link="/developers/guides/self-hosted/wordpress" title="WordPress" subtitle="Deploy a WordPress website" icon="simple:wordpress" >}}
{{< /cards >}}

## Static Site Generators

{{< cards >}}
  {{< card link="/developers/guides/static-sites/docusaurus" title="Docusaurus" subtitle="Deploy a static Docusaurus website" icon="simple:docusaurus" >}}
  {{< card link="/developers/guides/static-sites/eleventy" title="Eleventy (11ty)" subtitle="Deploy a static Eleventy website" icon="simple:eleventy" >}}
  {{< card link="/developers/guides/static-sites/hexo" title="Hexo" subtitle="Deploy a static Hexo website" icon="simple:hexo" >}}
  {{< card link="/developers/guides/static-sites/hugo" title="Hugo" subtitle="Deploy a static Hugo website" icon="simple:hugo" >}}
  {{< card link="/developers/guides/static-sites/hugo-cellar" title="Hugo + Cellar" subtitle="Publish Hugo assets and build artifacts to Cellar" icon="simple:hugo" >}}
  {{< card link="/developers/guides/static-sites/lume" title="Lume (Deno)" subtitle="Deploy a static Lume website with Deno" icon="deno" >}}
  {{< card link="/developers/guides/static-sites/maudit" title="Maudit" subtitle="Deploy a static Maudit website with Rust" icon="maudit" >}}
  {{< card link="/developers/guides/static-sites/mdbook" title="mdBook" subtitle="Deploy a static mdBook website" icon="simple:mdbook" >}}
  {{< card link="/developers/guides/static-sites/mkdocs" title="MkDocs" subtitle="Deploy a static MkDocs website" icon="docs" >}}
{{< /cards >}}
