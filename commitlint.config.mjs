// Commit subject conventions, described in CONTRIBUTING.md under "Commit messages".
//
// commitlint is installed by mise as a standalone npm tool, so shared configs such as
// @commitlint/config-conventional can't be resolved from here: every rule is set below.

// Capitalised, these open a subject that is a sentence or a file name rather than an
// imperative, as in GitHub's default `Update page.md`. Other capitals are left alone:
// many subjects open on a product name, as in `changelog: PostgreSQL 18 by default`.
const COMMIT_VERBS = new Set(`
  add address allow bump change clarify complete correct create delete document
  drop edit enable ensure fix improve init initial introduce list make mention
  merge move prepare publish refactor remove rename replace revert set support
  switch tweak update upgrade use
`.trim().split(/\s+/));

export default {
  // A prefix is a section (`guides`, `ai-llms`, a directory under content/doc/) or a
  // Conventional Commits type, with an optional scope and breaking-change `!`. The
  // default pattern rejects hyphens in the type and `!`, and accepts padded scopes.
  parserPreset: {
    parserOpts: {
      headerPattern: /^([a-z][a-z0-9-]*)(?:\(([^()\s](?:[^()]*[^()\s])?)\))?!?: (\S.*)$/,
      headerCorrespondence: ['type', 'scope', 'subject'],
    },
  },

  // The default ignores let `fixup!` and `squash!` commits through.
  defaultIgnores: false,
  ignores: [(message) => /^Merge /.test(message) || /^Revert ".+"/.test(message)],

  helpUrl: 'https://github.com/CleverCloud/documentation/blob/main/CONTRIBUTING.md#commit-messages',

  plugins: [
    {
      rules: {
        'header-no-autosquash': ({ header }) => [
          !/^(fixup|squash|amend)! /.test(header ?? ''),
          'an autosquash marker is left over, run `git rebase -i --autosquash`',
        ],
        'subject-lowercase-verb': ({ subject }) => {
          const first = (subject ?? '').split(/\s+/)[0];
          const capitalised = /^[A-Z]/.test(first) && COMMIT_VERBS.has(first.toLowerCase());
          return [!capitalised, `subject must start with a lowercase verb, write \`${first.toLowerCase()}\``];
        },
      },
    },
  ],

  rules: {
    'header-max-length': [2, 'always', 100],
    'header-no-autosquash': [2, 'always'],
    'header-trim': [2, 'always'],
    // `doc` describes every commit in a documentation repository and distinguishes none
    'scope-enum': [2, 'never', ['doc']],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'subject-lowercase-verb': [2, 'always'],
    'type-case': [2, 'always', 'lower-case'],
    'type-empty': [2, 'never'],
    'type-enum': [2, 'never', ['doc']],
  },
};
