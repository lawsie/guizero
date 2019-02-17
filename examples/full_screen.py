from guizero import App, Text, PushButton

def go_fs():
    app.full_screen = True

def exit_fs():
    app.full_screen = False

app = App()
go_fullscreen = PushButton(app, text="Go full screen", command=go_fs)
exit_fullscreen = Text(app, "To exit full screen, press the escape key")


app.display()
