# AGENTS.md

This file provides repository-wide guidance to coding agents working on Clever Cloud documentation. Task-specific deployment-guide workflows live in `.agents/skills/`.

## Common Development Commands

### Hugo Site Development

- **Install development dependencies**: `mise install` - Installs the tools declared in `mise.toml`
- **Local development**: `hugo server` - Serves site at <http://localhost:1313> with live reload
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

Content uses Hugo front matter with fields such as:

- `type: docs` - Content layout type
- `weight` - Sidebar ordering (integer)
- `linkTitle` - Short title for sidebar navigation
- `description` - SEO meta description
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
- Shared files should not contain headings (breaks ToC generation)

## Quality Standards

### Content Quality Requirements

- Use second person ("you") addressing readers directly
- Write in active voice, avoid passive constructions
- Use `organisation` and `organisations`, rather than `organization` and `organizations`; this isn't a general British-spelling requirement
- Keep sentences under 25 words when possible
- Provide concrete examples with real commands and configurations
- Explain prerequisites and non-obvious behaviour, while keeping the main task path concise

### Prohibited Elements

- First-person pronouns: I, me, my, we, us, our, let's
- Placeholder phrases: "please note", "at this time", "it should be noted"
- Overconfident claims: "simply", "just", "easily", "quickly", "obviously"
- Time-dependent promises: "soon", "in the future", "coming next month"

### Markdown and Editorial Standards

- **Markdown linting**: Run `markdownlint-cli2 "**/*.md"` with config in `.markdownlint.jsonc`
- **Editorial checks**: Run Vale with `vale <files>` for style and terminology
- **Build verification**: Always test with `hugo` before committing
- **Structure**: Use 2-4 well-developed paragraphs per section, minimize bullet lists
- **Paragraphs**: Aim for 3-6 lines for optimal readability

### Callouts

- Prefer GitHub-style callouts with a concise title on the marker line, as supported by the theme:

  ```markdown
  > [!NOTE] Current behaviour
  > This information helps readers understand the current behaviour

  > [!WARNING] Back up your data
  > Back up your application database before upgrading
  ```

- Use the Hugo `{{< callout >}}` shortcode only when GitHub-style syntax can't provide the required rendering or behaviour
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
- Split content and structural changes into separate commits when possible
- Start the subject with a lowercase imperative verb, except for changelog entries

### Code and Technical Examples

- Always provide complete, runnable code examples
- Keep commands literally copyable: don't put shell-invalid placeholders or bracketed optional arguments in executable code blocks
- Show optional flags in separate examples or explain where to add them
- Use exact environment variable names: `CC_WEBROOT`, `CC_NODE_BUILD_TOOL`, etc.
- Include setup context and expected output when helpful
- Use realistic names instead of "foo", "bar", "example"
- Show complete command sequences in changelog entries
- Add code comments only when they explain non-obvious behaviour
- Don't add a full stop to a short standalone line made of one simple sentence, especially a single-line code comment, label, or concise list item. Use normal terminal punctuation for developed or multi-sentence prose, including list items.
- Don't hard-wrap prose with formatting-only line breaks that don't affect rendering; keep each paragraph on one logical line and rely on editor word wrap.
- Sort lists and tables alphabetically unless a functional or chronological order is more useful

### Deployment Guides

- Prefer one clear path that uses platform defaults and native features
- Follow every documented command from a fresh project and test every behaviour the guide promises
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
- Optional: `CC_HUGO_VERSION="0.164"` to specify Hugo version (example value)

`CC_DISABLE_MISE` prevents Clever Cloud from installing the local development dependencies because the platform manages the deployment tools directly.

## Data Management

Runtime versions and software compatibility information is maintained in `/data/runtime_versions.yml` and should be kept current with platform capabilities. The site generates various output formats including standard HTML and a special LLMS output format at `/llms.txt` for AI consumption.

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
