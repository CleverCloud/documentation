# AGENTS.md

This file provides repository-wide guidance to coding agents working on Clever Cloud documentation.

## Common Development Commands

### Hugo Site Development

- **Install development dependencies**: `mise install` - Installs the tools declared in `mise.toml`
- **Local development**: `hugo server` - Serves site at <http://localhost:1313> with live reload
- **Build for production**: `hugo` - Outputs to `public/developers/`
- **Preview drafts**: `hugo server --buildDrafts` - Include draft content in local preview
- **Update CLI reference**: `./update-cli-reference.sh` - Fetches latest clever-tools documentation

### Content Generation

- **New guide**: `hugo new content guides/<framework>.md`
- **New documentation**: `hugo new content doc/develop/<feature>.md`
- **New application runtime**: `hugo new content --kind applications doc/deploy/applications/<runtime>.md`

## Project Architecture

### Content Structure

This is a Hugo-based documentation site using the Hextra theme with the following structure:

- **`/content/`** - All documentation content:
  - `doc/` - Main technical documentation (applications, add-ons, CLI, administration)
  - `guides/` - Framework-specific tutorials and step-by-step guides
  - `changelog/` - Platform updates and feature announcements
  - `api/` - API reference documentation
  - `postmortem/` - Incident reports and analysis
- **`/shared/`** - Reusable content blocks included via `{{% content "filename" %}}` shortcode
- **`/data/`** - Structured data files:
  - `runtime_versions.yml` - Supported runtime versions and EOL status
  - `tooltips.toml` - Tooltip definitions that auto-display on hover
  - `icons.yaml`, `software_versions_shared_dedicated.yml` - Additional data
- **`/static/`** - Static assets, such as images, fonts, and the favicon
- **`/layouts/`** - Hugo templates and shortcodes for content rendering

### Content Types and Front Matter

Content uses Hugo front matter with fields such as:

- `type: docs` - Content layout type
- `weight` - Sidebar ordering (integer)
- `linkTitle` - Short title for sidebar navigation
- `description` - Search engine optimization (SEO) meta description
- `keywords` - Array of SEO keywords
- `aliases` - Redirect paths for pages that previously existed at another URL; don't add aliases to a new page
- `draft: true` - Prevents publishing; remove this field when the page is ready instead of keeping `draft: false`
- `excludeSearch: true` - Excludes from search index (recommended for changelog)

For changelog entries, also include:

- `date: YYYY-MM-DD` - Publication date
- `tags` - Array of product tags (lowercase)
- `authors` - Array with `name`, `link`, `image` fields

### Moving or Merging Content

When a page moves to another URL, or when its content is merged into another page:

- Always add the old URL to the destination page's `aliases`, so Hugo keeps serving a redirect
- Carry over every alias the removed page already declared; they must keep resolving
- Update internal links to target the new URL directly instead of relying on the redirect, especially in `shared/` blocks included by many pages
- Check each redirect in the build output before committing

### Shared Content System

- Include shared content: `{{% content "filename" %}}`
- Include shared content with shortcodes: `{{% content-raw "filename" %}}`
- Shared files shouldn't contain headings, which break the table of contents

## Quality Standards

### Content Quality Requirements

- Use second person ("you") addressing readers directly
- Prefer active voice when it tells who acts: you, Clever Cloud, the CLI. Keep a passive to describe a state, such as `is enabled`, or when the actor doesn't matter
- Use `organisation` and `organisations`, rather than `organization` and `organizations`; this isn't a general British-spelling requirement: use US spelling everywhere else, such as `behavior` and `license`
- Spell out an acronym at its first use on a page, followed by the acronym in parentheses, such as `multi-factor authentication (MFA)`, then use the acronym alone. Skip this for acronyms most readers already know, such as API, CLI, DNS, or HTTP
- Use the serial comma before the last item of a list, such as `Go, Node.js, and Python`
- Write dates as `November 12, 2026`, and spell out ordinals in text, such as `first` instead of `1st`; ISO dates such as `2026-11-12` remain fine in logs, timelines, and front matter
- Don't put spaces around an em dash or an en dash, such as `the default—Node.js 24—applies`
- Use the present tense to describe how the platform behaves, such as `the build cache applies` instead of `will apply`, `won't apply`, or `is going to apply`; changelogs and postmortems can use `will` to announce a change
- Prefer contractions, such as `don't` and `isn't`
- Write `for example`, `that is`, `and so on`, `see`, `namely`, `note`, and `versus` instead of `e.g.`, `i.e.`, `etc.`, `cf.`, `viz.`, `N.B.`, and `vs.`, and don't use exclamation points
- Write `click`, `to`, `if`, `because`, `can`, `use`, `before`, and `Kubernetes` instead of `click on`, `in order to`, `in the event that`, `due to the fact that`, `is able to`, `leverage` or `utilize`, `prior to`, and `k8s`. Write `lets you deploy`, not `allows to deploy`, and use `set up`, `log in`, and `back up` as verbs, `setup`, `login`, and `backup` as nouns
- Don't hyphenate an adverb ending in `-ly`, such as `highly available`. Hyphenate a compound adjective before a noun, such as `long-term support` or `open-source project`; leave `up to date`, `open source`, `end of life`, and `step by step` open when they end the clause after a verb, such as `the image is up to date`
- Use the ellipsis character `…`, and one space between sentences
- Keep it short: keep a sentence under 25 words when possible; Vale suggests splitting longer ones
- Provide concrete examples with real commands and configurations
- Explain prerequisites and non-obvious behavior, while keeping the main task path concise

