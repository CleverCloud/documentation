---
title: Clever Cloud Documentation
description: Documentation and guides to deploy, manage, and monitor your services on Clever Cloud
layout: hextra-home
disableSidebar: false
width: wide
aliases:
- /doc/developer
---
<!-- markdownlint-disable MD033 MD034-->
{{< hextra/hero-badge link="https://github.com/clevercloud/documentation">}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  Contribute
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  Deploy your apps, databases,
  and services on Clever Cloud
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-6">
{{< hextra/hero-subtitle style="margin:.3rem 0 1rem 0">}}
  Documentation and guides to run and monitor
  applications, add-ons, and Kubernetes clusters
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-12">
{{< hero-button-primary text="Learn" link="/developers/doc/getting-started" >}}
{{< hero-button-secondary text="Explore" link="/developers/doc/" >}}
</div>

<div class="hx:mt-6"></div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="API"
    subtitle="Manage your applications, add-ons, and organisations through the REST API and its OpenAPI specification"
    link="/developers/api"
    class="hx:aspect-auto hx:md:aspect-[1.1/1] hx:max-md:min-h-[340px]"
    image="/images/icons.png"
    imageClass="hx:top-[40%] hx:left-[24px] hx:w-[180%] hx:sm:w-[110%] hx:dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(58, 56, 113, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Clever Tools CLI"
    subtitle="Create, deploy, and manage your applications and add-ons from your terminal or your CI/CD pipelines"
    link="/developers/doc/tools/cli"
    class="hx:aspect-auto hx:md:aspect-[1.1/1] hx:max-lg:min-h-[340px]"
    image="/images/metrics-home.png"
    imageClass="hx:top-[40%] hx:left-[36px] hx:w-[180%] hx:sm:w-[110%] hx:dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(203, 28, 66, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Step-by-step guides"
    subtitle="Follow detailed tutorials to deploy your favorite frameworks and tools, from Laravel to WordPress, on Clever Cloud"
    link="/developers/guides"
    class="hx:aspect-auto hx:md:aspect-[1.1/1] hx:max-md:min-h-[340px]"
    image="/images/brand.png"
    imageClass="hx:top-[40%] hx:left-[36px] hx:w-[110%] hx:sm:w-[110%] hx:dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(245, 116, 97, 0.1),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Environment Variables"
    subtitle="Configure your applications, their deployment, and their behavior, and get the credentials of their add-ons"
    link="/developers/doc/manage/environment-variables/reference"
  >}}

  {{< hextra/feature-card
    title="Deploy an application"
    subtitle="Find the supported languages, and how to configure your application to build and run it on Clever Cloud"
    link="/developers/doc/deploy/applications"
  >}}
  {{< hextra/feature-card
    title="Add databases and services"
    subtitle="Link MySQL, PostgreSQL, Redis, MongoDB, Elastic, or other managed add-ons to your applications"
    link="/developers/doc/deploy/addons"
  >}}

{{< /hextra/feature-grid >}}
