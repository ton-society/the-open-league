name="$1"
cp "$name" tmp.png
convert tmp.png \
        -gravity Center \
        \( -size 100x100 \
           xc:Black \
           -fill White \
           -draw 'circle 50 50 50 1' \
           -alpha Copy \
        \) -compose CopyOpacity -composite \
        "$name"
