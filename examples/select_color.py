from guizero import App, PushButton, Text


def get_color():
    color_selected = app.select_color("#000000")
    # color_selected = app.select_color()
    if color_selected is not None:
        color_name.value = "Color: " + color_selected
    else:
        color_name.value = ""


app = App()

PushButton(app, command=get_color, text="Get color")
color_name = Text(app)
color_name.value = "Color: #rrggbb"

app.display()
