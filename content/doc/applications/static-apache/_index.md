---
type: docs
title: Static with Apache
description: Deploy Static files with Apache HTTP server on Clever Cloud
comments: false
---

## Overview

If you only need to serve static files without executing any code on the backend, for instance for a javascript Single Page Application (SPA), you can create a static application.

This runtime is based on apache, so shares a lot with the [PHP runtime]({{< ref "doc/applications/php" >}}). This means you can use `.htaccess` files for redirection or access control.

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

{{< content "env-injection" >}}

Application deployment on Clever Cloud is via **Git or FTP**.

 {{< content "deploy-git" >}}

{{< content "deploy-ftp" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}

## Serving index.html for SPA (Single Page Application) routers

When you work with an SPA framework like React, Vue.js, Angular…, you're using client side routing.
This means when you click on a link going to `/the-page`, your browser doesn't make an HTTP request for `/the-page`.
Instead, the client side router highjacks the clicks on links, changes the DOM to display the page and ask the browser to change the URL in the address bar to `/the-page`.

What happens if you try to refresh the page?
If you do this, the browser will try to make an HTTP request for `/the-page`.
In most situations, SPA only have one HTML document at the root called `index.html`.
This is why, you'll probably get a 404 error.

To fix this, most people using SPA frameworks configure their HTTP server to serve the `index.html` for all unkown requests.
By this we mean for all requests that don't have a matching file on disk to serve.

To do this with our static applications, you need a `.htaccess` file like this at the root of your project:

```ApacheConf
RewriteEngine On

# If an existing asset or directory is requested, serve it
RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} -f [OR]
RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} -d
RewriteRule ^ - [L]

# If the requested resource doesn't exist, use index.html
RewriteRule ^ /index.html
```

## Prerendering with Prerender.io

When you use a SPA framework, you are using Client side rendering.
One of the problem with this method is a poor SEO as search engine crawlers have more difficulty reading the content of this type of application.
To minimize this issue, prerendering can be a solution.

If you want to Prerender your application on Clever Cloud, one solution is to use [Prerender.io](https://prerender.io/).
To use it with our static applications, you need a `.htaccess` file like this at the root of your project:

```ApacheConf
<IfModule mod_headers.c>
    RequestHeader set X-Prerender-Token "<PRERENDER_TOKEN>"
    RequestHeader set X-Prerender-Version "prerender-apache@2.0.0"
</IfModule>

<IfModule mod_rewrite.c>
    RewriteEngine On

    <IfModule mod_proxy_http.c>
        RewriteCond %{HTTP_USER_AGENT} googlebot|bingbot|yandex|baiduspider|facebookexternalhit|twitterbot|rogerbot|linkedinbot|embedly|quora\ link\ preview|showyoubot|outbrain|pinterest\/0\.|pinterestbot|slackbot|vkShare|W3C_Validator|whatsapp|redditbot|applebot|flipboard|tumblr|bitlybot|skypeuripreview|nuzzel|discordbot|google\ page\ speed|qwantify|bitrix\ link\ preview|xing-contenttabreceiver|google-inspectiontool|chrome-lighthouse|telegrambot [NC,OR]
        RewriteCond %{QUERY_STRING} _escaped_fragment_
        RewriteCond %{REQUEST_URI} ^(?!.*?(\.js|\.css|\.xml|\.less|\.png|\.jpg|\.jpeg|\.gif|\.pdf|\.doc|\.txt|\.ico|\.rss|\.zip|\.mp3|\.rar|\.exe|\.wmv|\.doc|\.avi|\.ppt|\.mpg|\.mpeg|\.tif|\.wav|\.mov|\.psd|\.ai|\.xls|\.mp4|\.m4a|\.swf|\.dat|\.dmg|\.iso|\.flv|\.m4v|\.torrent|\.ttf|\.woff|\.svg))

        RewriteRule ^(index\.html|index\.php)?(.*) http://service.prerender.io/%{REQUEST_SCHEME}://%{HTTP_HOST}$2 [P,END]
    </IfModule>
</IfModule>
```
You can find your `PRERENDER_TOKEN` on your [Prerender.io account](https://prerender.io/).

You can verify your configuration work using [this guide](https://docs.prerender.io/docs/how-to-test-your-site-after-you-have-successfully-validated-your-prerender-integration).
## Apache Configuration with `CC_WEBROOT`

If you set the `CC_WEBROOT = /<web-folder>` environment variable, make sure you put your `.htaccess` file at the root of your `/<web-folder>`. This is where Apache will look for directives when you deploy an application in a Static runtime.

If you don't set the [`CC_WEBROOT`]({{< ref "/doc/reference/reference-environment-variables/#php" >}}) environment variable, the root of your project is the root of your web server.
