from guizero import App, Window, PushButton

def go_fs():
    app.full_screen = True

def exit_fs():
    app.full_screen = False

app = App("Sup")
pb = PushButton(app, text="Go fullscreen", command=go_fs)
pb2 = PushButton(app, text="Exit fullscreen", command=exit_fs)

app.display()