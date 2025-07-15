{{- $content := . -}}
{{- $patternSearch := "\\{\\{%\\s*remote\\s+([^%}]+)\\s*%\\}\\}" -}}
{{- $patternClean := "\\{\\{%\\s*remote\\s+(.+?)\\s*%\\}\\}" -}}

{{- range $shortcodeFound := findRE $patternSearch $content -}}
    {{- $params := replaceRE $patternClean "$1" $shortcodeFound -}}
    {{- $url := "" -}}
    {{- $excludeSection := "## Clever Cloud complete documentation" -}}

    {{- if findRE "url\\s*=\\s*\"([^\"]+)\"" $params -}}
        {{- $url = replaceRE ".*url\\s*=\\s*\"([^\"]+)\".*" "$1" $params -}}
    {{- end -}}
    {{- if findRE "exclude\\s*=\\s*\"([^\"]+)\"" $params -}}
        {{- $excludeSection = replaceRE ".*exclude\\s*=\\s*\"([^\"]+)\".*" "$1" $params -}}
    {{- end -}}

    {{- if $url -}}
        {{- $remoteContent := resources.GetRemote $url -}}
        {{- if $remoteContent -}}
            {{- $text := $remoteContent.Content -}}
            {{- if $excludeSection -}}
                {{- $parts := split $text $excludeSection -}}
                {{- $text = index $parts 0 -}}
            {{- end -}}
            {{- $content = replace $content $shortcodeFound $text -}}
        {{- else -}}
            {{- warnf "Error loading remote content from: %s" $url -}}
            {{- $content = replace $content $shortcodeFound "**Error:** Unable to load remote content." -}}
        {{- end -}}
    {{- end -}}
{{- end -}}

{{- return $content -}}
