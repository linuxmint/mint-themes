#!/usr/bin/env python3
import os
import threading

from constants import X_HEX_ACCENTS, X_RGB_ACCENTS, x_hex_colors, x_rgb_colors
from constants import Y_HEX_ACCENT1, Y_HEX_ACCENT2
from constants import y_hex_colors1, y_hex_colors2

def x_colorize_directory (path, variation):
    for accent in X_HEX_ACCENTS:
        os.system(f"find {path} -name '*.*' -type f -exec sed -i 's/{accent}/{x_hex_colors[variation]}/gI' {{}}  \\;")
    for accent in X_RGB_ACCENTS:
        os.system(f"find {path} -name '*.*' -type f -exec sed -i 's/{accent}/{x_rgb_colors[variation]}/gI' {{}}  \\;")
def y_colorize_directory (path, variation):
    for accent in Y_HEX_ACCENT1:
        os.system(f"find {path} -name '*.*' -type f -exec sed -i 's/{accent}/{y_hex_colors1[variation]}/gI' {{}}  \\;")
    for accent in Y_HEX_ACCENT2:
        os.system(f"find {path} -name '*.*' -type f -exec sed -i 's/{accent}/{y_hex_colors2[variation]}/gI' {{}}  \\;")

if os.path.exists("usr"):
    os.system("rm -rf usr/")

start_dir = os.getcwd()

os.system("mkdir -p usr/share/themes")

# Mint-X ##################################################################
def xBuildGtk(gtk:str) -> None:
    os.chdir(f"src/Mint-X/theme/Mint-X/{gtk}/")
    os.system("pysassc ./sass/gtk.scss gtk.css")
    os.system("pysassc ./sass/gtk-dark.scss gtk-dark.css")
    os.chdir(start_dir)

xBuildGtk("gtk-4.0")
xBuildGtk("gtk-3.0")

os.system("cp -R src/Mint-X/theme/* usr/share/themes/")

def xDerivateGtk(theme:str, gtk:str) -> None:
    sass_dir = os.path.join(theme, gtk)
    os.system(f"""
        cd {sass_dir}
        pysassc ./sass/gtk.scss gtk.css
        pysassc ./sass/gtk-dark.scss gtk-dark.css
        rm -rf sass parse-sass.sh
    """)

def xDerivateCinnamon(color:str, theme:str) -> None:
    file = os.path.join(theme, "cinnamon", "theme.json")
    if os.path.exists(file):
        os.system(f"sed -i s'/Mint-X/Mint-X-{color}/' {file}")

    # Cinnamon colors
    file = os.path.join(theme, "cinnamon", "cinnamon.css")
    if os.path.exists(file):
        for accent in X_HEX_ACCENTS:
            os.system(f"sed -i s'/{accent}/{x_hex_colors[color]}/' {file}")
        for accent in X_RGB_ACCENTS:
            os.system(f"sed -i s'/{accent}/{x_rgb_colors[color]}/' {file}")

def xDerivateOpenbox(theme:str, color:str) -> None:
    file = os.path.join(theme, "openbox-3", 'themerc')
    if os.path.exists(file):
        for accent in X_HEX_ACCENTS:
            os.system(f"sed -i s'/{accent}/{x_hex_colors[color]}/' {file}")

def xAccentRecolorFile(theme:str, color:str) -> None:
    accent_files = []
    accent_files.append(os.path.join(theme, "gtk-2.0", "gtkrc"))
    accent_files.append(os.path.join(theme, "gtk-3.0", "settings.ini"))
    accent_files.append(os.path.join(theme, "gtk-3.0", "sass", "_colors.scss"))
    accent_files.append(os.path.join(theme, "gtk-4.0", "sass", "_colors.scss"))
    accent_files.append(os.path.join(theme, "libadwaita-1.5", "defaults-light.css"))
    accent_files.append(os.path.join(theme, "libadapta-1.5", "defaults-light.css"))
    accent_files.append(os.path.join(theme, "libadwaita-1.5", "defaults-dark.css"))
    accent_files.append(os.path.join(theme, "libadapta-1.5", "defaults-dark.css"))
    accent_files.append(os.path.join(theme, "libadwaita-1.7", "defaults-light.css"))
    accent_files.append(os.path.join(theme, "libadwaita-1.7", "defaults-dark.css"))
    for file in accent_files:
        if not os.path.exists(file):
            continue

        for accent in X_HEX_ACCENTS:
            os.system(f"sed -i s'/{accent}/{x_hex_colors[color]}/gI' {file}")

# Now do the other themes and color variations
def xGenTheme(color:str):
    path = os.path.join("src/Mint-X/variations", color)
    if not os.path.isdir(path):
        exit()

    theme = f"usr/share/themes/Mint-X-{color}"
    os.system(f"cp -R usr/share/themes/Mint-X {theme}")
    os.system(f"cp -R src/Mint-X/variations/{color}/* {theme}/")

    # Accent color
    xAccentRecolorFile(theme, color)

    # Build sass
    xDerivateGtk(theme, "gtk-4.0")
    xDerivateGtk(theme, "gtk-3.0")

    # Cinnamon
    xDerivateCinnamon(color, theme)

    # Openbox colors
    xDerivateOpenbox(theme, color)

# Mint-Y #################################################################

curdir = os.getcwd()

os.chdir("src/Mint-Y")
os.system("./build-themes.py")
os.chdir(curdir)

# Mint-Y color variations
def yDerivateGtk(color:str, lightDark:str, theme:str, gtk:str) -> None:
    # gtk3 and 4 have the same generation process unlike in build-themes so we can use 1 function for both
    os.system(f"cp -R src/Mint-Y/{gtk}/sass {theme}/{gtk}")
    y_colorize_directory(f"{theme}/{gtk}/sass", color)
    os.system(f"""
        cd {theme}/{gtk}
        pysassc ./sass/gtk-dark.scss gtk-dark.css
        pysassc ./sass/gtk{lightDark}.scss gtk.css
        rm -rf sass .sass-cache
    """)

