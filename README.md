# Clever Cloud documentation

The Clever Cloud documentation site uses [Hugo](https://gohugo.io/) and the [Hextra](https://imfing.github.io/hextra/) theme. It provides responsive navigation, dark mode, full-text search and the following content features:

- [Diagrams](https://imfing.github.io/hextra/docs/guide/diagrams/)
- [LaTeX mathematical notation](https://imfing.github.io/hextra/docs/guide/latex/)
- [Markdown](https://imfing.github.io/hextra/docs/guide/markdown/)
- [Shortcode support](https://imfing.github.io/hextra/docs/guide/shortcodes/)
- [Syntax highlighting](https://imfing.github.io/hextra/docs/guide/syntax-highlighting/)

## Published documentation

- [Clever Cloud documentation](https://www.clever.cloud/developers/)
- [API reference](https://www.clever.cloud/developers/api/)
- [Clever Tools CLI reference](https://www.clever.cloud/developers/doc/cli-reference/)
- [Environment variables reference](https://www.clever.cloud/developers/doc/develop/common-configuration/environment-variables/reference/)
- [Guides and tutorials](https://www.clever.cloud/developers/guides/)
- [Platform changelog](https://www.clever.cloud/developers/changelog/)
- [Technical documentation](https://www.clever.cloud/developers/doc/)

## Repository structure

- [`archetypes/`](./archetypes/): templates for new guides, documentation pages, and application runtime pages
- [`content/`](./content/): the site content
  - `api/`: API reference
  - `changelog/`: platform updates, one folder per year
  - `doc/`: technical documentation
  - `guides/`: framework and software deployment guides
  - `postmortem/`: incident reports
- [`data/`](./data/): structured data, such as the supported runtime versions in `runtime_versions.yml`, the Kubernetes versions, and the tooltip definitions in `tooltips.toml`
- [`layouts/`](./layouts/): Hugo templates and project shortcodes, including the Markdown output of each page and the `llms.txt` home page for large language models (LLMs)
- [`shared/`](./shared/): Markdown blocks that several pages include
- [`static/`](./static/): images, fonts, and the favicon
- [`update-cli-reference.sh`](./update-cli-reference.sh): regenerates the CLI reference page

## Local development

### Requirements

Install the following tools before building the site:

- [Git](https://git-scm.com/downloads)
- [Mise](https://mise.jdx.dev/getting-started.html)

Mise installs the Go, Hugo Extended, markdownlint-cli2 and Vale versions declared in [`mise.toml`](./mise.toml).

### Preview the site

Clone the repository and start Hugo's development server:

```bash
git clone https://github.com/CleverCloud/documentation.git
cd documentation
mise install
hugo server
```

The site is available at <http://localhost:1313> and refreshes when you modify a file. See the [`hugo server` documentation](https://gohugo.io/commands/hugo_server/) for the available options.

## Deploy on Clever Cloud

The site uses the Clever Cloud `static` runtime with the following environment variables:

```bash
CC_DISABLE_MISE="true"
CC_WEBROOT="public"
CC_STATIC_AUTOBUILD_OUTDIR="public/developers"
SERVER_ERROR_PAGE_404="developers/404.html"
```

`CC_DISABLE_MISE` prevents Clever Cloud from installing the development dependencies because the static runtime provides and manages its deployment tools. Configure the route so its path ends in `/developers`, which matches the site's configured base URL and output directory.

> [!TIP]
> Set `CC_HUGO_VERSION` to a supported version such as `0.167` to select the Hugo version used for deployment

## Contribute

You can contribute by [creating an issue](https://github.com/CleverCloud/documentation/issues) or [submitting a pull request](https://github.com/CleverCloud/documentation/pulls). Read the following project instructions before submitting a change:

- [Coding agent instructions](./AGENTS.md)
- [Contributing guidelines](./CONTRIBUTING.md)

The documentation is also available in the [llms.txt format](https://www.clever.cloud/developers/llms.txt).

## Add a page or guide

Use the archetypes in [`archetypes/`](./archetypes/) to create new content. These examples create a guide, a documentation page and an application runtime page:

```bash
hugo new content --kind guides guides/my-framework.md
hugo new content doc/develop/my-feature.md
hugo new content --kind applications doc/deploy/applications/my-runtime.md
```

Archetypes set `draft: true` so regular builds exclude unfinished pages. Preview drafts locally with:

```bash
hugo server --buildDrafts
```

Remove the `draft` field when the page is ready to publish.

### Update the CLI reference

The body of [`content/doc/cli-reference.md`](./content/doc/cli-reference.md) comes from the documentation of a Clever Tools release. Regenerate it from the latest release, or from the version you pass as argument, with:

```bash
./update-cli-reference.sh
./update-cli-reference.sh 5.3.0
```

The script keeps the page's front matter, which this repository maintains.

### Add a changelog entry

Clever Cloud team members add an entry to `content/changelog/` for each significant platform update. Keep entries concise and focused on information users need to understand or act on.

Store each entry under its publication year and name it with the `MM-DD-title.md` format, for example `content/changelog/2026/08-26-product-update.md`. Multiple entries can share the same date.

### Configure front matter

Hugo front matter stores page metadata. This project uses the following fields:

| Field           | Status      | Purpose                                                                                                                                     |
| --------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `aliases`       | Optional    | Redirects paths that existed previously. Omit the `/developers` base path, for example `/doc/docker`                                        |
| `authors`       | Changelog   | Lists contributors with `name`, `link` and `image` fields                                                                                   |
| `date`          | Changelog   | Sets the publication date or date-time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format                                         |
| `description`   | Recommended | Provides the page's description for search results and search engines                                                                       |
| `draft`         | Optional    | Excludes unfinished content from regular builds when set to `true`. Remove the field before publication                                     |
| `excludeSearch` | Optional    | Excludes the page from the search index when set to `true`. Set it for changelog entries                                                    |
| `keywords`      | Optional    | Lists search keywords                                                                                                                       |
| `linkTitle`     | Optional    | Sets a short sidebar label, usually the product name, and defaults to `title`                                                               |
| `tags`          | Changelog   | Lists lowercase product tags with consistent spelling                                                                                       |
| `title`         | Required    | Sets the page heading and search-oriented title. The generated HTML title adds the Clever Cloud name                                        |
| `type`          | Optional    | Selects a content layout and uses `docs` outside the changelog                                                                              |
| `weight`        | Optional    | Orders pages in the sidebar and defaults to `0`                                                                                             |

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

[CONTRIBUTING.md](./CONTRIBUTING.md#front-matter) explains how to write titles and when to use aliases. See the [Hugo front matter documentation](https://gohugo.io/content-management/front-matter/) for the supported formats and built-in fields.

### Add an image

Store documentation images under `static/images/` and reference them with Markdown:

```markdown
![Alt text](/images/your-image.jpg "Image title")
```

Use Hugo's [`figure` shortcode](https://gohugo.io/shortcodes/figure/) when the image needs attributes such as a width limit:

```markdown
{{< figure src="/developers/images/your-image.jpg" alt="Alt text" title="Image title" width="800px">}}
```

### Add shared content

Create reusable Markdown in [`shared/`](./shared/) when several pages need the same content, and include it in each of them with:

```markdown
{{% content "your-partial" %}}
```

> [!TIP]
> Use `{{% content-raw "your-partial" %}}` when the shared file contains shortcode markup. Don't add headings to shared files because they don't appear in the page table of contents

### Add a tooltip

Add a term and its definition to [`data/tooltips.toml`](./data/tooltips.toml). The site then displays the definition when readers hover over matching terms.

## Validate changes

Run a production build before submitting a change:

```bash
hugo
```

The repository provides [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) rules in [`.markdownlint.jsonc`](./.markdownlint.jsonc) and CLI configuration in [`.markdownlint-cli2.jsonc`](./.markdownlint-cli2.jsonc), which excludes the paths listed in [`.gitignore`](./.gitignore). Run the version installed by Mise:

```bash
markdownlint-cli2 "**/*.md"
```

Every pull request runs markdownlint on all the Markdown files of the repository, and fails if it reports an issue.

Editorial checks use [Vale](https://vale.sh/) with the project's own `Clever` style, in [`.github/styles/Clever/`](./.github/styles/Clever/), which implements the rules of [CONTRIBUTING.md](./CONTRIBUTING.md).

Mise can run the same styles locally, on the files you change or on the whole repository:

```bash
vale README.md AGENTS.md CONTRIBUTING.md archetypes content shared
```

The pull request workflow reports Vale alerts on changed lines without failing, so a green check doesn't prove that a change has none. [CONTRIBUTING.md](./CONTRIBUTING.md#-validation) lists which alerts to fix and what to review by hand.
