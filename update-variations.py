#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

# Mint-Y
Y_HEX_ACCENT1 = ["#9ab87c"]  # BASE
Y_HEX_ACCENT2 = ["#8fa876"]
Y_HEX_ACCENT3 = ["#afca95"]  # PRELIGHT/HOVER
Y_HEX_ACCENT4 = ["#779559"]  # PRESSED

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

y_hex_colors3 = {}
y_hex_colors3["Aqua"] = "#82b3ce"
y_hex_colors3["Blue"] = "#6e82c6"
y_hex_colors3["Brown"] = "#ad9078"
y_hex_colors3["Grey"] = "#a3a3a3"
y_hex_colors3["Orange"] = "#dcaa7a"
y_hex_colors3["Pink"] = "#c975a3"
y_hex_colors3["Purple"] = "#9b84cb"
y_hex_colors3["Red"] = "#d1716f"
y_hex_colors3["Sand"] = "#c9b27c"
y_hex_colors3["Teal"] = "#6dbbab"

y_hex_colors4 = {}
y_hex_colors4["Aqua"] = "#52819a"
y_hex_colors4["Blue"] = "#4b5a8d"
y_hex_colors4["Brown"] = "#796555"
y_hex_colors4["Grey"] = "#727272"
y_hex_colors4["Orange"] = "#a97747"
y_hex_colors4["Pink"] = "#924d73"
y_hex_colors4["Purple"] = "#6a5497"
y_hex_colors4["Red"] = "#9a4a47"
y_hex_colors4["Sand"] = "#947f51"
y_hex_colors4["Teal"] = "#4e8378"

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

    # Colorize GTK2 toolbar-menubar (these assets aren't generated)
    for variant in ["", "-Dark", "-Darker"]:
        path = "files/usr/share/themes/Mint-Y%s-%s/gtk-2.0/menubar-toolbar" % (variant, color)
        if os.path.exists(path):
            for filename in os.listdir(path):
                p = os.path.join(path, filename)
                os.system("./colorize.py %s %s" % (p, color))
