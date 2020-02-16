#!/usr/bin/python3
import os

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

def x_colorize_directory (path, variation):
    for accent in X_HEX_ACCENTS:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, x_hex_colors[variation]))
    for accent in X_RGB_ACCENTS:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, x_rgb_colors[variation]))

def y_colorize_directory (path, variation):
    for accent in Y_HEX_ACCENT1:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors1[variation]))
    for accent in Y_HEX_ACCENT2:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors2[variation]))
    for accent in Y_HEX_ACCENT3:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors3[variation]))
    for accent in Y_HEX_ACCENT4:
        os.system("find %s -name '*.*' -type f -exec sed -i 's/%s/%s/gI' {}  \\;" % (path, accent, y_hex_colors4[variation]))

# Mint-X
X_HEX_ACCENTS = ["#9ab87c", "#accd8a"]

x_hex_colors = {}
x_hex_colors["Aqua"] = "#6cabcd"
x_hex_colors["Blue"] = "#5b73c4"
x_hex_colors["Brown"] = "#aa876a"
x_hex_colors["Grey"] = "#9d9d9d"
x_hex_colors["Orange"] = "#db9d61"
x_hex_colors["Pink"] = "#c76199"
x_hex_colors["Purple"] = "#8c6ec9"
x_hex_colors["Red"] = "#c15b58"
x_hex_colors["Sand"] = "#c8ac69"
x_hex_colors["Teal"] = "#5aaa9a"

X_RGB_ACCENTS = ["172, 205, 138", "#accd8a"]

x_rgb_colors = {}
x_rgb_colors["Aqua"] = "108, 171, 205"
x_rgb_colors["Blue"] = "91, 115, 196"
x_rgb_colors["Brown"] = "170, 135, 106"
x_rgb_colors["Grey"] = "157,157,157"
x_rgb_colors["Orange"] = "219, 157, 97"
x_rgb_colors["Pink"] = "199, 97, 153"
x_rgb_colors["Purple"] = "140, 110, 201"
x_rgb_colors["Red"] = "193, 91, 88"
x_rgb_colors["Sand"] = "200, 172, 105"
x_rgb_colors["Teal"] = "90, 170, 154"

if os.path.exists("usr"):
    os.system("rm -rf usr/")

os.system("mkdir -p usr/share/themes")

os.system("cp -R src/Mint-X/theme/* usr/share/themes/")

for color in os.listdir("src/Mint-X/variations"):
    path = os.path.join("src/Mint-X/variations", color)
    if os.path.isdir(path):
        theme = "usr/share/themes/Mint-X-%s" % color
        theme_index = os.path.join(theme, "index.theme")
        os.system("cp -R usr/share/themes/Mint-X %s" % theme)
        os.system("cp -R src/Mint-X/variations/%s/* %s/" % (color, theme))

        # Theme name
        for key in ["Name", "GtkTheme", "IconTheme"]:
            change_value(key, "Mint-X-%s" % color, theme_index)

        # Accent color
        gtkrc = os.path.join(theme, "gtk-2.0", "gtkrc")
        settings_ini = os.path.join(theme, "gtk-3.0", "settings.ini")
        gtk_main_css = os.path.join(theme, "gtk-3.0", "gtk-main.css")
        for file in [gtkrc, settings_ini, gtk_main_css]:
            for accent in X_HEX_ACCENTS:
                os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(file)s" % {'accent': accent, 'color_accent': x_hex_colors[color], 'file': file})

        # Cinnamon theme name
        file = os.path.join(theme, "cinnamon", "theme.json")
        if os.path.exists(file):
            os.system("sed -i s'/Mint-X/Mint-X-%(color)s/' %(file)s" % {'color': color, 'file': file})

        # Cinnamon colors
        file = os.path.join(theme, "cinnamon", "cinnamon.css")
        if os.path.exists(file):
            for accent in X_HEX_ACCENTS:
                os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(file)s" % {'accent': accent, 'color_accent': x_hex_colors[color], 'file': file})
            for accent in X_RGB_ACCENTS:
                os.system("sed -i s'/%(accent)s/%(color_accent)s/' %(file)s" % {'accent': accent, 'color_accent': x_rgb_colors[color], 'file': file})


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

curdir = os.getcwd()

os.chdir("src/Mint-Y")
os.system("./build-themes.py")
os.chdir(curdir)

