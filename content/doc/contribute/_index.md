---
weight: 10
chapter: true
title: Contribute
shortdesc: Learn about the available shortcodes to write new documentation.
tags:
- contribute
keywords:
- contribution
- shortcode
- writing
type: docs
---

## Before writing something new

Before you start writing something new please create a [Github issue](https://github.com/CleverCloud/doc.clever-cloud.com/issues) so we can talk about it. Moslty to make sure someone is not already working on the same thing.

## Writing new content

There are a number of things you need to be aware of when writing new content. We use markdown files and Hugo to generate this documentation. The CSS classes available are in Bootstrap 4.5. A list of commonly used Hugo shortcode can be found in its [dedicated page]( {{< ref "doc/contribute/shortcodes" >}} )


### Debug Mode

If you add `debug=true` as params of your Hugo site, you should see every shortcode outlined on your website like so:

<div class="shortcode-debug"><strong>myshortcode </strong><p>This is a shortcode being used</div>