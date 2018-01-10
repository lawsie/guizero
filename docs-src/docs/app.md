# App

(Contains a `tkinter.Tk` object)

`__init__(self, title="guizero", width=500, height=500, layout="auto", bgcolor=None, bg=None)`

### What is it?
The `App` object is the basis of all GUIs created using guizero. It is the main window which contains all of the other widgets.

![App](images/app.png)

### How do I make one?

Create an `App` object like this:

```python
from guizero import App
app = App()
app.display()
```

### Starting parameters

When you create an `App` object you can specify any of the following parameters, all of which are optional. Specify parameters in the brackets like this: `app = App(bg="red", height=200)`

| Parameter | Data type | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| bg    | string    | None  | No         | The background colour of the app window. Takes a RGB h ex colour (e.g. #0099ff) or a known colour string (e.g. "black"). |
| height    | int       | 500     | No         | The height of the window in pixels. |
| layout    | string    | "auto"  | No         | Whether widgets pack themselves (`"auto"`) or you specify their position on a grid (`"grid"`) |
| title     | string    | "guizero" | No       | The title displayed in the bar at the top of the window. |
| width     | int       | 500     | No         | The width of the window in pixels.  |
| _bgcolor_    | _string_    | _None_  | _No_         | _Replaced by `bg` parameter_ |

Parameters in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero

### Methods

You can call the following methods on an `App` object.

| Method        | Takes     | Returns    | Description                |
| ------------- | --------- | ---------- | -------------------------- |
| after(time, command)   | time (int), command (function name)   | -          | Schedules a **single** call to `command` after `time` milliseconds. (To repeatedly call the same command, use `repeat()`)  |
| cancel(command)   | command (function name) | -          | Cancels a scheduled call to `command`    |
| destroy()   | -  | -          | Destroys the widget    |
| display()     |-          | -          | Displays the app on the screen. You **MUST** call this method at the end of your program to display the app on the screen. |
| focus()  | -  | -          | Gives focus to the widget  |
| on_close(command)   | command (function name)         | -          | Calls the given function when the user tries to close the window.      |
| repeat(time, command)  | time (int), command (function name)  | -          | Repeats `command` every `time` milliseconds. This is useful for scheduling a function to be regularly called, for example updating a value read from a sensor.   |
| _set_title(title)_   | _title (string)_         | -          | _Replaced by `title` property_        |
| _bgcolor_   | _bgcolor (string)_       | -          | _Replaced by `bg` property_   |

Parameters in _italics_ will still work but are **deprecated** - this means you should stop using them because they may not work in future versions of guizero

### Properties

You can set and get the following properties:

| Method        | Data type   | Description                |
| ------------- | ----------- | -------------------------- |
| bg            | string      | The background colour of the window   |
| height        | int         | The height of the window   |
| layout        | string      | The layout being used by the App (`"auto"`) or (`"grid"`) |
| title         | string      | The title of the window    |
| width         | int         | The width of the window    |


Refer to a property as `<name of widget>.property`. For example, if your `App` object is called `app` you would write `app.title`.

You can **set** the property (for example `app.title = "Hello world"`) or **get** the value of the property to use (for example `print(app.title)`).

### Examples

**Creating an App object**

Create an `App` object by calling the `App()` constructor. You should give the object a name so you can refer to it later - in this case we have called it `app`. It is best to keep the name you give to your `App` object quite short, as you will have to use it to tell other widgets where they should be stored.

At the end of the program you **MUST** tell the app object to begin the display loop.

```python
from guizero import App
app = App(title="My app", height=300, width=200)
app.display()
```

**Changing the title**

You can change the title of the app object once it has been created like this:

```python
from guizero import App
app = App(title="My app", height=300, width=200)
app.title = "A different title"
app.display()
```
This will display the app with the updated title:

![App title](images/app_set_title.png)
