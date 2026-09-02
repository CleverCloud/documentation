{{- /* Markdown output: keep the GitHub alert marker and its type.

The marker is emitted between two private-use sentinels (U+E000/U+E001) that
markdown-output.md turns back into "[!TYPE]". Writing the brackets here would
have them escaped by the HTML-to-Markdown conversion, and un-escaping them
afterwards would rewrite every "[!word]" the page happens to contain.

transform.HTMLToMarkdown only quotes the first line of a <pre> nested in a
<blockquote>, so an alert carrying a code block is emitted as a labelled block
rather than a quoted one: a boundary is worth less than valid code.

.AlertTitle is already HTML, so it is interpolated as is. */ -}}
{{- $marker := printf "\ue000%s\ue001" (upper .AlertType) -}}
{{- with .AlertTitle }}{{ $marker = printf "%s %s" $marker . }}{{ end -}}
{{- if strings.Contains .Text "<pre" -}}
<p><strong>{{ $marker }}</strong></p>
{{ .Text }}
{{- else -}}
<blockquote>
<p>{{ $marker }}</p>
{{ .Text }}
</blockquote>
{{- end -}}
