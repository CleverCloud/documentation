
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

Sources for quality content are currently being updated

#### 👍 Do

- **Don't assume prior knowledge:** explain prerequisites and non-obvious behaviour without burying the main task path
- **Use active voice:** passive voice can make it harder for the readers to figure out who's supposed to do something
- **Use second person:** address the reader directly
- **Keep it simple:** avoid jargon, complex sentences, and jokes
- **Keep it short:** keep the sentences short. Titles should be short and to the point. Keep longer content for the description metadata or the card subtitle.

#### 👎 Don't

- Placeholder phrases like _please note_ and _at this time_
- Words and phrases that make promises or project plans and strategies: See [Writing timeless documentation](https://developers.google.com/style/timeless-documentation)
- Using phrases like _simply_, _It's that simple_, _It's easy_, or _quickly_ in a procedure
- Over-politeness with the use of _please_: go straight to the point

#### 💡 Shortcodes and callouts

This doc uses Hugo with [Hextra theme](https://imfing.github.io/hextra/), which provides a variety of [shortcodes](https://imfing.github.io/hextra/docs/guide/shortcodes/) to enhance it and improve its readability.
For example :

- [Steps](https://imfing.github.io/hextra/docs/guide/shortcodes/steps/) are well suited for the `/guides/` section, or for any tutorial

Use GitHub-style callouts with a concise title on the marker line, as supported by the theme:

```markdown
> [!NOTE] Current behaviour
> This information helps readers understand the current behaviour

> [!WARNING] Back up your data
> Back up your application database before upgrading
```

Use the [Hextra callout shortcode](https://imfing.github.io/hextra/docs/guide/shortcodes/callout/) only when a GitHub-style callout can't provide the required rendering or behaviour. Don't overuse callouts: limit them to one or two per page.

#### Front matter and examples

- Give `title` a descriptive, SEO-oriented value without repeating "Clever Cloud", which the generated HTML title already includes. Keep `linkTitle` short, usually the product name, so it fits in the sidebar.
- Don't add `aliases` to a new page. Use them only to preserve URLs that existed previously.
- Remove `draft: true` when a page is ready to publish instead of keeping `draft: false`
- Keep commands literally copyable. Don't use shell-invalid placeholders or bracketed optional arguments in executable code blocks; show optional variants separately or explain where to add the flag.
- Add code comments only when they explain non-obvious behaviour
- Don't add a full stop to a short standalone line made of one simple sentence, especially a single-line code comment, label, or concise list item. Use normal terminal punctuation for developed or multi-sentence prose, including list items.
- Don't hard-wrap prose with formatting-only line breaks that don't affect rendering. Keep each paragraph on one logical line and rely on editor word wrap.
- Sort lists and tables alphabetically unless a functional or chronological order is more useful

#### Dependencies and versions

- All non-Docker runtimes provide a shared set of tools and version-management variables independently of the application's primary runtime. For example, `CC_NODE_VERSION` can select Node.js in a PHP application, while `CC_PHP_VERSION` can select PHP in a Node.js application. Other shared tools include Composer, Gradle, Hugo and Python.
- Prefer these dedicated environment variables and the package managers already provided by the runtime when they manage a dependency or its version. If a Mise task also needs the runtime-managed tool, derive its Mise version from the dedicated environment variable instead of hard-coding the version twice.
- For other deployment dependencies, prefer [Mise](https://mise.jdx.dev/) and a suitable backend such as [HTTP](https://mise.jdx.dev/dev-tools/backends/http.html) or [GitHub](https://mise.jdx.dev/dev-tools/backends/github.html) over custom download scripts, and pin versions when appropriate

### 💅 Style guide

- Don't override global styles for font type, size, or color
- Comment your code if you add any custom CSS
- When importing from an external CSS tool, import the relevant classes only rather than the whole file
- Opt for self hosting over CDN: When used in `<head>`, it can impact site's performance. Using CDN for test purposes when submitting your PR and deploying a review app is totally fine, however.

### ✅ Validation

Run `hugo` before submitting a change and fix any build error. Verify links, references, image paths, and shortcode syntax in the generated output. Inspect changed tabs, code blocks, cards, anchors, and copyable commands in the rendered HTML: a successful build alone doesn't prove that they render correctly.

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
changelog(metabase): announce 0.63.14 security update
guides: add SvelteKit
```

Use `guides: add Product` when adding a deployment guide. Start the subject with a lowercase imperative verb.

For changes to the documentation structure, Hugo configuration or templates, deployment, CI, tooling, or dependencies, use the standard Conventional Commits format `type(scope): commit message`:

```text
feat(hugo): add a shortcode for version tables
fix(ci): run Vale on shared content
refactor(layouts): simplify changelog rendering
chore(deps): update the Hextra theme
```

Keep content and structural changes in separate commits when possible so each commit can follow the appropriate convention.

### 🥸 When reviewing a PR

- **Latency:** Long PR review latency can be disappointing for the authors, and make merge conflicts arise in their branch. Long latency kills productivity and morale, so make sure to review PRs in a timely manner.
- **Don't nitpick:** If the PR respects the preceding standards and provide updated content, don't ask for changes just for the sake of it. If you think something isn't perfect, but it's not a big deal, don't ask for changes.
- **Provide alternatives:** If you think the author needs to change something, provide an example to illustrate your point. Use the `suggestion` feature on GitHub so the author can commit it directly if they agree with it.
- **It's OK to make mistakes:** Explain what's wrong, why, and how to improve. If someone is violating a standard, refer to this doc to explain.

## 💡☁️ Contributing as a Clever Cloud employee

If you are a member of Clever Cloud, act like you were submitting a PR and receiving feedback in any other Open Source project. This means:

- **Don't bring internal company debates into the PR Discussion:** If conflict arises, take it to a private channel or in-person discussion. Pair-programming is a great way to solve conflicts together, consider it.
- **Don't use authority or seniority to push your PRs:** If you are a senior, your PRs aren't more important than others. If you are a junior, your PRs aren't less important than others. No one cares who you are, just the work you've done on this PR, and the fact you are willing to contribute to this doc is already highly appreciated.
