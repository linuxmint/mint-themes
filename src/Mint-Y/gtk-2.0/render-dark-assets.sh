#! /bin/bash

# WARNING: "--export-filename" is for Inkscape >= 1.0

INKSCAPE="/usr/bin/inkscape"
OPTIPNG="/usr/bin/optipng"

SRC_FILE="assets-dark.svg"
ASSETS_DIR="assets-dark"
INDEX="assets.txt"

for i in `cat $INDEX`
do
if [ -f $ASSETS_DIR/$i.png ]; then
    echo $ASSETS_DIR/$i.png exists.
else
    echo
    echo Rendering $ASSETS_DIR/$i.png
    $INKSCAPE --export-id=$i \
              --export-id-only \
              --export-filename=$ASSETS_DIR/$i.png $SRC_FILE >/dev/null \
    && $OPTIPNG -o7 --quiet $ASSETS_DIR/$i.png
fi
done

cp -f $ASSETS_DIR/menubar_button.png menubar-toolbar/menubar_button-dark.png
cp -f $ASSETS_DIR/toolbar-entry-border-active-bg.png menubar-toolbar/toolbar-entry-border-active-bg-dark.png

exit 0
