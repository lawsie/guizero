# Combo

(Contains a `tkinter.OptionMenu` object)

`__init__(self, master, options, selected=None, command=None, grid=None, align=None)`

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

When you create a `Combo` object you **must** specify `master` and `options` and you can specify any of the optional parameters. Specify parameters in the brackets, like this: `combo = Combo(app, options=["Beef", "Chicken", "Fish", "Vegetarian"])`

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| options   | List    | -  | Yes         | A list of options to display |
| align   | string     | None     | -         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |
| command | function name | None | -   | The name of a function to call when a different option is selected. This function MUST take one argument as it will be auto-given the current value of the Combo. **The command can only be specified when creating the `Combo` object and cannot be changed later.** |
| grid   | List [int, int]   | None     | -         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |


### Methods

You can call the following methods on a `CheckBox` object.

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| add_option(option) | option (string) | - |  Adds a new item to the combo box with the value `option` |
| after(time, command)   | time (int), command (function name)   | -          | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| cancel(command)   | command (function name) | -          | Cancels a scheduled call to `command`    |
| clear() | - | - |  Removes all options from the Combo box |
| destroy()   | -  | -          | Destroys the widget    |
| disable()  | - | -          | Disables the widget so that it is "greyed out" and cannot be interacted with   |
| enable()  | -  | -          | Enables the widget   |
| focus()  | -  | -          | Gives focus to the widget  |
| hide()  | -   | -          | Hides the widget from view. This method will unpack the widget from the layout manager.   |
| repeat(time, command)  | time (int), command (function name)  | -          | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| select_default() | - | - |  Resets the combo box so that the first item is selected |
| show()  | - | -          | Displays the widget if it was previously hidden  |
| _get()_  | -  | _string_          | _Replaced by the `value` property_ |
| _set(text)_   | _text (string)_         | -         | _Replaced by the `value` property_      |






Methods in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero

### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| align         | string      | The alignment of this widget within its grid location |
| enabled       | boolean     | `True` if the widget is enabled |
| grid          | List        | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| master        | App or Box  | The container to which this widget belongs |
| value         | string      | The text associated with the currently selected option  |
| visible       | boolean     | If this widget is visible |


Refer to a property as `<name of widget>.property`. For example, if your `Combo` object is called `combo` you would write `combo.value`.

You can **set** the property (for example `combo.value = "Chicken"`) or **get** the value of the property to use (for example `print(combo.value)`).

### Examples

**Calling a function when the value selected changes**

You can call a function when the selected value in a `Combo` object changes. This must be set up at the time you create the `Combo` object and cannot be defined later. The function you call **MUST** take a minimum of one argument as it will automatically be passed a string containing the currently selected value from the `Combo` object.

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
