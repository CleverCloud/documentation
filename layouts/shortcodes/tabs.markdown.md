{{- /* Markdown output: every tab is emitted in order, each under its own label. */ -}}
{{- .Inner -}}
{{- range ($.Store.Get "tabs" | default slice) -}}
<p><strong>{{ partial "md-escape.md" .name }}</strong></p>
{{ .content | markdownify }}
{{- end -}}
