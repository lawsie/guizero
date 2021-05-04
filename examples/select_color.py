from guizero import App, PushButton, Text


def get_color():
    color_name.value = 'Color: ' + app.select_color('#000000')


app = App()

PushButton(app, command=get_color, text="Get color")
color_name = Text(app)
color_name.value = 'Color: #rrggbb'

app.display()
