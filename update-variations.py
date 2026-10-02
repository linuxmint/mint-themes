#!/usr/bin/python3
import os
import sys
import threading

from constants import Y_HEX_ACCENT1, Y_HEX_ACCENT2
from constants import y_hex_colors1, y_hex_colors2

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

def usage ():
    print ("Usage: update-variations.py color")
    print ("color can be 'Aqua', 'Blue', 'Grey', 'Orange', 'Pink', 'Purple', 'Red', 'Sand', 'Teal' or 'All'.")
    sys.exit(1)

def renderGtk2(variation:str):
    os.system(f"""
        cd {variation}/gtk-2.0
        rm -rf assets/*
        rm -rf assets-dark/*
        ./render-assets.sh
        ./render-dark-assets.sh
    """)

def renderGtk(variation:str, gtk:str):
    os.system(f"""
        cd {variation}/{gtk}
        rm -rf assets/*
        ./render-assets.sh
    """)

def renderXfce4(variation:str, style:str):
    os.system(f"""
        cd {variation}/{style}
        rm -rf *.png
        ./render-assets.sh
    """)

def update_color (color):
    variation = "src/Mint-Y/variations/%s" % color
    print("updating %s" % variation)
    os.system("rm -rf %s" % variation)
    os.system("mkdir -p %s/gtk-2.0" % variation)
    os.system("mkdir -p %s/gtk-3.0" % variation)
    os.system("mkdir -p %s/gtk-4.0" % variation)
    os.system("mkdir -p %s/xfwm4" % variation)
    os.system("mkdir -p %s/xfwm4-dark" % variation)

    # Copy assets files
    assets = []
    assets.append("gtk-2.0/assets.svg")
    assets.append("gtk-2.0/assets-dark.svg")
    assets.append("gtk-3.0/assets.svg")
    assets.append("gtk-4.0/assets.svg")
    assets.append("xfwm4/assets.svg")
    assets.append("xfwm4-dark/assets.svg")

    files = []
    files.append("gtk-2.0/assets")
    files.append("gtk-2.0/assets-dark")
    files.append("gtk-2.0/assets.txt")
    files.append("gtk-2.0/render-assets.sh")
    files.append("gtk-2.0/render-dark-assets.sh")
    files.append("gtk-3.0/assets")
    files.append("gtk-3.0/assets.txt")
    files.append("gtk-3.0/render-assets.sh")
    files.append("gtk-4.0/assets")
    files.append("gtk-4.0/assets.txt")
    files.append("gtk-4.0/render-assets.sh")
    files.append("xfwm4/render-assets.sh")
    files.append("xfwm4/assets.txt")
    files.append("xfwm4-dark/render-assets.sh")
    files.append("xfwm4-dark/assets.txt")

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

    # Render assets

    threads = []
    threads.append(threading.Thread(target=renderGtk2, args=(variation,)))
    threads.append(threading.Thread(target=renderGtk, args=(variation, "gtk-3.0")))
    threads.append(threading.Thread(target=renderGtk, args=(variation, "gtk-4.0")))
    threads.append(threading.Thread(target=renderXfce4, args=(variation, "xfwm4")))
    threads.append(threading.Thread(target=renderXfce4, args=(variation, "xfwm4-dark")))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if len(sys.argv) < 2:
    usage()
else:
    color_variation = sys.argv[1]
    if not color_variation in ["Aqua", "Blue", "Grey", "Orange", "Pink", "Purple", "Red", "Sand", "Teal", "All"]:
        usage()

# Mint-Y variations
curdir = os.getcwd()

if color_variation == "All":
    threads = []
    for color in y_hex_colors1.keys():
        t = threading.Thread(target=update_color, args=(color,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
else:
    update_color(color_variation)

os.chdir(curdir)
