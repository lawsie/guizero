# PushButton

(Extends the `Button` class from `tkinter`)

### Purpose
Display a button with text or an image, which calls a function when pressed

```
class guizero.PushButton(master, command, args=None, text="Button", icon=None, pady=10,
padx=10, grid=None, align=None)
```

### Create a PushButton object

Create a basic PushButton object like this:

```python
def do_nothing():
  print("Button was pressed")

app = App()
button = PushButton(app, do_nothing)
app.display()
```

The above code looks like this on Windows:
![PushButton on Windows](images/pushbutton_windows.png)


When creating a PushButton object, you can specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs |
| command | function name | None | Yes  | The name of a function to call when the button is pressed. |
| args    | List  | None | No       | If you wish to pass any arguments to the function specified in the command paramter, you can specify them as a list |
| text    | string   | "Button" | No       | The text to display on the button |
| icon    | string   | None | No       | The path to a GIF image file to display on the button. If both an image and text are specified, the image will override the text. |
| pady    | int   | 10 | No       | How much vertical padding to add between the text/icon and the edge of the button. |
| padx    | int   | 10 | No      | How much horizontal padding to add between the text/icon and the edge of the button. |
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | None     | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |



### Methods

You can call the following methods on your PushButton object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| change_command(newcommand, args)  | newcommand (function name), args (List)  | -          | Sets the function called when the button is pressed to the one specified as `newcommand`. You can optionally specify new `args` as a list. |
| set_text(text)   | text (string)         | -         | Sets the text on the button to the string specified in `text`.  |
| padding(padx, pady) | padx (int), pady(int) | - |  Sets the amount of x (horizontal) and y (vertical) padding between the text/icon and the edge of the button |
| disable | - | - |  Makes the button greyed out so you can't click on it |
| enable | - | - |  Makes the button clickable (opposite of disable) |
| toggle_state | - | - |  Changes the state of the button to the opposite of its current state - if it is currently enabled, disable it and vice versa |


### Examples

**Creating a PushButton**

The simplest way to create a PushButton object is as follows:

```python
def do_nothing():
  print("Button was pressed")

app = App()
button = PushButton(app, do_nothing)
app.display()

```
