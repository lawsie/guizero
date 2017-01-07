# CheckBox

(Extends the `Checkbutton` class from `tkinter`)

### Purpose
Display a check box to allow an option to be ticked or unticked

```
class guizero.CheckBox(master, text, command=None, grid=None, align=None)
```

### Create a CheckBox object

Create a basic CheckBox object like this:

```python
app = App()
checkbox = CheckBox(app, "Add extra glitter")
app.display()

```
The above code looks like this on Windows:
![Checkbox on Windows](images/checkbox_windows.png)


When creating a CheckBox object, you can specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| text   | string    | -  | Yes         | The text to display next to the check box |
| command | function name | None | No   | The name of a function to call when this checkbox is ticked/unticked |
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | None     | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |



### Methods

You can call the following methods on your CheckBox object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| get_text()  | -  | string          | Returns the text associated with this CheckBox |
| get_value()   | -         | int         | Returns 1 if the CheckBox is ticked or 0 if it is not ticked          |
| toggle() | - | - |  Switches the CheckBox to the opposite of its current value. i.e. if it is ticked, untick it and vice versa |
| change_text(newtext) | newtext (string) | - |  Sets the text associated with this CheckBox to the string `newtext` |



### Examples

**Creating a CheckBox**

The simplest way to create a CheckBox object is as follows:

```python
app = App()
glitter = CheckBox(app, "Add glitter")
sparkles = CheckBox(app, "Add sparkles")
app.display()
```

**Calling a function when a CheckBox value changes**

You can call a function when the value of a CheckBox changes (becomes ticked or unticked). In this example, all three CheckBoxes call the same function, but each CheckBox object could call a different function.

```python
def calculate_extras():
    total = 0
    if syrup.get_value() == 1:
        total += 20
    if sprinkles.get_value() == 1:
        total += 10
    if cream.get_value() == 1:
        total += 50
    cost.set(total)


app = App()

questions = Text(app, "What would you like with your coffee?")

syrup = CheckBox(app, "Caramel syrup (20p)", command=calculate_extras)
sprinkles = CheckBox(app, "Chocolate sprinkles (10p)", command=calculate_extras)
cream = CheckBox(app, "Whipped cream (50p)", command=calculate_extras)

cost_of_extras = Text(app, "Cost of extras:")
cost = TextBox(app, "0")

app.display()
```
![CheckBox calling a function](images/checkbox_function_windows.png)
