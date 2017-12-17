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
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| text   | string    | ""  | No         | Any text you wish to be pre-filled in the text box |
| width   | int    | 10     | No         | The width of the text box|
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | None     | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |


### Methods

You can call the following methods on your TextBox object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| append(text)  | text (string) | -          | Adds the provided `text` to the end of the current text within the text box |
| clear()   | -             | -          | Clears the textbox            |
| _get()_ | - | string |  Returns a string containing current contents of the textbox |
| _set(text)_ | text (string) | - |  Sets the text within the text box to the `text` provided |

Methods in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero

### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| value         | string      | The text in the TextBox |

### Examples

**Creating a TextBox with default text**

You can set the default text in a TextBox when it is created using the `text` parameter:

```python
from guizero import App, TextBox
app = App()
input_box = TextBox(app, text="Type here")
app.display()
```
