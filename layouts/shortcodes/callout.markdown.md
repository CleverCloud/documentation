{{- /* Markdown output: a callout becomes a GitHub alert, so callouts and
alert-style blockquotes read the same way. See render-blockquote-alert.markdown.md
for the sentinels and for why a callout carrying a code block is not quoted. */ -}}
{{- $types := dict "info" "NOTE" "warning" "WARNING" "error" "CAUTION" -}}
{{- $marker := printf "\ue000%s\ue001" (index $types (.Get "type" | default "default") | default "NOTE") -}}
{{- with .Get "emoji" }}{{ $marker = printf "%s %s" $marker . }}{{ end -}}
{{- $body := .InnerDeindent | markdownify -}}
{{- if strings.Contains $body "<pre" -}}
<p><strong>{{ $marker }}</strong></p>
{{ $body }}
{{- else -}}
<blockquote>
<p>{{ $marker }}</p>
{{ $body }}
</blockquote>
{{- end -}}
