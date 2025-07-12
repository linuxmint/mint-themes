#! /bin/bash

INKSCAPE="inkscape"
OPTIPNG="optipng"

SRC_FILE="assets.svg"
ASSETS_DIR="."

INDEX="assets.txt"

# check command avalibility
has_command() {
  "$1" -v $1 > /dev/null 2>&1
}

mkdir -p $ASSETS_DIR

for i in `cat $INDEX`
do
if ! [ -f $ASSETS_DIR/$i.png ]; then
    echo Rendering $ASSETS_DIR/$i.png

    $INKSCAPE --export-id=$i \
              --export-id-only \
              --export-filename=$ASSETS_DIR/$i.png $SRC_FILE >/dev/null
    $OPTIPNG -o7 --quiet $ASSETS_DIR/$i.png
fi
done

if ! [ -f title-2-active.png ]; then
  ln -s title-1-active.png title-2-active.png
  ln -s title-1-active.png title-3-active.png
  ln -s title-1-active.png title-4-active.png
  ln -s title-1-active.png title-5-active.png
  ln -s title-1-inactive.png title-2-inactive.png
  ln -s title-1-inactive.png title-3-inactive.png
  ln -s title-1-inactive.png title-4-inactive.png
  ln -s title-1-inactive.png title-5-inactive.png
fi

exit 0
