{{- /* Body of the Markdown output format: the rendered page converted back to
Markdown, so shortcodes, shared blocks and links resolve exactly as they do in
HTML. The replaceRE turns the private-use sentinels emitted by
render-blockquote-alert.markdown.md and callout.markdown.md back into GitHub
alert markers. The sentinels are private-use code points, chosen to be
collision-resistant and verified absent from the corpus, not impossible to type. */ -}}
{{- .Title | replaceRE "\n" " " | printf "# %s" }}

{{ .Content | transform.HTMLToMarkdown | replaceRE "\ue000([A-Z]+)\ue001" "[!$1]" }}
