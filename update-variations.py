#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

# Mint-Y
Y_HEX_ACCENT1 = ["#9ab87c", "779559", "9abe76"]
Y_HEX_ACCENT2 = ["#8fa876"]

y_hex_colors1 = {}
y_hex_colors1["Aqua"] = "#6cabcd"
y_hex_colors1["Blue"] = "#5b73c4"
y_hex_colors1["Brown"] = "#aa876a"
y_hex_colors1["Grey"] = "#9d9d9d"
y_hex_colors1["Orange"] = "#db9d61"
y_hex_colors1["Pink"] = "#c76199"
y_hex_colors1["Purple"] = "#8c6ec9"
y_hex_colors1["Red"] = "#c15b58"
y_hex_colors1["Sand"] = "#c8ac69"
y_hex_colors1["Teal"] = "#5aaa9a"

y_hex_colors2 = {}
y_hex_colors2["Aqua"] = "#6aa0bd"
y_hex_colors2["Blue"] = "#596eb5"
y_hex_colors2["Brown"] = "#9c7e65"
y_hex_colors2["Grey"] = "#8f8f8f"
y_hex_colors2["Orange"] = "#cc9560"
y_hex_colors2["Pink"] = "#b85f90"
y_hex_colors2["Purple"] = "#866cba"
y_hex_colors2["Red"] = "#b35a57"
y_hex_colors2["Sand"] = "#b89f65"
y_hex_colors2["Teal"] = "#579c8e"

# Mint-Y variations
os.system("rm -rf src/Mint-Y/variations")
os.system("mkdir -p src/Mint-Y/variations")

curdir = os.getcwd()

for color in y_hex_colors1.keys():

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
        for accent in Y_HEX_ACCENT1:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors1[color], 'file': asset_path})
        for accent in Y_HEX_ACCENT2:
            os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors2[color], 'file': asset_path})

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
