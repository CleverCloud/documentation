# AGENTS.md

This file points coding agents working on the Clever Cloud documentation to the project instructions. Read both files before you change anything; every rule in them applies to agents:

- [CONTRIBUTING.md](./CONTRIBUTING.md): writing standards, front matter and example rules, moving or merging pages, deployment guides, validation requirements, and commit messages
- [README.md](./README.md): repository structure, local development, how to add pages, changelog entries, images, shared content, and tooltips, the front matter fields, and the validation commands

## Before you report a change as done

- Run the [validation](./CONTRIBUTING.md#-validation) on the files you change, and inspect the rendered HTML of the pages they affect
- Measure the line breaks of the rendered pages you change in a browser, at a desktop width of about 1,050 pixels of content: a list item shouldn't wrap, and the last line of a paragraph shouldn't hold only a few words. Narrower screens wrap lines differently
- Check that each redirect you add resolves in the build output, as [CONTRIBUTING.md](./CONTRIBUTING.md#move-merge-or-remove-a-page) requires when a page moves
- Write the commit subject with the [commit conventions](./CONTRIBUTING.md#commit-messages), and keep content and structural changes in separate commits
- Describe a pull request or an issue as [CONTRIBUTING.md](./CONTRIBUTING.md#-when-submitting-a-pr) asks: its main lines and what reviewers need, not a list of every change

## Generated content

Don't edit the body of `content/doc/cli-reference.md` by hand. `scripts/update-cli-reference.sh` regenerates it from the documentation of a Clever Tools release and keeps its front matter, which is the only part maintained in this repository.