def yDerivateCinnamon(color:str, lightDark:str, theme:str) -> None:
    os.system(f"cp -R src/Mint-Y/cinnamon/sass {theme}/cinnamon/")
    y_colorize_directory(f"{theme}/cinnamon/sass", color)
    if lightDark == "-dark":
        os.system(f"cd {theme}/cinnamon; cp sass/cinnamon-dark.scss sass/cinnamon.scss")
    os.system(f"""
        cd {theme}/cinnamon; pysassc ./sass/cinnamon.scss cinnamon.css
        rm -rf sass .sass-cache
""")

def yDerivateOpenbox(curdir:str, theme:str, color:str) -> None:
    os.chdir(curdir)
    # for accent in Y_HEX_ACCENT1: is redundant because the command used file, that just generated the last file
    # in files (e.g. theme/libadwaita-1.7/default-dark.css) again. The output is unchanged with the line removed
    for accent in Y_HEX_ACCENT2:
        os.system(f"sed -i s'/{accent}/{y_hex_colors2[color]}/gI' {os.path.join(theme, "openbox-3", "themerc")}")

def yAccentRecolorFile(theme:str, color:str) -> None:
    files = []
    files.append(os.path.join(theme, "gtk-2.0", "gtkrc"))
    files.append(os.path.join(theme, "gtk-2.0", "main.rc"))
    files.append(os.path.join(theme, "gtk-2.0", "panel.rc"))
    files.append(os.path.join(theme, "gtk-2.0", "apps.rc"))
    files.append(os.path.join(theme, "gtk-2.0", "menubar-toolbar.rc"))
    files.append(os.path.join(theme, "libadwaita-1.5", "defaults-light.css"))
    files.append(os.path.join(theme, "libadapta-1.5", "defaults-light.css"))
    files.append(os.path.join(theme, "libadwaita-1.5", "defaults-dark.css"))
    files.append(os.path.join(theme, "libadapta-1.5", "defaults-dark.css"))
    files.append(os.path.join(theme, "libadwaita-1.7", "defaults-light.css"))
    files.append(os.path.join(theme, "libadwaita-1.7", "defaults-dark.css"))
    for file in files:
        if not os.path.exists(file):
            continue

        for accent in Y_HEX_ACCENT1:
            os.system(f"sed -i s'/{accent}/{y_hex_colors1[color]}/gI' {file}")
        for accent in Y_HEX_ACCENT2:
            os.system(f"sed -i s'/{accent}/{y_hex_colors2[color]}/gI' {file}")

def accentRecolorDirectory(theme:str, color:str) -> None:
    directories = []
    directories.append(os.path.join(theme, "cinnamon/common-assets"))
    directories.append(os.path.join(theme, "cinnamon/light-assets"))
    directories.append(os.path.join(theme, "cinnamon/dark-assets"))
    for directory in directories:
        if os.path.exists(directory):
            y_colorize_directory(directory, color)

def copyAssets(lightDark:str, theme:str, path:str) -> None:
    os.system(f"rm -rf {theme}/gtk-4.0/assets")
    os.system(f"rm -rf {theme}/gtk-3.0/assets")
    os.system(f"rm -rf {theme}/gtk-2.0/assets")
    os.system(f"cp -R {path}/gtk-2.0/assets{lightDark} {theme}/gtk-2.0/assets")
    os.system(f"cp -R {path}/xfwm4{lightDark}/*.png {theme}/xfwm4/")
    os.system(f"cp -R {path}/gtk-3.0/assets {theme}/gtk-3.0/assets")
    os.system(f"cp -R {path}/gtk-4.0/assets {theme}/gtk-4.0/assets")

def yGenTheme(color:str):
    for variant in ["", "-Dark"]:
        original_name = f"Mint-Y{variant}"
        path = os.path.join(f"src/Mint-Y/variations/{color}")
        lightDark = variant.lower()
        if not os.path.isdir(path):
            exit()

        print(f"Derivating {original_name}-{color}")

        # Copy theme
        theme = f"usr/share/themes/{original_name}-{color}"
        os.system(f"cp -R usr/share/themes/{original_name} {theme}")

        yDerivateGtk(color, lightDark, theme, "gtk-4.0")
        yDerivateGtk(color, lightDark, theme, "gtk-3.0")
        yDerivateCinnamon(color, lightDark, theme)

        # Accent color
        yAccentRecolorFile(theme, color)

        # Remove metacity-theme-3.xml (it doesn't need to be derived since it's using GTK colors,
        # and Cinnamon doesn't want to list it)
        os.system(f"rm -f {os.path.join(theme, 'metacity-1', 'metacity-theme-3.xml')}")

        accentRecolorDirectory(theme, color)

        # Assets
        copyAssets(lightDark,theme, path)

        # Openbox theme
        yDerivateOpenbox(curdir, theme, color)

threads = []
for color in os.listdir("src/Mint-X/variations"):
    t = threading.Thread(target=xGenTheme, args=(color,))
    threads.append(t)

for color in y_hex_colors1.keys():
    t = threading.Thread(target=yGenTheme, args=(color,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

# execute after the threads have completed
os.system("rm -rf usr/share/themes/Mint-X/gtk-3.0/sass usr/share/themes/Mint-X/gtk-3.0/parse-sass.sh")
os.system("rm -rf usr/share/themes/Mint-X/gtk-4.0/sass usr/share/themes/Mint-X/gtk-4.0/parse-sass.sh")

# Files
os.system("cp -R files/* ./")
