{{- /* Body of the Markdown output format: the rendered page converted back to
Markdown, so shortcodes, shared blocks and links resolve exactly as they do in
HTML. See utils/html-to-markdown.md for the link resolution and the blockquote
handling, ported from imfing/hextra#1044 until Hextra ships them. */ -}}
{{- .Title | replaceRE "\n" " " | printf "# %s" }}

{{ partial "utils/html-to-markdown.md" (dict "page" . "html" .Content) }}
