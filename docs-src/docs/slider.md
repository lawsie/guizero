# Slider

(Extends the `Scale` class from `tkinter`)

### Purpose
Display a slider which can be used to specify a value within a range

```
class guizero.Slider(master, start=0, end=100, orient=HORIZONTAL, command=None, grid=None, align=None)
```

### Create a Slider object

Create a basic Slider object like this:

```python
app = App()
slider = Slider(app)
app.display()
```

The above code looks like this on Windows:
![Combo on Windows](images/slider_windows.png)


When creating a Slider object, you can specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| start   | int    | 0  | No         | The smallest value selectable on the slider |
| end | int | 100 | No   | The largest value selectable on the slider |
| orient | HORIZONTAL or VERTICAL | HORIZONTAL | No   | Whether you wish to display your slider horizontally or vertically |
| command | function name | None | No   | The name of a function to call when the slider value is changed |
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | None     | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |



### Methods

You can call the following methods on your Slider object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| add_command(command)  | command (function name)  | -          | Sets the function called when the slider value is changed to the function specified in `command` |




### Examples

**Creating a Slider**

The simplest way to create a Slider object is as follows:

```python
app = App()
slider = Slider(app)
app.display()
```

**Calling a function when the slider value changes**

You can specify a function to call when the slider value changes. Your function **MUST** have a minimum of one parameter as it will automatically receive a string containing the value of the slider (called `slider_value` in the example) when it is called.

This code has a slider and a text box, and the text box updates automatically to display the current value of the slider.

![Text box and slider](images/textbox_slider_windows.png)

```python
def slider_changed(slider_value):
    textbox.set(slider_value)

app = App()
slider = Slider(app, command=slider_changed)
textbox = TextBox(app)
app.display()
```
