# guizero

## 1.2.0 - 2021-05-04
- Added `filename` to `select_file` dialog
- Added `when_resized` and `when_double_clicked` events
- Removed previously deprecated `App.on_closed` method
- A window icon can be set using the `.icon` property
- Add `select_color` popup
- Documentation updates and fixes
- Added new examples and recipes
- Tests updated to cope with a greater range of operating systems. Tests work on Windows, macOS and Raspberry Pi OS.
- contributors [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie), [mirelsol](https://github.com/mirelsol), [maroph](https://github.com/maroph)

## 1.1.1 - 2020-11-27
- PushButton image bug fix for macOS
- Documentation updates regarding how to use tk, particularly for ListBox widget
- Refactored `.description` property due to issue with TextBox widget
- Fix TextBox widget where you cant set the value if its disabled
- Removed `bgcolor` from App constructor which had previously been deprecated
- Resolved issue with `Waffle` and being able to click "outside" the waffle
- contributors [martinohanlon](https://github.com/martinohanlon), [aajshaw](https://github.com/aajshaw)

## 1.1.0 - 2019-10-25
- Added ability to be able to change the grid of a widget at run time
- Added `hide_text` to `TextBox` for use with passwords
- Added open file and folder pop-ups `select_file` and `select_folder`
- Changes to `Text` to better support cascading of text color, font and size
- Various documentation updates 
- contributors [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie)

## 1.0.0 - 2019-07-11
- Previously deprecated methods have now been removed
- Resolved race condition in the `repeat`, `cancel` methods
- Refactored alerts (renamed pop-ups), they can now also be called from `App` & `Window` objects
- Added `question` pop-up
- Created windows MSI installer for guizero
- Deprecated `App.on_closed` method and replaced with `App.when_closed` property
- contributors [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie), [MrYsLab](https://github.com/MrYsLab), [scotty3785](https://github.com/scotty3785)

## 0.6.4 - 2019-05-08)
- Fixed TextBox command to be on key release
- Fix Text not inheriting properties
- Added add_tk_warning when inserting a tk widget into the wrong container
- Update docs
- contributors [martinohanlon](https://github.com/martinohanlon), [hyle01](https://github.com/hyle01) 

## 0.6.3 - 2019-04-18
- ListBox scrollbar bug fix (again)
- Removed pillow requires dependency
- Added pillow as an extra dependency `pip3 install guizero[images]`
- Installation instructions update
- contributors [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie) 

## 0.6.2 - 2019-04-05
- Ability to [add tk widgets](./usingtk/) into a guizero app with `.add_tk_widget()`
- ListBox scrollbar bug fix
- MenuBar background colour bug fix
- `setup.py` changes to allow dunders to be accessed from guizero module
- contributors [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie) 

## 0.6.1 - 2019-03-08
- New [Drawing widget](./drawing/) for creating "drawings"
- Added full screen support for `App` and `Window`
- Doc updates
- Minor bug fixes
- contributors [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie) 

## 0.6.0 - 2019-02-08
- Refactoring of layout functions
- Enabled `align` for the `auto` layout
- `width` and `height` can now be set to `"fill"`
- Modified `setup.py` to restrict install to Python 3 only
- Minor bug fixes
- contributors [martinohanlon](https://github.com/martinohanlon), [bennuttal](https://github.com/bennuttall), [yeyeto2788](https://github.com/yeyeto2788), [knowledgejunkie](https://github.com/knowledgejunkie), [lawsie](https://github.com/lawsie)

## 0.5.4 - 2018-10-16
- Fixed `Box` to size properly
- Added `border` to `Box`
- Added `width` and `height` to widget constructor
- Added `resize` method to all widgets
- Minor bug fixes
- contributors [martinohanlon](https://github.com/martinohanlon)

## 0.5.3 - 2018-07-18
- Various bug fixes
- wrapping multiline `TextBox` data
- `ButtonGroup`, `ComboBox` now allow 0 options at init
- Minimum pillow version is now 4.3.0
- `update` method added to `Add` and `Window`
- contributors [martinohanlon](https://github.com/martinohanlon), [scotty3785](https://github.com/scotty3785), [MrYsLab](https://github.com/MrYsLab), [bsimmo](https://github.com/bsimmo)

## 0.5.2 - 2018-06-01
- Refactoring of `ButtonGroup`, including API breaking change - if no hidden values are specified, `ButtonGroup.value` now returns the text value not a generate string number [#178](https://github.com/lawsie/guizero/issues/178)
- A widgets properties `bg`, `text_color`, `text_size`, `font`, `width`, `height` can be restored by to their default by setting them to `None` [#181](https://github.com/lawsie/guizero/issues/181)
- Slider is now sized properly when orientated vertically [#186](https://github.com/lawsie/guizero/issues/186)
- `Combo` and `ButtonGroup` now support `append`, `insert`, `remove`, `clear` and depreciated `add_option` [#180](https://github.com/lawsie/guizero/issues/180)
- Refactoring of class hierarchy 
- Various bug fixes
- contributors [martinohanlon](https://github.com/martinohanlon)

## 0.5.1 - 2018-05-14

- `App`, `Window`, `Box` now support the following properties and will cascade them to widgets within them:
    - `bg`
    - `text_color`
    - `text_size`
    - `font`
    - `enabled`
- Introduced `ListBox`
- Bug fixes relating to `bg` and `text_color` causing widgets to change colour when selected
- Minor bug fixes with `CheckBox`, `Waffle` and `Combo`
- Documentation fixes and updates
- contributors to this release [martinohanlon](https://github.com/martinohanlon), [lawsie](https://github.com/lawsie), [Harlekuin](https://github.com/Harlekuin)

## 0.5.0 - 2018-04-10

- v0.5.0 includes significant refactoring of the guizero code base and introduces many new features
- New image functionality introduced when PIL is installed:
    - images can be passed as `Tk.PhotoImage` or `PIL.Image` objects as well as file paths
    - more images types are supported
    - animated images (gifs) are supported
    - images are scaled when the size is changed
- `ButtonGroup` - `selected` is now optional, `enabled` properties now supported, `value_text` fixed
- Fixed multiple `App` bug
- Created `Window` class to support multi-window applications
- Added `multiline` and `scrollbar` functionality to `TextBox`
- Refactored guizero to introduce a class hierarchy making guizero wide code changes easier to implement
- Added the following events to all widgets, this should be considered experimental in this release:
    - `when_clicked`
    - `when_left_button_pressed`
    - `when_left_button_released`
    - `when_right_button_pressed`
    - `when_right_button_released`
    - `when_key_pressed`
    - `when_key_released`
    - `when_mouse_enters`
    - `when_mouse_leaves`
    - `when_mouse_dragged`
- Various minor bug fixes
- Automated tests have been introduced
- contributors to this release [martinohanlon](https://github.com/martinohanlon), [scotty3785](https://github.com/scotty3785), [IDF31](https://github.com/IDF31), [drussell1974](https://github.com/drussell1974)  - ta very much :)

## 0.4.5 - 2018-03-04

- colors can now be specified as either `"red"`, `"#ffffff"`, or `(red, green, blue)` 
- change `Picture` `image` startup parameter to be optional
- updated `Picture` and `PushButton` errors and docs to show that PNG and GIF images can be used in Windows & Linux
- refactored `Waffle` resolving bugs that setting properties didnt change its appearance
- changed waffle so you can reference a pixel using `waffle[x,y]`
- added `text_color`, `text_size` and `font` properties to `Slider`
- added `width` and `height` properties to:
    - `Box`
    - `ButtonGroup`
    - `CheckBox`
    - `Combo`
    - `Picture`
    - `Slider`
    - `Text`
- added `width` property to:
    - `TextBox`
- contributors to this release [Coal0](https://github.com/coal0), [martinohanlon](https://github.com/martinohanlon), [scotty3785](https://github.com/scotty3785) - :)

## 0.4.4 - 2018-02-12

- made `PushButton` `command` optional
- `Combo` command functions can now have 0 arguments
- `Waffle` command functions can now have 0 arguments
- refactored command functions and added `update_command` to: 
    - `ButtonGroup`
    - `CheckBox`
    - `Combo`
    - `PushButton`
    - `Slider`
    - `Waffle`
- refactored `text_color`, `text_size` and `font` properties and added them to:
    - `ButtonGroup`
    - `Combo`
    - `CheckBox`
    - `PushButton`
    - `Text`
    - `TextBox`
- refactored `bg` (background) and added to:
    - `Box`
    - `ButtonGroup`
    - `CheckBox`
    - `Combo`
    - `Picture`
    - `PushButton`
    - `Slider`
    - `Text`
    - `TextBox`
 - contributors to this release [m4ddav3](https://github.com/m4ddav3), [Coal0](https://github.com/coal0), [lawsie](https://github.com/lawsie), [martinohanlon](https://github.com/martinohanlon) - :)

## 0.4.3 - 2018-01-10

Minor features, bug fixes and internal refactoring

- added `xspan`, `yspan` to grid layout (Credit: [penguintutor](https://github.com/penguintutor))
- fixed `show()` for widgets in a grid layout
- added `master`, `grid`, `align` and `visible` properties to widgets
- added `layout` property to containers
- fixed `Waffle` `height` (Credit: [scotty3785](https://github.com/scotty3785))
- minor doc updates
- 0.4.2 was never released due to some pypi / wheel problems

## 0.4.1 - 2017-12-28

Bug fixes and deployment test

- PushButton bug fixes
- added `enabled` property to widgets which support `Enable` / `Disable`
- documentation tidy up
- added build notes to documentation

## 0.4 - 2017-12-19

Thank you to everyone who has taken time to contribute code, suggest helpful improvements and report their use of the library. I am extremely grateful to the following people who have contributed pull requests since the last version:
[bcroston](https://github.com/bcroston), [bennuttall](https://github.com/bennuttall), [Coal0](https://github.com/Coal0),  [martinohanlon](https://github.com/martinohanlon) and  [scotty3785](https://github.com/scotty3785)

I am also very pleased to announce that [martinohanlon](https://github.com/martinohanlon) has very kindly agreed to maintain guizero whilst I am on maternity leave, beginning December 2017.

General changes:

- All classes rewritten with internal Tk objects rather than extending the Tk object, meaning you can access all Tk functionality as `Object.tk.tkmethod()` (Credit for idea: [bennuttall](https://github.com/bennuttall))
- Improved use of library with tab complete editors (e.g. ipython) – only the guizero properties and methods are listed so the list is shorter and more friendly. (Credit for idea: [bennuttall](https://github.com/bennuttall))
- [Bug fix] Grid layout now lays items out properly. Previously the x and y axes were flipped. (Whoops!) **This fix will cause apps with a grid layout to look different, but now behave correctly. You may need to update old code as a result of this change.**
- All classes now inherit from mixins, adding 9 new common methods usable on most widgets - `after()`, `cancel()`, `destroy()`, `disable()`, `enable()`, `focus()`, `hide()`, `show()`, `repeat()`,  (Credit: [Coal0](https://github.com/Coal0) and [martinohanlon](https://github.com/martinohanlon))
- The new `repeat()` method allows you to easily specify a repeated callback to a function, making it extremely easy to perform repetitive actions such as updating the GUI based on readings from a sensor.
- Documentation and examples have been improved and updated

App:

- New constructor argument `bg` replaces deprecated `bgcolor` argument. If both are specified, `bg` overrides `bgcolor`.
- `set_title()` and `bgcolor()` methods are now deprecated and have been replaced by `title` and `bg` properties
- New additional properties `width` and `height`

ButtonGroup:

- `get()` and `set()` methods are now deprecated and have been replaced by the `value` property
- New `value_text` property to get the text associated with the selected option

CheckBox:

- `get_text()`, `get_value()` and `change_text()` methods are now deprecated and have been replaced by the `value` and `text` properties
- New `toggle()` method added

Combo:

- `get()` and `set()` methods are now deprecated and have been replaced by the `value` property
- [Bug fix] `set_default()` now correctly resets the combo back to its originally specified value, whether this was the first option or a specified option

Picture:

- `set()` method is now deprecated and has been replaced by the `value` property

PushButton:

- `set_text()` method is now deprecated and has been replaced by the `text` property
- New properties for `text_color`, `bg`, `font`, `text_size`, `height` and `width` – make your buttons look pretty!
- Find out whether a button is pressed (1) or released (0) with the new `value` property
- New `icon()` method to set the icon of a button after it is created
- `toggle_state()` method deprecated and renamed to `toggle()` for consistency

Slider:

- New `value` property for getting and setting the value of the slider

Text:

- New constructor arguments `text_color` and `bg`
- `color` constructor argument now deprecated and replaced by `text_color`. If both are specified, `text_color` overrides `color`.
- `get()`, `set()`, `color()`, `font_face()` and `font_size()` methods are now deprecated, replaced by properties `value`, `text_color`, `bg`, `font` and `size`

TextBox:

- `get()` and `set()` methods now deprecated and replaced by `value` property

Waffle:

- All waffles will now have a memory. The `remember` constructor argument remains for backwards compatibility only **and will be removed in a future release**.
- You can now click on a Waffle, and specify a command to run when the Waffle is clicked on. The function given as the command should take two arguments as it will be passed the x, y coordinates of the pixel that was clicked. (Credit: [scotty3785](https://github.com/scotty3785))
- Changed internal implementation of the Waffle so it should now be able to redraw more efficiently. (Credit: [scotty3785](https://github.com/scotty3785))
