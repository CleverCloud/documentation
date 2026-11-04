# Contributing guidelines

This document sets the standards that human contributors and coding agents follow in the Clever Cloud documentation. Inspiration and research for this document come from the [Awesome Code Review](https://github.com/joho/awesome-code-review) project. The [README](./README.md) explains how to set up the project, add content, and run the checks; [AGENTS.md](./AGENTS.md) points coding agents to both files.

## Standards

These general standards apply to every change in this repository.

### 🏯 Structure

The structure of this documentation aims to be as clear as possible for Clever Cloud users. Submitted changes can be merged as long as they respect these standards:

- Readers know where to go or where to click to find information
- Readers know why they're on a specific page
- The site keeps a coherent and [intuitive design](https://www.figma.com/fr/resource-library/ui-design-principles/)

Follow the established structure. To propose changes to the structure, open an issue first to discuss it, or post it in the forum.

#### Move, merge, or remove a page

When a page moves to another URL, or when you merge its content into another page:

- Add the old URL to the destination page's `aliases`, so Hugo keeps serving a redirect
- Carry over every alias the removed page already declared; they must keep resolving
- Update internal links to target the new URL directly instead of relying on the redirect, especially in `shared/` blocks included by many pages
- Check each redirect in the build output before committing

### ✒️ Content

Follow these guidelines while writing new content. The goal is to help you write in a **clear, precise, and unambiguous language**. They're not meant to be a burden, but to help you deliver the best content possible.

#### 👍 Do

- **Don't assume prior knowledge:** explain prerequisites and non-obvious behavior without burying the main task path
- **Spell out acronyms:** at their first use on a page, write the full term followed by the acronym in parentheses, such as *multi-factor authentication (MFA)*. Then use the acronym alone. Skip this for acronyms most readers already know, such as API, CLI, DNS, or HTTP
- **Use the serial comma:** add a comma before the last item of a list, such as `Go, Node.js, and Python`
- **Write dates in the US format:** `November 12, 2026`, and spell out ordinals in text, such as `first` instead of `1st`. ISO dates such as `2026-11-12` remain fine in logs, timelines, and front matter
- **Don't space dashes:** write `the default—Node.js 24—applies`, for an em dash as for an en dash
- **Use the present tense:** describe how the platform behaves, such as `the build cache applies` instead of `will apply`, `won't apply`, or `is going to apply`. Changelogs and postmortems can use `will` to announce a change
- **Use US spelling:** write `behavior` and `license`. The only exception is `organisation`
- **Prefer contractions:** write `don't` and `isn't`
- **Avoid Latin abbreviations and exclamation points:** write `for example`, `that is`, `and so on`, `see`, `namely`, `note`, and `versus` instead of `e.g.`, `i.e.`, `etc.`, `cf.`, `viz.`, `N.B.`, and `vs.`
- **Prefer plain words:** write `click`, `to`, `if`, `because`, `can`, `use`, `before`, and `Kubernetes` instead of `click on`, `in order to`, `in the event that`, `due to the fact that`, `is able to`, `leverage` or `utilize`, `prior to`, and `k8s`. Write `lets you deploy`, not `allows to deploy`. Use `set up`, `log in`, and `back up` as verbs, `setup`, `login`, and `backup` as nouns
- **Use the project terminology:** write `add-on`, `email`, `feedback`, `plugin`, `URL`, and `WebSocket`. The Vale vocabulary in `.github/styles/config/vocabularies/Doc/` lists the rejected forms in `reject.txt`, matched case-sensitively, and the product names and terms the spell check accepts in `accept.txt`. The spell check ignores their case, so check capitalization yourself
- **Hyphenate with care:** don't hyphenate an adverb ending in `-ly`, such as `highly available`. Hyphenate a compound adjective before a noun, such as `long-term support` or `open-source project`, and leave `up to date`, `open source`, `end of life`, and `step by step` open when they end the clause after a verb, such as `the image is up to date`
- **Mind the typography:** use the ellipsis character `…`, and one space between sentences
- **Prefer active voice when it tells who acts:** you, Clever Cloud, the CLI. Passive voice can make it harder for readers to figure out who's supposed to do something. A passive is fine to describe a state, such as *is enabled*, or when the actor doesn't matter
- **Use second person:** address the reader directly
- **Keep it simple:** avoid jargon, complex sentences, and jokes
- **Keep it short:** keep a sentence under 25 words when possible. Keep a paragraph to four or five lines, about 80 words, unless the content strictly needs more. Vale suggests splitting longer sentences and paragraphs over 100 words. Titles should be short and to the point. Keep longer content for the description metadata or the card subtitle
- **Prefer prose to lists:** write two to four well-developed paragraphs per section, and keep bullet lists for items readers scan or compare

#### 👎 Don't

- First-person pronouns such as *I*, *me*, *my*, *we*, *us*, *our*, or *let's*. Changelog entries are the only exception: they can use *we*, *us*, and *our* to speak for Clever Cloud, never *I*, *me*, or *my*
- Placeholder phrases like *please note*, *note that*, *at this time*, *it should be noted*, *keep in mind*, *be aware that*, *feel free to*, *don't hesitate to*, *as mentioned*, *it's important to note*, *it's worth noting*, *basically*, or *actually*
- Words and phrases that make promises or tie the content to a moment, such as *soon*, *currently*, *for now*, *not yet*, *today*, *recently*, *upcoming*, *coming next month*, or *in the future*: describe the current state of the platform instead. This doesn't apply to changelog entries, which can announce commitments such as how long a version stays available
- Using phrases like *simply*, *just*, *easy*, *easily*, *obviously*, *of course*, *as simple as*, *straightforward*, *seamless*, *effortless*, *trivial*, *with ease*, *It's that simple*, *It's easy*, or *quickly* in a procedure
- Over-politeness with the use of *please*: go straight to the point

#### 💡 Shortcodes and callouts

This documentation uses Hugo with the [Hextra theme](https://imfing.github.io/hextra/), which provides [shortcodes](https://imfing.github.io/hextra/docs/guide/shortcodes/) that improve readability:

- [Cards](https://imfing.github.io/hextra/docs/guide/shortcodes/cards/) with `{{< cards >}}` link to related resources
- Hero subtitles with `{{< hextra/hero-subtitle >}}` introduce a guide
- [Steps](https://imfing.github.io/hextra/docs/guide/shortcodes/steps/) with `{{% steps %}}` suit the `/guides/` section, or any tutorial
- [Tabs](https://imfing.github.io/hextra/docs/guide/shortcodes/tabs/) with `{{< tabs >}}` and named `{{< tab name="npm" >}}` children show alternatives side by side

The project adds its own shortcodes in `layouts/shortcodes/`, such as `content` and `content-raw` for [shared content](./README.md#add-shared-content).

Use GitHub-style callouts with a concise title on the marker line, as supported by the theme:

```markdown
> [!NOTE] Current behavior
> This information helps readers understand the current behavior

> [!WARNING] Back up your data
> Back up your application database before upgrading
```

Choose the type from what readers risk if they skip the callout, not from how important its content feels. Keep `[!WARNING]` for an action that can go wrong, such as data loss, downtime, a security exposure, or a breaking or irreversible change. Use `[!NOTE]` for a limit of scope or availability, such as a feature Docker applications don't support, a default value, or a behavior to know. Use `[!TIP]` for a recommendation. When you rewrite a page, check the type of each callout it already has instead of carrying it over.

Use the [Hextra callout shortcode](https://imfing.github.io/hextra/docs/guide/shortcodes/callout/) only when a GitHub-style callout can't provide the required rendering or behavior. Don't overuse callouts: limit them to one or two per page.

#### Front matter

The [README](./README.md#configure-front-matter) lists the front matter fields this project uses. When you set them:

- Give `title` a descriptive value, written for search engine optimization (SEO), without repeating `Clever Cloud`, which the generated HTML title already includes. Keep `linkTitle` short, usually the product name, so it fits in the sidebar
- Don't add `aliases` to a new page. Use them only to preserve URLs that existed previously
- Remove `draft: true` when a page is ready to publish instead of keeping `draft: false`

#### Code and command examples

- Provide complete, runnable examples with real commands and configurations, and include setup context and expected output when helpful
- Keep commands literally copyable. Don't use shell-invalid placeholders or bracketed optional arguments in executable code blocks; show optional variants separately or explain where to add the flag
- Use exact environment variable names, such as `CC_WEBROOT` and `CC_NODE_BUILD_TOOL`
- Use realistic names instead of `foo`, `bar`, or `example`
- Show complete command sequences in changelog entries
- Add code comments only when they explain non-obvious behavior

#### Formatting

- Don't add a full stop to a short standalone line made of one simple sentence, especially a single-line code comment, label, or concise list item. Use normal terminal punctuation for developed or multi-sentence prose, including list items
- Don't hard-wrap prose with formatting-only line breaks that don't affect rendering. Keep each paragraph on one logical line and rely on editor word wrap
- Sort list items alphabetically, or by increasing or decreasing line length, and table rows alphabetically. An editorial logic, such as a functional, chronological, or step-by-step order, takes priority over both
- End every text file with a newline

#### Dependencies and versions

- All non-Docker runtimes provide a shared set of tools and version-management variables independently of the application's primary runtime. For example, `CC_NODE_VERSION` can select Node.js in a PHP application, while `CC_PHP_VERSION` can select PHP in a Node.js application. Other shared tools include Composer, Gradle, Hugo, and Python.
- Prefer these dedicated environment variables and the package managers already provided by the runtime when they manage a dependency or its version. If a Mise task also needs the runtime-managed tool, derive its Mise version from the dedicated environment variable instead of hard-coding the version twice.
- For other deployment dependencies, prefer [Mise](https://mise.jdx.dev/) and a suitable backend such as [HTTP](https://mise.jdx.dev/dev-tools/backends/http.html) or [GitHub](https://mise.jdx.dev/dev-tools/backends/github.html) over custom download scripts, and pin versions when appropriate

#### Deployment guides

- Prefer one clear path that uses platform defaults and native features
- Follow every documented command from a fresh project and test every behavior the guide promises
- Verify the default build and run configuration before documenting any scaling override
- Omit `-a` when the current directory is linked to only one application; use an application alias to disambiguate or link resources
- Follow the option style used by recent guides, including short Clever Tools options where established
- Place the standard `clever domain` and custom-domain example immediately after application creation
- Use `openssl rand -base64 32` when a guide needs a portable password-generation example and OpenSSL is already a prerequisite
- Make sure captured command output doesn't expose credentials, tokens, add-on environment values, or unrelated account data
- Validate public-storage claims with an unauthenticated request and persistence claims after a restart or rebuild

### 💅 Style guide

- Don't override global styles for font type, size, or color
- Comment your code if you add any custom CSS
- When importing from an external CSS tool, import the relevant classes only rather than the whole file
- Opt for self hosting over CDN: When used in `<head>`, it can impact site's performance. Using CDN for test purposes when submitting your PR and deploying a review app is totally fine, however.

### ✅ Validation

Run the [checks described in the README](./README.md#validate-changes) before submitting a change: a `hugo` build without errors, `markdownlint-cli2`, and `vale` on the files you change. Then check the commits of your branch with `commitlint`.

Fix every markdownlint issue, and every Vale error and warning on the lines you change, then review each Vale suggestion. A passive that describes a state or a word quoted as an example can stay. Vale doesn't check everything: review structure, list order, and the accuracy of commands yourself. It doesn't lint the GitHub issue forms in `.github/ISSUE_TEMPLATE/` either, so review their text too.

Verify links, references, image paths, and shortcode syntax in the generated output. Inspect changed tabs, code blocks, cards, anchors, and copyable commands in the rendered HTML: a successful build alone doesn't prove that they render correctly.

## 🫶 Pull requests

These are the guidelines when submitting or reviewing a PR in this repository. The better you follow them, the faster the review process is.

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

A page stored directly under `content/doc/` is its own section. Reserve `docs(scope)` for README, CONTRIBUTING, and AGENTS.md, which document the repository itself. Don't use `doc` as a type, a section, or a scope: in a documentation repository it describes every commit and distinguishes none.

Keep content and structural changes in separate commits when possible so each commit can follow the appropriate convention.

Keep the subject line, prefix included, to 100 characters at most. Put any further detail in the commit body.

### 🥸 When reviewing a PR

- **Latency:** Long PR review latency can be disappointing for the authors, and make merge conflicts arise in their branch. Long latency kills productivity and morale, so make sure to review PRs in a timely manner.
- **Don't nitpick:** If the PR respects the preceding standards and provide updated content, don't ask for changes for the sake of it. If you think something isn't perfect, but it's not a big deal, don't ask for changes.
- **Provide alternatives:** If you think the author needs to change something, provide an example to illustrate your point. Use the `suggestion` feature on GitHub so the author can commit it directly if they agree with it.
- **It's OK to make mistakes:** Explain what's wrong, why, and how to improve. If someone is violating a standard, refer to this doc to explain.

## 💡☁️ Contributing as a Clever Cloud employee

If you are a member of Clever Cloud, act like you were submitting a PR and receiving feedback in any other open-source project. This means:

- **Don't bring internal company debates into the PR Discussion:** If conflict arises, take it to a private channel or in-person discussion. Pair-programming is a great way to solve conflicts together, consider it.
- **Don't use authority or seniority to push your PRs:** If you are a senior, your PRs aren't more important than others. If you are a junior, your PRs aren't less important than others. What matters is the work you've done on this PR, not who you are. Your contribution to this doc is already highly appreciated.
