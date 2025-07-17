{{- $content := . -}}
{{- $content = partial "markdown/include_shortcode_content.md" $content -}}
{{- $content = partial "markdown/include_runtimes_versions.md" $content -}}
{{- $content = partial "markdown/include_software_versions_shared_dedicated.md" $content -}}
{{ $content }}
