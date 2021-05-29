#!/bin/sh

if [[ -z $1 ]]; then
	echo "Usage: $0 <markdown file> <template file>"
	exit
fi

TITLE=$(sed 's/# //; 1q' $1)

TEMP="${2:-template.html}"

if [[ ! -e $TEMP ]]; then
	echo "$TEMP does not exist. Getting it from github..."
	curl "https://raw.githubusercontent.com/sabyabhoi/abw/main/template.html"
fi

sed -e 's|{0}|'"$TITLE"'|g' $TEMP | head -n -2

tail -n +2 $1 | markdown

echo "</body></html>"
