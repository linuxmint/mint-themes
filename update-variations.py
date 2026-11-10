#!/usr/bin/python3
import os
import subprocess
import sys

from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn, TimeElapsedColumn

from constants import Y_HEX_ACCENT1, Y_HEX_ACCENT2
from constants import y_hex_colors1, y_hex_colors2

def change_value (key, value, file):
    if value is not None:
        command = "sed -i '/%(key)s=/c\\%(key)s=%(value)s' %(file)s" % {'key':key, 'value':value, 'file':file}
    else:
        command = "sed -i '/%(key)s=/d' %(file)s" % {'key':key, 'file':file}
    os.system(command)

def usage ():
    print ("Usage: update-variations.py color")
    print ("color can be 'Aqua', 'Blue', 'Grey', 'Orange', 'Pink', 'Purple', 'Red', 'Sand', 'Teal' or 'All'.")
    sys.exit(1)

def render (progress, name, script, assets_dir):
    # Run a render script in the current folder, advancing a bar for each asset it renders
    with open("assets.txt") as f:
        names = f.read().split()
    with open(script) as f:
        if "@2" in f.read():
            names = names + [asset + "@2" for asset in names]

    task = progress.add_task(name, total=len(names))
    process = subprocess.Popen(["./" + script], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    for line in process.stdout:
        if line.startswith("Rendering"):
            progress.advance(task)
    process.wait()

    for asset in names:
        if not os.path.exists("%s/%s.png" % (assets_dir, asset)):
            progress.console.print("[red]Missing %s/%s.png[/red]" % (os.getcwd(), asset))

def update_color (color):
    variation = "src/Mint-Y/variations/%s" % color
    print("updating %s" % variation)
    os.system("rm -rf %s" % variation)
    os.system("mkdir -p %s/gtk-2.0" % variation)
    os.system("mkdir -p %s/gtk-3.0" % variation)
    os.system("mkdir -p %s/gtk-4.0" % variation)
    os.system("mkdir -p %s/xfwm4" % variation)
    os.system("mkdir -p %s/xfwm4-dark" % variation)

    # Copy assets files
    assets = []
    assets.append("gtk-2.0/assets.svg")
    assets.append("gtk-2.0/assets-dark.svg")
    assets.append("gtk-3.0/assets.svg")
    assets.append("gtk-4.0/assets.svg")
    assets.append("xfwm4/assets.svg")
    assets.append("xfwm4-dark/assets.svg")

    files = []
    files.append("gtk-2.0/assets")
    files.append("gtk-2.0/assets-dark")
    files.append("gtk-2.0/assets.txt")
    files.append("gtk-2.0/render-assets.sh")
    files.append("gtk-2.0/render-dark-assets.sh")
    files.append("gtk-3.0/assets")
    files.append("gtk-3.0/assets.txt")
    files.append("gtk-3.0/render-assets.sh")
    files.append("gtk-4.0/assets")
    files.append("gtk-4.0/assets.txt")
    files.append("gtk-4.0/render-assets.sh")
    files.append("xfwm4/render-assets.sh")
    files.append("xfwm4/assets.txt")
    files.append("xfwm4-dark/render-assets.sh")
    files.append("xfwm4-dark/assets.txt")

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

    # Render assets
    bar_color = y_hex_colors1[color]
    progress = Progress(TextColumn("{task.description}"),
                        BarColumn(complete_style=bar_color, finished_style=bar_color),
                        TaskProgressColumn(), TimeElapsedColumn())
    progress.start()
    os.chdir(variation)
    os.chdir("gtk-2.0")
    os.system("rm -rf assets/*")
    os.system("rm -rf assets-dark/*")
    render(progress, "gtk-2.0", "render-assets.sh", "assets")
    render(progress, "gtk-2.0 dark", "render-dark-assets.sh", "assets-dark")
    os.chdir("../gtk-3.0/")
    os.system("rm -rf assets/*")
    render(progress, "gtk-3.0", "render-assets.sh", "assets")
    os.chdir("../gtk-4.0/")
    os.system("rm -rf assets/*")
    render(progress, "gtk-4.0", "render-assets.sh", "assets")
    os.chdir("../xfwm4/")
    os.system("rm -rf *.png")
    render(progress, "xfwm4", "render-assets.sh", ".")
    os.chdir("../xfwm4-dark/")
    os.system("rm -rf *.png")
    render(progress, "xfwm4 dark", "render-assets.sh", ".")
    os.chdir(curdir)
    progress.stop()

if len(sys.argv) < 2:
    usage()
else:
    color_variation = sys.argv[1]
    if not color_variation in ["Aqua", "Blue", "Grey", "Orange", "Pink", "Purple", "Red", "Sand", "Teal", "All"]:
        usage()

# Mint-Y variations
curdir = os.getcwd()

if color_variation == "All":
    for color in y_hex_colors1.keys():
        update_color(color)
else:
    update_color(color_variation)
