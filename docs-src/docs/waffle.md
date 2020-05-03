# Waffle

(Contains a `tkinter.Frame` object)

```python
__init__(
    self, 
    master, 
    height=3, 
    width=3, 
    dim=20, 
    pad=5, 
    color="white", 
    dotty=False, 
    grid=None, 
    align=None, 
    command=None, 
    remember=True, 
    visible=True, 
    enabled=None, 
    bg=None)
```

### What is it
The `Waffle` object display an n*n grid of squares with custom dimensions and padding.

![Waffle on Windows](images/waffle_windows.png)

### How do I make one?

Create a `Waffle` object like this:

```python
from guizero import App, Waffle
app = App()
waffle = Waffle(app)
app.display()
```

### Starting parameters

When you create a `Waffle` object you **must** specify `master` and you can specify any of the optional parameters. Specify parameters in the brackets, like this: `waffle = Waffle(app, height=25)`

| Parameter  | Takes              | Default | Compulsory | Description                                                                                                                                                                                                                     |
|------------|--------------------|---------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master     | App, Window or Box | -       | Yes        | The container to which this widget belongs                                                                                                                                                                                      |
| align      | string             | None    | -          | Alignment of this widget within its container. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`.                                                                                                                       |
| color      | [color](colors.md) | "white" | -          | The default colour of pixels on the waffle                                                                                                                                                                                      |
| command    | function name      | None    | -          | The name of a function to call when the waffle is clicked. This function MUST take either zero or two arguments, if the function takes two arguments the `x` and `y` co-ordinates of the pixel which was clicked will be given. |
| dim        | int                | 20      | -          | How large one of the pixels on the waffle is                                                                                                                                                                                    |
| dotty      | boolean            | False   | -          | Whether the pixels display as dots/circles (True) or squares (False)                                                                                                                                                            |
| grid       | List [int, int]    | None    | -          | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout.                                                                                                                   |
| height     | int                | 3       | -          | Set the height in waffle pixels                                                                                                                                                                                                 |
| pad        | int                | 5       | -          | How much space is between the pixels on the waffle                                                                                                                                                                              |
| width      | int                | 3       | -          | Set the width in waffle pixels                                                                                                                                                                                                  |
| visible    | boolean            | True    | No         | If the widget should be visible.                                                                                                                                                                                                |
| enabled    | boolean            | None    | No         | If the widget should be enabled. If `None` (the default) the enabled property will be inherited from the master                                                                                                                 |
| bg         | [color](colors.md) | None    | No         | The background colour of the waffle. Takes a [color](colors.md) value.                                                                                                                                                          |


### Methods

You can call the following methods on your Waffle object.

| Method                           | Takes                                                         | Returns                     | Description                                                                                                                                                    |
|----------------------------------|---------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| after(time, command, args=None)  | time (int), command (function name), args (list of arguments) | -                           | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| cancel(command)                  | command (function name)                                       | -                           | Cancels a scheduled call to `command`                                                                                                                          |
| destroy()                        | -                                                             | -                           | Destroys the widget                                                                                                                                            |
| disable()                        | -                                                             | -                           | Disables the widget so that it cannot be interacted with                                                                                                       |
| enable()                         | -                                                             | -                           | Enables the widget                                                                                                                                             |
| focus()                          | -                                                             | -                           | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)                                                                      |
| get_all()                        | -                                                             | List                        | Returns the pixel colours in the grid as a 2D list.                                                                                                            |
| get_pixel(x, y)                  | x (int), y (int)                                              | string                      | Returns the colour of the pixel at the specified coordinates. 0,0 is the top left of the grid.                                                                 |
| hide()                           | -                                                             | -                           | Hides the widget from view. This method will unpack the widget from the layout manager.                                                                        |
| pixel(x, y)                      | (int), y (int)                                                | [WafflePixel](#wafflepixel) | Returns the pixel at the specified coordinates. 0,0 is the top left of the grid. `Waffle.pixel(x,y)` is the equivalent of `Waffle[x,y]`                        |
| repeat(time, command, args=None) | time (int), command (function name), args (list of arguments) | -                           | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| set_all(color)                   | color ([color](colors.md))                                    | -                           | Sets all pixels to the specified colour.                                                                                                                       |
| set_pixel(x, y, color)           | x (int), y (int), color ([color](colors.md))                  | -                           | Sets the pixel at the specified coordinates to the specified colour. 0,0 is the top left of the grid.                                                          |
| show()                           | -                                                             | -                           | Displays the widget                                                                                                                                            |
| update_command(command)          | command (function name)                                       | -                           | Updates the function to call when the Waffle is clicked                                                                                                        |

### Properties

You can set and get the following properties:

| Method     | Data type          | Description                                                                                           |
|------------|--------------------|-------------------------------------------------------------------------------------------------------|
| align      | string             | The alignment of this widget within its container                                                     |
| bg         | [color](colors.md) | The background colour of the widget                                                                   |
| color      | [color](colors.md) | The default colour of pixels on the waffle                                                            |
| dotty      | bool               | If `True` the waffle will display circles                                                             |
| enabled    | boolean            | `True` if the widget is enabled                                                                       |
| grid       | List               | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| height     | [size](size.md)    | Set the height in waffle pixels                                                                       |
| master     | App or Box         | The container to which this widget belongs                                                            |
| pad        | int                | The size of the padding between pixels                                                                |
| pixel_size | int                | The size of the one pixel                                                                             |
| width      | [size](size.md)    | Set the width in waffle pixels                                                                        |
| visible    | boolean            | If this widget is visible                                                                             |

### Example

**Set a pixel colour**

A Waffle can remember the colour of each pixel within it.

```python
from guizero import App, Waffle

app = App()

my_waffle = Waffle(app)
my_waffle[2,1].color = "red"

# Your waffle will remember what colour each pixel is
print(my_waffle[2,1].color)

# Even the ones auto-set at the start (which are white by default)
print(my_waffle[1,1].color)

app.display()
```

## WafflePixel

A WafflePixel object is returned by `Waffle.pixel(x,y)` and `Waffle[x,y]`.

```python
from guizero import App, Waffle

app = App()

my_waffle = Waffle(app)
my_waffle.pixel(x,y).color = "red"
my_waffle[x,y].dotty = True

app.display()
```

### Properties

You can set and get the following properties:

| Method   | Data type          | Description                                       |
|----------|--------------------|---------------------------------------------------|
| x        | int                | Returns the x position of the pixel on the widget |
| x        | int                | Returns the y position of the pixel on the widget |
| canvas_x | int                | Returns the x position of the pixel on the canvas |
| canvas_y | int                | Returns the y position of the pixel on the canvas |
| color    | [color](colors.md) | Sets or returns the color of the pixel            |
| dotty    | bool               | Set to `True` to make the pixel a circle          |
| size     | int                | Returns the size of the pixel in _display_ pixels |
