# TextBox

```python
__init__(
    self,
    master,
    text="",
    width=10,
    height=1,
    grid=None,
    align=None,
    visible=True,
    enabled=None,
    multiline=False,
    scrollbar=False,
    command=None,
    hide_text=False)
```

### What is it
The `TextBox` object displays a text box which the user can type in.

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

| Parameter | Data type          | Default | Compulsory | Description                                                                                                                                                                                               |
|-----------|--------------------|---------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master    | App, Window or Box | -       | Yes        | The container to which this widget belongs                                                                                                                                                                |
| align     | string             | None    | -          | Alignment of this widget within its container. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`.                                                                                                 |
| grid      | List [int, int]    | None    | -          | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout.                                                                                             |
| text      | string             | ""      | -          | Any text you wish to be pre-filled in the text box                                                                                                                                                        |
| width     | int                | 10      | -          | Set the width of the widget in characters or to `"fill"`                                                                                                                                                  |
| height    | int                | 1       | -          | Set the height of the widget in characters or to `"fill"`, only effective if `multiline` is `True`                                                                                                        |
| visible   | boolean            | True    | No         | If the widget should be visible.                                                                                                                                                                          |
| enabled   | boolean            | None    | No         | If the widget should be enabled. If `None` (the default) the enabled property will be inherited from the master                                                                                           |
| multiline | boolean            | False   | No         | Create a multi-line text box.                                                                                                                                                                             |
| scrollbar | boolean            | False   | No         | Add a vertical scrollbar to a multi-line text box                                                                                                                                                         |
| command   | function name      | None    | -          | The name of a function to call when the text is changed. This function MUST take either zero or one argument, if the function takes one argument the key which was added to the textbox will be returned. |
| hide_text | boolean            | False   | -          | When set to `True` will hide the text replacing typed characters with `*`. Setting to a character will result in the text being hidden with that character.                                               |


### Methods

You can call the following methods on your TextBox object.

| Method                           | Takes                                                         | Returns | Description                                                                                                                                                    |
|----------------------------------|---------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| after(time, command, args=None)  | time (int), command (function name), args (list of arguments) | -       | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| append(text)                     | text (string)                                                 | -       | Adds the provided `text` to the end of the current text within the text box                                                                                    |
| cancel(command)                  | command (function name)                                       | -       | Cancels a scheduled call to `command`                                                                                                                          |
| clear()                          | -                                                             | -       | Clears the textbox                                                                                                                                             |
| destroy()                        | -                                                             | -       | Destroys the widget                                                                                                                                            |
| disable()                        | -                                                             | -       | Disables the widget so that it is "greyed out" and cannot be interacted with                                                                                   |
| enable()                         | -                                                             | -       | Enables the widget                                                                                                                                             |
| focus()                          | -                                                             | -       | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)                                                                      |
| hide()                           | -                                                             | -       | Hides the widget from view. This method will unpack the widget from the layout manager.                                                                        |
| repeat(time, command, args=None) | time (int), command (function name), args (list of arguments) | -       | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| resize(width, height)            | width (int), height (int)                                     | -       | Sets the width and height of the widget                                                                                                                        |
| show()                           | -                                                             | -       | Displays the widget if it was previously hidden                                                                                                                |
| update_command(command)          | command (function name)                                       | -       | Updates the function to call when the text is changed.                                                                                                         |

### Properties

You can set and get the following properties:

| Method     | Data type          | Description                                                                                                                                                 |
|------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| align      | string             | The alignment of this widget within its container                                                                                                           |
| bg         | [color](colors.md) | The background colour of the widget                                                                                                                         |
| enabled    | boolean            | `True` if the widget is enabled                                                                                                                             |
| font       | string             | The font of the text                                                                                                                                        |
| grid       | List               | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid                                                       |
| height     | [size](size.md)    | Set the height of the widget in characters or to `"fill"`, only effective if `multiline` is `True`                                                          |
| hide_text  | boolean / char     | When set to `True` will hide the text replacing typed characters with `*`. Setting to a character will result in the text being hidden with that character. |
| master     | App or Box         | The container to which this widget belongs                                                                                                                  |
| value      | string             | The text in the TextBox                                                                                                                                     |
| visible    | boolean            | If this widget is visible                                                                                                                                   |
| width      | [size](size.md)    | Set the width of the widget in characters or to `"fill"`                                                                                                    |
| text_size  | int                | The size of the text                                                                                                                                        |
| text_color | [color](colors.md) | The colour of the text                                                                                                                                      |
| tk         | tkinter.Entry      | The internal tkinter object, see [Using tkinter](usingtk.md)                                                                                                |

### Examples

**Creating a TextBox with default text**

You can set the default text in a TextBox when it is created using the `text` parameter:

```python
from guizero import App, TextBox
app = App()
input_box = TextBox(app, text="Type here")
app.display()
```

**Creating a password TextBox with hidden text**

You can hide the text in a TextBox using the `hide_text` parameter:

```python
from guizero import App, TextBox
app = App()
password_box = TextBox(app, hide_text=True)
app.display()
```

**Creating a multi-line TextBox**

You can create a text box which is capable of capturing multiple lines of text by setting the `multiline` parameter to `True` and giving the textbox a `height`:

```python
from guizero import App, TextBox
app = App()
input_box = TextBox(app, text="Type lines here", height=10, multiline=True)
app.display()
```

Multi-line text boxes can also be given a scrollbar by setting the `scrollbar` parameter to `True`:

```python
input_box = TextBox(app, text="Type lines here", height=10, multiline=True, scrollbar=True)
```