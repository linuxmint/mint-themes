#!/usr/bin/env python3

import os

VARIATIONS = ["Mint-Y",
              "Mint-Y-Dark"]

DEST = '../../usr/share/themes'

curdir = os.getcwd()

print("Updating Gtk4 assets")
os.chdir("gtk-4.0/")
os.system("pysassc ./sass/gtk.scss gtk.css")
os.system("pysassc ./sass/gtk-dark.scss gtk-dark.css")
os.system("./render-assets.sh")
print("Gtk4 assets updated")

os.chdir(curdir)

print("Updating Gtk3 assets")
os.chdir("gtk-3.0/")
os.system("pysassc ./sass/gtk.scss gtk.css")
os.system("pysassc ./sass/gtk-dark.scss gtk-dark.css")
os.system("./render-assets.sh")
print("Gtk3 assets updated")

os.chdir(curdir)

print("Updating Gtk2 assets")
os.chdir("gtk-2.0/")
os.system("./render-assets.sh")
os.system("./render-dark-assets.sh")
print("Gtk2 assets updated")

os.chdir(curdir)

print("Updating Cinnamon assets")
os.chdir("cinnamon/")
os.system("pysassc ./sass/cinnamon.scss cinnamon.css")
os.system("pysassc ./sass/cinnamon-dark.scss cinnamon-dark.css")
print("Cinnamon assets updated")

os.chdir(curdir)

print("Updating Xfwm4 assets")
os.chdir("xfwm4/")
os.system("./render-assets.sh")

os.chdir(curdir)

print("Updating Xfwm4 dark assets")
os.chdir("xfwm4-dark/")
os.system("./render-assets.sh")

os.chdir(curdir)

if __name__ == '__main__':
    print("Building themes")
    for variation in VARIATIONS:
        dest_folder = os.path.join(DEST, variation)
        os.system("mkdir -p %s" % dest_folder)
        if variation == "Mint-Y":
            print("    Building Mint-Y")
            # Gtk2
            version_folder = os.path.join(dest_folder, "gtk-2.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-2.0/assets %s" % version_folder)
            os.system("cp gtk-2.0/*.rc %s" % version_folder)
            os.system("cp gtk-2.0/gtkrc %s" % version_folder)
            # Gtk3
            version_folder = os.path.join(dest_folder, "gtk-3.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-3.0/assets %s" % version_folder)
            os.system("cp gtk-3.0/gtk.css %s" % version_folder)
            os.system("cp gtk-3.0/gtk-dark.css %s" % version_folder)
            os.system("cp gtk-3.0/thumbnail.png %s" % version_folder)
            # Gtk4
            version_folder = os.path.join(dest_folder, "gtk-4.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-4.0/assets %s" % version_folder)
            os.system("cp gtk-4.0/gtk.css %s" % version_folder)
            os.system("cp gtk-4.0/gtk-dark.css %s" % version_folder)
            # Metacity
            os.system("cp -R metacity-1 %s" % dest_folder)
            # Cinnamon
            version_folder = os.path.join(dest_folder, "cinnamon")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R cinnamon/common-assets %s" % version_folder)
            os.system("cp -R cinnamon/light-assets %s" % version_folder)
            os.system("cp cinnamon/mint-y-thumbnail.png %s" % os.path.join(version_folder, "thumbnail.png"))
            os.system("cp cinnamon/cinnamon.css %s" % version_folder)
            # XFWM
            version_folder = os.path.join(dest_folder, "xfwm4")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R xfwm4/*.png %s" % version_folder)
            os.system("cp -R xfwm4/themerc %s" % version_folder)

        elif variation == "Mint-Y-Dark":
            print("    Building Mint-Y-Dark")
            # Gtk2
            version_folder = os.path.join(dest_folder, "gtk-2.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-2.0/assets-dark %s" % version_folder)
            os.system("rm -rf %s" % os.path.join(version_folder, "assets"))
            os.system("mv %s %s" % (os.path.join(version_folder, "assets-dark"), os.path.join(version_folder, "assets")))
            os.system("cp gtk-2.0/*.rc %s" % version_folder)
            os.system("cp gtk-2.0/gtkrc-dark %s" % os.path.join(version_folder, "gtkrc"))
            os.system("cp gtk-2.0/menubar-toolbar-dark.rc %s" % os.path.join(version_folder, "menubar-toolbar.rc"))
            # Gtk3
            version_folder = os.path.join(dest_folder, "gtk-3.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-3.0/assets %s" % version_folder)
            os.system("cp gtk-3.0/gtk-dark.css %s" % os.path.join(version_folder, "gtk.css"))
            os.system("cp gtk-3.0/gtk-dark.css %s" % os.path.join(version_folder, "gtk-dark.css"))
            os.system("cp gtk-3.0/thumbnail-dark.png %s" % os.path.join(version_folder, "thumbnail.png"))
            # Gtk4
            version_folder = os.path.join(dest_folder, "gtk-4.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-4.0/assets %s" % version_folder)
            os.system("cp gtk-4.0/gtk-dark.css %s" % os.path.join(version_folder, "gtk.css"))
            os.system("cp gtk-4.0/gtk-dark.css %s" % os.path.join(version_folder, "gtk-dark.css"))
            # Cinnamon
            version_folder = os.path.join(dest_folder, "cinnamon")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R cinnamon/common-assets %s" % version_folder)
            os.system("cp -R cinnamon/dark-assets %s" % version_folder)
            os.system("cp cinnamon/mint-y-dark-thumbnail.png %s" % os.path.join(version_folder, "thumbnail.png"))
            os.system("cp cinnamon/cinnamon-dark.css %s" % os.path.join(version_folder, "cinnamon.css"))
            # XFWM
            version_folder = os.path.join(dest_folder, "xfwm4")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R xfwm4-dark/*.png %s" % version_folder)
            os.system("cp -R xfwm4-dark/themerc %s" % version_folder)
