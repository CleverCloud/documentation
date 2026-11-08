{{- /* Markdown output: a badge becomes its text, linked if it has a link. The HTML
badge is a div, which the conversion would turn into a paragraph of its own,
cutting the sentence around it. */ -}}
{{- $content := .Get "content" | default (.Get 0) -}}
{{- $link := .Get "link" -}}
{{- if $link -}}
<a href="{{ partial "md-escape.md" $link }}">{{ partial "md-escape.md" $content }}</a>
{{- else -}}
{{ partial "md-escape.md" $content }}
{{- end -}}
