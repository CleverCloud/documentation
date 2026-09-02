{{- /* Markdown output: same destination resolution as Hextra's
layouts/_markup/render-link.html (theme pinned to v0.12.3), without target/rel
and without the external-link arrow icon, which the HTML-to-Markdown conversion
turned into a stray space before punctuation. Diff against the theme file when
the Hextra module is bumped. */ -}}
{{- $dest := .Destination -}}
{{- $url := urls.Parse $dest -}}

{{- if and $dest (hasPrefix $dest "/") -}}
  {{- with or (.PageInner.GetPage $url.Path) (.PageInner.Resources.Get $url.Path) (resources.Get $url.Path) -}}
    {{- $query := cond $url.RawQuery (printf "?%s" $url.RawQuery) "" -}}
    {{- $fragment := cond $url.Fragment (printf "#%s" $url.Fragment) "" -}}
    {{- $dest = printf "%s%s%s" .RelPermalink $query $fragment -}}
  {{- else -}}
    {{- $hasBasePrefix := and (ne site.Home.RelPermalink "/") (hasPrefix $dest site.Home.RelPermalink) -}}
    {{- if not $hasBasePrefix -}}
      {{- $dest = (relURL (strings.TrimPrefix "/" $dest)) -}}
    {{- end -}}
  {{- end -}}
{{- end -}}

{{- with . -}}
<a href="{{ $dest | safeURL }}"{{ with .Title }} title="{{ . }}"{{ end }}>{{ .Text | safeHTML }}</a>
{{- end -}}
