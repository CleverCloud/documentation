---
weight: 150
chapter: true
title: Shortcode
shortdesc: Learn about the available shortcodes to write new documentation.
tags:
- contribute
keywords:
- contribution
- shortcode
- writing
type: docs
draft: true
---

To call a shortcode you need to write `{{</* myshortcode */>}}`.

## Alert shortcode

Use the `alert` shortcode when you want to outline something in particular. The first parameter is the level of the alert, the second is an optional title. Everything inside the shortcode will be the message. The list of alert level is available on [Bootstrap documentation](https://getbootstrap.com/docs/4.0/components/alerts/).

Here's an example for a warning alert:

```go
{{</* callout  type="warning"*/>}}
This is the message of the warning.
{{</* /callout */>}}. 
```

This will render:

{{< callout type="warning" >}}
This is the message of the warning.
{{< /callout >}}.

## image shortcode

Use the `image` shortcode if you want to embed an image. The first parameter is the link to the image. The second is the title/caption of the image.

```go
{{</* image "/images/image.png" "Image Title" */>}}
```

## readfile shortcode

Use the `readfile` shortcode to include a partial document in your content. It acts as a templating solution to enable reuse of common content.

```go
{{</* readfile "commonContent.html" */>}}
```

It's possible to search and replace variable during templating. Make sure you have a dictionary called `str_replace_dict` in the frontmatter section of the page.

```go
str_replace_dict:
  "@application-type@": "Go"
```

## githubReadme shortcode

Use the `githubReadme` shortcode to embed the Readme of an existing Github project in a page. The first parameter is the group and name of the repository.

This shortcode will embed the clever-tools readme.

```go
{{</* githubReadme "CleverCloud/clever-tools" */>}}
```

## tooltip shortcode

Use the `tooltip` shortcode to provide a definition of the a term in a tooltip. All terms definitions are fetched from the glossary under `/data/glossary.json`.
the `title` parameter is the identifier of the object from `glossary.json`.

This tooltip

```go
{{</* tooltip title="paas" */>}}PaaS{{</* /tooltip */>}}
```

will produce {{< tooltip title="paas" >}}PaaS{{< /tooltip >}}

## ref shortcode

This is a default Hugo shortcode to link to another content page.

This will output the relative link to the common configuration page: `reference/common-configuration/#private-ssh-key`

```go
{{</* ref "doc/reference/common-configuration.md#private-ssh-key" */>}}
```
