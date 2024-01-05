
<div align="center">
  <h1 align="center">Clever Cloud Documentation</h1>
  <p align="center">
This is a Hugo project with a theme called "Hextra" added a module..</p>
</div>

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

To start you can build the project with the command `hugo`. This will generate the files of the static site inside the folder called `/public/` at the root of the project.

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

## Project basic configuration and architecture

The theme used here is called [Hexa](https://imfing.github.io/hextra/).

The `hugo.sh` script will run the compilation with the right options and server the content of the public folder.

This is why the Clever Cloud application running this app needs to have a webroot serving `/public/`.

## Adding or modifying content

Follox these instructions to contibute to the doc.

### Run locally

1. Clone this repo: `git clone git@github.com:CleverCloud/documentation.git`
2. Go to the repo root `cd documentation`
3. Start the theme module: `hugo mod get github.com/imfing/hextra` (optional, but do it if you encounter an error on step 4,to update the theme)
4. Run `hugo server`

Local site is displayed on http://localhost:1313
