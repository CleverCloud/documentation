{{- $content := . -}}
{{- $patternSearch := "\\{\\{%\\s*content/([^%}]+)\\s*%\\}\\}" -}}
{{- $patternClean := "\\{\\{%\\s*content/(.+?)\\s*%\\}\\}" -}}

{{- range $shortcodeFound := findRE $patternSearch $content -}}
    {{- $name := replaceRE $patternClean "$1" $shortcodeFound -}}
    {{- $filepath := printf "layouts/shortcodes/content/%s.md" $name -}}
    {{- with os.ReadFile $filepath -}}
        {{- $content = replace $content $shortcodeFound . -}}
    {{- end -}}
{{- end -}}

{{- return $content -}}
