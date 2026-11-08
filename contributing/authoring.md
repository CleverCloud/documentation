# Authoring guide

This guide explains how to add and maintain the repository content: pages, their metadata, shared content, examples, deployment guides, runtime pages, and changelog entries.

For the text itself, follow the [style guide](./style-guide.md). To check and submit your change, follow [CONTRIBUTING.md](../CONTRIBUTING.md).

## Add a page or guide

Create new content from the archetypes in [`archetypes/`](../archetypes/), which set the front matter and the structure of each kind of page. These examples create a guide, a documentation page, and an application runtime page:

```bash
hugo new content --kind guides guides/frameworks/my-framework.md
hugo new content doc/develop/my-feature.md
hugo new content --kind applications doc/deploy/applications/my-runtime.md
```

Store a guide in the section that matches its subject, and add it to the section index. Add the card of a guide in `guides/static-sites/` to [`shared/static-guides.md`](../shared/static-guides.md), which this index and the Static runtime pages include.

Archetypes set `draft: true`, so regular builds exclude unfinished pages. Preview drafts locally with `hugo server --buildDrafts`. When the page is ready to publish, remove the `draft` field instead of setting it to `false`.

## Set the front matter

Hugo front matter stores the metadata of a page. This project uses the following fields:

| Field           | Status      | Purpose                                                                                                 |
| --------------- | ----------- | ------------------------------------------------------------------------------------------------------- |
| `aliases`       | Optional    | Redirects paths that existed previously. Omit the `/developers` base path, for example `/doc/docker`    |
| `authors`       | Changelog   | Lists contributors with `name`, `link`, and `image` fields                                              |
| `date`          | Changelog   | Sets the publication date or date-time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format     |
| `description`   | Recommended | Provides the description of the page for search results and search engines                              |
| `draft`         | Optional    | Excludes unfinished content from regular builds when set to `true`. Remove the field before publication |
| `excludeSearch` | Optional    | Excludes the page from the search index when set to `true`. Set it for changelog entries                |
| `keywords`      | Optional    | Lists search keywords                                                                                   |
| `linkTitle`     | Optional    | Sets a short sidebar label, usually the product name, and defaults to `title`                           |
| `tags`          | Changelog   | Lists lowercase product tags with consistent spelling                                                   |
| `title`         | Required    | Sets the page heading and search-oriented title. The generated HTML title adds the Clever Cloud name    |
| `type`          | Optional    | Selects a content layout and uses `docs` outside the changelog                                          |
| `weight`        | Optional    | Orders pages in the sidebar and defaults to `0`                                                         |

Write a descriptive `title`, for search engine optimization (SEO), that doesn't repeat `Clever Cloud`: the generated HTML title includes it. Keep `linkTitle` short, usually the product name, to fit in the sidebar.

Don't add `aliases` to a new page: use them only to preserve URLs that existed previously. The [Hugo front matter documentation](https://gohugo.io/content-management/front-matter/) describes the supported formats and the built-in fields.

## Move, merge, or remove a page

When a page moves to another URL, or when you merge its content into another page:

- Add the old URL to the `aliases` of the destination page, so that Hugo keeps serving a redirect
- Carry over every alias the removed page already declared: they must keep resolving
- Update internal links to target the new URL directly instead of relying on the redirect
- Check each redirect in the build output before committing

Updating the links matters most in the `shared/` blocks, which many pages include.

## Use shortcodes and shared content

