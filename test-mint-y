#!/bin/bash

CURDIR=`pwd`

cd src/Mint-Y
./build-themes.py

cd $CURDIR

sudo rm -rf /usr/share/themes/Mint-Y
sudo cp -R usr/share/themes/Mint-Y /usr/share/themes/Mint-Y

sudo rm -rf /usr/share/themes/Mint-Y-Dark
sudo cp -R usr/share/themes/Mint-Y-Dark /usr/share/themes/Mint-Y-Dark

# Force refresh
gsettings set org.cinnamon.desktop.interface gtk-theme 'Mint-Y-Blue'
gsettings set org.cinnamon.desktop.interface gtk-theme 'Mint-Y'

gsettings set org.cinnamon.theme name 'Mint-Y-Blue'
gsettings set org.cinnamon.theme name 'Mint-Y-Dark'
