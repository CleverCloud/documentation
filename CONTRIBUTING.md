
# Contributing guidelines

This document provides explicit standards expected in Clever Cloud documentation. Inspiration and research for this document comes from the incredible [Awesome Code Review](https://github.com/joho/awesome-code-review) project. You'll find repository instructions for coding agents and LLMs:

- [Coding agent instructions](./AGENTS.md)

## Standards

Those are general standards to fulfill for every modification in this repository

### 🏯 Structure

The structure of this docs aims to be as clear as possible for Clever Cloud users. Submitted changes can be merged as long as they respect these standards:

- Readers know where to go or where to click to find an information
- Readers know why they're on a specific page
- The site keeps a coherent and [intuitive design](https://www.figma.com/fr/resource-library/ui-design-principles/)

Follow the established structure in this doc. If you wish to propose changes to the structure, open an issue first to discuss it, or post it in the forum.

### ✒️ Content

Follow these guidelines while writing new content. The goal is to help you write in a **clear, precise, and unambiguous language**. They're not meant to be a burden, but to help you deliver the best content possible.

#### 👍 Do

- **Don't assume prior knowledge:** explain prerequisites and non-obvious behavior without burying the main task path
- **Spell out acronyms:** at their first use on a page, write the full term followed by the acronym in parentheses, such as _multi-factor authentication (MFA)_. Then use the acronym alone. Skip this for acronyms most readers already know, such as API, CLI, DNS, or HTTP
- **Use the serial comma:** add a comma before the last item of a list, such as `Go, Node.js, and Python`
- **Write dates in the US format:** `November 12, 2026`, and spell out ordinals in text, such as `first` instead of `1st`. ISO dates such as `2026-11-12` remain fine in logs, timelines, and front matter
- **Don't space dashes:** write `the default—Node.js 24—applies`, for an em dash as for an en dash
- **Use the present tense:** describe how the platform behaves, such as `the build cache applies` instead of `will apply`, `won't apply`, or `is going to apply`. Changelogs and postmortems can use `will` to announce a change
- **Use US spelling:** write `behavior` and `license`. The only exception is `organisation`
- **Prefer contractions:** write `don't` and `isn't`
- **Avoid Latin abbreviations and exclamation points:** write `for example`, `that is`, `and so on`, `see`, `namely`, `note`, and `versus` instead of `e.g.`, `i.e.`, `etc.`, `cf.`, `viz.`, `N.B.`, and `vs.`
- **Prefer plain words:** write `click`, `to`, `if`, `because`, `can`, `use`, `before`, and `Kubernetes` instead of `click on`, `in order to`, `in the event that`, `due to the fact that`, `is able to`, `leverage` or `utilize`, `prior to`, and `k8s`. Write `lets you deploy`, not `allows to deploy`. Use `set up`, `log in`, and `back up` as verbs, `setup`, `login`, and `backup` as nouns
- **Use the project terminology:** write `add-on`, `email`, `feedback`, `plugin`, `URL`, and `WebSocket`. The Vale vocabulary in `.github/styles/config/vocabularies/Doc/` lists the accepted and rejected terms
- **Hyphenate with care:** don't hyphenate an adverb ending in `-ly`, such as `highly available`. Hyphenate a compound adjective before a noun, such as `long-term support`, and leave `up to date`, `open source`, `end of life`, and `step by step` open when they end the clause after a verb, such as `the image is up to date`
- **Mind the typography:** use the ellipsis character `…`, and one space between sentences
- **Prefer active voice:** passive voice can make it harder for the readers to figure out who's supposed to do something. A passive is fine to describe a state, such as _is enabled_, or when the actor doesn't matter
- **Use second person:** address the reader directly
- **Keep it simple:** avoid jargon, complex sentences, and jokes
- **Keep it short:** keep a sentence under 25 words when possible. Keep a paragraph to four or five lines, about 80 words, unless the content strictly needs more. Titles should be short and to the point. Keep longer content for the description metadata or the card subtitle.

#### 👎 Don't

- First-person pronouns such as _I_, _my_, _we_, _our_, or _let's_. Changelog entries are the only exception: they can use _we_, _us_, and _our_ to speak for Clever Cloud, never _I_, _me_, or _my_
- Placeholder phrases like _please note_, _note that_, _at this time_, _it should be noted_, _keep in mind_, _be aware that_, _feel free to_, _don't hesitate to_, _as mentioned_, _it's important to note_, _it's worth noting_, _basically_, or _actually_
- Words and phrases that make promises or tie the content to a moment, such as _soon_, _currently_, _for now_, _not yet_, _today_, or _in the future_: describe the current state of the platform instead. This doesn't apply to changelog entries, which can announce commitments such as how long a version stays available.
- Using phrases like _simply_, _just_, _easy_, _easily_, _obviously_, _of course_, _as simple as_, _straightforward_, _seamless_, _effortless_, _trivial_, _with ease_, _It's that simple_, _It's easy_, or _quickly_ in a procedure
- Over-politeness with the use of _please_: go straight to the point

#### 💡 Shortcodes and callouts

This doc uses Hugo with [Hextra theme](https://imfing.github.io/hextra/), which provides a variety of [shortcodes](https://imfing.github.io/hextra/docs/guide/shortcodes/) to enhance it and improve its readability.
For example :

- [Steps](https://imfing.github.io/hextra/docs/guide/shortcodes/steps/) are well suited for the `/guides/` section, or for any tutorial

Use GitHub-style callouts with a concise title on the marker line, as supported by the theme:

```markdown
> [!NOTE] Current behavior
> This information helps readers understand the current behavior

> [!WARNING] Back up your data
> Back up your application database before upgrading
```

Use the [Hextra callout shortcode](https://imfing.github.io/hextra/docs/guide/shortcodes/callout/) only when a GitHub-style callout can't provide the required rendering or behavior. Don't overuse callouts: limit them to one or two per page.

#### Front matter and examples

- Give `title` a descriptive value, written for search engine optimization (SEO), without repeating `Clever Cloud`, which the generated HTML title already includes. Keep `linkTitle` short, usually the product name, so it fits in the sidebar.
- Don't add `aliases` to a new page. Use them only to preserve URLs that existed previously.
- Remove `draft: true` when a page is ready to publish instead of keeping `draft: false`
- Keep commands literally copyable. Don't use shell-invalid placeholders or bracketed optional arguments in executable code blocks; show optional variants separately or explain where to add the flag.
- Add code comments only when they explain non-obvious behavior
- Don't add a full stop to a short standalone line made of one simple sentence, especially a single-line code comment, label, or concise list item. Use normal terminal punctuation for developed or multi-sentence prose, including list items.
- Don't hard-wrap prose with formatting-only line breaks that don't affect rendering. Keep each paragraph on one logical line and rely on editor word wrap.
- Sort lists and tables alphabetically unless a functional or chronological order is more useful

#### Dependencies and versions

- All non-Docker runtimes provide a shared set of tools and version-management variables independently of the application's primary runtime. For example, `CC_NODE_VERSION` can select Node.js in a PHP application, while `CC_PHP_VERSION` can select PHP in a Node.js application. Other shared tools include Composer, Gradle, Hugo, and Python.
- Prefer these dedicated environment variables and the package managers already provided by the runtime when they manage a dependency or its version. If a Mise task also needs the runtime-managed tool, derive its Mise version from the dedicated environment variable instead of hard-coding the version twice.
- For other deployment dependencies, prefer [Mise](https://mise.jdx.dev/) and a suitable backend such as [HTTP](https://mise.jdx.dev/dev-tools/backends/http.html) or [GitHub](https://mise.jdx.dev/dev-tools/backends/github.html) over custom download scripts, and pin versions when appropriate

### 💅 Style guide

- Don't override global styles for font type, size, or color
- Comment your code if you add any custom CSS
- When importing from an external CSS tool, import the relevant classes only rather than the whole file
- Opt for self hosting over CDN: When used in `<head>`, it can impact site's performance. Using CDN for test purposes when submitting your PR and deploying a review app is totally fine, however.

### ✅ Validation

Run `mise install` to install the development dependencies declared in `mise.toml`, then run `hugo` before submitting a change and fix any build error. Verify links, references, image paths, and shortcode syntax in the generated output. Inspect changed tabs, code blocks, cards, anchors, and copyable commands in the rendered HTML: a successful build alone doesn't prove that they render correctly.

Run `markdownlint-cli2` and `vale` on the files you change: fix every error and warning on the lines you change, and review each suggestion. A passive that describes a state or a word quoted as an example can stay. Vale doesn't check everything: review structure, list order, and the accuracy of commands yourself. It doesn't lint the GitHub issue forms either, so review their text too.

## 🫶 Pull requests

These are the guidelines when submitting or reviewing a PR in this repository. The better you follow them, the faster the is the review process.

### 🚨 Priority

Priority goes to PRs that reference a problem addressed in an issue fitting the current milestone, or that fix a bug. But that doesn't mean that you can't submit or review a PR that doesn't fit those criteria if you think it's important. If you think it's important, it probably is.

### 🫡 When submitting a PR

- **Keep it small:** The quality of the review is inversely proportional to the size of the PR. Smaller PRs simplify the reviewing process and increase the chances of getting constructive feedback.
- **Accept the feedback:** If reviewers ask you to make changes, do it. If you disagree, explain why. If you aren't sure, ask for clarification. Don't nitpick on the feedback, and don't take it personally.

#### Commit messages

For content updates, use `section(page): commit message`. The section and page identify the documentation area you changed:

```text
addons(postgresql): document pg_partman support
applications(nodejs): clarify pnpm configuration
guides: add SvelteKit
```

Use `guides: add Product` when adding a deployment guide. Start the subject with a lowercase imperative verb.

Changelog entries are the exception. Use `changelog: what you announce`, naming the product and its version or the change itself rather than starting with a verb:

```text
changelog: Keycloak 26.7.3
changelog: MySQL 8.0.46 and 8.4.10
changelog: PostgreSQL 18 by default
changelog: images updates, 2026W34
```

Commit a changelog entry with the documentation pages and data files it relies on, so it never lands before the pages it links to.

For changes to the documentation structure, Hugo configuration or templates, deployment, CI, tooling, or dependencies, use the standard Conventional Commits format `type(scope): commit message`:

```text
feat(hugo): add a shortcode for version tables
fix(ci): run Vale on shared content
refactor(layouts): simplify changelog rendering
chore(deps): update the Hextra theme
```

The scope follows the files you change, not the effect readers see. A change limited to `layouts/` or `assets/` is `fix(layouts)` or `feat(layouts)` even when it alters how a documentation page renders.

Some changes span several sections or don't belong to one page. Use these forms instead of inventing a section:

```text
refactor(structure): merge the administrate and reference pages into their hubs
fix(aliases): redirect legacy URLs still hit with 404s
fix(links): point internal links at their new destination
ai-llms: document driving Clever Cloud from an AI agent
docs(contributing): document the commit conventions
```

A page stored directly under `content/doc/` is its own section. Reserve `docs(scope)` for README, CONTRIBUTING, and AGENTS.md, which document the repository itself. Don't use `doc` as a type or a section: in a documentation repository it describes every commit and distinguishes none.

Keep content and structural changes in separate commits when possible so each commit can follow the appropriate convention.

### 🥸 When reviewing a PR

- **Latency:** Long PR review latency can be disappointing for the authors, and make merge conflicts arise in their branch. Long latency kills productivity and morale, so make sure to review PRs in a timely manner.
- **Don't nitpick:** If the PR respects the preceding standards and provide updated content, don't ask for changes for the sake of it. If you think something isn't perfect, but it's not a big deal, don't ask for changes.
- **Provide alternatives:** If you think the author needs to change something, provide an example to illustrate your point. Use the `suggestion` feature on GitHub so the author can commit it directly if they agree with it.
- **It's OK to make mistakes:** Explain what's wrong, why, and how to improve. If someone is violating a standard, refer to this doc to explain.

## 💡☁️ Contributing as a Clever Cloud employee

If you are a member of Clever Cloud, act like you were submitting a PR and receiving feedback in any other open-source project. This means:

- **Don't bring internal company debates into the PR Discussion:** If conflict arises, take it to a private channel or in-person discussion. Pair-programming is a great way to solve conflicts together, consider it.
- **Don't use authority or seniority to push your PRs:** If you are a senior, your PRs aren't more important than others. If you are a junior, your PRs aren't less important than others. What matters is the work you've done on this PR, not who you are. Your contribution to this doc is already highly appreciated.
