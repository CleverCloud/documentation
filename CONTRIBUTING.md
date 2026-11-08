# Contributing guidelines

This document explains how to propose, check, and submit a change to the Clever Cloud documentation, and how to review one. Human contributors and coding agents follow it, with the guides it links to:

| To                                                                   | Read                                                |
| -------------------------------------------------------------------- | --------------------------------------------------- |
| Set up the project and preview the site                              | [README](./README.md)                               |
| Write or rephrase content                                            | [Style guide](./contributing/style-guide.md)        |
| Add or move a page, write examples, guides, or changelog entries     | [Authoring guide](./contributing/authoring.md)      |
| Work as a coding agent                                               | [AGENTS.md](./AGENTS.md), then the guides above     |

## Propose a change

Contribute by [creating an issue](https://github.com/CleverCloud/documentation/issues) or [submitting a pull request](https://github.com/CleverCloud/documentation/pulls). Priority goes to pull requests that fix a bug or address an issue of the current milestone. Another pull request can still matter: if you think it's important, it probably is.

The structure of this documentation aims to be as clear as possible for Clever Cloud users. Submitted changes can be merged as long as they respect these three standards:

- Readers know where to go or where to click to find information
- Readers know why they're on a specific page
- The site keeps a coherent and [intuitive design](https://www.figma.com/fr/resource-library/ui-design-principles/)

Follow the established structure. To change it, open an issue first to discuss your proposal, or post it in the forum.

Keep each pull request small: the quality of a review drops as the size of the change grows. Smaller pull requests simplify the review, and increase the chances of getting constructive feedback.

## Check your change

Run these checks before you submit a change, with the tools Mise installs, as the [README](./README.md#requirements) explains. A check that passes doesn't prove everything: review the rendered pages too.

### Build the site and check the links

Run a production build, which must finish without errors, then check the internal links and anchors of the build in `public/developers/`:

```bash
hugo
scripts/check-internal-links.py
```

The script runs offline, and reports broken links, aliases that lead nowhere, and anchors a page doesn't define.

### Lint the Markdown

The repository provides [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) rules in [`.markdownlint.jsonc`](./.markdownlint.jsonc), and CLI configuration in [`.markdownlint-cli2.jsonc`](./.markdownlint-cli2.jsonc), which excludes the paths listed in [`.gitignore`](./.gitignore). Run it, and fix every issue it reports:

```bash
markdownlint-cli2 "**/*.md"
```

Every pull request runs markdownlint on all the Markdown files of the repository, and fails if it reports an issue.

### Check the editorial style

[Vale](https://vale.sh/) implements the rules of the [style guide](./contributing/style-guide.md) with the project's own `Clever` style, in [`.github/styles/Clever/`](./.github/styles/Clever/). Run it on the files you change, or on the whole repository:

```bash
vale README.md AGENTS.md CONTRIBUTING.md contributing archetypes content shared
```

Fix every Vale error and warning on your changed lines, then review each suggestion. A passive describing a state, or a word quoted as an example, can stay. The pull request workflow reports alerts on changed lines without failing, so a green check doesn't prove there are none.

### Review the rendered pages

Vale doesn't check everything. Review the structure, the order of lists, and the accuracy of commands yourself. Vale doesn't lint the GitHub issue forms in `.github/ISSUE_TEMPLATE/` either, so review their text too.

In the generated output, verify the links, references, image paths, and shortcode syntax. Inspect the changed tabs, code blocks, cards, anchors, and copyable commands in the rendered HTML: a successful build alone doesn't prove that they render correctly.

### Check the commits

Check the commits of your branch with [commitlint](https://commitlint.js.org/) before you push them. It applies the [commit conventions](#commit-messages) described below, with the rules defined in [`commitlint.config.mjs`](./commitlint.config.mjs):

```bash
commitlint --from origin/main
```

Every pull request runs commitlint on its commits once markdownlint passes, and fails if a subject breaks a rule.

## Commit messages

For content updates, use `section(page): commit message`, where section and page name the area you changed:

```text
addons(postgresql): document pg_partman support
applications(nodejs): clarify pnpm configuration
guides: add SvelteKit
```

Use `guides: add Product` when you add a deployment guide. Start the subject with a lowercase imperative verb.

Changelog entries are the exception to this rule. Use `changelog: what you announce`, naming the product and its version, or the change itself, rather than starting with a verb:

```text
changelog: Keycloak 26.7.3
changelog: MySQL 8.0.46 and 8.4.10
changelog: PostgreSQL 18 by default
changelog: images updates, 2026W34
```

Commit a changelog entry with the pages and data files it needs, so it never lands before the pages it links to.

For changes to the documentation structure, Hugo configuration or templates, deployment, CI, tooling, or dependencies, use the standard Conventional Commits format, `type(scope): commit message`:

```text
feat(hugo): add a shortcode for version tables
fix(ci): run Vale on shared content
refactor(layouts): simplify changelog rendering
chore(deps): update the Hextra theme
```

The scope follows the files you change, not the effect readers see. A change limited to `layouts/` or `assets/` is `fix(layouts)` or `feat(layouts)`, even when it alters how a documentation page renders.

Some changes span several sections, or don't belong to one page. Use these forms instead of inventing a section:

```text
refactor(structure): merge the administrate and reference pages into their hubs
fix(aliases): redirect legacy URLs still hit with 404s
fix(links): point internal links at their new destination
ai-llms: document driving Clever Cloud from an AI agent
docs(contributing): document the commit conventions
docs(style-guide): explain how to choose a callout
```

A page directly under `content/doc/` is its own section. Reserve `docs(scope)` for README, CONTRIBUTING, AGENTS.md, and the `contributing/` guides, which document the repository. Don't use `doc` as a type, a section, or a scope: in a documentation repository, it describes every commit and distinguishes none.

Keep content and structural changes in separate commits when possible, so each follows its convention. Keep the subject line, prefix included, to 100 characters at most, and put further detail in the body.

## Open a pull request

Describe a pull request or an issue briefly. Give the main lines of the change, and what reviewers need to understand and check it, such as its reason and how you verified it. Don't repeat the changes, which speak for themselves. Stay concise and factual, and verify each claim.

Accept the feedback. If reviewers ask you to make changes, make them. If you disagree, explain why, and if you aren't sure, ask for clarification. Don't nitpick on the feedback, and don't take it personally.

## Review a pull request

Review pull requests in a timely manner. A long review latency disappoints authors, causes merge conflicts in their branch, and hurts productivity and morale on both sides.

Judge the work, not the author: the same review criteria apply to every contribution. When a pull request respects these guidelines and provides updated content, don't ask for changes for their own sake. Don't ask for them either for something imperfect that isn't a big deal.

When you ask for a change, illustrate it with an example. Use GitHub's `suggestion` feature, so the author can commit it directly if they agree. Mistakes are fine: explain what's wrong, why, and how to improve it, and refer to these guidelines when a change breaks one of them.

These guidelines draw on the [Awesome Code Review](https://github.com/joho/awesome-code-review) project.
