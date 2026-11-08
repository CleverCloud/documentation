# AGENTS.md

This file points coding agents to the instructions of the Clever Cloud documentation, whose rules all apply to agents. Before you change anything, read [CONTRIBUTING.md](./CONTRIBUTING.md) and the three files listed below:

- [Style guide](./contributing/style-guide.md): how to write and rephrase text, in pages, changelog entries, or code comments
- [Authoring guide](./contributing/authoring.md): how to add or move a page, and write examples, guides, or runtime pages
- [README.md](./README.md): the structure of the repository, the local preview, and the deployment of the site

## Before you report a change as done

- Run the [checks](./CONTRIBUTING.md#check-your-change) on the files you change, and inspect the rendered HTML of the pages they affect
- Measure the line breaks of the rendered pages you change in a browser, at about 1,050 pixels of content width
- Check that each redirect you add resolves in the build output, when [a page moves](./contributing/authoring.md#move-merge-or-remove-a-page)
- Write the commit subject with the [commit conventions](./CONTRIBUTING.md#commit-messages)
- Keep content and structural changes in separate commits
- Describe a pull request or an issue [briefly](./CONTRIBUTING.md#open-a-pull-request): its main lines and what reviewers need, not every change

When you measure the line breaks, a list item shouldn't wrap, and the last line of a paragraph shouldn't hold only a few words. Narrower screens wrap lines differently, so measure at this desktop width. Measure the Markdown files GitHub displays, such as this one, at 1,012 pixels, the content width of its file view.

Don't edit the body of `content/doc/cli-reference.md` by hand: [regenerate it](./contributing/authoring.md#update-generated-content).
