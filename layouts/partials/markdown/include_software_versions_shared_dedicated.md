{{- $content := . -}}
{{- $versionsPattern := "\\{\\{<\\s*software_versions_shared_dedicated\\s+([^>]+)\\s*>\\}\\}" -}}

{{- range $versionFound := findRE $versionsPattern $content -}}
    {{- $dbname := replaceRE $versionsPattern "$1" $versionFound -}}
    {{- $versions := index site.Data.software_versions_shared_dedicated $dbname -}}
    {{- $output := "### Regular versions\n" -}}
    {{- with $versions.dedicated -}}
        {{- range . -}}
            {{- $output = printf "%s- %s\n" $output . -}}
        {{- end -}}
    {{- end -}}
    {{- if $versions.dev -}}
        {{- $output = printf "%s\n### DEV plan\n" $output -}}
        {{- range $versions.dev -}}
            {{- $output = printf "%s- %s\n" $output . -}}
        {{- end -}}
        {{- $output = printf "%s\n%s" $output site.Data.software_versions_shared_dedicated.dev_message -}}
    {{- end -}}
    {{- $content = replace $content $versionFound $output -}}
{{- end -}}

{{- return $content -}}
