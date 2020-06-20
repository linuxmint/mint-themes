![auto branch icon](https://github.com/SebastJava/mint-themes/blob/auto/0-auto-branch-icon.svg)
# Automated color updates (wip)
This branch is only for adding automated color updates, making Mint-Y build now 100% automated. Before, some parts had to be done by hand.  

Please take note the `colorize.py` script got deleted because it only changed hues, not saturation and lightness. And `files/usr/share/themes/` got deleted also, as it is not being used anymore. Now everything is 100% automated, the right way. I am not pretending to be a professional programmer. I just looked at the scripts already existing there in linuxmint/mint-themes, i saw how things were done, and i just carefully added some additional lines, basically.

### Required
If you want to build your own theme, you will need to install those packages:  
  * Inkscape, preferably version 1.0 or higher  
  * optipng  
  * imagemagick

### Warning
There are a few `render-assets.sh` scripts scattered around the `src/Mint-Y` directory and its sub-directories. They contain some `--export-filename` or `--export-png` Inkscape commands. Check that you have the required command for your version of Inkscape, or just replace as required:  

  * Inkscape version 1.0 or higher: `--export-filename`  
  * Inkscape version 0.x: `--export-png`
