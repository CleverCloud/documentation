# Style guide

This guide describes how to write the Clever Cloud documentation: who you write for, in which voice, and with which words, punctuation, and layout. It applies to every documentation page, guide, and changelog entry, with the exceptions it states. Its goal is a clear, precise, and unambiguous language, not a burden.

[Vale](https://vale.sh/) checks many of these rules with the project's `Clever` style, whose rule files in [`.github/styles/Clever/`](../.github/styles/Clever/) hold the complete lists of words that this guide only illustrates. [CONTRIBUTING.md](../CONTRIBUTING.md#check-the-editorial-style) explains which alerts to fix. Vale doesn't catch every mistake, so the rules of this guide apply even when it stays silent.

## Write for the reader

Don't assume prior knowledge: explain prerequisites and non-obvious behavior without burying the main task path. At its first use, explain in a few words each tool, file, or concept of an ecosystem, such as a build tool, a lock file, or a framework. Introduce a framework before an example uses it, and skip unrelated language features.

Address readers directly, in the second person, and keep it simple: avoid jargon, complex sentences, and jokes. Don't use first-person pronouns, such as *I*, *me*, *my*, *we*, *us*, *our*, or *let's*. Changelog entries are the only exception to this rule: they can use *we*, *us*, and *our* to speak for Clever Cloud, never *I*, *me*, or *my*.

Prefer active voice when it tells who acts: you, Clever Cloud, the CLI. A passive voice can make it harder for readers to figure out who's supposed to do something. It remains fine to describe a state, such as *is enabled*, or when the actor doesn't matter.

Show how products work together. Highlight the Clever Cloud products that complement each other, or that enable or simplify a feature, such as Cellar to store the files of an application. When a product has a limit, link to the product or feature that covers the need.

## Describe the current state

Describe how the platform behaves in the present tense: write *the build cache applies*, not *will apply*, *won't apply*, or *is going to apply*. Changelogs and postmortems can use *will* to announce a change.

Avoid words and phrases that make promises or tie the content to a moment, such as *soon*, *currently*, *for now*, *not yet*, *today*, *recently*, *upcoming*, *coming next month*, or *in the future*. Changelog entries are the exception to this rule: they can announce commitments, such as how long a product version stays available.

Leave prices and version history, such as *available since version 2.3*, out of documentation pages: describe the current state, and announce changes in a changelog entry. Among them, only the Kubernetes page can show prices, and writing that a feature is free or not billed is fine.

## Choose your words

Prefer plain words: write *click*, *to*, *if*, *because*, *can*, *use*, and *before* instead of *click on*, *in order to*, *in the event that*, *due to the fact that*, *is able to*, *leverage* or *utilize*, and *prior to*. Write *lets you deploy*, not *allows to deploy*. Use *set up*, *log in*, and *back up* as verbs, and *setup*, *login*, and *backup* as nouns. Prefer contractions, such as *don't*.

Use the project terminology: *add-on*, *email*, *feedback*, *Kubernetes* rather than *k8s*, *plugin*, *URL*, and *WebSocket*. Write *region*, not *zone*, for the location of an application or an add-on, as the `--region` option of Clever Tools does. Use US spelling, such as *behavior* and *license*, everywhere except for the British *organisation*.

The Vale vocabulary in [`.github/styles/config/vocabularies/Doc/`](../.github/styles/config/vocabularies/Doc/) lists the rejected forms in `reject.txt`, matched case-sensitively. Its `accept.txt` file lists the product names and terms the spell check accepts, whatever their case: check their capitalization yourself.

At its first use on a page, write the full term followed by its acronym in parentheses, such as *multi-factor authentication (MFA)*, then use the acronym alone. Skip this step for the acronyms that most readers already know, such as API, CLI, DNS, or HTTP.

Some words delay the point or judge the difficulty for readers. Remove them:

- Placeholder phrases, such as *please note*, *note that*, *keep in mind*, *feel free to*, or *basically*
- Over-politeness with *please*: go straight to the point
- In a procedure, words that make it sound easy, such as *simply*, *just*, *obviously*, or *straightforward*

Vale lists them all in [`placeholder-phrases.yml`](../.github/styles/Clever/placeholder-phrases.yml) and [`overconfident.yml`](../.github/styles/Clever/overconfident.yml), and the plain words in [`word-list.yml`](../.github/styles/Clever/word-list.yml).

## Sentences and paragraphs

Keep a sentence under 25 words when possible. Keep a paragraph to four or five lines, about 80 words, unless the content strictly needs more. Vale suggests splitting longer sentences, and paragraphs over 100 words.

Prefer prose to lists: write two to four well-developed paragraphs per section. Group related sentences. In the rendered page, avoid a paragraph whose last line holds a few words, and runs of one-sentence paragraphs.

Keep titles short and to the point. Longer content belongs in the description metadata or the card subtitle.

## Lists and tables

Keep bullet lists for items readers scan or compare. Keep each item to one line, and move explanations and exceptions, such as an *unless* clause, to a paragraph after the list.

Sort list items alphabetically, or by increasing or decreasing line length, and table rows alphabetically. An editorial logic, such as a functional, chronological, or step-by-step order, takes priority over both.

Don't add a full stop to a short standalone line of one simple sentence, such as a concise list item, a label, or a one-line code comment. Developed or multi-sentence prose, including list items, keeps its terminal punctuation.

## Punctuation and typography

- Use the serial comma before the last item of a list, such as *Go, Node.js, and Python*
- Write dates in the US format, such as *November 12, 2026*, and spell out ordinals, such as *first*
- Don't space dashes: *the default—Node.js 24—applies*, for an em dash as for an en dash
- Use the ellipsis character `…`, and one space between sentences
- Don't use exclamation points

ISO dates such as `2026-11-12` remain fine in logs, timelines, and front matter.

Replace the Latin abbreviations with their plain English equivalents: *for example*, *that is*, *and so on*, *see*, *namely*, *note*, and *versus* instead of *e.g.*, *i.e.*, *etc.*, *cf.*, *viz.*, *N.B.*, and *vs.*

Don't hyphenate an adverb ending in *-ly*, such as *highly available*. Hyphenate a compound adjective before a noun, such as *long-term support* or *open-source project*. Leave *up to date*, *open source*, *end of life*, and *step by step* open when they end the clause after a verb, such as the phrase *the image is up to date*.

## Callouts

Use GitHub-style callouts, as the Hextra theme supports them, with a concise title on the marker line:

```markdown
> [!NOTE] Current behavior
> This information helps readers understand the current behavior

> [!WARNING] Back up your data
> Back up your application database before upgrading
```

Choose the type from what readers risk if they skip the callout, not from how important its content feels:

- `[!WARNING]` for a risky action: data loss, downtime, security exposure, or a breaking or irreversible change
- `[!NOTE]` for a limit of scope or availability, a default value, or a behavior to know
- `[!TIP]` for a recommendation

A feature Docker applications don't support is a limit, so it goes in a `[!NOTE]`. When you rewrite a page, check the type of each callout it already has instead of carrying it over.

Don't overuse callouts: limit them to one or two per page. Use the [Hextra callout shortcode](https://imfing.github.io/hextra/docs/guide/shortcodes/callout/) only when a GitHub-style callout can't provide the required rendering or behavior.
