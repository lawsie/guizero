## Multiple Windows

A guizero application should only have have one single [App](app.md) object - this is the main window and controller of your program.

If you want to create a second (or 3rd, 4th, 5th) window, your program should use a [Window](window.md) object.

### A Second window

When you create a second `Window` you need to pass it the `App`, just like when you create a widget:

```python
from guizero import App, Window

app = App(title="Main window")
window = Window(app, title="Second window")

app.display()

```

Adding widgets to the second window is the same as adding them to an `App`. You tell the widget which window it will be in by passing it the name of the `Window`:

```python
from guizero import App, Window, Text

app = App(title="Main window")
window = Window(app, title="Second window")
text = Text(window, text="This text will show up in the second window")

app.display()

```

### Opening and closing windows

When a `Window` object is created it is immediately displayed on the screen. You can control whether a window is visible or not using the `show()` and `hide()` methods.

This code creates a window which is shown when a button on the `App` is clicked and closed when a button is clicked in the `Window`.

```python
from guizero import App, Window, PushButton

def open_window():
    window.show()

def close_window():
    window.hide()

app = App(title="Main window")

window = Window(app, title="Second window")
window.hide()

open_button = PushButton(app, text="Open", command=open_window)
close_button = PushButton(window, text="Close", command=close_window)

app.display()
```

### Modal windows

When a window is opened using `show()` it opens side by side with the main window, and both windows can be used at the same time.

A "modal" window prevents the other windows in the application being used until it is closed. To create a modal window, you can pass `True` to the optional `wait` parameter of `show`.

This will force all other windows to wait until this window is closed before they can be used.

```python
def open_window():
    window.show(wait=True)
```
