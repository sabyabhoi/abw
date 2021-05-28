#!/bin/sh

TITLE=$(sed 's/# //; 1q' $1)

sed -e 's|{0}|'"$TITLE"'|g' ./static/template.html

tail -n +2 $1 | markdown

echo "</body></html>"
