
<div align="center">
  <h1 align="center">Clever Cloud Documentation</h1>
  <p align="center">

This is a Hugo project with a theme called "Hextra" added as a module.</p>
</div>

## See deployed Documentation

- [Developers Hub](https://developers.clever-cloud.com/)
- [Developers Documentation](https://developers.clever-cloud.com/doc/)
- [Reference Environnement Variables](https://developers.clever-cloud.com/doc/reference/reference-environment-variables/)
- [Guides and Tutorials](https://developers.clever-cloud.com/guides/)

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

The theme used here is called [Hextra](https://imfing.github.io/hextra/).

The `clevercloud-deploy-script.sh` script will run the compilation with the right options and server the content of the public folder.

This is why the Clever Cloud application running this app needs to have a webroot serving `/public/`.

## Adding or modifying content

Follow these instructions to contibute to the doc.

### Run locally

1. Clone this repo: `git clone git@github.com:CleverCloud/documentation.git`
2. Go to the repo root `cd documentation`
3. Start the theme module: `hugo mod get github.com/imfing/hextra` (optional, but do it if you encounter an error on step 4, to update the theme)
4. Run `hugo server`

Local site is displayed on http://localhost:1313

All pages are in `/content` directory, backuped as a Hugo module. You don't need to commit anything in this folder, it's automatically updated when you commit at the root of this project.

## Example of Relevant Topics

1. Text of schematic content improvements
2. Grammar or orthograph improvements
3. Any revelant pieces of infos from our mail support
4. Tutorials to setup a supported technology/framework.

## Contributing Process

You can either make a [pull-request](https://github.com/CleverCloud/doc.clever-cloud.com/pulls) OR submit a content via the **Contribute** button here: https://www.clever-cloud.com/doc

## Coding style

Each page begins with a [YAML](http://www.yaml.org/) section used for metadata, and the rest of the article is written in [markdown](https://daringfireball.net/projects/markdown/syntax). Make sure to reduce inline HTML to the maximum, although it is needed for some table formatting.

### Automatically create a new page

You can manuelly create a new page or use Hugo CLI to save time and create it from the template in `/archetypes`.

- Run `hugo new content doc/<folder_name>/<title>.md` to create a new **Documentation** page
- Run `hugo new content guides/<folder_name>/<title>.md` to create a new **Guide**. 

### YAML section

- **title**: The title used for the search result and the `H1` of the article page.
- **Description**: Used to search terms via search bar and better indexing on search engines.
- **tags**: The tags are used to categorize the article in sections (within Account Setup, Dashboard Setup, CLI, Apps, Addons, Developer, Billing, Support and FAQ)

### Article section

The first header in your content should be a `H2`, as the `H1` will be used by the `title` variable in the YAML section.

You can add an optional language identifier to enable syntax highlighting in your fenced code block.
For example, to syntax highlight Ruby code:

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

We use highlightjs to perform language detection and syntax highlighting. You can find out which keywords are valid [here](https://highlightjs.org/static/demo/).


### Write and use partials

Partials are located under the `partial` folder at the root of this project. They are written in Markdown.

#### Rendering partial in page

Partials are called using the following shortcode: 
```
{{< readfile "/path/to/partial/from/root/of/project.md" >}}
```

#### Using variables in a partial

You may want to display different chunks of partial content depending on which page you are working on.
This is achieved by creating two things:

1. a placeholder word to replace in the partial content.
This placeholder word must:
- begin and finish with an `@`
- be the most self-explanatory possible
- be used only once in this partial unless specific case (see note below)
- not be used in other partials unless you want to replace it with the exact same value
Example placeholder word: `@addon-name@`

2. creating the key `str_replace_dict` in the front matter section and add to it the matching placeholder word and their replacements.
You must add this in the front matter of *each* page using the partial.
e.g: 
```
str_replace_dict:
  "@addon-name@": "my addon name"
  "@another-variable@": "other variable replacement str"
```

Notes:
- the function used to find and replace uses [regex](https://regex-golang.appspot.com/assets/html/index.html), please make sure not to use reserved characters. If you have to use some, think about it twice and if you still need them, escape them properly.
- the function will only replace the first occurence it founds, if you have to replace two times the same key, have it appear twice in the front matter `str_replace_dict` also.

e.g:
```
partial/mypartial.md

Text @addon-name@ holding two codes @addon-name@.
```

```
folder/file.md

---
...
str_replace_dict:
  "@addon-name@": "PostgreSQL"
  "@addon-name@": "PostgreSQL"
---
```

Output: `Text PostgreSQL holding two codes PostgreSQL.`

## Licence

Clever Cloud Doc by Clever Cloud is licensed under a Creative Commons Attribution 4.0 International License.
Based on a work at [https://developers.clever-cloud.com](https://developers.clever-cloud.com).

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a>