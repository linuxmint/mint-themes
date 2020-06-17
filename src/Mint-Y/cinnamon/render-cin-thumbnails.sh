#! /bin/bash

INKSCAPE="/usr/bin/inkscape"
OPTIPNG="/usr/bin/optipng"
SRC_FILE="mint-y-thumbnails-src.svg"
INDEX='mint-y-thumbnail mint-y-dark-thumbnail'

for i in $INDEX
do
if [ -f $i.png ]; then
    echo $i.png exists.
else
    echo
    echo Rendering $i.png
    $INKSCAPE --export-id=$i \
              --export-id-only \
              --export-filename=$i.png $SRC_FILE >/dev/null \
    && $OPTIPNG -o7 --quiet $i.png
fi
done
exit 0
