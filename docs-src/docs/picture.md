# Picture

(Contains a `tkinter.Label` object)

```python
__init__(
    self, 
    master, 
    image=None, 
    grid=None, 
    align=None, 
    visible=True, 
    enabled=None, 
    width=None, 
    height=None)
```

### What is it?
The `Picture` object displays an image.

![Picture on Windows](images/picture_windows.png)

### How do I make one?

Create a `Picture` object like this:

```python
from guizero import App, Picture
app = App()
picture = Picture(app, image="test.gif")
app.display()
```
You must specify the correct path to the image. The image in the example is in the same directory as the program. If the image is in a different directory, specify a relative path, for example if the picture is in a subfolder called **images** you would write:

```python
picture = Picture(app, image="images/test.gif")
```

### Image support

Depending on your operating system and whether you installed the guizero [additional image features](index.md#additional-features-install) will determine what [image types you can use](images.md) with `Picture`.

By default GIF and PNG are supported, except macOS which only supports GIF.

### Starting parameters

When you create a `Picture` object you **must** specify `master` and you can specify any of the optional parameters. Specify parameters in the brackets, like this: `picture = Picture(app, image="test.gif")`

| Parameter | Takes              | Default | Compulsory | Description                                                                                                     |
|-----------|--------------------|---------|------------|-----------------------------------------------------------------------------------------------------------------|
| master    | App, Window or Box | -       | Yes        | The container to which this widget belongs                                                                      |
| image     | string             | None    | -          | The file path, tkinter.PhotoImage or PIL.Image you wish to display                                              |
| align     | string             | None    | -          | Alignment of this widget within its container. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`.       |
| grid      | List [int, int]    | None    | -          | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout.   |
| visible   | boolean            | True    | No         | If the widget should be visible.                                                                                |
| enabled   | boolean            | None    | No         | If the widget should be enabled. If `None` (the default) the enabled property will be inherited from the master |
| width     | [size](size.md)    | None    | No         | Set the width of the widget in pixels                                                                           |
| height    | [size](size.md)    | None    | No         | Set the height of the widget in pixels                                                                          |



### Methods

You can call the following methods on a `Picture` object.

| Method                           | Takes                                                         | Returns | Description                                                                                                                                                    |
|----------------------------------|---------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| after(time, command, args=None)  | time (int), command (function name), args (list of arguments) | -       | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| cancel(command)                  | command (function name)                                       | -       | Cancels a scheduled call to `command`                                                                                                                          |
| destroy()                        | -                                                             | -       | Destroys the widget                                                                                                                                            |
| disable()                        | -                                                             | -       | Disables the widget so that it is "greyed out" and cannot be interacted with                                                                                   |
| enable()                         | -                                                             | -       | Enables the widget                                                                                                                                             |
| focus()                          | -                                                             | -       | Gives focus to the widget (e.g. focusing a `TextBox` so that the user can type inside it)                                                                      |
| hide()                           | -                                                             | -       | Hides the widget from view. This method will unpack the widget from the layout manager.                                                                        |
| repeat(time, command, args=None) | time (int), command (function name), args (list of arguments) | -       | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| resize(width, height)            | width (int), height (int)                                     | -       | Sets the width and height of the widget                                                                                                                        |
| show()                           | -                                                             | -       | Displays the widget if it was previously hidden                                                                                                                |

### Properties

You can set and get the following properties:

| Method  | Data type          | Description                                                                                           |
|---------|--------------------|-------------------------------------------------------------------------------------------------------|
| align   | string             | The alignment of this widget within its container                                                     |
| bg      | [color](colors.md) | The background colour of the widget                                                                   |
| enabled | boolean            | `True` if the widget is enabled                                                                       |
| grid    | List               | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid |
| height  | [size](size.md)    | Set the height of the widget in pixels                                                                |
| image   | string             | The file path, tkinter.PhotoImage or PIL.Image you wish to display                                    |
| master  | App or Box         | The container to which this widget belongs                                                            |
| value   | string             | The file path, tkinter.PhotoImage or PIL.Image you wish to display                                    |
| visible | boolean            | If this widget is visible                                                                             |
| width   | [size](size.md)    | Set the width of the widget in pixels                                                                 |

Refer to a property as `<name of widget>.property`. For example, if your `Picture` object is called `picture` you would write `picture.value`.

You can **set** the property (for example `picture.value = "star.gif"`) or **get** the value of the property to use (for example `print(picture.value)`).


