This theme uses libsass to process the sass/*.scss. Never edit any of the .css files manually.

#### Editing the theme

In most cases edits will done in sass/_common.scss or sass/_applications.scss. This is where the style of each widget is actually defined. The sass directory contains several other supporting style sheets:

* _colors.scss This file contains the global color definitions

* _colors-public.scss SCSS colors exported through gtk to allow for 3rd party apps color mixing

* _drawing.scss Drawing helper mixins/functions to allow for easier definition of widget drawing

Once you have made your edits run ./parse-sass.sh to update the css files

--

#### Editing the images in the `assets` folder

* Open the `assets.svg` file in inkscape. Each object in the .svg file corresponds to an image in the `assets` folder.

* Find the object you want to edit and make your changes. Important: Don't change the obejct id.

* Save `assets.svg` and delete the images corresponding to the edited .svg objects from the `assets` folder (or just delete everything in the `assets` folder).

* Run `./render-assets.sh` from a terminal.
