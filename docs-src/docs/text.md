# Text

```python
__init__(
    self,
    master,
    text="",
    size=12,
    color="black",
    bg=None,
    font="Helvetica",
    grid=None,
    align=None,
    visible=True,
    enabled=None,
    width=None,
    height=None)
```

### What is it?
The `Text` object displays non editable text in your app, useful for titles, labels and instructions.

![Text on Windows](images/text_windows.png)

### How do I make one?

Create a `Text` object like this:

```python
from guizero import App, Text
app = App()
text = Text(app, text="Hello World")
app.display()
```

### Starting parameters

When you create a `Text` object, you **must** specify a `master` and you can specify any of the the optional parameters. Specify parameters in the brackets, like this: `text = Text(app, text="hi")`

| Parameter | Data type          | Default     | Compulsory | Description                                                                                                           |
|-----------|--------------------|-------------|------------|-----------------------------------------------------------------------------------------------------------------------|
| master    | App, Window or Box | -           | Yes        | The container to which this widget belongs                                                                            |
| align     | string             | None        | -          | Alignment of this widget within its container. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`.             |
| color     | [color](colors.md) | black       | -          | The colour of the text. Accepts some colour strings (e.g. `red`) and colours specified in hex format (e.g. `#0099ff`) |
| font      | string             | "Helvetica" | -          | The font face that the text will be displayed in. Availability of fonts depends on which fonts are installed locally. |
| grid      | List [int, int]    | None        | -          | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout.         |
| size      | int                | 12          | -          | The font size of the text                                                                                             |
| text      | string             | ""          | -          | The text you want to display                                                                                          |
| visible   | boolean            | True        | No         | If the widget should be visible.                                                                                      |
| enabled   | boolean            | None        | No         | If the widget should be enabled. If `None` (the default) the enabled property will be inherited from the master       |
| width     | [size](size.md)    | None        | No         | Set the width of the widget in characters or to `"fill"`                                                              |
| height    | [size](size.md)    | None        | No         | Set the height of the widget in characters or to `"fill"`                                                             |


### Methods

You can call the following methods on a `Text` object..

| Method                           | Takes                                                         | Returns | Description                                                                                                                                                    |
|----------------------------------|---------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| after(time, command, args=None)  | time (int), command (function name), args (list of arguments) | -       | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| append(text)                     | text (string)                                                 | -       | Adds the provided `text` to the end of the current text within the object                                                                                      |
| cancel(command)                  | command (function name)                                       | -       | Cancels a scheduled call to `command`                                                                                                                          |
| clear()                          | -                                                             | -       | Clears the text                                                                                                                                                |
| destroy()                        | -                                                             | -       | Destroys the widget                                                                                                                                            |
| disable()                        | -                                                             | -       | Disables the widget so that it is "greyed out" and cannot be interacted with                                                                                   |
| enable()                         | -                                                             | -       | Enables the widget                                                                                                                                             |
| focus()                          | -                                                             | -       | Gives focus to the widget                                                                                                                                      |
| hide()                           | -                                                             | -       | Hides the widget from view. This method will unpack the widget from the layout manager.                                                                        |
| repeat(time, command, args=None) | time (int), command (function name), args (list of arguments) | -       | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| resize(width, height)            | width (int), height (int)                                     | -       | Sets the width and height of the widget                                                                                                                        |
| show()                           | -                                                             | -       | Displays the widget if it was previously hidden                                                                                                                |


### Properties

You can set and get the following properties:

| Method     | Data type          | Description                                                                                           |
|------------|--------------------|-------------------------------------------------------------------------------------------------------|
| align      | string             | The alignment of this widget within its container                                                     |
| bg         | [color](colors.md) | The background colour of the widget                                                                   |
| enabled    | boolean            | `True` if the widget is enabled                                                                       |
| font       | string             | The font of the text                                                                                  |
| grid       | List               | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| height     | [size](size.md)    | Set the height of the widget in characters or to `"fill"`                                             |
| master     | App or Box         | The container to which this widget belongs                                                            |
| text_size  | int                | The size of the text                                                                                  |
| text_color | [color](colors.md) | The colour of the text                                                                                |
| tk         | tkinter.Label      | The internal tkinter object, see [Using tkinter](usingtk.md)                                          |
| value      | string             | The text                                                                                              |
| visible    | boolean            | If this widget is visible                                                                             |
| width      | [size](size.md)    | Set the width of the widget in characters or to `"fill"`                                              |
