*early-pre-beta-release (Not complete yet!)*
## Mint-Y new colors: Pure. Vitaminized. And readable.

I started working on this fork on 2020-02-11. It is a work-in-progress. I will probably send pull requests to linuxmint/mint-themes from here.

All the new Mint-Y colors are here except the Mint green. We will talk about Mint green later.

**Ready to install and test:**

`cp -R usr/share/themes/* ~/.themes/` (this is early-pre-beta-release!)

**If you want to build your own version, do as follow:**

  * Install **Optipng** and **Sassc**.
  * Take the time to explore and understand the mint-themes directory and sub-directories, and then make your changes.
  * Run **update-variations.py** first, and then **generate-themes.py**.
  * Move files/usr/share/themes/ or usr/share/themes/ to /usr/share/themes/ if not already done automatically. As superuser. You could prefer to put your new themes in ~/.themes/ first, for (less dangerous) testing purposes. This ~/.themes/ overrides the other one, on your user account only.
  * Change your theme from your Preferences.

**Known issues:**

  * Mint green is still the old one.
  * New thumbnails are not done yet, so at first sight, in cinnamon-settings themes, nothing looks new! But just click and see...
  * usr/share/themes/Mint-Y-(colors)/gtk-2.0/menubar-toolbar/(asset).png are apparently generated, but they remain in /assets/. So these are still the old green ones. (I am not using colorize.py; this needs further investigation...)

![Mint-Y-Variations-Pal-1a-10-LR.png preview](Mint-Y-Colors/Mint-Y-Variations-Pal-1a-10-LR.png)
