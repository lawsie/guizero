## Commands 

Widgets in guizero can be given a `command` when created, which can be used to call a function when the widget is used.

By using commands you can make your GUI change and take actions when the user uses it e.g. clicking a button, selecting an option, typing a message. 

### Example

Create an application which puts `hello world` on the GUI when a button is pressed:

```python
from guizero import App, Text, PushButton

def say_hello():
    text.value = "hello world"

app = App()
text = Text(app)
button = PushButton(app, command=say_hello)
app.display()
```
