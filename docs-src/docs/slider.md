# Slider

(Contains a `tkinter.Scale` object)

`__init__(self, master, start=0, end=100, horizontal=True, command=None, grid=None, align=None)`

### What is it?
The `Slider` object displays a bar and selector which can be used to specify a value in a range.

The above code looks like this on Windows:
![Slider on Windows](images/slider_windows.png)

### How do I make one?

Create a `Slider` object like this:

```python
from guizero import App, Slider
app = App()
slider = Slider(app)
app.display()
```

### Starting paramters

When you create a `Slider` object, you **must** specify a `master` and you can specify any of the the optional parameters. Specify parameters in the brackets, like this: `slider = Slider(app, horizontal=False)`

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs |
| align   | string     | None     | -         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |
| command | function name | None | -   | The name of a function to call when the slider value is changed |
| end | int | 100 | -   | The largest value selectable on the slider |
| grid   | List [int, int]   | None     | -         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| horizontal | Boolean | True | -   | Whether you wish to display your slider horizontally or vertically (defaults to horizontal) |
| start   | int    | 0  | -         | The smallest value selectable on the slider |


### Methods

You can call the following methods on a `Slider` object.

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| add_command(command)  | command (function name)  | -          | Sets the function called when the slider value is changed to the function specified in `command` |
| after(time, command)   | time (int), command (function name)   | -          | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| cancel(command)   | command (function name) | -          | Cancels a scheduled call to `command`    |
| destroy()   | -  | -          | Destroys the widget    |
| disable()  | - | -          | Disables the widget so that it is "greyed out" and cannot be interacted with   |
| enable()  | -  | -          | Enables the widget   |
| focus()  | -  | -          | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)  |
| hide()  | -   | -          | Hides the widget from view. This method will unpack the widget from the layout manager.   |
| repeat(time, command)  | time (int), command (function name)  | -          | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| show()  | - | -          | Displays the widget if it was previously hidden  |

### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| align         | string      | The alignment of this widget within its grid location |
| enabled       | boolean     | `True` if the widget is enabled |
| grid          | List        | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| master        | App or Box  | The container to which this widget belongs |
| value         | string      | The current value of the slider  |
| visible       | boolean     | If this widget is visible |

### Examples

**Calling a function when the slider value changes**

You can specify a function to call when the slider value changes. Your function **MUST** have a minimum of one parameter as it will automatically receive a string containing the value of the slider (called `slider_value` in the example) when it is called.

This code has a slider and a text box, and the text box updates automatically to display the current value of the slider.

![Text box and slider](images/textbox_slider_windows.png)

```python
from guizero import App, Slider, TextBox
def slider_changed(slider_value):
    textbox.value = slider_value

app = App()
slider = Slider(app, command=slider_changed)
textbox = TextBox(app)
app.display()
```
