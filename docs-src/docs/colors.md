## Colors (or Colo**u**rs)

You can set colors in guizero using:

- the name of the color - `white`
- a #rgb hex value - `#ffffff`
- a list of rgb values - `(255,255,255)`

Colors can be used as either starting parameters, for example:

```python
app = App(bg = "red")
app = App(bg = "#ff0000")
app = App(bg = (255, 0, 0))
```

or as properties, for example:

```python
text = Text(app, text = "hi")
text.text_color = "green"
text.text_color = "#00ff00"
text.text_color = (0, 255, 0)
```

If a color is set using a list of rgb values (`(255,255,255)`) it will be returned as an #rgb hex value (`#ffffff`)

### Color names

Some color names can be given as strings, for example

- `white`
- `black`
- `red`
- `green`
- `blue`
- `yellow`

A complete list of color names is available at [wiki.tcl.tk/37701](https://wiki.tcl.tk/37701)

### rgb hex value

A rgb color value must start with a `#` and 6 characters following, 2 each for the red, green and blue value in hex. Each value must be `00` - `ff`. Here are some examples:

- white = `#ffffff`
- black = `#000000`
- red = `#ff0000`
- green = `#00ff00`
- blue = `#0000ff`
- yellow = `#ffff00`

You can mix your own color by changing the red, green and blue values.

There is a RGB calculator application at [https://www.w3schools.com/colors/colors_rgb.asp](https://www.w3schools.com/colors/colors_rgb.asp) where you can create your own color and get the `#rrggbb` value.

### rgb list

The `(red, green, blue)` list color must contain three elements in the order red, green, blue. Each value must be between 0 - 255. Here are some examples:

- white = (255, 255, 255)
- black = (0, 0, 0)
- red = (255, 0, 0)
- green = (0, 255, 0)
- blue = (0, 0, 255)
- yellow = (255, 255, 0)
