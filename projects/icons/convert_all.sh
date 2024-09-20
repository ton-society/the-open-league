#!/bin/bash
target="$1"
hashes="$2"

IFS=$'\n'

for file in `find . -iname "*png"`
do
	h=$(md5sum "$file" | awk '{print $1}')
	key="$hashes/${file}_$h"
	if ! [ -f $key  ]
	then
		echo "Flag is not exists for $key"
		touch "$key"
		convert "${file}" \
		        -gravity Center \
		        \( -size 100x100 \
		           xc:Black \
		           -fill White \
		           -draw 'circle 50 50 50 1' \
		           -alpha Copy \
		        \) -compose CopyOpacity -composite \
		        "${target}/${file}"
	else
		echo "No changes for $file"
	fi
done
IFS=$' '