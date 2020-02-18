# Mint-Y-Colors
*by SebastJava*

This Mint-Y-Colors directory contains no essential program or data files. This directory contains the source color tables to be used (copy-paste) in **update-variations.py,** **generate-themes.py,** icons and possibly other places.

**0-Old-Archives/Mint-Y-Colors-40**: this is the old starting base. Colors were initially set there. And color contrasts were adjusted when needed to get at least a 3:1 color contrast with the white foreground text. Later, column 1a was used to build the subsequent Mint-Y-Variations-Pal-1a-xx. Some of these #HEX colors values got slightly readjusted when building this Mint-Y-Variations-Pal-1a-xx, because... it is only when making this Mint-Y-Variations-Pal-1a-xx that i considered the contrast between the colors and a dark theme background, in addition to the previously considered white foreground text. This is just to say please refer to Mint-Y-Variations-Pal-1a-xx for up-to-date values.

**Mint-Y-Variations-Pal-1a-10**: These are all the new current color values, except the Mint green. Mint green is still undetermined as of 2020-02-18. This Mint-Y-Variations-Pal-1a-xx contains the new accent colors on column 1, and their corresponding variants for dark themes on column 2, and there is also columns 3 and 4 for hover and pressed button states. This file is the source color table used or to be used in update-variations.py, generate-themes.py, icons and possibly other places.

**messages-colors**: This is were you can see (svg file) and copy-paste (txt file) proposed subtle changes for variables like $link_color and $suggested_color in src/Mint-Y/gtk-3.0/sass/_colors.scss and in the gtk-2.0 directory.