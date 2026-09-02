{{- /* Markdown output: a plain fenced block, keeping the language and the
optional filename label. Templates for a non-HTML output format are text
templates, so every interpolated value is escaped explicitly; without it a
filename such as "<appId>" would be read back as an HTML tag and dropped. */ -}}
{{- $lang := .Attributes.lang | default .Type -}}
{{- with .Attributes.filename }}<p><code>{{ partial "md-escape.md" . }}</code></p>
{{ end -}}
<pre><code{{ with $lang }} class="language-{{ partial "md-escape.md" $lang }}"{{ end }}>{{ .Inner | htmlEscape | safeHTML }}</code></pre>
