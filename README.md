# Creating Mint-Y-\<color\> variations is now 100% automated

**You no longer need to manually re-edit all those `files/usr/share/themes/` directories and files. All these color variations had to be redone over and over again. Now, it all happens automatically in a matter of minutes.**  

* Quickly and easily update colors. Because you can change your mind at any time and because color trends are always evolving.
* Open the doors to some small application that would empower people to create their own color variations.
* Make things much easier for all those people making forks or clones from mint-themes.

NOTE : Updated for Inkscape version 1.1 and up. Not retro-compatible with the old Inkscape version 0.x. Please check the troubleshooting section for this retro-compatibility issue.

| path                                      | thumbnails for all color variations (light)                      | thumbnails for all color variations (dark)                            |
| ----------------------------------------- |:----------------------------------------------------------------:|:---------------------------------------------------------------------:|
| src/Mint-Y/variations/\<color\>/gtk-3.0/  | <img src="src/Mint-Y/gtk-3.0/thumbnail@2.png" height="35">       | <img src="src/Mint-Y/gtk-3.0/thumbnail-dark@2.png" height="35">       |
| src/Mint-Y/variations/\<color\>/cinnamon/ | <img src="src/Mint-Y/cinnamon/mint-y-thumbnail.png" width="180"> | <img src="src/Mint-Y/cinnamon/mint-y-dark-thumbnail.png" width="180"> |

## A big pull request
This is a big pull request, but it is divided into 5 small branches. This is a group of 5 branches. The first 4 are pull requests. And this fifth one here, this `PR-all-auto`, is there to get to see the whole picture and test everything. All the other `PR-*` branches got merged into this `PR-all-auto`. So, you can go step-by-step, and check each little branch one-by-one before merging them one-by-one into the master branch, or you could just test this big `PR-all-auto` and then merge it all at once into the master branch.

* **PR-cinthumb**: creates `src/Mint-Y/cinnamon/mint-y-thumbnail.png` and `mint-y-dark-thumbnail.png`.
* **PR-thumbnails**: creates `src/Mint-Y/gtk-3.0/thumbnail.png` and `thumbnail-dark.png`.
* **PR-variations**: contains modified `update-variations.py` and `generate-themes.py` to include these new things.
* **PR-xfwm4**: creates `src/Mint-Y/xfwm4/` and `xfwm4-dark/` (updated for Inkscape version >= 1.1)

...And then **PR-all-auto** merges all these branches for testing purposes and it also contains this readme file here.  
NOTE : This **PR-all-auto** also holds additonnal updates for compatibility with Inkscape version >= 1.1.  

After having merged this group of PRs, you could just delete this `files/usr/share/themes/` directory. That was for manual edits and it is no longer required. And you should also delete this `colorize.py`. This script is very ingenious, sophisticated, but it only varies the hues, keeping the same saturation and lightness levels. It just doesn't work that way, IMHO.

## How to build
YOU MUST RUN `./update-variations.py All` at first !  
Later, you could re-edit those colors one-by-one with some `./update-variations.py <color>`.

1. Merge all those 4 branches or just test and merge this `PR-all-auto` branch here.
1. You MUST run `./update-variations.py All` at first. Later, you could try some new colors updates one-by-one.
1. Run `./generate-themes.py`.
1. `cd ~/mint-themes` and then `sudo cp -rf usr/share/themes/* /usr/share/themes`.
1. Force refresh your Menu > Preferences > Themes.

## Troubleshooting

**Inkscape version >= 1.1 versus the old version 0.x**  
Many files got updated for Inkscape version 1.1 and up. I strongly recommend you get the latest Inkscape from PPA:

```
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt update
sudo apt install inkscape
```

The Inkscape version found in the official repository is many years old and never gets updated. You are missing many great improvements. However, if you don't want to upgrade your Inkscape, then you will need to search through all files in `src/Mint-Y` and replace all:

`export-filename` -> `export-png`

for compatibility with the old Inkscape version 0.x...
