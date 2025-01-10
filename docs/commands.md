## Commands

Widgets in guizero can be given a `command` when created, which can be used to call a function when the widget is used.

By using commands you can make your GUI change and take actions when the user interacts with it, for example by clicking a button, selecting an option or typing a message.

### Example

This code will display `hello world` when the button is pressed:

```python
from guizero import App, Text, PushButton

def say_hello():
    text.value = "hello world"

app = App()
text = Text(app)
button = PushButton(app, command=say_hello)
app.display()
```

Arguments can be passed to the command function using the `args` parameter.

```python
from guizero import App, Text, PushButton

def say_goodbye(first_name, last_name):
    text.value = first_name + " " + last_name

app = App()
text = Text(app)
button = PushButton(app, command=say_goodbye, args=['John', 'Doe'])
app.display()
```
