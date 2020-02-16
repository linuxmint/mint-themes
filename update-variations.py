#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

# Mint-Y old green
Y_HEX_ACCENT1 = ["#92b372"]  # BASE
Y_HEX_ACCENT2 = ["#8fa876"]  # BASE-DARK
Y_HEX_ACCENT3 = ["#afca95"]  # PRELIGHT/HOVER
Y_HEX_ACCENT4 = ["#779559"]  # PRESSED
# Mint-Y new colors
y_hex_colors1 = {}
y_hex_colors1["Aqua"] = "#0BB2B4"
y_hex_colors1["Blue"] = "#0D91D3"
y_hex_colors1["Brown"] = "#7F542B"
y_hex_colors1["Grey"] = "#767676"
y_hex_colors1["Orange"] = "#EF6410"
y_hex_colors1["Pink"] = "#E54980"
y_hex_colors1["Purple"] = "#B41AB4"
y_hex_colors1["Red"] = "#DF2121"
y_hex_colors1["Sand"] = "#927D4E"
y_hex_colors1["Teal"] = "#008080"

y_hex_colors2 = {}
y_hex_colors2["Aqua"] = "#0BA0A1"
y_hex_colors2["Blue"] = "#0C81BC"
y_hex_colors2["Brown"] = "#7F542B"
y_hex_colors2["Grey"] = "#767676"
y_hex_colors2["Orange"] = "#DF5807"
y_hex_colors2["Pink"] = "#D93D74"
y_hex_colors2["Purple"] = "#9E22A0"
y_hex_colors2["Red"] = "#CA1E1E"
y_hex_colors2["Sand"] = "#927D4E"
y_hex_colors2["Teal"] = "#007474"

y_hex_colors3 = {}
y_hex_colors3["Aqua"] = "#5DCCCD"
y_hex_colors3["Blue"] = "#5EB6E2"
y_hex_colors3["Brown"] = "#AA8D72"
y_hex_colors3["Grey"] = "#A4A4A4"
y_hex_colors3["Orange"] = "#F49860"
y_hex_colors3["Pink"] = "#EE86AA"
y_hex_colors3["Purple"] = "#CD66CD"
y_hex_colors3["Red"] = "#EA6B6B"
y_hex_colors3["Sand"] = "#B6A889"
y_hex_colors3["Teal"] = "#55AAAA"

y_hex_colors4 = {}
y_hex_colors4["Aqua"] = "#087778"
y_hex_colors4["Blue"] = "#09618D"
y_hex_colors4["Brown"] = "#55381D"
y_hex_colors4["Grey"] = "#4F4F4F"
y_hex_colors4["Orange"] = "#9F430B"
y_hex_colors4["Pink"] = "#993155"
y_hex_colors4["Purple"] = "#781178"
y_hex_colors4["Red"] = "#951616"
y_hex_colors4["Sand"] = "#615334"
y_hex_colors4["Teal"] = "#005555"

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
    os.chdir("gtk-2.0")
    os.system("rm -rf assets/*")
    os.system("rm -rf assets-dark/*")
    os.system("./render-assets.sh")
    os.system("./render-dark-assets.sh")
    os.chdir("../gtk-3.0/")
    os.system("rm -rf assets/*")
    os.system("./render-assets.sh")
    os.chdir(curdir)
