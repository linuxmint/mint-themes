#!/usr/bin/env python3

import os

VARIATIONS = ["Mint-Y",
              "Mint-Y-Dark"]

dirs = ["cinnamon",
        "gtk-2.0",
        "gtk-3.0",
        "gtk-4.0",
        "xfwm4",
        "xfwm4-dark"]

DEST = '../../usr/share/themes'

curDir = os.getcwd()

def updateTheme(themeDir:str) -> None:
    print(f"Updating {themeDir} assets")
    os.chdir(themeDir)
    os.system("./*.sh")
    os.chdir(curDir)

for theme in dirs:
    updateTheme(theme)

if __name__ != '__main__':
    exit()

def buildGtk2(lightDark:str) -> None:
    version_folder = os.path.join(dest_folder, "gtk-2.0")
    os.system(f"mkdir -p {version_folder}")
    os.system(f"cp -R gtk-2.0/assets{lightDark} {version_folder}")
    os.system(f"cp gtk-2.0/*.rc {version_folder}")
    os.system(f"cp gtk-2.0/gtkrc{lightDark} {os.path.join(version_folder, 'gtkrc')}")
    if lightDark == "-dark":
        os.system(f"rm -rf {os.path.join(version_folder, 'assets')}")
        os.system(f"mv {os.path.join(version_folder, 'assets-dark')} {os.path.join(version_folder, 'assets')}")
        os.system(f"cp gtk-2.0/menubar-toolbar-dark.rc {os.path.join(version_folder, "menubar-toolbar.rc")}")

def buildGtk3(lightDark:str) -> None:
    version_folder = os.path.join(dest_folder, "gtk-3.0")
    os.system(f"mkdir -p {version_folder}")
    os.system(f"cp -R gtk-3.0/assets {version_folder}")
    os.system(f"cp gtk-3.0/gtk{lightDark}.css {os.path.join(version_folder, 'gtk.css')}")
    os.system(f"cp gtk-3.0/gtk-dark.css {os.path.join(version_folder, 'gtk-dark.css')}")
    os.system(f"cp gtk-3.0/thumbnail{lightDark}.png {os.path.join(version_folder, 'thumbnail.png')}")

def buildGtk4(lightDark:str) -> None:
    version_folder = os.path.join(dest_folder, "gtk-4.0")
    os.system(f"mkdir -p {version_folder}")
    os.system(f"cp -R gtk-4.0/assets {version_folder}")
    os.system(f"cp gtk-4.0/gtk{lightDark}.css {os.path.join(version_folder, 'gtk.css')}")
    os.system(f"cp gtk-4.0/gtk-dark.css {os.path.join(version_folder, 'gtk-dark.css')}")

def buildCinnamon(lightDark:str) -> None:
    version_folder = os.path.join(dest_folder, "cinnamon")
    os.system(f"mkdir -p {version_folder}")
    os.system(f"cp -R cinnamon/common-assets {version_folder}")
    os.system(f"cp cinnamon/mint-y{lightDark}-thumbnail.png {os.path.join(version_folder, 'thumbnail.png')}")
    os.system(f"cp cinnamon/cinnamon{lightDark}.css {os.path.join(version_folder, 'cinnamon.css')}")
    if lightDark == "":
        os.system(f"cp -R cinnamon/light-assets {version_folder}")
    elif lightDark == "-dark":
        os.system(f"cp -R cinnamon/dark-assets {version_folder}")

def buildXfwm4(lightDark:str) -> None:
    version_folder = os.path.join(dest_folder, "xfwm4")
    os.system(f"mkdir -p {version_folder}")
    os.system(f"cp -R xfwm4{lightDark}/*.png {version_folder}")
    os.system(f"cp -R xfwm4{lightDark}/themerc {version_folder}")

def buildOpenbox(lightDark:str) -> None:
    version_folder = os.path.join(dest_folder, "openbox-3")
    os.system(f"mkdir -p {version_folder}")
    os.system(f"cp openbox-3/themerc{lightDark} {version_folder}/themerc")

print("Building themes")
for variation in VARIATIONS:
    print(f"    Building {variation}")
    dest_folder = os.path.join(DEST, variation)
    lightDark = variation.replace("Mint-Y", "").lower()
    os.system("mkdir -p %s" % dest_folder)
    buildGtk2(lightDark)
    buildGtk3(lightDark)
    buildGtk4(lightDark)
    buildCinnamon(lightDark)
    buildXfwm4(lightDark)
    buildOpenbox(lightDark)
    os.system("cp -R libadwaita-* %s/" % dest_folder)
    if variation == "Mint-Y":
        os.system("cp -R metacity-1 %s" % dest_folder)
