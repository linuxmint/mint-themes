#!/usr/bin/python3
import sys
import os
import re
import colorsys
HEX_COLOR_REGEX = r'#([A-Fa-f0-9]{6})'
RGB_COLOR_REGEX = r'rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+(?:\.\d+)?))?\)'

# Greens are between these hue values:
MIN_HUE = 57
MAX_HUE = 180

hex_colors = {}
rgb_colors = {}

IGNORED_COLORS = []
IGNORED_COLORS.append("73d216") # success color (always green)
IGNORED_COLORS.append("6db442") # suggested color (always green)

def hex_to_rgb(color):
    return tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))

def rgb_to_hsv(color):
    red = int(color[0])
    green = int(color[1])
    blue = int(color[2])
    hue, saturation, value = colorsys.rgb_to_hsv(red/255., green/255., blue/255.)
    return (round(hue*360), round(saturation*100), round(value*100))

def parse_file(path):
    with open(path) as file:
        for color in re.findall(RGB_COLOR_REGEX, file.read()):
            if color not in rgb_colors.keys():
                rgb_colors[color] = 1
            else:
                rgb_colors[color] += 1
    with open(path) as file:
        for color in re.findall(HEX_COLOR_REGEX, file.read()):
            color = color.lower()
            if color not in IGNORED_COLORS:
                if color not in hex_colors.keys():
                    hex_colors[color] = 1
                else:
                    hex_colors[color] += 1

def parse_dir(path):
    for root,d_names,f_names in os.walk(path):
        for f in f_names:
            p = os.path.join(root, f)
            name, extension = os.path.splitext(p)
            if extension in [".css", ".scss", ".xml", ".svg", ".rc", ".xpm"]:
                parse_file(p)


if len(sys.argv) < 2:

    # Cinnamon
    parse_dir("src/Mint-Y/cinnamon/sass")
    parse_dir("src/Mint-Y/cinnamon/common-assets")
    parse_dir("src/Mint-Y/cinnamon/dark-assets")
    parse_dir("src/Mint-Y/cinnamon/light-assets")

    # GTK2
    parse_dir("src/Mint-Y/gtk-2.0/menubar-toolbar")
    parse_file("src/Mint-Y/gtk-2.0/apps.rc")
    parse_file("src/Mint-Y/gtk-2.0/gtkrc")
    parse_file("src/Mint-Y/gtk-2.0/gtkrc-dark")
    parse_file("src/Mint-Y/gtk-2.0/gtkrc-darker")
    parse_file("src/Mint-Y/gtk-2.0/main.rc")
    parse_file("src/Mint-Y/gtk-2.0/panel.rc")
    parse_file("src/Mint-Y/gtk-2.0/assets.svg")
    parse_file("src/Mint-Y/gtk-2.0/assets-dark.svg")

    # GTK3
    parse_dir("src/Mint-Y/gtk-3.0/sass")
    parse_file("src/Mint-Y/gtk-3.0/assets.svg")

    # Metacity
    parse_dir("src/Mint-Y/metacity-1")

    # Xfwm4 (ignore this one... loads of very similar colors in there)
    # parse_dir("src/Mint-Y/xfwm4")

else:
    # parse a different directory
    parse_dir(sys.argv[1])

for color in rgb_colors.keys():
    occurences = rgb_colors[color]
    hue, saturation, value = rgb_to_hsv(color)
    if hue > MIN_HUE and hue < MAX_HUE:
        print (color, hue, saturation, value, "(appears %d times)" % occurences)

for color in sorted(hex_colors.keys()):
    occurences = hex_colors[color]
    rgb = hex_to_rgb(color)
    hue, saturation, value = rgb_to_hsv(rgb)
    if hue > MIN_HUE and hue < MAX_HUE:
        print (color, rgb, hue, saturation, value, "(appears %d times)" % occurences)

