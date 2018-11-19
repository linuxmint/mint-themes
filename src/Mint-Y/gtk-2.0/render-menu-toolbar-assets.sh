#! /bin/bash

./render-assets.sh
./render-dark-assets.sh

cp assets-dark/button.png                               menubar-toolbar/button.png
cp assets-dark/button-active.png                        menubar-toolbar/button-active.png
cp assets-dark/button-hover.png                         menubar-toolbar/button-hover.png
cp assets-dark/button-insensitive.png                   menubar-toolbar/button-insensitive.png
cp assets/menubar.png                                   menubar-toolbar/menubar.png
cp assets-dark/menubar.png                              menubar-toolbar/menubar-dark.png
cp assets/menubar_button.png                            menubar-toolbar/menubar_button.png
cp assets-dark/menubar_button.png                       menubar-toolbar/menubar_button-dark.png
cp assets/toolbar-entry-border-active-bg.png            menubar-toolbar/toolbar-entry-border-active-bg.png
cp assets-dark/toolbar-entry-border-active-bg.png       menubar-toolbar/toolbar-entry-border-active-bg-dark.png
cp assets/toolbar-entry-border-bg.png                   menubar-toolbar/toolbar-entry-border-bg.png
cp assets-dark/toolbar-entry-border-bg.png              menubar-toolbar/toolbar-entry-border-bg-dark.png
cp assets/toolbar-entry-border-disabled-bg.png          menubar-toolbar/toolbar-entry-border-disabled-bg.png
cp assets-dark/toolbar-entry-border-disabled-bg.png     menubar-toolbar/toolbar-entry-border-disabled-bg-dark.png
