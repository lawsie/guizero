from guizero import App, Text, PushButton

def update_size(e):
    app_size.value = "{}.{}".format(e.width, e.height)

def resize():
    app.resize(700,1000)

app = App()
app_size = Text(app)
app.when_resized = update_size

resize_button = PushButton(app, text="resize", command=resize)

app.display()