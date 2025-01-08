## Using tkinter

If you are an advanced user, you can still make use of tkinter when using guizero.

You can combine the use of `guizero` and `tkinter` seamlessly in a program, taking advantage of the simplified syntax of guizero whilst still being able to access the full range of functionality in tkinter if you need it.

### Using tkinter widgets in guizero

You can add tk widgets into your guizero app using the `add_tk_widget` method of `App`, `Window` and `Box`.

In this example, we are adding the tkinter widget `Spinbox` into a guizero `App`:

```python
from guizero import App, Text
from tkinter import Spinbox

app = App()
text = Text(app, text="A Spinbox widget")

spinbox = Spinbox(from_=0, to=10)
app.add_tk_widget(spinbox)

app.display()
```

When adding a tk widget to a `Box` or a `Window` you will have to specify its `tk` property when creating the tk widget.

```python
box = Box(app)
spinbox = Spinbox(box.tk, from_=0, to=10)
box.add_tk_widget(spinbox)
```

### Using a tkinter method on a guizero object

Each guizero widget itself contains a tk widget - you can find out which by looking on the guizero documentation page for the widget. For example, a guizero `TextBox` contains a tkinter `Entry` object. You can access the internal object using the syntax `<object_name>.tk`.

In this example, we have guizero `App` and `TextBox` widgets and are using the tk widgets `config` method to change the mouse cursor when it is over the `TextBox`.

```python
from guizero import App, TextBox
app = App()
name = TextBox(app, text="Laura")
name.tk.config(cursor="target") 
app.display()
```