### Prohibited Elements

- First-person pronouns: I, me, my, we, us, our, let's; changelog entries are the only exception and can use `we`, `us`, and `our` to speak for Clever Cloud, never `I`, `me`, or `my`
- Placeholder phrases: `please`, `note that`, `at this time`, `it should be noted`, `keep in mind`, `be aware that`, `feel free to`, `don't hesitate to`, `as mentioned`, `it's important to note`, `it's worth noting`, `basically`, `actually`
- Overconfident claims: `simply`, `just`, `easy`, `easily`, `quickly`, `obviously`, `of course`, `as simple as`, `it's that simple`, `straightforward`, `seamless`, `effortless`, `trivial`, `with ease`
- Time-dependent promises: `soon`, `currently`, `for now`, `not yet`, `today`, `recently`, `upcoming`, `in the future`, `coming next month`; this doesn't apply to changelog entries, which can announce commitments such as how long a version stays available

### Markdown and Editorial Standards

- **Markdown linting**: Run `markdownlint-cli2 "**/*.md"` with the configuration in `.markdownlint.jsonc`
- **Editorial checks**: Run Vale with `vale <files>` for style and terminology. Before considering the work done, fix every error and warning on the lines you change and review each suggestion. A passive that describes a state or a word quoted as an example can stay. Vale doesn't check structure, list order, command accuracy, or the GitHub issue forms in `.github/ISSUE_TEMPLATE/`: review them yourself
- **Terminology**: Write `add-on`, `email`, `feedback`, `plugin`, `URL`, and `WebSocket`. `.github/styles/config/vocabularies/Doc/reject.txt` lists the rejected forms, matched case-sensitively. `accept.txt` lists the product names and terms that the spell check accepts; it ignores their case, so check capitalization yourself
- **Build verification**: Always test with `hugo` before committing
- **Structure**: Use 2-4 well-developed paragraphs per section, minimize bullet lists
- **Paragraphs**: Keep a paragraph to four or five lines, about 80 words, unless the content strictly needs more; Vale suggests splitting paragraphs over 100 words

### Callouts

- Prefer GitHub-style callouts with a concise title on the marker line, as supported by the theme:

  ```markdown
  > [!NOTE] Current behavior
  > This information helps readers understand the current behavior

  > [!WARNING] Back up your data
  > Back up your application database before upgrading
  ```

- Use the Hugo `{{< callout >}}` shortcode only when GitHub-style syntax can't provide the required rendering or behavior
- Limit callouts to one or two per page

### Commit Messages

- For content updates, use `section(page): commit message`, for example:
  - `addons(postgresql): document pg_partman support`
  - `applications(nodejs): clarify pnpm configuration`
  - `guides: add SvelteKit` for a new deployment guide
- For changelog entries, use `changelog: what you announce`. Name the product and its version, or the change itself, instead of starting with a verb:
  - `changelog: Keycloak 26.7.3`
  - `changelog: MySQL 8.0.46 and 8.4.10`
  - `changelog: PostgreSQL 18 by default`
  - `changelog: images updates, 2026W34`
- Commit a changelog entry with the documentation pages and data files it relies on, so an announcement never lands before the pages it links to
- For documentation structure, Hugo, deployment, CI, tooling, or dependency changes, use standard Conventional Commits, for example:
  - `feat(hugo): add a shortcode for version tables`
  - `fix(ci): run Vale on shared content`
  - `refactor(layouts): simplify changelog rendering`
  - `chore(deps): update the Hextra theme`
