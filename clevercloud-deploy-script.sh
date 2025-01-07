wget https://github.com/gohugoio/hugo/releases/download/v$HUGO_VERSION/hugo_extended_"$HUGO_VERSION"_Linux-64bit.tar.gz
tar xvf hugo_extended_"$HUGO_VERSION"_Linux-64bit.tar.gz
chmod +x ./hugo
./hugo mod get github.com/imfing/hextra@$HEXTRA_VERSION
./hugo --gc --minify --destination public/developers
echo "AddType text/markdown;charset=UTF-8 .md" > public/.htaccess
