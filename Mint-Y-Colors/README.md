### A new approach to please everyone
There are 16.7 million color possibilities. We can't make them all. We want to offer 11 or 12 of them. With the dark and darker variants, that makes 33 or 36.

This new approach here is to offer a smaller range of colors, focusing on the most popular, but with much more variations. Something for each one of us. So, there are some heavily subdued colors for the nostalgic people. And there are also some vibrant colors to bring some happiness into those rainy days. But most of this new Mint-Yz color palette is made of well-balanced colors for a flat, modern user interface.

This translates into having some dull colors taken from the old Mint-Y. Those old ones are renamed with the "Classic" suffix, so, you know what you get. On the opposite, there are a few others that are coming from the previous versions of this Mint-Yz. These are renamed with the "Shine" suffix so, they are also clearly identified. And then there are all the others, and that is the majority of this new Mint-Yz. All these colors that are not part of the "Classic" or "Shine" groups are coming from https://flatuicolors.com/. These are well balanced colors and they should suit most people.

### The files
* **Mint-Y-Variations SVG and PNG files:** This is where the colors were selected and adjusted. View them all there, grouped into one picture, one vision. (Mint-Y-Variations-src.svg linked)
* **constants.py:** All the #HEX values from Mint-Y-Variations.svg are there. This new file should replace the old https://github.com/linuxmint/mint-themes/blob/master/constants.py.

### message-colors.svg
Copy-Paste those lines from the message-colors.svg file:

    $link_color: #(LATESTCOLOR);
    $link_visited_color: #(LATESTCOLOR);
    //___
    $selection_mode_bg: $selected_bg_color;
    $selection_mode_fg: $selected_fg_color;
    $warning_color: #(LATESTCOLOR);
    $warning_fg_color: white;
    $error_color: #(LATESTCOLOR);
    $error_fg_color: white;
    $success_color: #(LATESTCOLOR);
    $destructive_color: #(LATESTCOLOR);
    $suggested_color: #(LATESTCOLOR);
    $question_color: #(LATESTCOLOR);
    //___
    $drop_target_color: #(LATESTCOLOR);

These lines replaces the corresponding ones in:

    ~/mint-themes/src/Mint-Y/gtk-3.0/sass/_colors.scss