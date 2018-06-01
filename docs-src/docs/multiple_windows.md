## Multiple Windows

A guizero application should only have have 1 [App](app.md) object, this is the main window and controller of your program.

If you want to create a 2nd (or 3rd, 4th, 5th) window, your program should use a [Window](window.md) object.

### A 2nd Window

Creating a 2nd Window is easy and just like creating a widget you need to pass it the App:

```python
from guizero import App, Window

app = App(title="Main window")
window = Window(app, title="2nd window")

app.display()

```

Adding widgets to the 2nd window is the same as adding them to an app, by passing the name of the window:

```python
from guizero import App, Window, Text

app = App(title="Main window")
window = Window(app, title="2nd window")
text = Text(window, text="text")

app.display()

```

### Opening and closing windows

When a `Window` object is created it is immediately displayed on the screen, you can control it using the `show()` and `hide()` methods.

To make a window which is shown when a button on the `App` is clicked and closed when a button is clicked on the `Window`.

```python
from guizero import App, Window

def open_window():
    window.show()

def close_window():
    window.hide()

app = App(title="Main window")

window = Window(app, title="2nd window")
window.hide()

open_button = PushButton(app, text="Open", command=open_window)
close_button = PushButton(window, text="Close", command=close_window)

app.display()
```

### Modal windows

When a window is opened using `show()` it is opening side by side with the main window, and both windows can be used at the same time

To open a "modal" window which prevents the other windows in the applcation being used until it is closed you can pass `True` to the optional `wait` parameter of `show` e.g. `window.show(wait=True)`.

This will force all other windows to wait until this window is closed before they can be used.

```python
def open_window():
    window.show(wait=True)
```
