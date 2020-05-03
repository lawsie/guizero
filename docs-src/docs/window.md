# Window

(Contains a `tkinter.TopLevel` object)

```python
__init__(
    self, 
    master, 
    title="guizero", 
    width=500, 
    height=500, 
    layout="auto", 
    bg=None, 
    visible=True)
```

### What is it?
The `Window` object create a new window in guizero.

![Window](images/window.png)

### How do I make one?

Create an `Window` object like this:

```python
from guizero import App, Window
app = App()
window = Window(app)
app.display()
```

### Starting parameters

When you create a `Window` object you **must** specify a `master` and you can specify any of the the optional parameters. Specify parameters in the brackets like this: `window = Window(app, bg="red", height=200)`

| Parameter | Data type          | Default   | Compulsory | Description                                                                                   |
|-----------|--------------------|-----------|------------|-----------------------------------------------------------------------------------------------|
| master    | App                | -         | Yes        | The app to which the window belongs                                                           |
| bg        | [color](colors.md) | None      | No         | The background colour of the window. Takes a [color](colors.md) value.                        |
| height    | int                | 500       | No         | The height of the window in pixels.                                                           |
| layout    | string             | "auto"    | No         | Whether widgets pack themselves (`"auto"`) or you specify their position on a grid (`"grid"`) |
| title     | string             | "guizero" | No         | The title displayed in the bar at the top of the window.                                      |
| width     | int                | 500       | No         | The width of the window in pixels.                                                            |
| visible   | boolean            | True      | No         | If the window should be visible.                                                              |

### Methods

You can call the following methods on a `Window` object.

| Method                                                                                               | Takes                                                                                               | Returns                                                                                           | Description                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| add_tk_widget(tk_widget, grid=None, align=None, visible=True, enabled=None, width=None, height=None) | tk_widget (tk), grid (list), align (str), visible (bool), enabled (bool), width (int), height (int) | Widget                                                                                            | Adds a tk widget into a guizero container. Note - this is an advanced feature see [Using tk](usingtk.md) for more information.                                 |
| after(time, command, args=None)                                                                      | time (int), command (function name), args (list of arguments)                                       | -                                                                                                 | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)                                      |
| cancel(command)                                                                                      | command (function name)                                                                             | -                                                                                                 | Cancels a scheduled call to `command`                                                                                                                          |
| disable()                                                                                            | -                                                                                                   | -                                                                                                 | Disables all the widgets in the window so that they cannot be interacted with                                                                                  |
| destroy()                                                                                            | -                                                                                                   | -                                                                                                 | Destroys the windows                                                                                                                                           |
| enable()                                                                                             | -                                                                                                   | -                                                                                                 | Enables all the widgets in the window                                                                                                                          |
| error(title, text)                                                                                   | title (str), text (str)                                                                             | -                                                                                                 | Displays a popup box with an error icon                                                                                                                        |
| exit_full_screen()                                                                                   | -                                                                                                   | -                                                                                                 | Exit full screen display                                                                                                                                       |
| focus()                                                                                              | -                                                                                                   | -                                                                                                 | Gives focus to the window                                                                                                                                      |
| hide()                                                                                               | -                                                                                                   | -                                                                                                 | Hides the window from view.                                                                                                                                    |
| info(title, text)                                                                                    | title (str), text (str)                                                                             | -                                                                                                 | Displays a popup box with an information icon                                                                                                                  |
| question(title, text, initial_value=None)                                                            | title (str), text (str), initial_value (str)                                                        | Pressing `Ok` returns value entered into the box is returned and pressing `Cancel` returns `None` | Displays a popup box with a question box which can accept a text response                                                                                      |
| repeat(time, command, args=None)                                                                     | time (int), command (function name), args (list of arguments)                                       | -                                                                                                 | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor. |
| select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False)           | title (str), folder (str), filetypes (list), save (bool)                                            | Full path of the file selected as a string                                                        | Display a box to select a file to open or save. If Open or Save is pressed the filename path is returned. If Cancel is pressed `None` is returned.             |
| select_folder(title="Select folder", folder=".")                                                     | title (str), folder (str)                                                                           | Full path of the folder selected as a string                                                      | Display a box to select a folder. If a folder is selected the folder path is returned, otherwise `None` is returned.                                           |
| set_full_screen(keybind)                                                                             | String                                                                                              | -                                                                                                 | Set the application to display full screen. Option to specify a key to exit full screen (default is 'Esc'.)                                                    |
| show(wait = False)                                                                                   | -                                                                                                   | -                                                                                                 | Displays the window if it was previously hidden                                                                                                                |
| update()                                                                                             | -                                                                                                   | -                                                                                                 | Force the window to update itself, useful if changes aren't reflected in the UI.                                                                               |
| warn(title, text)                                                                                    | title (str), text (str)                                                                             | -                                                                                                 | Displays a popup box with a warning icon                                                                                                                       |
| yesno(title, text)                                                                                   | title (str), text (str)                                                                             | Pressing `Yes` returns `True` and pressing `No` returns `False`                                   | Displays a popup box with yes and no options                                                                                                                   |
| _on_close(command)_                                                                                  | _command (function name)_                                                                           | -                                                                                                 | _Calls the given function when the user tries to close the window._                                                                                            |


### Properties

You can set and get the following properties:

| Method      | Data type          | Description                                                                                   |
|-------------|--------------------|-----------------------------------------------------------------------------------------------|
| bg          | [color](colors.md) | The background colour of the window                                                           |
| children    | list(widgets)      | A list of widgets in this container                                                           |
| enabled     | boolean            | `True` if the window is enabled                                                               |
| font        | string             | The font that widgets should use                                                              |
| full_screen | boolean            | False                                                                                         |
| height      | int                | The height of the window                                                                      |
| layout      | string             | The layout being used by the Window (`"auto"`) or (`"grid"`)                                  |
| title       | string             | The title of the window                                                                       |
| text_size   | int                | The size of the text widgets should use                                                       |
| text_color  | [color](colors.md) | The colour of the text widgets should use                                                     |
| visible     | boolean            | If the window is visible                                                                      |
| width       | int                | The width of the window                                                                       |
| when_closed | function           | The function to call when the `Window` is closed. Setting to `None` (the default) will reset. |


Refer to a property as `<name of widget>.property`. For example, if your `Window` object is called `window` you would write `window.title`.

You can **set** the property (for example `window.title = "Hello world"`) or **get** the value of the property to use (for example `print(window.title)`).

### Examples

**Creating a Window object**

Create an `Window` object by calling the `Window()` constructor. You should give the object a name so you can refer to it later - in this case we have called it `window`. It is best to keep the name you give to your `Window` object quite short, as you will have to use it to tell other widgets where they should be stored.


```python
from guizero import App, Window
app = App(title="My app", height=300, width=200)
window = Window(title = "2nd Window", height=300, width=200)
app.display()
```

**Showing and hiding a Window**

`Window` objects can be shown and hidden using the `show()` and `hide()` methods:

```python
from guizero import App, Window, PushButton

def open_window():
    window_2.show()

app = App(title="My app", height=300, width=200)
window = Window(app, title = "2nd Window", height=300, width=200)
window.hide()

open_button(app, text="open 2nd window", command=open_window)

app.display()
```

If you want a `Window` to become the main window and stop all other windows responding until it is closed you can set the optional `wait` parameter to `True` when using `show`:

```python
def open_window():
    window_2.show(wait = True)
```
