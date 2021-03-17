from guizero import App, Text

def update_size(e):
    app_size.value = "{}.{}".format(e.width, e.height)

app = App()
app_size = Text(app)
app.when_resized = update_size

app.display()