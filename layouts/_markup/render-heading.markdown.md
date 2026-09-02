{{- /* Markdown output: a plain heading. Hextra's render-heading.html appends an
anchor span and an empty <a>, which the HTML-to-Markdown conversion turned into
"## Title[](#title)" on every heading. */ -}}
<h{{ .Level }}>{{ .Text | safeHTML }}</h{{ .Level }}>
