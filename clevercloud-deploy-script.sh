#!/bin/bash

HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
DEST_BIN="${HOME}/.local/bin/"
FILENAME="hugo.tar.gz"

wget -O ${FILENAME} -q ${HUGO_URL}

mkdir -p ${DEST_BIN}
tar xvf ${FILENAME} -C ${DEST_BIN}
rm ${FILENAME}

hugo mod get -u
hugo --gc --minify --destination public
