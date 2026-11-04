---
title: Update external documentation after PR {{ env.PR_NUMBER }}
labels: enhancement
---

## External documentation update needed

Review the corresponding external documentation after these changes:

- Author: @{{ payload.sender.login }}
- PR: {{ env.PR_URL }}
- Modified files: {{ env.CHANGED_FILES }}

Open a pull request in the relevant repository:

- [Astro](https://github.com/withastro/docs)
- [Nuxt](https://github.com/nuxt/nuxt)
