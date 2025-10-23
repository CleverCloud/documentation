# AI Content Creation Rules for Clever Cloud Documentation

This document provides comprehensive guidance for AI systems on creating high-quality content for Clever Cloud's documentation platform, including technical documentation, guides, and changelog entries.

## Development Environment

This is a Hugo-based documentation site using the Hextra theme.

### Hugo Development Commands
- **Build and serve locally**: `hugo server` (site available at http://localhost:1313)
- **Build for production**: `hugo` (outputs to `public/developers/`)
- **Preview with drafts**: `hugo server --buildDrafts`
- **Generate new content**:
  - `hugo new content guides/<framework>.md`
  - `hugo new content/doc/administrate/<feature>.md`
  - `hugo new content --kind applications doc/applications/<runtime>.md`
- **Update CLI reference**: `./update-cli-reference.sh`

### Project Structure
- **Content organization**: `/content/` contains all documentation:
  - `doc/` - Main documentation (applications, addons, CLI, etc.)
  - `guides/` - Framework-specific tutorials and guides
  - `changelog/` - Platform updates and announcements
  - `api/` - API documentation
  - `postmortem/` - Incident reports
- **Shared content**: `/shared/` contains reusable content blocks
- **Data files**: `/data/` contains structured data (runtime versions, tooltips, etc.)
- **Static assets**: `/static/` for images, fonts, and other assets

### Content Management System
- Uses Hugo front matter with fields: `type`, `weight`, `linkTitle`, `description`, `excludeSearch`, `aliases`, `draft`, `tags`, `authors`
- New pages have `draft: true` by default - change to `false` to publish
- Tooltips defined in `data/tooltips.toml` and auto-display on hover
- **Quality enforcement**:
  - Markdown linting via markdownlint-cli2 (config: `.markdownlintignore`, `.markdownlint.jsonc`)
  - Editorial checks via Vale.sh (config: `.vale.ini`)
  - Vocabulary in `.github/styles/config/vocabularies/Doc/accept.txt`

## Content Types Overview

### 1. Technical Documentation (`/content/doc/`)
Formal reference material for platform features, APIs, and configurations.
- **Style**: Professional, precise, instructional
- **Structure**: Hierarchical with clear sections
- **Purpose**: Enable users to accomplish specific tasks

### 2. Guides & Tutorials (`/content/guides/`)
Step-by-step instructions for implementing specific technologies or frameworks.
- **Style**: Educational, conversational but focused
- **Structure**: Progressive steps with examples
- **Purpose**: Guide users through complete implementation

### 3. Changelog Entries (`/content/changelog/`)
Technical blog-style posts announcing platform updates and new features.
- **Style**: Engaging, informative, personality allowed
- **Structure**: Context → announcement → practical examples → links
- **Purpose**: Inform users about platform evolution

## Writing Style Guidelines

### Universal Rules (All Content Types)

#### Language Standards
- Use **second person** ("you") to address readers directly
- Write in **active voice** - avoid passive constructions
- Use **British spelling** for "organisation" not "organization"
- **Avoid first-person pronouns**: I, me, my, we, us, our, let's
- Keep sentences **short and clear** (max 25 words when possible)
- **No jargon** - explain technical terms when first introduced

#### Prohibited Phrases
- Placeholder phrases: "please note", "at this time", "it should be noted"
- Overconfident claims: "simply", "just", "easily", "quickly", "obviously"
- Time-dependent promises: "soon", "in the future", "coming next month"
- Over-politeness: excessive use of "please"

#### Required Elements
- **Don't assume prior knowledge** - over-explain rather than under-explain
- Address the reader's **specific use case** and context
- Provide **concrete examples** with real commands, code, or configurations
- Include **relevant links** to related documentation

### Documentation-Specific Rules

#### Structure Requirements
```yaml
---
type: docs
linkTitle: Short Title
title: Full Page Title
description: SEO-friendly description explaining what users will learn
aliases:
- /old/url/path
---
```

#### Content Organization
- **Overview section** - Brief explanation of what the technology/feature is
- **Create/Setup section** - How to get started
- **Configure section** - Detailed configuration options
- **Advanced features** - Optional capabilities
- **Examples and references** - Practical implementations

#### Technical Specifications
- Always specify **current versions** of software/tools
- Include **environment variables** with exact names and examples
- Provide **command-line examples** with proper syntax
- Use **callouts for important information**:
  ```markdown
  > [!NOTE] Context about new features
  > [!TIP] Helpful suggestions
  > [!WARNING] Important considerations
  ```

### Guide-Specific Rules

#### Engaging Introduction
- Start with **hero subtitle shortcode** explaining the framework/tool benefits
- Use **hextra shortcodes** for enhanced presentation:
  ```markdown
  {{< hextra/hero-subtitle >}}
    Brief engaging description of what users will build
  {{< /hextra/hero-subtitle >}}
  ```

#### Step-by-Step Structure
- Use **steps shortcode** for sequential instructions:
  ```markdown
  {{% steps %}}
  ### Step Title
  Content and commands
  {{% /steps %}}
  ```

- Include **tab groups** for different package managers/approaches:
  ```markdown
  {{< tabs items="npm,yarn,pnpm" >}}
    {{< tab >}}Content for npm{{< /tab >}}
    {{< tab >}}Content for yarn{{< /tab >}}
  {{< /tabs >}}
  ```

#### Learning Resources
- End with **cards section** linking to related documentation:
  ```markdown
  {{< cards >}}
    {{< card link="/path" title="Title" subtitle="Description" icon="icon-name" >}}
  {{< /cards >}}
  ```

### Changelog-Specific Rules

#### Front Matter Format
```yaml
---
title: Descriptive title about the update/feature
description: Brief one-line summary
date: YYYY-MM-DD
tags:
  - relevant-product-tags
authors:
  - name: Full Name
    link: https://github.com/username
    image: https://github.com/username.png?size=40
excludeSearch: true
---
```

#### Writing Style for Changelog
- **More personality allowed** - can be engaging and slightly conversational
- **Lead with impact** - explain why this matters to users
- **Provide context** - link to upstream releases, related changes
- **Include practical examples** - show users exactly how to use new features
- **Multiple entries per day acceptable** - don't batch unrelated updates

#### Content Flow Pattern
1. **Context paragraph** - What changed and why it matters
2. **Technical details** - Versions, new features, improvements
3. **Implementation examples** - Concrete commands or configuration
4. **Related links** - Documentation, examples, community resources

#### Command Examples in Changelog
Always show **complete command sequences**:
```bash
# Enable the feature
clever features enable operators

# Check current version
clever keycloak version check yourKeycloakNameOrId

# Update to latest
clever keycloak version update yourKeycloakNameOrId
```

## Technical Implementation Standards

### Code Examples
- **Always complete and runnable** - no placeholder variables without explanation
- **Include setup context** - show what directory, prerequisites needed
- **Use realistic names** - avoid "foo", "bar", "example"
- **Show expected output** when helpful

### Environment Variables
- **Exact variable names** with proper casing: `CC_NODE_BUILD_TOOL`
- **Show complete examples**:
  ```bash
  CC_WEBROOT="public"
  CC_RUN_COMMAND="npm start"
  ```
- **Explain the impact** of each variable

### File References
- **Absolute paths** when referencing project structure
- **Relative paths** when showing user actions: `./package.json`
- **Proper syntax highlighting** for code blocks

## Content Quality Checklist

### Before Publishing Documentation
- [ ] All commands tested and work as shown
- [ ] Environment variables verified with exact syntax
- [ ] Links point to correct, existing pages
- [ ] Examples use realistic project names and values
- [ ] No first-person pronouns (I, we, us, our)
- [ ] Short, clear sentences under 25 words
- [ ] Proper callouts for important information

### Before Publishing Changelog
- [ ] Clear benefit/impact stated upfront
- [ ] Version numbers and dates accurate
- [ ] Complete command examples provided
- [ ] Author information included with GitHub avatar
- [ ] Tags relevant to affected products
- [ ] Links to documentation and examples working

### Before Publishing Guides
- [ ] Step-by-step flow tested end-to-end
- [ ] All code examples complete and functional
- [ ] Prerequisites clearly stated
- [ ] Expected outcomes explained
- [ ] Hextra shortcodes used appropriately
- [ ] Learning resources section included

## Shared Content Usage

### Including Reusable Blocks
- Use `{{% content "filename" %}}` for basic shared content
- Use `{{% content-raw "filename" %}}` for content containing shortcodes
- Available shared blocks in `/shared/` directory include common procedures

### Creating New Shared Content
- Extract **commonly repeated information** into `/shared/filename.md`
- **No headings** in shared content (breaks table of contents)
- Focus on **procedural steps** rather than context

## Maintenance and Updates

### Keeping Content Current
- **Version numbers** should reflect current platform state
- **Screenshots and UI references** need regular updates
- **External links** should be verified periodically
- **Deprecated features** should be clearly marked

### Community Integration
- **Link to community discussions** for new features
- **Reference GitHub examples** when available
- **Encourage feedback** on experimental features
- **Update based on user reports** and common issues

## Deployment Configuration

The site is configured for Clever Cloud hosting with the `static` runtime and these required environment variables:
- `CC_WEBROOT="public"`
- `CC_STATIC_AUTOBUILD_OUTDIR="public/developers"`
- `SERVER_ERROR_PAGE_404="developers/404.html"`
- Optional: `CC_HUGO_VERSION="0.151"` to specify Hugo version (example value)

## Quality Assurance Requirements

### Build Verification
Always test changes with the `hugo` command before committing to ensure the build is functional. Fix any build errors immediately as they prevent deployment. Verify that all links, references, image paths, and shortcode syntax work correctly in the generated output.

### File Standards
All files must end with a single blank line to comply with git standards and POSIX requirements.

### Content Quality Standards
Minimise the use of bullet points and lists. Use them only when essential for clarity or information efficiency.
Structure each section with 2-4 well-developed paragraphs. Avoid single text blocks or overly fragmented content.
Aim for paragraphs of 3-6 lines for optimal readability. Each paragraph should contain a complete thought or concept.
Use descriptive section titles. Titles should create useful table of contents entries.
Organise information logically so each section forms a coherent, useful unit.
Ensure all necessary information is included in readable prose, not fragmented lists.

This document ensures consistent, high-quality content across all Clever Cloud documentation while respecting the different styles appropriate for technical docs, educational guides, and announcement posts.
