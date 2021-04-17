#! /bin/bash

# WARNING: "--export-filename" is for Inkscape >= 1.0

INKSCAPE="/usr/bin/inkscape"

SRC_FILE="assets.svg"
DARK_SRC_FILE="assets-dark.svg"
ASSETS_DIR="../xfwm4"
DARK_ASSETS_DIR="../xfwm4-dark"
INDEX="assets.txt"

for i in `cat $INDEX`
do

if [ -f $ASSETS_DIR/$i.xpm ]; then
    echo $ASSETS_DIR/$i.xpm exists.
else
    echo
    echo Rendering $ASSETS_DIR/$i.png and converting to xpm
    $INKSCAPE --export-id=$i \
          --export-id-only \
          --export-filename=$ASSETS_DIR/$i.png $SRC_FILE >/dev/null \
    && convert $ASSETS_DIR/$i.png $ASSETS_DIR/$i.xpm
    rm -f $ASSETS_DIR/$i.png
fi
if [ -f $DARK_ASSETS_DIR/$i.xpm ]; then
    echo $DARK_ASSETS_DIR/$i.xpm exists.
else
    echo
    echo Rendering $DARK_ASSETS_DIR/$i.png and converting to xpm
    $INKSCAPE --export-id=$i \
          --export-id-only \
          --export-filename=$DARK_ASSETS_DIR/$i.png $DARK_SRC_FILE >/dev/null \
    && convert $DARK_ASSETS_DIR/$i.png $DARK_ASSETS_DIR/$i.xpm
    rm -f $DARK_ASSETS_DIR/$i.png
fi
done
exit 0
