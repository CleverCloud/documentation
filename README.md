# Clever Cloud Documentation

In this repo you will find all the content from the [Clever Cloud Doc](https://www.clever-cloud.com/doc/).

As this documentation is open for content contribution, any helpful pull-request will be merged.

## Example of Relevant Topics

1. Text of schematic content improvements
2. Grammar or orthograph improvements
3. Any revelant pieces of infos from our mail support
4. Tutorials to setup a supported technology/framework.

## Contributing Process

You can either make a [pull-request](https://github.com/CleverCloud/doc.clever-cloud.com/pulls) OR submit a content via the **Contribute** button here: https://www.clever-cloud.com/doc

## Coding style

Each page begins with a [YAML](http://www.yaml.org/) section used for metadata, and the rest of the article is written in [markdown](https://daringfireball.net/projects/markdown/syntax). Make sure to reduce inline HTML to the maximum, although it is needed for some table formatting.

### YAML section

* **title**: The title used for the search result and the `H1` of the article page.
* **shortdesc**: Used to search terms via Algolia and shows up when you're using the search.
* **tags**: The tags are used to categorize the article in sections (within Account Setup, Dashboard Setup, CLI, Apps, Addons, Developer, Billing, Support and FAQ)
* **keywords**: Used to reference the article in Algolia's index for improved search (optional).

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

## Licence

Clever Cloud Doc by Clever Cloud is licensed under a Creative Commons Attribution 4.0 International License.
Based on a work at [https://www.clever-cloud.com/doc](https://www.clever-cloud.com/doc/).

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a>