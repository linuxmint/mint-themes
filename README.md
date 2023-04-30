Adding a Mint-Y theme
=====================

1. Add new colors to `constants.py`
2. Add new hue to `colorize.py`
3. Add the new color name to the lists in `update-variations.py`
4. Run the Python script `update-variations.py` for the new color (e.g. `python3 update-variations.py Red`). 
This will generate new assets in `src/Mint-Y/variations/`.
5. Run the Python script `generate-themes.py`. This will create the themes in the local directory `usr/share/themes`.
6. Manually add a `index.theme` file to the theme directories. It's best to copy and adapt one from the existing themes.
7. Test the themes by copying them to `~/.themes` and applying them.
8. In Git commit and push all newly created files to a new branch.
