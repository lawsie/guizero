# Combo

(Contains a `tkinter.OptionMenu` object)

```python
__init__(
    self,
    master,
    options=[],
    selected=None,
    command=None,
    grid=None,
    align=None,
    visible=True,
    enabled=None,
    width=None,
    height=None)
```

### What is it?
The `Combo` object displays a drop down box allowing a single option to be selected from a list of options.

![Combo on Windows](images/combo_windows.png)

### How do I make one?

Create a `Combo` object like this:

```python
from guizero import App, Combo
app = App()
combo = Combo(app, options=["Beef", "Chicken", "Fish", "Vegetarian"])
app.display()
```

### Starting parameters

When you create a `Combo` object you **must** specify a `master`  and you can specify any of the optional parameters. Specify parameters in the brackets, like this: `combo = Combo(app, options=["Beef", "Chicken", "Fish", "Vegetarian"])`

| Parameter | Takes              | Default | Compulsory | Description                                                                                                                                                                                               |
|-----------|--------------------|---------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| master    | App, Window or Box | -       | Yes        | The container to which this widget belongs                                                                                                                                                                |
| options   | List               | []      | No         | A list of options to display                                                                                                                                                                              |
| selected  | string             | None    | No         | The option to select by default                                                                                                                                                                           |
| align     | string             | None    | -          | Alignment of this widget within its container. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`.                                                                                                 |
| command   | function name      | None    | -          | The name of a function to call when a different option is selected. This function MUST take either zero or one argument, if the function takes one argument the current value of the Combo will be given. |
| grid      | List [int, int]    | None    | -          | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout.                                                                                             |
| visible   | boolean            | True    | No         | If the widget should be visible.                                                                                                                                                                          |
| enabled   | boolean            | None    | No         | If the widget should be enabled. If `None` (the default) the enabled property will be inherited from the master                                                                                           |
| width     | [size](size.md)    | None    | No         | Set the width of the widget in characters or to `"fill"`                                                                                                                                                  |
| height    | [size](size.md)    | None    | No         | Set the height of the widget in characters or to `"fill"`                                                                                                                                                 |



### Methods

You can call the following methods on a `Combo` object.

| Method                           | Takes                                                         | Returns  | Description                                                                                                                                                    |
|----------------------------------|---------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| append(option)                   | item (string)                                                 | -        | Appends a new `option` to the end of the Combo.                                                                                                                |
| after(time, command, args=None)  | time (int), command (function name), args (list of arguments) | -        | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| cancel(command)                  | command (function name)                                       | -        | Cancels a scheduled call to `command`                                                                                                                          |
| clear()                          | -                                                             | -        | Removes all options from the Combo box                                                                                                                         |
| destroy()                        | -                                                             | -        | Destroys the widget                                                                                                                                            |
| disable()                        | -                                                             | -        | Disables the widget so that it is "greyed out" and cannot be interacted with                                                                                   |
| enable()                         | -                                                             | -        | Enables the widget                                                                                                                                             |
| focus()                          | -                                                             | -        | Gives focus to the widget                                                                                                                                      |
| hide()                           | -                                                             | -        | Hides the widget from view. This method will unpack the widget from the layout manager.                                                                        |
| insert(index, option)            | index (int), item (string)                                    | -        | Insert a new `option` in the Combo at `index`                                                                                                                  |
| remove(option)                   | item (string)                                                 | Boolean  | Removes the first `option` from the Combo. Returns `True` if an item was removed.                                                                              |
| repeat(time, command, args=None) | time (int), command (function name), args (list of arguments) | -        | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| resize(width, height)            | width (int), height (int)                                     | -        | Sets the width and height of the widget                                                                                                                        |
| select_default()                 | -                                                             | -        | Resets the combo box so that the first item is selected                                                                                                        |
| show()                           | -                                                             | -        | Displays the widget if it was previously hidden                                                                                                                |
| update_command(command)          | command (function name)                                       | -        | Updates the function to call when a different option is selected.                                                                                              |



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
| value      | string             | The text associated with the currently selected option                                                |
| visible    | boolean            | If this widget is visible                                                                             |
| width      | [size](size.md)    | Set the width of the widget in characters or to `"fill"`                                              |
| text_size  | int                | The size of the text                                                                                  |
| text_color | [color](colors.md) | The colour of the text                                                                                |


Refer to a property as `<name of widget>.property`. For example, if your `Combo` object is called `combo` you would write `combo.value`.

You can **set** the property (for example `combo.value = "Chicken"`) or **get** the value of the property to use (for example `print(combo.value)`).

### Examples

**Calling a function when the value selected changes**

You can call a function when the selected value in a `Combo` object changes. The function you call can take either zero or one argument, if the function takes one argument it will automatically be passed a string containing the currently selected value from the `Combo` object.

```python
from guizero import App, Text, Combo
def you_chose(selected_value):
    if selected_value == "Tiny goblet":
        result.value = "You chose...wisely"
    else:
        result.value = "You chose...poorly"

app = App()
instructions = Text(app, text="Choose a goblet")
combo = Combo(app, options=["", "Huge golden goblet", "Jewel encrusted goblet", "Tiny goblet"], command=you_chose)
result = Text(app)
app.display()
```

![Combo calling a function](images/combo_function_windows.png)
