{{- /*
Markdown output of the include shortcode, ported from imfing/hextra#1044 until
Hextra ships it.

The HTML include renders the shortcodes of the included page through
RenderShortcodes, with their HTML templates, so cards, tabs or callouts would
reach utils/html-to-markdown.md as HTML instead of going through their
*.markdown.md variants. Here, a page without shortcodes is inserted as is, so
the including page renders it in place, list indentation included. A page with
shortcodes, which start with "{{<" or "{{%", renders them with the templates of
this output format, then converts the result back to Markdown, so that it
doesn't depend on markup.goldmark.renderer.unsafe. Such a page is rendered on
its own, so this output has known limits: an escaped shortcode example stays
escaped, reference links and footnotes defined in the including page don't
resolve, and its own footnotes restart at 1.

@param {string} (positional parameter 0) The path to the page, relative to the content directory.

@example {{% include "functions/_common/glob-patterns" %}}
*/ -}}

{{- with .Get 0 -}}
  {{- with site.GetPage . -}}
    {{- if findRE `\{\{[<%]` .RawContent 1 -}}
      {{- $html := .RawContent | $.Page.RenderString (dict "display" "block") -}}
      {{- partial "utils/html-to-markdown.md" (dict "page" $.Page "html" $html) -}}
    {{- else -}}
      {{- .RawContent -}}
    {{- end -}}
  {{- else -}}
    {{- errorf "The %q shortcode was unable to find %q. See %s" $.Name . $.Position -}}
  {{- end -}}
{{- else -}}
  {{- errorf "The %q shortcode requires a positional parameter indicating the path of the file to include. See %s" .Name .Position -}}
{{- end -}}
