#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

HEX_ACCENTS = ["#9ab87c", "#8fa876", "#779559", "#9abe76", "#9ab87d", "#88a66a", "#81a65b"]
hex_colors = {}
hex_colors["Aqua"] = "#6cabcd"
hex_colors["Blue"] = "#5b73c4"
hex_colors["Brown"] = "#aa876a"
hex_colors["Grey"] = "#9d9d9d"
hex_colors["Orange"] = "#db9d61"
hex_colors["Pink"] = "#c76199"
hex_colors["Purple"] = "#8c6ec9"
hex_colors["Red"] = "#c15b58"
hex_colors["Sand"] = "#c8ac69"
hex_colors["Teal"] = "#5aaa9a"

RGB_ACCENTS = ["172, 205, 138"]
rgb_colors = {}
rgb_colors["Aqua"] = "108, 171, 205"
rgb_colors["Blue"] = "91, 115, 196"
rgb_colors["Brown"] = "170, 135, 106"
rgb_colors["Grey"] = "157,157,157"
rgb_colors["Orange"] = "219, 157, 97"
rgb_colors["Pink"] = "199, 97, 153"
rgb_colors["Purple"] = "140, 110, 201"
rgb_colors["Red"] = "193, 91, 88"
rgb_colors["Sand"] = "200, 172, 105"
rgb_colors["Teal"] = "90, 170, 154"

# Mint-Y variations
os.system("rm -rf src/Mint-Y/variations")
os.system("mkdir -p src/Mint-Y/variations")

curdir = os.getcwd()

for color in rgb_colors.keys():

    variation = "src/Mint-Y/variations/%s" % color
    print("updating %s" % variation)
    os.system("mkdir -p %s/gtk-2.0" % variation)
    os.system("mkdir -p %s/gtk-3.0" % variation)

    # Copy assets files
    assets = []
    assets.append("gtk-2.0/assets.svg")
    assets.append("gtk-2.0/assets-dark.svg")
    assets.append("gtk-3.0/assets.svg")

    files = []
    files.append("gtk-2.0/assets")
    files.append("gtk-2.0/assets-dark")
    files.append("gtk-2.0/assets.txt")
    files.append("gtk-2.0/render-assets.sh")
    files.append("gtk-2.0/render-dark-assets.sh")
    files.append("gtk-3.0/assets")
    files.append("gtk-3.0/assets.txt")
    files.append("gtk-3.0/render-assets.sh")

    for file in files:
        os.system("cp -R src/Mint-Y/%s %s/%s" % (file, variation, file))
    for asset in assets:
        os.system("cp -R src/Mint-Y/%s %s/%s" % (asset, variation, asset))

    # Colorize assets svg
    for asset in assets:
        asset_path = "%s/%s" % (variation, asset)
        for accent in HEX_ACCENTS:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(file)s" % {'accent': accent, 'color_accent': hex_colors[color], 'file': asset_path})

    # Render assets
    os.chdir(variation)
    os.chdir("gtk-2.0")
    os.system("rm -rf assets/*")
    os.system("rm -rf assets-dark/*")
    os.system("./render-assets.sh")
    os.system("./render-dark-assets.sh")
    os.chdir("../gtk-3.0/")
    os.system("rm -rf assets/*")
    os.system("./render-assets.sh")
    os.chdir(curdir)
