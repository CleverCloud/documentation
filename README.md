# Clever Cloud Documentation

This project is based on [Hugo](https://gohugo.io/) and uses [Hextra](https://imfing.github.io/hextra/) theme. It provides a great design, a responsive layout, dark mode support, full-text search. It's lightweight, fast, and SEO-ready, with many built-in features:

- [Complete Markdown support](https://imfing.github.io/hextra/docs/guide/markdown/)
- [Complete shortcodes set](https://imfing.github.io/hextra/docs/guide/shortcodes/)
- [Diagrams](https://imfing.github.io/hextra/docs/guide/diagrams/)
- [LaTeX math formulae](https://imfing.github.io/hextra/docs/guide/latex/)
- [Syntax highlighting](https://imfing.github.io/hextra/docs/guide/syntax-highlighting/)

## See deployed Documentation

- [Home page](https://www.clever.cloud/developers/)
- [Documentation](https://www.clever.cloud/developers/doc/)
- [API Documentation](https://www.clever.cloud/developers/api/)
- [Guides and Tutorials](https://www.clever.cloud/developers/guides/)
- [Reference Clever Tools CLI](https://www.clever.cloud/developers/doc/reference/cli/)
- [Reference Environment Variables](https://www.clever.cloud/developers/doc/reference/reference-environment-variables/)
- [Clever Cloud Platform Changelog](https://www.clever.cloud/developers/changelog/)

## Quickstart

### Install Hugo

To begin your journey with the Clever Cloud Documentation, you need Hugo Extended. You can:
- [Install it](https://gohugo.io/installation/) globally on your system
- Get its [binary](https://github.com/gohugoio/hugo/releases) and put it in the project's root

### Clone the project, preview locally

Once your system is set up, clone this repository:

```bash
git clone https://github.com/CleverCloud/documentation
```

Then:

1. Go to the documentation folder: `cd documentation`
2. Run `hugo server` to build and start the local server

Local site is available on <http://localhost:1313>, it refreshes as you modify the files, you can keep the server running with no need to restart. Find `server` command options in the [Hugo documentation](https://gohugo.io/commands/hugo_server/#options).

## Deploying on Clever Cloud

The site is configured for Clever Cloud hosting with the `static` runtime and these required environment variables:

```bash
# Declare what's the web server root, where to build the documentation
# You must have a `/developers` at the end of your application's route
CC_WEBROOT="public"
CC_STATIC_AUTOBUILD_OUTDIR="public/developers"

# Declare the location of the 404 custom page
SERVER_ERROR_PAGE_404="developers/404.html"
```

To get a working website, you must use [path routing](https://www.clever.cloud/developers/doc/administrate/domain-names/#path-routing) and add a `/developers` route to your domain.

> [!TIP]
> You can set the Hugo version with `CC_HUGO_VERSION` with a value like `0.148`

## Contributing

You can contribute by [creating an issue](https://github.com/CleverCloud/documentation/issues) or [submitting a pull request](https://github.com/CleverCloud/documentation/pulls). If you use AI tools or LLMs, you'll find specific instructions for them:

- [AI tools and LLMs instructions](./.github/copilot-instructions.md)
- [Claude Code guidance](./CLAUDE.md)
- [Contributing guidelines](./CONTRIBUTING.md)

Clever Cloud documentation is also available following the [llms.txt specification](https://www.clever.cloud/developers/llms.txt).

## Adding a new page or guide

To generates a file from a template (in `/archetypes`), run one of the following Hugo commands:

```bash
hugo new content guides/<framework>.md
hugo new content/doc/administrate/<feature>.md
hugo new content --kind applications doc/applications/<runtime>.md
```

In new page/guide front matter, `draft` is set to `true` to prevent it from being mistakenly published.

> [!TIP]
> Use `hugo server --buildDrafts` command to preview drafts locally

### Adding a changelog entry (internal only)

For any significant change to the platform (updates, new features, etc.) a new entry is created in the `content/changelog` folder.

Several entries can be made per day, it's not a problem. Each entry should provide clear, straightforward information on the essentials. If you find yourself writing an enormous amount of content, this may not be the right approach. However, you can always add a little charm to your changelog, but it's a tricky business, requiring careful, well-placed word choice.

The filename format is a markdown file with a `.md` extension:

```
yyyy-mm-dd-your-title.md
```

### Front matter configuration

Hugo uses front matter to enrich posts with metadata. Front matter allows you to keep metadata attached to an instance of a content type—i.e., embedded inside a content file. We use the following Front matter variables:

- [`type`](https://gohugo.io/methods/page/type/) (optional)
  - The type of content layout to apply. The value is a `<string>`, set it to `docs` except in changelog.

- [`weight`](https://gohugo.io/methods/page/weight/) (optional)
  - The weight of the content, used to order the sidebar. The value is an `<integer>`, default is `0`.

- [`linkTitle`](https://gohugo.io/methods/page/linktitle/) (optional)
  - The title of the content displayed in the sidebar. The value is a `<string>`, default is the `title` value.

- [`title`](https://gohugo.io/methods/page/title/) (required)
  - The title displayed in the main heading. The value is a `<string>`.

- [`description`](https://gohugo.io/methods/page/description/) (recommended)
  - The description displayed in meta-description for SEO purposes. The value is a `<string>`.

- [`excludeSearch`](https://imfing.github.io/hextra/docs/guide/configuration/#search-index) (optional)
  - Indicates whether the page should be indexed in search. Default is `false`, we recommend setting it to `true` for changelog entries.

- [aliases](https://gohugo.io/methods/page/aliases) (optional)
  - Aliases redirects the user to the right page. The value is a list of `<string>`, each string being a path to redirect from, relative to the base URL (without the `/developer`, for example: `/doc/docker`).

- [comments](https://gohugo.io/content-management/comments/) (optional)
  - Whether to show the feedback block or not. The value is a `<boolean>`, default is `true`.

- [`draft`](https://gohugo.io/methods/page/draft/) (optional)
  - Whether the page is a draft or not. The value is a `<boolean>`, default is `false`. If set to `true`, the page is not built except if you use the `--buildDrafts` flag.

- [`keywords`](https://gohugo.io/content-management/front-matter/#keywords) (optional)
  - Keywords are used for SEO purposes. The value is a list of `<string>`, each string being a keyword.

- [`tags`](https://gohugo.io/content-management/front-matter/#taxonomies) (recommended)
  - Tags are recommended only in Changelog for easy product identification. They are written in lowercase and, if possible, use the same spelling throughout the posts. The value is a list of `<string>`.

- [`authors`](https://gohugo.io/content-management/front-matter/#taxonomies) (mostly used in changelog)
  - Can be set to showcase the people behind the product. Authors are defined with a `name`, `link` for their Github or any other social network, and an `image` for the profile picture. The profile picture can be set with the GitHub avatar with a link like `https://github.com/BlackYoup.png` and the parameter `?size=40` for reducing the image size (recommended for performance). The values are all of `<string>` type.

- [`date`](https://gohugo.io/methods/page/date/) (mostly used in changelog)
  - The date that will be displayed in the post. The value is a string in ISO 8601 like `yyyy-mm-dd`.

For example, a changelog entry front matter could look like this:

```yaml
---
title: Redis updated to v7.2.4
description: Redis has been updated to v7.2.4 mostly to prevent security issues
date: 2024-01-11
tags:
  - redis
authors:
  - name: BlackYoup
    link: https://github.com/BlackYoup
    image: https://github.com/BlackYoup.png?size=40
excludeSearch: true
---
```

### Adding an image

Adding an image can be useful to highlight an interface change, for example. Use such markdown syntax for that:

```markdown
![Alt text](/images/your-image.jpg "Title of the image")
```

If needed, you can also use [the `figure` shortcode](https://gohugo.io/shortcodes/figure/) to add attributes such as a width limit:

```markdown
{{< figure src="/developers/images/your-image.jpg" alt="Alt text" title="Title of the image" width="800px">}}
```

- [Learn more about Hugo shortcodes](https://gohugo.io/shortcodes/)

### Adding a new shared content

You can include shared content in several pages. To use this feature:

1. Create a new markdown file in `/shared`
2. Add it to the relevant pages with: `{{% content "your-partial" %}}`

> [!TIP]
> If you need to include a shared content including shortcodes, use `{{% content-raw "your-partial" %}}` instead. Don't include headings (starting with `#`) in it as they won't be rendered in the page Table of Contents (ToC).

## Tooltips

Tooltips are useful to provide additional information on terms or acronyms that may not be familiar to all readers. They help improve the accessibility and comprehension of your documentation without cluttering the main text.

To create a tooltip, add the term and its associated tooltip definition in the [`data/tooltips.toml`](./data/tooltips.toml) file. Once defined, tooltips automatically display when users hover over associated terms in the documentation.

## Markdown Linting

Hugo uses [Goldmark](https://github.com/yuin/goldmark), a Markdown parser written in Go, compliant with [CommonMark 0.30](https://spec.commonmark.org/). Therefore, for better readability and maintainability, all markdown files for this project are linted with [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2). We strongly recommend that you follow the validation rules described [here](https://github.com/DavidAnson/markdownlint#rules--aliases).

This linter can be downloaded and run locally, or used via Visual Studio Code:

- <https://github.com/DavidAnson/vscode-markdownlint> for Visual Studio Code
- <https://github.com/DavidAnson/markdownlint-cli2> as a `npm` package

**Ignored markdown files** are listed in the `.markdownlintignore`.
**Ignored specifications**, such as some HTML tag of Web Components, are configured in the `.markdownlint.jsonc`

## Editorial checks

This project uses [Vale.sh](https://vale.sh) to run editorial checks on the documentation. Install Vale on your machine or as an IDE extension if you want to run checks. This project is already configured to use it on pull requests.
