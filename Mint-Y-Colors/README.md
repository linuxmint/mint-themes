### message-colors.svg use:

Copy-Paste those lines from the **svg file:**

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