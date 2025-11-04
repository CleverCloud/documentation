# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. Additional AI guidance is available in `.github/copilot-instructions.md` for comprehensive content creation rules.

## Common Development Commands

### Hugo Site Development
- **Local development**: `hugo server` - Serves site at http://localhost:1313 with live reload
- **Build for production**: `hugo` - Outputs to `public/developers/`
- **Preview drafts**: `hugo server --buildDrafts` - Include draft content in local preview
- **Update CLI reference**: `./update-cli-reference.sh` - Fetches latest clever-tools documentation

### Content Generation
- **New guide**: `hugo new content guides/<framework>.md`
- **New documentation**: `hugo new content/doc/administrate/<feature>.md`
- **New application runtime**: `hugo new content --kind applications doc/applications/<runtime>.md`

## Project Architecture

### Content Organization
This is a Hugo-based documentation site using the Hextra theme with the following structure:

- **`/content/`** - All documentation content:
  - `doc/` - Main technical documentation (applications, addons, CLI, administration)
  - `guides/` - Framework-specific tutorials and step-by-step guides
  - `changelog/` - Platform updates and feature announcements
  - `api/` - API reference documentation
  - `postmortem/` - Incident reports and analysis
- **`/shared/`** - Reusable content blocks included via `{{% content "filename" %}}` shortcode
- **`/data/`** - Structured data files:
  - `runtime_versions.yml` - Supported runtime versions and EOL status
  - `tooltips.toml` - Tooltip definitions that auto-display on hover
  - `icons.yaml`, `software_versions_shared_dedicated.yml` - Additional data
- **`/static/`** - Static assets (images, fonts, favicon, etc.)
- **`/layouts/`** - Hugo templates and shortcodes for content rendering

### Content Types and Front Matter
All content uses Hugo front matter with specific fields:
- `type: docs` - Content layout type
- `weight` - Sidebar ordering (integer)
- `linkTitle` - Short title for sidebar navigation
- `description` - SEO meta description
- `keywords` - Array of SEO keywords
- `aliases` - Array of redirect paths (relative to base URL)
- `draft: true` - Prevents publishing (change to `false` to publish)
- `excludeSearch: true` - Excludes from search index (recommended for changelog)

For changelog entries, also include:
- `date: YYYY-MM-DD` - Publication date
- `tags` - Array of product tags (lowercase)
- `authors` - Array with `name`, `link`, `image` fields

### Shared Content System
- Include shared content: `{{% content "filename" %}}`
- Include shared content with shortcodes: `{{% content-raw "filename" %}}`
- Shared files should not contain headings (breaks ToC generation)

## Quality Standards

### Content Quality Requirements
- Use second person ("you") addressing readers directly
- Write in active voice, avoid passive constructions
- Use British spelling: "organisation" not "organization"
- Keep sentences under 25 words when possible
- Provide concrete examples with real commands and configurations
- Over-explain rather than under-explain technical concepts

### Prohibited Elements
- First-person pronouns: I, me, my, we, us, our, let's
- Placeholder phrases: "please note", "at this time", "it should be noted"
- Overconfident claims: "simply", "just", "easily", "quickly", "obviously"
- Time-dependent promises: "soon", "in the future", "coming next month"

### Markdown and Editorial Standards
- **Markdown linting**: Uses markdownlint-cli2 with config in `.markdownlint.jsonc`
- **Editorial checks**: Uses Vale.sh for style and terminology
- **Build verification**: Always test with `hugo` command before committing
- **Structure**: Use 2-4 well-developed paragraphs per section, minimize bullet lists
- **Paragraphs**: Aim for 3-6 lines for optimal readability

### Code and Technical Examples
- Always provide complete, runnable code examples
- Use exact environment variable names: `CC_WEBROOT`, `CC_NODE_BUILD_TOOL`, etc.
- Include setup context and expected output when helpful
- Use realistic names instead of "foo", "bar", "example"
- Show complete command sequences in changelog entries

## Deployment Configuration
The site is configured for Clever Cloud hosting with the `static` runtime and these required environment variables:
- `CC_WEBROOT="public"`
- `CC_STATIC_AUTOBUILD_OUTDIR="public/developers"`
- `SERVER_ERROR_PAGE_404="developers/404.html"`
- Optional: `CC_HUGO_VERSION="0.152"` to specify Hugo version (example value)

## Data Management
Runtime versions and software compatibility information is maintained in `/data/runtime_versions.yml` and should be kept current with platform capabilities. The site generates various output formats including standard HTML and a special LLMS output format at `/llms.txt` for AI consumption.

## Hugo Shortcodes and Features

### Content Shortcodes
- `{{% content "filename" %}}` - Include shared content from `/shared/` directory
- `{{% content-raw "filename" %}}` - Include shared content containing shortcodes
- `{{% steps %}}` - Create step-by-step instructions for guides
- `{{< tabs items="npm,yarn,pnpm" >}}` - Create tabbed content sections
- `{{< cards >}}` - Display card layouts for related resources
- `{{< callout >}}` - Create note, tip, warning callouts
- `{{< hextra/hero-subtitle >}}` - Add engaging subtitles in guides

### Hugo Content Types
- **Documentation pages**: Use `type: docs` in front matter
- **Guides**: Use step-by-step structure with hero subtitles and cards
- **Changelog entries**: Include date, tags, and author information
- **API documentation**: Structured reference content

### Hextra Theme Features
- **Search**: Full-text search using FlexSearch
- **Dark mode**: Automatic theme switching
- **Responsive navigation**: Sidebar and mobile-friendly menus
- **Edit links**: Direct GitHub editing integration
- **Syntax highlighting**: Code block highlighting with copy functionality

## File Standards
All files must end with a single blank line to comply with git standards and POSIX requirements.
