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
name = TextBox(app, text="Enter your name")

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

## Toggle 2 buttons

Have 2 buttons, **start** and **stop** with them changing the `enabled` state of each other.

```python
from guizero import App, PushButton

def start():
    start_button.disable()
    stop_button.enable()

def stop():
    start_button.enable()
    stop_button.disable()

app = App()
start_button = PushButton(app, command=start, text="start")
stop_button = PushButton(app, command=stop, text="stop", enabled=False)
app.display()
``` 

## Change your apps appearance

Your app doesn't have to use the standard colors and text, let your user pick the background and text color from 2 combo's.

```python
from guizero import App, Combo, Text

def update_bg():
    app.bg = bg_combo.value

def update_text():
    app.text_color = text_combo.value

colors = ["black", "white", "red", "green", "blue"]

app = App()
app.bg = "black"
app.text_color = "white"

title1 = Text(app, text="Background color")
bg_combo = Combo(app, options=colors, selected=app.bg, command=update_bg)

title2 = Text(app, text="Text color")
text_combo = Combo(app, options=colors, selected=app.text_color, command=update_text)

app.display()
```

## Scale an image

Display an image on the screen with 2 sliders, 1 for height and 1 for width.

```python
from guizero import App, Slider, Picture

def resize():
    picture.width = width.value
    picture.height = height.value
    
app = App(layout="grid")

picture = Picture(app, image="image.gif", grid=[0,1])

width = Slider(app, command=resize, grid=[0,0], start=1, end=picture.width)
width.width = picture.width
width.value = picture.width

height = Slider(app, command=resize, horizontal=False, grid=[1,1], start=1, end=picture.height)
height.height = picture.height
height.value = picture.height

app.display()
```
