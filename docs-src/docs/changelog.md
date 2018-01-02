# guizero

## 0.4.2 - in dev

Minor features, bug fixes and internal refactoring

- added `xspan`, `yspan` to grid layout (Credit: [penguintutor](https://github.com/penguintutor))
- fixed `show()` for widgets in a grid layout
- added `master`, `grid`, `align` and `visible` properties to widgets
- added `layout` property to containers

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

