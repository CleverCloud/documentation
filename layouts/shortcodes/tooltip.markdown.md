{{- /* Markdown output: the tooltip becomes its definition in parentheses. */ -}}
{{- $title := .Get "title" -}}
{{- $def := index hugo.Data.tooltips $title -}}
{{- .Inner }}{{ with $def }} ({{ partial "md-escape.md" . }}){{ end -}}
