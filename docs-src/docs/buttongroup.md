# ButtonGroup

```python
__init__(
    self,
    master,
    options=[],
    selected=None,
    horizontal=False,
    command=None,
    grid=None,
    align=None,
    args=None,
    visible=True,
    enabled=None,
    width=None,
    height=None)
```

### What is it?
The `ButtonGroup` object displays a group of radio buttons, allowing the user to choose a single option.

![ButtonGroup](images/buttongroup.png)

### How do I make one?

Create a `ButtonGroup` object like this:

```python
from guizero import App, ButtonGroup
app = App()
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], selected="cheese")
app.display()
```

### Starting parameters

When you create a `ButtonGroup` object you **must** specify a `master` and you can specify any of the optional parameters. Specify parameters in the brackets like this: `choice = ButtonGroup(app, options=["cheese", "ham", "salad"], selected=1)`

| Parameter  | Takes              | Default | Compulsory | Description                                                                                                                                                                                                          |
|------------|--------------------|---------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master     | App, Window or Box | -       | Yes        | The container to which this widget belongs                                                                                                                                                                           |
| options    | list or 2D List    | -       | No         | Either a list or a 2D list of [text, value] pairs. If a 2D list is specified, the first item in the pair will be displayed on the interface, and the second item will be a hidden value associated with this option. |
| selected   | string             | -       | -          | The option that should be selected, if a value isn't provided the first option will be selected.                                                                                                                     |
| align      | string             | None    | -          | Alignment of this widget within its container. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`.                                                                                                            |
| command    | function name      | None    | -          | The name of a function to call when the selected option changes.                                                                                                                                                     |
| args       | list               | None    | -          | If you wish to pass any arguments to the function specified in the command parameter, you can specify them as a list                                                                                                 |
| grid       | list [int, int]    | None    | -          | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout.                                                                                                        |
| horizontal | boolean            | False   | -          | Whether the buttons stack vertically or horizontally. (Defaults to vertical)                                                                                                                                         |
| visible    | boolean            | True    | No         | If the widget should be visible.                                                                                                                                                                                     |
| enabled    | boolean            | None    | No         | If the widget should be enabled. If `None` (the default) the enabled property will be inherited from the master                                                                                                      |
| width      | [size](size.md)    | None    | No         | Set the width of the widget in characters or to `"fill"`                                                                                                                                                             |
| height     | [size](size.md)    | None    | No         | Set the height of the widget in characters or to `"fill"`                                                                                                                                                            |


### Methods

You can call the following methods on an `ButtonGroup` object.

| Method                              | Takes                                                                                | Returns | Description                                                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| append(option)                      | item (string)                                                                        | -       | Appends a new `option` to the end of the ButtonGroup.                                                                                                          |
| after(time, command, args=None)     | time (int), command (function name), args (list of arguments)                        | -       | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| cancel(command)                     | command (function name)                                                              | -       | Cancels a scheduled call to `command`                                                                                                                          |
| destroy()                           | -                                                                                    | -       | Destroys the widget                                                                                                                                            |
| disable()                           | -                                                                                    | -       | Disables the widget so that it is "greyed out" and cannot be interacted with                                                                                   |
| enable()                            | -                                                                                    | -       | Enables the widget                                                                                                                                             |
| focus()                             | -                                                                                    | -       | Gives focus to the widget                                                                                                                                      |
| get_group_as_list()                 | -                                                                                    | list    | Returns a list containing all of the text/hidden value pairs from the ButtonGroup (useful for debugging)                                                       |
| hide()                              | -                                                                                    | -       | Hides the widget from view. This method will unpack the widget from the layout manager.                                                                        |
| insert(index, option)               | index (int), option (string)                                                         | -       | Insert a new `option` in the ButtonGroup at `index`                                                                                                            |
| remove(option)                      | item (string)                                                                        | Boolean | Removes the first `option` from the ButtonGroup. Returns `True` if an item was removed.                                                                        |
| repeat(time, command, args=None)    | time (int), command (function name), args (list of arguments)                        | -       | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| resize(width, height)               | width (int), height (int)                                                            | -       | Sets the width and height of the widget                                                                                                                        |
| show()                              | -                                                                                    | -       | Displays the widget if it was previously hidden                                                                                                                |
| update_command(command, args =None) | command (function name), args (_Optional_ List of arguments to be passed to command) | -       | Updates the function to call when the selected option changes                                                                                                  |


### Properties

You can set and get the following properties:

| Method     | Data type          | Description                                                                                           |
|------------|--------------------|-------------------------------------------------------------------------------------------------------|
| align      | string             | The alignment of this widget within its container                                                     |
| bg         | [color](colors.md) | The background colour of the widget                                                                   |
| children   | List               | A list of the widgets in this container. `[RadioButton, *]`                                           |
| enabled    | boolean            | `True` if the widget is enabled                                                                       |
| font       | string             | The font of the text                                                                                  |
| grid       | List               | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| height     | [size](size.md)    | Set the height of the widget in characters or to `"fill"`                                             |
| master     | App or Box         | The container to which this widget belongs                                                            |
| value      | string             | The hidden value associated with the currently selected option                                        |
| value_text | string             | The text associated with the currently selected option                                                |
| visible    | boolean            | If this widget is visible                                                                             |
| width      | [size](size.md)    | Set the width of the widget in characters or to `"fill"`                                              |
| text_size  | int                | The size of the text                                                                                  |
| text_color | [color](colors.md) | The colour of the text                                                                                |
| tk         | tkinter.Frame      | The internal tkinter object, see [Using tkinter](usingtk.md)                                          |

Refer to a property as `<name of widget>.property`. For example, if your `ButtonGroup` object is called `choice` you would write `choice.value`.

You can **set** the property (for example `choice.value = "2"`) or **get** the value of the property to use (for example `print(choice.value)`).

### Examples

**Creating a ButtonGroup with a 2D list**

If you want to create a ButtonGroup object with your own hidden values you can specify a 2D list of options:

```python
from guizero import App, ButtonGroup, Text

def update_text():
    what_is_selected.value = activities.value

app = App()
activities = ButtonGroup(app, options=[
                              ["Roller Skating", "skate"],
                              ["White water rafting", "WWR"],
                              ["Mountain climbing", "climb"]
                            ],
                            selected="skate", command=update_text)

what_is_selected = Text(app, text="skate")
app.display()
```

### Using ButtonGroup tk widgets

Advanced users can gain internal access to the internal tkinter widgets used by `ButtonGroup`. For more information on using tkinter in combination with guizero see [Using tkinter](usingtk.md).

The `ButtonGroup` widget contains a `tkinter.Frame` object, which frames multiple guizero `RadioButton` widgets. Each `RadioButton` widget contains a `tkinter.Radiobutton` object.

The `.children` property returns the list of `RadioButton` widgets in the order they appear in the `ButtonGroup`:

To access the internal `RadioButton` tk object you would use the child's `tk` property e.g.

```python
button_group = ButtonGroup(app)

for radio_button in ButtonGroup.children:
    tk_radio_button = radio_button.tk
```