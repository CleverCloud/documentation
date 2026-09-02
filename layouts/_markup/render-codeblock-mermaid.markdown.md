{{- /* Markdown output: keep the diagram in a mermaid-tagged fence. */ -}}
<pre><code class="language-mermaid">{{ .Inner | htmlEscape | safeHTML }}</code></pre>
