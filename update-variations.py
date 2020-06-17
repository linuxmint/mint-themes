#!/usr/bin/python3
import os
import sys

from constants import Y_HEX_ACCENT1, Y_HEX_ACCENT2, Y_HEX_ACCENT3, Y_HEX_ACCENT4
from constants import y_hex_colors1, y_hex_colors2, y_hex_colors3, y_hex_colors4

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

def usage ():
    print ("Usage: update-variations.py color")
    print ("color can be one name like 'Aqua' or 'Blue', or just 'All'.")
    sys.exit(1)

def update_color (color):
    variation = "src/Mint-Y/variations/%s" % color
    print("updating %s" % variation)
    os.system("rm -rf %s" % variation)
    os.system("mkdir -p %s/cinnamon" % variation)
    os.system("mkdir -p %s/gtk-2.0" % variation)
    os.system("mkdir -p %s/gtk-3.0" % variation)
    os.system("mkdir -p %s/xfwm4-src" % variation)

    # Copy assets files
    assets = []
    assets.append("cinnamon/mint-y-thumbnails-src.svg")
    assets.append("gtk-2.0/assets.svg")
    assets.append("gtk-2.0/assets-dark.svg")
    assets.append("gtk-3.0/assets.svg")
    assets.append("xfwm4-src/assets.svg")
    assets.append("xfwm4-src/assets-dark.svg")

    files = []
    files.append("cinnamon/render-cin-thumbnails.sh")
    files.append("gtk-2.0/assets") # copy this to delete assets/* later!?
    files.append("gtk-2.0/assets-dark") # copy this to delete assets-dark/* later!?
    files.append("gtk-2.0/assets.txt")
    files.append("gtk-2.0/menubar-toolbar")
    files.append("gtk-2.0/render-assets.sh")
    files.append("gtk-2.0/render-dark-assets.sh")
    files.append("gtk-3.0/assets") # copy this to delete assets/* later!?
    files.append("gtk-3.0/assets.txt")
    files.append("gtk-3.0/render-assets.sh")
    files.append("xfwm4-src/xfwm4")
    files.append("xfwm4-src/xfwm4-dark")
    files.append("xfwm4-src/assets.txt")
    files.append("xfwm4-src/render-assets.sh")

    for file in files:
        os.system("cp -R src/Mint-Y/%s %s/%s" % (file, variation, file))
    for asset in assets:
        os.system("cp -R src/Mint-Y/%s %s/%s" % (asset, variation, asset))

    # Update assets svg
    for asset in assets:
        asset_path = "%s/%s" % (variation, asset)
        for accent in Y_HEX_ACCENT1:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors1[color], 'file': asset_path})
        for accent in Y_HEX_ACCENT2:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors2[color], 'file': asset_path})
        for accent in Y_HEX_ACCENT3:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors3[color], 'file': asset_path})
        for accent in Y_HEX_ACCENT4:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors4[color], 'file': asset_path})

    # Render assets
    os.chdir(variation)
    os.chdir("cinnamon")
    os.system("./render-cin-thumbnails.sh")
    os.chdir("../gtk-2.0/")
    os.system("rm -rf assets/*")
    os.system("rm -rf assets-dark/*")
    os.system("./render-assets.sh")
    os.system("./render-dark-assets.sh")
    os.chdir("../gtk-3.0/")
    os.system("rm -rf assets/*")
    os.system("./render-assets.sh")
    # No "rm -rf assets/*" in xfwm4: render-assets.sh deletes the color ones only.
    os.chdir("../xfwm4-src/")
    os.system("./render-assets.sh")
    os.chdir(curdir)

if len(sys.argv) < 2:
    usage()
else:
    color_variation = sys.argv[1]
    if not color_variation in ["Aqua", "Blue", "BlueTwo", "Brown", "Grey", "Minty", "MintyTwo", "Orange", "Pink", "Purple", "Red", "All"]:
        usage()

# Mint-Y variations
curdir = os.getcwd()

if color_variation == "All":
    for color in y_hex_colors1.keys():
        update_color(color)
else:
    update_color(color_variation)