# Mint-Y color variations
for color in y_hex_colors1.keys():
    for variant in ["", "-Dark", "-Darker"]:
        original_name = "Mint-Y%s" % variant
        path = os.path.join("src/Mint-Y/variations/%s" % color)
        if os.path.isdir(path):
            print("Derivating %s-%s" % (original_name, color))

            # Copy theme
            theme = "usr/share/themes/%s-%s" % (original_name, color)
            theme_index = os.path.join(theme, "index.theme")
            os.system("cp -R usr/share/themes/%s %s" % (original_name, theme))

            # Theme name
            for key in ["Name", "GtkTheme"]:
                change_value(key, "%s-%s" % (original_name, color), theme_index)

            for key in ["IconTheme"]:
                change_value(key, "Mint-Y-%s" % color, theme_index)

            for key in ["MetacityTheme"]:
                metacity_variant = original_name.replace("Darker", "Dark")
                change_value(key, "%s-%s" % (metacity_variant, color), theme_index)

            # Regenerate GTK3 sass
            os.system("cp -R src/Mint-Y/gtk-3.0/sass %s/gtk-3.0/" % theme)
            y_colorize_directory("%s/gtk-3.0/sass" % theme, color)
            os.chdir("%s/gtk-3.0" % theme)
            if (variant == "-Dark"):
                os.system("cp sass/gtk-dark.scss sass/gtk.scss")
                os.system("sassc ./sass/gtk.scss gtk.css")
            elif (variant == "-Darker"):
                os.system("cp sass/gtk-darker.scss sass/gtk.scss")
                os.system("sassc ./sass/gtk.scss gtk.css")
                os.system("sassc ./sass/gtk-dark.scss gtk-dark.css")
            else:
                os.system("rm sass/gtk-dark.scss sass/gtk-darker.scss")
                os.system("sassc ./sass/gtk.scss gtk.css")

            os.system("rm -rf sass .sass-cache")
            os.chdir(curdir)

            # Regenerate Cinnamon sass
            if (variant != "-Darker"):
                # Darker variants have no cinnamon style
                os.system("cp -R src/Mint-Y/cinnamon/sass %s/cinnamon/" % theme)
                y_colorize_directory("%s/cinnamon/sass" % theme, color)
                os.chdir("%s/cinnamon" % theme)
                if (variant == "-Dark"):
                    os.system("cp sass/cinnamon-dark.scss sass/cinnamon.scss")
                os.system("sassc ./sass/cinnamon.scss cinnamon.css")
                os.system("rm -rf sass .sass-cache")
                os.chdir(curdir)

            # Accent color
            files = []
            files.append(os.path.join(theme, "gtk-2.0", "gtkrc"))
            files.append(os.path.join(theme, "gtk-2.0", "main.rc"))
            files.append(os.path.join(theme, "gtk-2.0", "panel.rc"))
            files.append(os.path.join(theme, "gtk-2.0", "apps.rc"))
            files.append(os.path.join(theme, "gtk-2.0", "menubar-toolbar", "gtkrc"))
            files.append(os.path.join(theme, "metacity-1", "metacity-theme-2.xml"))
            files.append(os.path.join(theme, "metacity-1", "metacity-theme-3.xml"))
            for file in files:
                if os.path.exists(file):
                    for accent in Y_HEX_ACCENT1:
                        os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors1[color], 'file': file})
                    for accent in Y_HEX_ACCENT2:
                        os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors2[color], 'file': file})
                    for accent in Y_HEX_ACCENT3:
                        os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors3[color], 'file': file})
                    for accent in Y_HEX_ACCENT4:
                        os.system("sed -i s'/%(accent)s/%(color_accent)s/gI' %(file)s" % {'accent': accent, 'color_accent': y_hex_colors4[color], 'file': file})

            # Remove metacity-theme-3.xml (it doesn't need to be derived since it's using GTK colors, and Cinnamon doesn't want to list it)
            os.system("rm -f %s" % os.path.join(theme, "metacity-1", "metacity-theme-3.xml"))

            directories = []
            directories.append(os.path.join(theme, "cinnamon/common-assets"))
            directories.append(os.path.join(theme, "cinnamon/light-assets"))
            directories.append(os.path.join(theme, "cinnamon/dark-assets"))
            for directory in directories:
                if os.path.exists(directory):
                    y_colorize_directory(directory, color)

            # Assets
            os.system("rm -rf %s/gtk-3.0/assets" % theme)
            os.system("rm -rf %s/gtk-2.0/assets" % theme)
            if variant == "-Dark":
                os.system("cp -R %s/gtk-2.0/assets-dark %s/gtk-2.0/assets" % (path, theme))
            else:
                os.system("cp -R %s/gtk-2.0/assets %s/gtk-2.0/assets" % (path, theme))
            os.system("cp -R %s/gtk-3.0/assets %s/gtk-3.0/assets" % (path, theme))


# Files
os.system("cp -R usr/share/themes/* ~/.themes/")
