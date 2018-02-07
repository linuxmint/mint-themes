#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

ACCENT = "#9ab87c"

colors = {}
colors["Aqua"] = "#6cabcd"
colors["Blue"] = "#5b73c4"
colors["Brown"] = "#aa876a"
colors["Grey"] = "#9d9d9d"
colors["Orange"] = "#db9d61"
colors["Pink"] = "#c76199"
colors["Purple"] = "#8c6ec9"
colors["Red"] = "#c15b58"
colors["Sand"] = "#c8ac69"
colors["Teal"] = "#5aaa9a"

if os.path.exists("usr"):
    os.system("rm -rf usr/")

os.system("mkdir -p usr/share/themes")

os.system("cp -R Mint-X/theme/* usr/share/themes/")

for color in os.listdir("Mint-X/variations"):
    path = os.path.join("Mint-X/variations", color)
    if os.path.isdir(path):
        theme = "usr/share/themes/Mint-X-%s" % color
        theme_index = os.path.join(theme, "index.theme")
        gtkrc = os.path.join(theme, "gtk-2.0", "gtkrc")
        os.system("cp -R usr/share/themes/Mint-X %s" % theme)
        os.system("cp -R Mint-X/variations/%s/* %s/" % (color, theme))
        for key in ["Name", "GtkTheme", "IconTheme"]:
            change_value(key, "Mint-X-%s" % color, theme_index)
        os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(gtkrc)s" % {'accent': ACCENT, 'color_accent': colors[color], 'gtkrc': gtkrc})

os.system("cp -R files/* ./")
