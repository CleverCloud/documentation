{{- $content := . -}}
{{- $pattern := "\\{\\{%\\s*content\\s+\"(?P<name>[^\"]+)\"\\s*%\\}\\}" -}}

{{- range $shortcodeFound := findRE $pattern $content -}}
    {{- $name := replaceRE $pattern "${name}" $shortcodeFound -}}
    {{- $filepath := printf "layouts/shortcodes/content/%s.md" $name -}}
    {{- with os.ReadFile $filepath -}}
        {{- $content = replace $content $shortcodeFound . -}}
    {{- end -}}
{{- end -}}

{{- return $content -}}
