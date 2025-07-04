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
  <div class="hx-w-2 hx-h-2 hx-rounded-full hx-bg-primary-400"></div>
  Contribute
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx-mt-6 hx-mb-6">
{{< hextra/hero-headline >}}
  Deploy and manage your apps
  on Clever Cloud
{{< /hextra/hero-headline >}}
</div>

<div class="hx-mb-12">
{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Documentation and guides to deploy,
  manage, and monitor your apps.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx-mb-6">
{{< hero-button-primary text="Quickstart" link="doc/quickstart" >}}
{{< hero-button-secondary text="Explore" link="doc/" >}}
</div>

<div class="hx-mt-6"></div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Environment Variables"
    subtitle="Environment variables are a simple way of configuring your applications, their deployment and their behaviour."
    link="doc/reference/reference-environment-variables"
    class="hx-aspect-auto md:hx-aspect-[1.1/1] max-md:hx-min-h-[340px]"
    image="/images/icons.png"
    imageClass="hx-top-[40%] hx-left-[24px] hx-w-[180%] sm:hx-w-[110%] dark:hx-opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(58, 56, 113, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="API"
    subtitle="The Clever Cloud API reference."
    link="api"
    class="hx-aspect-auto md:hx-aspect-[1.1/1] max-lg:hx-min-h-[340px]"
    image="/images/metrics-home.png"
    imageClass="hx-top-[40%] hx-left-[36px] hx-w-[180%] sm:hx-w-[110%] dark:hx-opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(203, 28, 66, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="The CLI Clever Tools"
    subtitle="An official Command Line Interface for Clever Cloud."
    link="doc/cli"
    class="hx-aspect-auto md:hx-aspect-[1.1/1] max-md:hx-min-h-[340px]"
    image="/images/brand.png"
    imageClass="hx-top-[40%] hx-left-[36px] hx-w-[110%] sm:hx-w-[110%] dark:hx-opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(245, 116, 97, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Steps by Steps Guides"
    subtitle="Find detailed tutorials to deploy your favorite framework on Clever Cloud"
    link="guides"
  >}}

  {{< hextra/feature-card
    title="Deploy an application"
    subtitle="See supported languages and how to configure your app to deploy successfully"
    link="doc/applications"
  >}}
  {{< hextra/feature-card
    title="Connect your application to dependencies"
    subtitle="See available add-ons such as MySQL, PostgreSQL, Redis, Mongo, Elastic…"
    link="doc/addons"
  >}}

{{< /hextra/feature-grid >}}
