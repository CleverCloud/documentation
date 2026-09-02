{{- /* Markdown output: a card becomes a list item with its link and subtitle. */ -}}
{{- $link := .Get "link" -}}
{{- $title := .Get "title" | default $link -}}
{{- $subtitle := .Get "subtitle" -}}
<li>{{ with $link }}<a href="{{ partial "md-escape.md" . }}">{{ partial "md-escape.md" $title }}</a>{{ else }}{{ partial "md-escape.md" $title }}{{ end }}{{ with $subtitle }}: {{ . | markdownify }}{{ end }}</li>