This documentation uses the [Hextra theme](https://imfing.github.io/hextra/), whose [shortcodes](https://imfing.github.io/hextra/docs/guide/shortcodes/) improve readability:

- [Cards](https://imfing.github.io/hextra/docs/guide/shortcodes/cards/), with `{{< cards >}}`, link to related resources
- Hero subtitles, with `{{< hextra/hero-subtitle >}}`, introduce a guide
- [Steps](https://imfing.github.io/hextra/docs/guide/shortcodes/steps/), with `{{% steps %}}`, suit the `/guides/` section, or any tutorial
- [Tabs](https://imfing.github.io/hextra/docs/guide/shortcodes/tabs/), with `{{< tabs >}}` and named `{{< tab name="npm" >}}` children, show alternatives side by side

The project adds its own shortcodes in [`layouts/shortcodes/`](../layouts/shortcodes/), such as `content` and `content-raw` for shared content. The [style guide](./style-guide.md#callouts) explains how to choose and write callouts.

### Shared content

When several pages need the same content, write it once in [`shared/`](../shared/), and include it in each of them:

```markdown
{{% content "your-partial" %}}
```

Use `{{% content-raw "your-partial" %}}` when the shared file contains shortcode markup. Don't add headings to shared files: they don't appear in the table of contents of the page.

### Images

Store documentation images under `static/images/`, and reference them with Markdown:

```markdown
![Alt text](/images/your-image.jpg "Image title")
```

When the image needs attributes, such as a width limit, use the Hugo [`figure` shortcode](https://gohugo.io/shortcodes/figure/):

```markdown
{{< figure src="/developers/images/your-image.jpg" alt="Alt text" title="Image title" width="800px">}}
```

### Tooltips

Add a term and its definition to [`data/tooltips.toml`](../data/tooltips.toml): the site shows it when readers hover over the term.

### Source formatting

Keep each paragraph on one logical line, and rely on editor word wrap: don't hard-wrap prose with line breaks that don't affect rendering. End every text file with a newline character.

## Write commands and examples

Provide complete examples that run, with real commands and configurations. Add setup context and expected output when they help. Use realistic names instead of `foo`, `bar`, or `example`, and exact environment variable names, such as `CC_WEBROOT`.

Keep commands literally copyable. Don't use shell-invalid placeholders or bracketed optional arguments in executable code blocks: show optional variants separately, or explain where to add the flag. Archetypes are the exception: replace their placeholders, such as `<runtime>` or `RUNTIME`, before you publish the page.

Add code comments only when they explain non-obvious behavior.

## Configure dependencies

All non-Docker runtimes provide a shared set of tools and version-management variables, whatever the runtime of the application. For example, `CC_NODE_VERSION` can select Node.js in a PHP application, while `CC_PHP_VERSION` can select PHP in a Node.js application. Other shared tools include Composer, Gradle, Hugo, and Python.

Prefer these dedicated environment variables, and the package managers the runtime already provides, when they manage a dependency or its version. If a Mise task also needs a runtime-managed tool, derive its Mise version from the dedicated environment variable instead of hard-coding the same version twice.

For other deployment dependencies, prefer [Mise](https://mise.jdx.dev/) and a suitable backend, such as [HTTP](https://mise.jdx.dev/dev-tools/backends/http.html) or [GitHub](https://mise.jdx.dev/dev-tools/backends/github.html), over custom download scripts. Pin their versions whenever it's appropriate.

Don't document the deprecated `clevercloud/*.json` configuration files and fields when environment variables or the detection of the project replace them. Document them only when they have no alternative.

## Write a deployment guide

Prefer one clear path that uses platform defaults and native features. Follow every documented command from a fresh project, and test every behavior the guide promises. Verify the default build and run configuration before documenting any scaling override.

Write the Clever Tools commands the way recent guides do:

- Follow their option style, including short Clever Tools options where established
- Omit `-a` when the current directory is linked to only one application
- Use an application alias to disambiguate or link resources
- Place the standard `clever domain` and custom-domain example right after the application creation

When a guide needs a portable password-generation example and OpenSSL is already a prerequisite, use `openssl rand -base64 32`.

Check that the command output you capture in a guide doesn't expose credentials, tokens, add-on environment values, or unrelated account data. Validate public-storage claims with an unauthenticated request, and persistence claims after a restart or rebuild.

## Write a runtime page

The pages of `content/doc/deploy/applications/` describe how Clever Cloud builds and starts each runtime. Start from the `applications` [archetype](#add-a-page-or-guide), which sets their structure: overview, mandatory needs with a minimal application, build phase, version, caches, Clever Tasks, and Go Further cards.

Give a minimal application, with the command to try it locally when the ecosystem has one. When the application starts its own web server, it listens on `0.0.0.0` and on the port in `PORT`. When Clever Cloud starts the server, such as Puma for Ruby, explain it instead.

Show the commands the build runs, in their order, and the variables that change them. Deploy every example, and test every behavior the page describes, including the failures it warns about. Remove what you can't verify.

When Clever Cloud provides a list of versions, add it to [`data/runtime_versions.yml`](../data/runtime_versions.yml), and generate the table with the `runtimes_versions` shortcode, not by hand. Quote the versions in this file, so that YAML doesn't read `3.10` as `3.1`. When the project sets its version, such as a Stack snapshot, explain how instead.

Keep the headings deployment logs link to, such as *Manage your static files and assets* on the Ruby page: the link checker doesn't see them. Link related pages with cards in a *Go Further* section, not with shared content blocks.

## Add a changelog entry

Only Clever Cloud team members add entries to `content/changelog/`, one per significant platform update. To report an error, [open an issue](https://github.com/CleverCloud/documentation/issues). Keep entries concise, and focused on what users need to understand or act on.

Store each entry under its publication year, and name it with the `MM-DD-title.md` format, such as `content/changelog/2026/08-26-product-update.md`. Multiple entries can share the same date. Show complete command sequences, and commit the entry with the pages it relies on, as the [commit conventions](../CONTRIBUTING.md#commit-messages) explain.

A changelog entry can use the following front matter:

```yaml
---
title: Product 1.2 is available
description: Product 1.2 adds a new feature and fixes an upgrade issue
date: 2026-08-26
tags:
  - product
authors:
  - name: Clever Cloud
    link: https://github.com/CleverCloud
    image: https://github.com/CleverCloud.png?size=40
excludeSearch: true
---
```

## Update generated content

Don't edit the body of [`content/doc/cli-reference.md`](../content/doc/cli-reference.md) by hand. It comes from the documentation of a Clever Tools release, and this repository maintains only its front matter. Regenerate it from the latest release, or from the version you pass as argument, with:

```bash
scripts/update-cli-reference.sh
scripts/update-cli-reference.sh 5.3.0
```

The script keeps the front matter of the page.

## Change the theme and assets

- Don't override global styles for font type, size, or color
- Comment your code if you add custom CSS
- Import only the relevant classes from an external CSS tool, not the whole file
- Prefer self-hosting over a CDN, which can impact the performance of the site when used in `<head>`

A CDN remains fine for test purposes, when you submit your pull request and deploy a review app.
