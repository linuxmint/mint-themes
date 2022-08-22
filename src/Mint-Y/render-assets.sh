#! /bin/bash

INKSCAPE="/usr/bin/inkscape"
OPTIPNG="/usr/bin/optipng"

INDEX="assets.txt"
if [[ $1 != "-dark" ]]; then
    SRC_FILE="assets.svg"
    ASSETS_DIR="assets"
else
    SRC_FILE="assets"$1".svg"
    ASSETS_DIR="assets"$1
fi
mkdir -p $ASSETS_DIR

render()
{
    echo Rendering $1
    if [[ "$1" == *"@2"* ]]; then
        $INKSCAPE --export-id=$2 --export-dpi=192 \
                "${INKSCAPE_OPTS[@]}" $1 $SRC_FILE >/dev/null 2>&1 \
        && $OPTIPNG -o7 --quiet $1
    else
        $INKSCAPE --export-id=$2 "${INKSCAPE_OPTS[@]}" $1 $SRC_FILE >/dev/null 2>&1 \
        && $OPTIPNG -o7 --quiet $1
    fi
}

# Set options for Inkscape depending on version.
INKSCAPE_OPTS=( --export-id-only )
case $($INKSCAPE -V | cut -d' ' -f2) in
    # NB: The export option (-e or -o) must be the last option in the INKSCAPE_OPTS array.
    0.*) INKSCAPE_OPTS+=('-z' '-e');; # -z specifies not to launch GUI, -e is export
    1.*) INKSCAPE_OPTS+=('-o');;      # v1.0+ uses no GUI by default, -e replaced by -o
esac

for i in `cat $INDEX`
do 
    if [ -f $ASSETS_DIR/$i.png ]; then
        echo $ASSETS_DIR/$i.png exists.
    else
        render $ASSETS_DIR/$i.png $i &
        # allow only to execute number of jobs in parallel
        # equal to number of processors
        if [[ $(jobs -r -p | wc -l) -gt $(nproc) ]]; then
        # wait only for first job
        wait $(jobs -p)
        fi
    fi
    if [[ $1 == "s2" ]]; then
        if [ -f $ASSETS_DIR/$i@2.png ]; then
            echo $ASSETS_DIR/$i@2.png exists.
        else
            render $ASSETS_DIR/$i@2.png $i &
            # allow only to execute number of jobs in parallel
            # equal to number of processors
            if [[ $(jobs -r -p | wc -l) -gt $(nproc) ]]; then
            # wait only for first job
            wait $(jobs -p)
            fi
        fi
    fi
done
exit 0
