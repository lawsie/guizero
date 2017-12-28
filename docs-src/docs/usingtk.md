## Using tkinter methods

If you are an advanced user, you can still make use of any tkinter method which is not implemented in guizero.

Each guizero widget itself contains a tk widget - you can find out which by looking on the guizero documentation page for the widget. For example, a guizero `TextBox` contains a tkinter `Entry` object. You can always access the internal object using the syntax `<object_name>.tk`.

### Using a tkinter method on a guizero object

In this example, we have guizero `App` and `TextBox` widgets.

```python
from guizero import App, TextBox
app = App()
name = TextBox(app)
app.display()
```

You want to make the text in the box appear red, but you discover that at the moment this isn't possible in guizero. So instead, you access the internal tk widget directly using `<object_name>.tk` and then you call the tkinter method:

```python
from guizero import App, TextBox
app = App()
name = TextBox(app, text="Laura")
name.tk.config(foreground="red")    # config() is a tkinter method
app.display()
```

You can combine the use of `guizero` and `tkinter` seamlessly in a program, taking advantage of the simplified syntax of guizero whilst still being able to access the full range of functionality in tkinter if you need it.
