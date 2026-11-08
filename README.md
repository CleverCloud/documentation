# Clever Cloud documentation

The Clever Cloud documentation site uses [Hugo](https://gohugo.io/) and the [Hextra](https://imfing.github.io/hextra/) theme. It provides responsive navigation, dark mode, and full-text search, and supports the following content features:

- [Diagrams](https://imfing.github.io/hextra/docs/guide/diagrams/)
- [LaTeX mathematical notation](https://imfing.github.io/hextra/docs/guide/latex/)
- [Markdown](https://imfing.github.io/hextra/docs/guide/markdown/)
- [Shortcode support](https://imfing.github.io/hextra/docs/guide/shortcodes/)
- [Syntax highlighting](https://imfing.github.io/hextra/docs/guide/syntax-highlighting/)

## Published documentation

- [Clever Cloud documentation](https://www.clever.cloud/developers/)
- [API reference](https://www.clever.cloud/developers/api/)
- [Clever Tools CLI reference](https://www.clever.cloud/developers/doc/cli-reference/)
- [Environment variables reference](https://www.clever.cloud/developers/doc/manage/environment-variables/reference/)
- [Guides and tutorials](https://www.clever.cloud/developers/guides/)
- [Platform changelog](https://www.clever.cloud/developers/changelog/)
- [Technical documentation](https://www.clever.cloud/developers/doc/)

The documentation is also available in the [llms.txt format](https://www.clever.cloud/developers/llms.txt).

## Repository structure

- [`archetypes/`](./archetypes/): templates for new guides, documentation pages, and application runtime pages
- [`content/`](./content/): the site content
  - `api/`: API reference
  - `changelog/`: platform updates, one folder per year
  - `doc/`: technical documentation
  - `guides/`: deployment guides, one folder per section, such as `frameworks/` or `self-hosted/`
  - `postmortem/`: incident reports
  - `shared/`: blocks that several pages include, never published on their own
- [`contributing/`](./contributing/): the style guide and the authoring guide, which [CONTRIBUTING.md](./CONTRIBUTING.md) introduces
- [`data/`](./data/): structured data, such as runtime versions, Kubernetes versions, and glossary terms
- [`layouts/`](./layouts/): Hugo templates and shortcodes, including the Markdown and `llms.txt` outputs
- [`scripts/`](./scripts/): maintenance scripts, such as the CLI reference generator and the offline internal link checker
- [`static/`](./static/): images, fonts, and the favicon

## Local development

### Requirements

Install the following tools before building the site:

- [Git](https://git-scm.com/downloads)
- [Mise](https://mise.jdx.dev/getting-started.html)

Mise installs the commitlint, Go, Hugo Extended, markdownlint-cli2, Node.js, and Vale versions declared in [`mise.toml`](./mise.toml), which both the local build and the [checks of a change](./CONTRIBUTING.md#check-your-change) use.

### Preview the site

Clone the repository and start Hugo's development server:

```bash
git clone https://github.com/CleverCloud/documentation.git
cd documentation
mise install
hugo server
```

The site is available at <http://localhost:1313> and refreshes when a file changes. See the [`hugo server` documentation](https://gohugo.io/commands/hugo_server/) for its options.

## Deploy on Clever Cloud

The site uses the Clever Cloud `static` runtime with the following environment variables:

```bash
CC_DISABLE_MISE="true"
CC_WEBROOT="public"
CC_STATIC_AUTOBUILD_OUTDIR="public/developers"
SERVER_ERROR_PAGE_404="developers/404.html"
```

`CC_DISABLE_MISE` stops Clever Cloud from installing the development tools because the static runtime manages its deployment tools. Configure the route so its path ends in `/developers`, which matches the base URL and output directory of the site.

> [!TIP]
> Set `CC_HUGO_VERSION` to a supported version such as `0.167` to select the Hugo version used for deployment

## Contribute

You can contribute by [creating an issue](https://github.com/CleverCloud/documentation/issues) or [submitting a pull request](https://github.com/CleverCloud/documentation/pulls). Before you submit a change, read the [contributing guidelines](./CONTRIBUTING.md), which explain how to check and submit it. They link to the [style guide](./contributing/style-guide.md) and the [authoring guide](./contributing/authoring.md). Coding agents also follow [AGENTS.md](./AGENTS.md).
