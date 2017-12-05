# guizero 0.4 - what’s new

- All classes rewritten with internal Tk objects rather than extending the Tk object, meaning you can access all Tk functionality as `Object.tk.tkmethod()`
- Improves use of library with tab complete editors (e.g. ipython) – only the guizero properties and methods are listed so the list is shorter and more friendly
- [Bug fix] Grid layout now lays items out properly. Previously the x and y axes were flipped. (Whoops!)
- All classes now inherit from `_Widget`, adding a lot of functionality which can be accessed by all widgets.

## App
- New constructor argument `bg` replaces deprecated `bgcolor` argument. If both are specified, `bg` overrides `bgcolor`.
- `set_title()` and `bgcolor()` methods are now deprecated and have been replaced by `title` and `bg` properties
- New additional properties `width` and `height`
- New `destroy()` method added

## ButtonGroup
- `get()` and `set()` methods are now deprecated and have been replaced by the `value` property
- New `value_text` property to get the text associated with the selected option

## CheckBox
- `get_text()`, `get_value()` and `change_text()` methods are now deprecated and have been replaced by the `value` and `text` properties
- New `toggle()` method added

## Combo
- `get()` and `set()` methods are now deprecated and have been replaced by the `value` property
- [Bug fix] `set_default()` now correctly resets the combo back to its originally specified value, whether this was the first option or a specified option

## Picture
- `set()` method is now deprecated and has been replaced by the `value` property

## PushButton
- `set_text()` method is now deprecated and has been replaced by the `value` property
- New properties for `text_color`, `bg`, `font`, `text_size`, `height` and `width` – make your buttons look pretty!
- New `icon()` method to set the icon of a button after it is created
- `toggle_state()` method deprecated and renamed to `toggle()` for consistency

## Slider
- New `value` property for getting and setting the value of the slider

## Text
- New constructor arguments `text_color` and `bg`
- `color` constructor argument now deprecated and replaced by `text_color`. If both are specified, `text_color` overrides `color`.
- `get()`, `set()`, `color()`, `font_face()` and `font_size()` methods are now deprecated, replaced by properties `value`, `text_color`, `bg`, `font` and `size`

## TextBox
- `get()` and `set()` methods now deprecated and replaced by `value` property

## Waffle
- All waffles will now have a memory. The `remember` constructor argument remains for backwards compatibility, but will always be True.
- You can now click on a waffle, and specify a command to run when the waffle is clicked on. The function given as the command should take two arguments as it will be passed the x, y coordinates of the pixel that was clicked.
- Changed implementation of the waffle so it should now be able to redraw more efficiently
