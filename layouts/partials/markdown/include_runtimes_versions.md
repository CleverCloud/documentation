{{- $content := . -}}
{{- $runtimesPattern := "\\{\\{<\\s*runtimes_versions\\s+([^>]+)\\s*>\\}\\}" -}}

{{- range $runtimeFound := findRE $runtimesPattern $content -}}
    {{- $runtime := replaceRE $runtimesPattern "$1" $runtimeFound -}}
    {{- $runtime = trim $runtime " " -}}
    {{- $versions := index site.Data.runtime_versions $runtime -}}
    {{- $output := "" -}}
    {{- with $versions -}}
        {{- if .default -}}
            {{- $output = printf "%s### Default version\n" $output -}}
            {{- range .default -}}
                {{- $output = printf "%s- %s\n" $output . -}}
            {{- end -}}
        {{- end -}}

        {{- if .accepted -}}
            {{- $output = printf "%s\n### Accepted version(s)\n" $output -}}
            {{- range .accepted -}}
                {{- $output = printf "%s- %s\n" $output . -}}
            {{- end -}}
        {{- end -}}

        {{- if .eol_source -}}
            {{- $output = printf "%s\nCheck the [end-of-life (EOL)](%s) status of these versions." $output .eol_source -}}
        {{- end -}}
    {{- end -}}

    {{- $content = replace $content $runtimeFound $output -}}
{{- end -}}

{{- return $content -}}
