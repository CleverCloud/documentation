
# Clever Cloud Documentation

This is a Hugo project with a theme called "Hextra" added a module..</p>

## See deployed Documentation

- [Developers Hub](https://developers.clever-cloud.com/)
- [Developers Documentation](https://developers.clever-cloud.com/doc/)
- [Reference Environnement Variables](https://developers.clever-cloud.com/doc/reference/reference-environment-variables/)
- [Guides and Tutorials](https://developers.clever-cloud.com/guides/)

## Features

- **Beautiful Design** - Inspired by Nextra, Hextra utilizes Tailwind CSS to offer a modern design that makes your site look outstanding.
- **Responsive Layout and Dark Mode** - It looks great on all devices, from mobile, tablet to desktop. Dark mode is also supported to accomodate various lighting conditions.
- **Fast and Lightweight** - Powered by Hugo, a lightning-fast static-site generator housed in a single binary file, Hextra keeps its footprint minimal. No Javascript or Node.js are needed to use it.
- **Full-text Search** - Built-in offline full-text search powered by FlexSearch, no additional configuration required.
- **Battery-included** - Markdown, syntax highlighting, LaTeX math formulae, diagrams and Shortcodes elements to enhance your content. Table of contents, breadcumbs, pagination, sidebar navigation and more are all automatically generated.
- **Multi-language and SEO Ready** - Multi-language sites made easy with Hugo's multilingual mode. Out-of-the-box support is included for SEO tags, Open Graph, and Twitter Cards.

## Quickstart

### Clone this repo

To begin your journey with the Clever Cloud Documentation, you need to clone this repo.

Check your Go version, it need to be above go `1.21.1`.

### Start locally

To run the site in your browser, there is a server built in Hugo you can summon with:  
`hugo server`  
A bunch of option a available:

```bash
 -b, --baseURL string         hostname and path to the root
  -D, --buildDrafts            include content marked as draft
      --cacheDir string        filesystem path to cache directory
      --cleanDestinationDir    remove files from destination not found in static directories
  -c, --contentDir string      filesystem path to content directory
      --disableFastRender      enables full re-renders on changes
```

Hugo refreshes the site as you modify the files, you can keep the server running with no need to restart.

There is no need to build before submitting your Pull Request or before deploying.

## Project basic configuration and architecture

The theme used here is called [Hexa](https://imfing.github.io/hextra/).

The `hugo.sh` script runs the compilation with the right options and server the content of the public folder.

This is why the Clever Cloud application running this app needs to have a webroot serving `/public/`.

## Adding or modifying content

Follow these instructions to contribute to the doc.

### Run locally

1. Clone this repo: `git clone git@github.com:CleverCloud/documentation.git`
2. Go to the repo root `cd documentation`
3. Start the theme module: `hugo mod get github.com/imfing/hextra` (optional, but do it if you encounter an error on step 4,to update the theme)
4. Run `hugo server`

Local site is displayed on <http://localhost:1313>

### Linting Markdown

Hugo uses [Goldmak](https://github.com/yuin/goldmark), a Markdown parser written in Go, compliant with CommonMark 0.30(see [the specification here](https://spec.commonmark.org/)).

Therefore, for better readability and maintaining, all markdown files for this project are linted with <https://github.com/DavidAnson/markdownlint-cli2>.  
We strongly recommend that you follow the validation rules described here: <https://github.com/DavidAnson/markdownlint#rules--aliases>.

This linter can be downloaded and run locally, or used via VSCode:

- <https://github.com/DavidAnson/vscode-markdownlint> for VSCode
- <https://github.com/DavidAnson/markdownlint-cli2> as a NPM package

#### Linting configuration

**Ignored markdown files** are listed in the `.markdownlintignore`.  
**Ignored specifications**, such as some HTML tag of Web Components, are configured in the `.markdownlint.jsonc`
**Editorial checks** with [Vale.sh](https://vale.sh). Install Vale on your machine or as a VSCode extension if you want to run checks before submitting your PR. This project is already configured to use it.

## Adding a new Guide

Run `hugo new content guides/<framework>.md`. Hugo generates a new file from a guide template (stored in `/archetypes`).

In this new guide file's metadata, set `draft: true` to publish it.

## Adding changelog entries *(internal only)*

For any significant change to the platform (updates, new features, etc.) a new entry is created in the "content/changelog" folder.

Several entries can be made per day, it's not a problem.

Each entry should provides clear, straightforward information on the essentials. If you find yourself writing an enormous amount of content, this may not be the right approach. However, you can always add a little charm to your changelog, but it's a tricky business, requiring careful, well-placed word choice.

Whenever possible, the famous "Bugs fixes and improvements" should be avoided.

### Filename convention for new entries

The filename is not very important for the Hugo build and publication process, but it will serve as a slug for the URL. Ideally, it can start with the date in **ISO 8601** format and the title in Kebab case. This naming convention allow the files to be sorted easily in any editor.

The format is a markdown file with a `.md` extention:

```text
yyyy-mm-dd-your-title.md
```

### Front matter configuration

Hugo uses front matter to enrich posts with metadata. Front matter allows you to keep metadata attached to an instance of a content type—i.e., embedded inside a content file. We use the following Front matter variables:

- [`title`](https://gohugo.io/methods/page/title/) (required)
  - The title that will be displayed in the main heading. The value is a `<string>`.

- [`date`](https://gohugo.io/methods/page/description/) (recommended)
  - The date that will be displayed in the post. The value is a string in ISO 8601 like `yyyy-mm-dd`.

- [`description`](https://gohugo.io/methods/page/description/) (recommended)
  - The description that will be displayed in meta-description for SEO purposes. The value is a `<string>`.

- [`tags`](https://gohugo.io/content-management/taxonomies/#default-taxonomies) (recommended)
  - Tags are recommended for easy product identification. They are written in lowercase and, if possible, use the same spelling throughout the posts. The value is a `<string>`.

- [`category`](https://gohugo.io/content-management/taxonomies/#default-taxonomies) (optional)
  - The category is used here to add a "new" label on the changelog homepage when a specific entry is a new feature that should be highlighted visually. The value must be `new`, and nothing else.

- [`authors`](https://gohugo.io/content-management/taxonomies/#default-taxonomies) (optional)
  - Can be set to showcase the people behind the product. Authors are defined with a `name`, `link` for their Github or any other social network, and an `image` for the profile picture. The profile picture can be set with the Github avatar with a link like `https://github.com/BlackYoup.png` and a the parameter `?size=40` for reducing the image size (recommended for performance). The values are all of `<string>` type.

- [`excludeSearch`](https://imfing.github.io/hextra/docs/guide/configuration/#search-index) (recommended)
  - Indicates whether the changelog will be indexed in search. It can be activated for a post if deemed necessary. The values to be set are either `true` or `false`

```yaml
---
title: Redis updated to v7.2.4
date: 2024-01-11
tags:
  - redis
authors:
  - name: BlackYoup
    link: https://github.com/BlackYoup
    image: https://github.com/BlackYoup.png?size=40
excludeSearch: true
description: Redis has been updated to v7.2.4 mostly to prevent security issues.
---
```

### Adding images and screenshots

Adding an image can be useful for highlighting a change of interface, for example.
You can achieve this by using a shortcode, which is a simple snippet inside the content files, calling a built-in or custom templates.
The shortcode we are using here is `figure`, as show below. Then move your image in the `/images/changelog/your-image.jpg` folder of this project.

The image size can be modified and adapted using the `width` and `height` parameters.

Example :

```go
{{< figure src="/images/changelog/console-new-ip-par.png" caption="The new IP shown in the console" width="800px">}}
```
