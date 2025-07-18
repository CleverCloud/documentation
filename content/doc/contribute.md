---
type: docs
weight: 14
title: Contribute
description: Learn about the available shortcodes to write new documentation
tags:
- contribute
keywords:
- contribution
- shortcode
- writing
aliases:
- /administrate/guides/contribute
- /contribute/writing
- /doc/contribute/writing
- /doc/get-help/community
- /readme
comments: false
---

Would you like to contribute to this documentation?

## Before writing something new

Before you start writing something new please create a [Github issue](https://github.com/CleverCloud/documentation/issues) so we can talk about it. Moslty to make sure someone is not already working on the same thing.

## Writing new content

There are a number of things you need to be aware of when writing new content. We use Markdown files and [Hugo](https://gohugo.io/) to generate this documentation.

### Debug Mode

If you add `debug=true` as params of your Hugo site, you should see every shortcode outlined on your website like so:

```html
<div class="shortcode-debug"><strong>myshortcode </strong><p>This is a shortcode being used</div>
```
