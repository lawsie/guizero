# Text

(Contains a `tkinter.Label` object)

`__init__(self, master, text="", size=12, color="black", text_color=None, bg=None, font="Helvetica", grid=None, align=None)`

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

| Parameter | Data type | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| text   | string    | ""  | No         | The text you want to display |
| size   | int    | 12     | No         | The font size of the text |
| color   | string     | black     | No         | The colour of the text. Accepts some colour strings (e.g. `red`) and colours specified in hex format (e.g. `#0099ff`)  |
| font   | string     | "Helvetica"     | No         | The font face that the text will be displayed in. Availability of fonts depends on which fonts are installed locally. |
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | None    | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |


### Methods

You can call the following methods on a `Text` object..

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| append(text)  | text (string) | -          | Adds the provided `text` to the end of the current text within the object |
| clear()   | -             | -          | Clears the text            |
| _color(color)_ | color (string) | -      | Sets the colour of the text to the `color` provided. This can be a defined colour (e.g. "blue") or a hex format rgb colour (e.g. "#ff0000") |
| _font_face(font)_ | font (string) | - | Sets the font face to the `font` provided |
| _font_size(size)_ | size (int) | - |  Sets the font size to the `size` provided |
| _get()_ | - | string |  Returns a string containing the text from the object |
| _set(text)_ | text (string) | - |  Sets the text within the object to the `text` provided |
| after(time, command)   | time (int), command (function name)   | -          | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| repeat(time, command)  | time (int), command (function name)  | -          | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| cancel(command)   | command (function name) | -          | Cancels a scheduled call to `command`    |
| destroy()   | -  | -          | Destroys the widget    |
| disable()  | - | -          | Disables the widget so that it is "greyed out" and cannot be interacted with   |
| enable()  | -  | -          | Enables the widget   |
| focus()  | -  | -          | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)  |
| hide()  | -   | -          | Hides the widget from view. This method will unpack the widget from the layout manager.   |
| show()  | - | -          | Displays the widget   |

Methods in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero


### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| value         | string      | The text   |
| text_color    | string      | The colour of the text  |
| bg            | string      | The background colour  |
| font          | string      | The font of the text  |
| size          | int         | The size of the text  |

