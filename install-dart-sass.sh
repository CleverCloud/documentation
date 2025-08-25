#!/bin/bash
set -e

URL="https://github.com/sass/dart-sass/releases/download/$DART_SASS_VERSION/dart-sass-$DART_SASS_VERSION-linux-x64.tar.gz"

curl -fsSL "$URL" | tar -xz -C "$HOME/.local/bin" --strip-components=1
echo "Dart Sass $VERSION installed to ~/.local/bin/sass"
