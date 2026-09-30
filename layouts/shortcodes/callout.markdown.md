{{- /* Markdown output: a callout becomes a GitHub alert, so callouts and alert-style blockquotes read the same way. */ -}}
{{- $types := dict "info" "NOTE" "warning" "WARNING" "error" "CAUTION" -}}
{{- $marker := printf "[!%s]" (index $types (.Get "type" | default "default") | default "NOTE") -}}
{{- with .Get "emoji" }}{{ $marker = printf "%s %s" $marker . }}{{ end -}}
{{- partial "utils/markdown-block.md" (dict "page" .Page "content" (.InnerDeindent | markdownify) "marker" $marker) -}}
