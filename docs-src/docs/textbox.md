# TextBox

(Contains a `tkinter.Entry` object)

`__init__(self, master, text="", width=10, grid=None, align=None)`

### What is it
The `TextBox` object sisplay a text box which the user can type in.

![TextBox on Windows](images/textbox_windows.png)

### How do I make one?

Create a `TextBox` object like this:

```python
from guizero import App, TextBox
app = App()
input_box = TextBox(app)
app.display()
```

### Starting parameters

When you create a `TextBox` object you **must** specify `master` and you can specify any of the optional parameters. Specify parameters in the brackets, like this: `textbox = TextBox(app, text="Please enter some text")`

| Parameter | Data type | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs |
| align   | string     | None     | -         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |
| grid   | List [int, int]   | None     | -         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| text   | string    | ""  | -         | Any text you wish to be pre-filled in the text box |
| width   | int    | 10     | -         | The width of the text box|


### Methods

You can call the following methods on your TextBox object.

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| after(time, command)   | time (int), command (function name)   | -          | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| append(text)  | text (string) | -          | Adds the provided `text` to the end of the current text within the text box |
| cancel(command)   | command (function name) | -          | Cancels a scheduled call to `command`    |
| clear()   | -             | -          | Clears the textbox            |
| destroy()   | -  | -          | Destroys the widget    |
| disable()  | - | -          | Disables the widget so that it is "greyed out" and cannot be interacted with   |
| enable()  | -  | -          | Enables the widget   |
| focus()  | -  | -          | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)  |
| hide()  | -   | -          | Hides the widget from view. This method will unpack the widget from the layout manager.   |
| repeat(time, command)  | time (int), command (function name)  | -          | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| show()  | - | -          | Displays the widget if it was previously hidden   |
| _get()_ | - | _string_ |  _Replaced by `value` property_ |
| _set(text)_ | _text (string)_ | - |  _Replaced by `value` property_ |

Methods in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero

### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| align         | string      | The alignment of this widget within its grid location |
| enabled       | boolean     | `True` if the widget is enabled |
| grid          | List        | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| master        | App or Box  | The container to which this widget belongs |
| value         | string      | The text in the TextBox |
| visible       | boolean     | If this widget is visible |

### Examples

**Creating a TextBox with default text**

You can set the default text in a TextBox when it is created using the `text` parameter:

```python
from guizero import App, TextBox
app = App()
input_box = TextBox(app, text="Type here")
app.display()
```
