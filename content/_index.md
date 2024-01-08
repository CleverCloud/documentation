---
type: docs
title: Clever Cloud Documentation
layout: hextra-home
disableSidebar: false
type: default
width: normal
---
<!-- markdownlint-disable MD033 MD034-->
{{< hextra/hero-badge link="https://github.com/clevercloud/documentation">}}
  <div class="w-2 h-2 rounded-full bg-primary-400"></div>
  Contribute
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="mt-6 mb-6">
{{< hextra/hero-headline >}}
  Deploy and manage your apps  
  on Clever Cloud
{{< /hextra/hero-headline >}}
</div>

<div class="mb-12">
{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Documentation and guides to deploy,  
  manage, and monitor your apps.
{{< /hextra/hero-subtitle >}}
</div>

<div class="mb-6">
{{< hero-button-primary text="Quickstart" link="doc/quickstart" >}}
{{< hero-button-secondary text="Explore" link="doc/" >}}
</div>

<div class="mt-6"></div>

{{< feature-grid >}}
  {{< feature-card
    title="Environment Variables"
    subtitle="Environment variables are a simple way of configuring your applications, their deployment and their behaviour."
    link="/doc/reference/reference-environment-variables"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[340px]"
    image="/images/icons.png"
    imageClass="top-[40%] left-[24px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(58, 56, 113, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< feature-card
    title="API"
    subtitle="The Clever Cloud API reference."
    link="/doc/extend/cc-api"
    class="aspect-auto md:aspect-[1.1/1] max-lg:min-h-[340px]"
    image="/images/metrics-home.png"
    imageClass="top-[40%] left-[36px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(203, 28, 66, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< feature-card
    title="The CLI Clever Tools"
    subtitle="An official Command Line Interface for Clever Cloud."
    link="/doc/cli"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[340px]"
    image="/images/brand.png"
    imageClass="top-[40%] left-[36px] w-[110%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(245, 116, 97, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< feature-card
    title="Steps by Steps Guides"
    subtitle="Find detailed tutorials to deploy your favorite framework on Clever Cloud"
    link="/guides"
  >}}
  
  {{< feature-card
    title="Deploy an application"
    subtitle="See supported languages and how to configure your app to deploy successfully"
    link="/doc/applications"
  >}}
  {{< feature-card
    title="Connect your application to dependencies"
    subtitle="See our available add-ons such as MySQL, PostgreSQL, Redis, Mongo, Elastic..."
    link="/doc/addons"
  >}}
  
{{< /feature-grid >}}
