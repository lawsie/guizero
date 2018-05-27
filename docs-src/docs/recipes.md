# Recipes

These are examples of how you can use `guizero` to create user interfaces. Don't be restricted to these ideas, check out [Using guizero](start.md) and the [widgets](app.md).

## Hello World

Create a guizero app and display some text.

```python
from guizero import App, Text
app = App()
text = Text(app, text="hello world")
app.display()
```

## Get some text

Get some data from the user using a `TextBox`.

```python
from guizero import App, TextBox

app = App()
name = TextBox(app. text="Enter your name")

app.display()
```

## Push a button

Use a `PushButton` to display a message when the button is pressed. 

```python
from guizero import App, TextBox, PushButton, Text

def update_text():
    label.value = name.value

app = App()
label = Text(app, text="What's your name?")
name = TextBox(app)
button = PushButton(app, command=update_text)

app.display()
```

## Display an image

Use a `Picture` object to display an image.

```python
from guizero import App, Picture
app = App()
pic = Picture(app, image="myimage.gif")
app.display()
```

