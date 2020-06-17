#!/usr/bin/python3
import os

from constants import X_HEX_ACCENTS, X_RGB_ACCENTS, x_hex_colors, x_rgb_colors
from constants import Y_HEX_ACCENT1, Y_HEX_ACCENT2, Y_HEX_ACCENT3, Y_HEX_ACCENT4
from constants import y_hex_colors1, y_hex_colors2, y_hex_colors3, y_hex_colors4

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

if os.path.exists("usr"):
    os.system("rm -rf usr/")

os.system("mkdir -p usr/share/themes")

# MINT-X GENERATE
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

curdir = os.getcwd()

# MINT-Y GENERATE
os.chdir("src/Mint-Y")
os.system("./build-themes.py")
os.chdir(curdir)

# Mint-Y color variations
for color in y_hex_colors1.keys():
    for variant in ["-Base", "-Darkest", "-Darker"]:
        original_name = "Mint-Y2%s" % variant
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
                metacity_variant = original_name.replace("Darker", "Darkest")
                change_value(key, "%s-%s" % (metacity_variant, color), theme_index)

            # Regenerate GTK3 sass
            os.system("cp -R src/Mint-Y/gtk-3.0/sass %s/gtk-3.0/" % theme)
            y_colorize_directory("%s/gtk-3.0/sass" % theme, color)
            os.chdir("%s/gtk-3.0" % theme)
            if (variant == "-Darkest"):
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
                if (variant == "-Darkest"):
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
            os.system("rm -rf %s/cinnamon/thumbnail.png" % theme)
            os.system("rm -rf %s/gtk-2.0/assets" % theme)
            os.system("rm -rf %s/gtk-2.0/menubar-toolbar/*.png" % theme)
            os.system("rm -rf %s/gtk-3.0/assets" % theme)
            os.system("rm -rf %s/gtk-3.0/thumbnail.png" % theme)
            os.system("rm -rf %s/xfwm4" % theme)

            if variant == "-Darkest":
                os.system("cp -R %s/cinnamon/mint-y-dark-thumbnail.png %s/cinnamon/thumbnail.png" % (path, theme))
                os.system("cp -R %s/gtk-2.0/assets-dark %s/gtk-2.0/assets" % (path, theme))
                os.system("cp -R %s/gtk-3.0/thumbnail-dark.png %s/gtk-3.0/thumbnail.png" % (path, theme))
                os.system("cp -R %s/xfwm4-src/xfwm4-dark %s/xfwm4" % (path, theme))
            else:
                if variant == "-Base":
                    os.system("cp -R %s/cinnamon/mint-y-thumbnail.png %s/cinnamon/thumbnail.png" % (path, theme))
                os.system("cp -R %s/gtk-2.0/assets %s/gtk-2.0/assets" % (path, theme))
                os.system("cp -R %s/gtk-3.0/thumbnail.png %s/gtk-3.0/thumbnail.png" % (path, theme))
                os.system("cp -R %s/xfwm4-src/xfwm4 %s/xfwm4" % (path, theme))
            os.system("cp -R %s/gtk-2.0/menubar-toolbar/*.png %s/gtk-2.0/menubar-toolbar" % (path, theme))
            os.system("cp -R %s/gtk-3.0/assets %s/gtk-3.0/assets" % (path, theme))

