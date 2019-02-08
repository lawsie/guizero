from guizero import App, Text, TextBox, Slider, PushButton, Combo, Box
from random import randint, choice

colors_text = ["red", "purple", "black", "blue", "green"]
colors_bg = ["pink", "yellow", "orange", "white", "cyan"]
fonts = ["garamond", "arial", "helvetica", "courier new", "times new roman", "comic sans"]

def randomise():
    app.bg = choice(colors_bg)
    for widget in app.children:
        widget.bg = choice(colors_bg)
        widget.text_color = choice(colors_text)
        widget.text_size = randint(8,20)
        widget.font = choice(fonts)

def reset():
    app.bg = None
    app.text_color = None
    app.text_size = None
    app.font = None

app = App(width=300, height=200)

title = Text(app, "Customise your app")
text = TextBox(app, text="then reset to default", width=20)
combo = Combo(app, ["by setting to None"])
code = Text(app, text="widget.bg = None", font="courier new")
box = Box(app, layout="grid")
but_random = PushButton(box, text="random", command=randomise, grid=[0,0])
but_reset = PushButton(box, text="reset", command=reset, grid=[1,0])

app.display()