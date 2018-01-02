# Waffle

(Contains a `tkinter.Frame` object)

`__init__(self, master, height=3, width=3, dim=20, pad=5, color="white", dotty=False, grid=None, align=None, command=None)`

### What is it
The `Waffle` object display an n*n grid of squares with custom dimensions and padding

![Waffle on Windows](images/waffle_windows.png)

### How do I make one?

Create a `Waffle` object like this:

```python
from guizero import App, Waffle
app = App()
waffle = Waffle(app)
app.display()
```

When you create a `Waffle` object you **must** specify `master` and you can specify any of the optional parameters. Specify parameters in the brackets, like this: `waffle = Waffle(app, height=25)`

| Parameter | Takes     | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box| -       | Yes        | The container to which this widget belongs |
| align     | string     | None   | -         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |
| color     | string    | "white" | -         | The starting colour of all pixels on the waffle |
| dim       | int       | 20      | -         | How large one of the pixels on the waffle is |
| dotty     | boolean   | False   | -         | Whether the pixels display as dots/circles (True) or squares (False) |
| grid      | List [int, int]     | None       | -         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| height    | int       | 3       | -         | How many pixels high the waffle is |
| pad       | int       | 5       | -         | How much space is between the pixels on the waffle |
| width     | int       | 3       | -         | How many pixels wide the waffle is |
| _remember_  | _boolean_   | _True_   | -         | _No longer needed - all Waffles will now have a memory._ |

Parameters in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero

### Methods

You can call the following methods on your Waffle object.

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| after(time, command)   | time (int), command (function name)   | -          | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| cancel(command)   | command (function name) | -          | Cancels a scheduled call to `command`    |
| destroy()   | -  | -          | Destroys the widget    |
| focus()  | -  | -          | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)  |
| get_all()     | - | List | IMPORTANT: To use this function, you must set remember=True when you create the Waffle. Returns the pixel colours in the grid as a 2D list. |
| get_pixel(x, y)| x (int), y (int) | string |  IMPORTANT: To use this function, you must set remember=True when you create the Waffle. Returns the colour of the pixel at the specified coordinates. 0,0 is the top left of the grid. |
| hide()  | -   | -          | Hides the widget from view. This method will unpack the widget from the layout manager.   |
| repeat(time, command)  | time (int), command (function name)  | -          | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| set_all(color)     | color (string) | -          | Sets all pixels to the specified colour (allows hex code e.g. #0099ff or colour name e.g. "red") |
| set_pixel(x, y, color)   | x (int), y (int), color (string)     | -         | Sets the pixel at the specified coordinates to the specified colour. 0,0 is the top left of the grid.  |
| show()  | - | -          | Displays the widget   |

### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| align         | string      | The alignment of this widget within its grid location |
| color         | int         | The color of the whole waffle |
| dotty         | bool        | If `True` the waffle will display circles  |
| grid          | List        | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| height        | int         | The height of the waffle  |
| master        | App or Box  | The container to which this widget belongs |
| pad           | int         | The size of the padding between pixels   |
| pixel_size    | int         | The size of the one pixel  |
| width         | int         | The width of the waffle |
| visible       | boolean     | If this widget is visible |

### Example

**Set a pixel colour**

A Waffle can remember the colour of each pixel within it.

```python
from guizero import App, Waffle

app = App()

my_waffle = Waffle(app)
my_waffle.set_pixel(2, 1, "red")

# Your waffle will remember what colour each pixel is
print(my_waffle.get_pixel(2,1))

# Even the ones auto-set at the start (which are white by default)
print(my_waffle.get_pixel(1,1))

app.display()

```
