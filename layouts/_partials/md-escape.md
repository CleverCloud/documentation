{{- /* Escape a plain-text value before interpolating it into the HTML that the
Markdown output format converts back to Markdown. Templates for a non-HTML
output format are text templates, so nothing is escaped automatically.

Only pass values that are plain text. A value that is already HTML must not go
through here: escaping its "&" turns an existing entity into "&amp;rsquo;",
which the conversion then decodes back to a visible "&rsquo;". That is why
render-blockquote-alert.markdown.md interpolates .AlertTitle as is. */ -}}
{{- . | replaceRE "&" "&amp;" | replaceRE "<" "&lt;" | replaceRE ">" "&gt;" | replaceRE "\"" "&quot;" -}}
