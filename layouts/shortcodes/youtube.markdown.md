{{- /* Markdown output: the embedded player becomes a plain link to the video. */ -}}
{{- $id := or (.Get "id") (.Get 0) -}}
{{- with $id -}}
<p><a href="https://www.youtube.com/watch?v={{ . }}">Watch the video on YouTube</a></p>
{{- end -}}
