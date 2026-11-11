{{- /* Markdown output of the asciinema shortcode of the theme: a link to the asciicast file, which asciinema plays in a terminal. */ -}}
{{- $file := .Get "file" | default (.Get 0) -}}
{{- with resources.Get $file -}}
[Terminal recording]({{ (. | fingerprint).Permalink }})
{{- end -}}