- The scope follows the files you change, not the effect readers see: a change limited to `layouts/` or `assets/` is `fix(layouts)` or `feat(layouts)`
- For changes spanning several sections or not tied to one page, use these forms instead of inventing a section:
  - `refactor(structure): merge the administrate and reference pages into their hubs`
  - `fix(aliases): redirect legacy URLs still hit with 404s`
  - `fix(links): point internal links at their new destination`
  - `ai-llms: document driving Clever Cloud from an AI agent` for a page stored directly under `content/doc/`, which is its own section
- Reserve `docs(scope)` for README, CONTRIBUTING, and AGENTS.md; never use `doc` as a type or a section
- Split content and structural changes into separate commits when possible
- Start the subject with a lowercase imperative verb, except for changelog entries

### Code and Technical Examples

- Always provide complete, runnable code examples
- Keep commands literally copyable: don't put shell-invalid placeholders or bracketed optional arguments in executable code blocks
- Show optional flags in separate examples or explain where to add them
- Use exact environment variable names, such as `CC_WEBROOT` and `CC_NODE_BUILD_TOOL`
- Include setup context and expected output when helpful
- Use realistic names instead of `foo`, `bar`, `example`
- Show complete command sequences in changelog entries
- Add code comments only when they explain non-obvious behavior
- Don't add a full stop to a short standalone line made of one simple sentence, especially a single-line code comment, label, or concise list item. Use normal terminal punctuation for developed or multi-sentence prose, including list items.
- Don't hard-wrap prose with formatting-only line breaks that don't affect rendering; keep each paragraph on one logical line and rely on editor word wrap.
- Sort lists and tables alphabetically unless a functional or chronological order is more useful

### Deployment Guides

- Prefer one clear path that uses platform defaults and native features
- Follow every documented command from a fresh project and test every behavior the guide promises
- Verify the default build and run configuration before documenting any scaling override
- Omit `-a` when the current directory is linked to only one application; use an application alias to disambiguate or link resources
- Follow the option style used by recent guides, including short Clever Tools options where established
- Place the standard `clever domain` and custom-domain example immediately after application creation
- Use `openssl rand -base64 32` when a guide needs a portable password-generation example and OpenSSL is already a prerequisite
- Make sure captured command output doesn't expose credentials, tokens, add-on environment values, or unrelated account data
- Validate public-storage claims with an unauthenticated request and persistence claims after a restart or rebuild
- Inspect generated HTML for tabs, code blocks, cards, links, and copyable commands; a successful Hugo build alone doesn't validate rendering
- Give `title` a descriptive, SEO-oriented value without repeating "Clever Cloud"; keep `linkTitle` short, usually the product name

## Deployment Configuration

The site is configured for Clever Cloud hosting with the `static` runtime and these required environment variables:

- `CC_DISABLE_MISE="true"`
- `CC_WEBROOT="public"`
- `CC_STATIC_AUTOBUILD_OUTDIR="public/developers"`
- `SERVER_ERROR_PAGE_404="developers/404.html"`
- Optional: `CC_HUGO_VERSION="0.167"` to specify Hugo version (example value)

`CC_DISABLE_MISE` prevents Clever Cloud from installing the local development dependencies because the platform manages the deployment tools directly.

## Data Management

Runtime versions and software compatibility information is maintained in `/data/runtime_versions.yml` and should be kept current with platform capabilities. The site generates various output formats including standard HTML and a special output format for large language models at `/llms.txt` for AI consumption.

## Hugo Shortcodes and Features

### Content Shortcodes

- `{{% content "filename" %}}` - Include shared content from `/shared/` directory
- `{{% content-raw "filename" %}}` - Include shared content containing shortcodes
- `{{% steps %}}` - Create step-by-step instructions for guides
- `{{< tabs >}}` with named `{{< tab name="npm" >}}` children - Create tabbed content sections
- `{{< cards >}}` - Display card layouts for related resources
- `{{< callout >}}` - Create a callout only when GitHub-style syntax isn't sufficient
- `{{< hextra/hero-subtitle >}}` - Add engaging subtitles in guides

### Hugo Content Types

- **Documentation pages**: Use `type: docs` in front matter
- **Guides**: Use step-by-step structure, hero subtitles, and cards when they improve the guide
- **Changelog entries**: Include date, tags, and author information
- **API documentation**: Structured reference content

### Hextra Theme Features

- **Search**: Full-text search using FlexSearch
- **Dark mode**: Automatic theme switching
- **Responsive navigation**: Sidebar and mobile-friendly menus
- **Edit links**: Direct GitHub editing integration
- **Syntax highlighting**: Code block highlighting with copy functionality

## File Standards

All text files must end with a newline.
