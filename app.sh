#!/bin/sh

TITLE=$(sed 's/# //; 1q' $1)

sed -e 's|{0}|'"$TITLE"'|g' ./static/template.html | head -n -2

tail -n +2 $1 | markdown

echo "</body></html>"
