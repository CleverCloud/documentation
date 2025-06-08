#! /bin/bash

hugo --gc --minify
echo "AddType text/markdown;charset=UTF-8 .md" > public/.htaccess
