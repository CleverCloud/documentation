{{- /* Markdown output: the embedded player becomes a plain link to the video, or
to the playlist when the shortcode only has a list. */ -}}
{{- $id := or (.Get "id") (.Get 0) -}}
{{- $list := .Get "list" -}}
{{- if $id -}}
  {{- $query := dict "v" $id -}}
  {{- with $list }}{{ $query = merge $query (dict "list" .) }}{{ end -}}
<p><a href="https://www.youtube.com/watch?{{ querify $query }}">Watch the video on YouTube</a></p>
{{- else if $list -}}
<p><a href="https://www.youtube.com/playlist?{{ querify "list" $list }}">Watch the playlist on YouTube</a></p>
{{- end -}}
