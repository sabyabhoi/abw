#!/bin/sh

TITLE=$(sed 's/# //; 1q' $1)

TEMP="${2:-template.html}"

if [[ ! -e $TEMP ]]; then
	echo "$TEMP does not exist. Getting it from github..."
	curl "https://raw.githubusercontent.com/sabyabhoi/abw/main/static/template.html"
fi

sed -e 's|{0}|'"$TITLE"'|g' $TEMP | head -n -2

tail -n +2 $1 | markdown

echo "</body></html>"
