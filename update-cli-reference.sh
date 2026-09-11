#!/usr/bin/env bash
# Regenerate the CLI reference page from the documentation of a Clever Tools release
# Usage: ./update-cli-reference.sh [VERSION], defaults to the latest release
set -euo pipefail

FILE="content/doc/cli-reference.md"
REPO="CleverCloud/clever-tools"

cd "$(dirname "$0")"

if [ ! -f "${FILE}" ]; then
  echo "${FILE} not found, its front matter is kept from one regeneration to the next" >&2
  exit 1
fi

VERSION="${1:-$(curl -fsSL "https://api.github.com/repos/${REPO}/releases/latest" | sed -nE 's/^[[:space:]]*"tag_name":[[:space:]]*"([^"]+)".*/\1/p')}"
if [ -z "${VERSION}" ]; then
  echo "Unable to find the latest Clever Tools release, pass a version as argument" >&2
  exit 1
fi
URL="https://raw.githubusercontent.com/${REPO}/refs/tags/${VERSION}/skills/clever-tools/references/full-documentation.md"

TMP="$(mktemp)"
trap 'rm -f "${TMP}" "${FILE}.new"' EXIT

# Download before writing anything, so a failed request leaves the page untouched
curl -fsSL "${URL}" -o "${TMP}"

{
  # Keep the front matter of the current page, it is maintained here, not upstream
  awk 'NR == 1 && $0 != "---" { exit 1 } { print } NR > 1 && $0 == "---" { exit }' "${FILE}"
  printf '\n<!-- markdownlint-disable MD036 -->\n\n'
  # Normalize the generated Markdown to pass the site's markdownlint rules
  perl -e '
    my ($in_code, $has_output, $need_blank, $prev) = (0, 0, 0, "");
    sub emit {
      my ($line) = @_;
      print "\n" if $need_blank && $has_output;
      print "$line\n";
      ($need_blank, $has_output, $prev) = (0, 1, $line);
    }
    # Apply a substitution outside inline code spans only
    sub outside_code {
      my ($line, $fn) = @_;
      my @parts = split /(`[^`]*`)/, $line;
      $_ = /^`/ ? $_ : $fn->($_) for @parts;
      return join "", @parts;
    }
    while (my $line = <STDIN>) {
      chomp $line;
      if ($in_code) {
        print "$line\n";
        $prev = $line;
        if ($line =~ /^```\s*$/) { $in_code = 0; $need_blank = 1 }
        next;
      }
      if ($line =~ /^```/) {
        $line = "```console" if $line =~ /^```\s*$/;
        $need_blank = 1;
        emit($line);
        $in_code = 1;
        next;
      }
      if ($line =~ /^\s*$/) { $need_blank = 1; next }
      $line =~ s/^>\s*(?=\S)/> /;
      $line =~ s{If you are using docker, use the image provided \[here\]\((https://hub\.docker\.com/[^)]+)\)}{If you are using Docker, use the [Clever Tools image from Docker Hub]($1)};
      $line = outside_code($line, sub {
        my ($text) = @_;
        $text =~ s/(?<![<\w])<([a-z][a-z0-9-]*)>/`<$1>`/g;
        $text =~ s{(?<![(<\[/\w])(https?://[^\s<>()]*[^\s<>().,;:!?])}{<$1>}g;
        return $text;
      });
      $need_blank = 1 if $line =~ /^- / && $prev ne "" && $prev !~ /^(- |\s)/;
      emit($line);
    }
  ' < "${TMP}"
} > "${FILE}.new"

mv "${FILE}.new" "${FILE}"
echo "${FILE} updated from Clever Tools ${VERSION}"
