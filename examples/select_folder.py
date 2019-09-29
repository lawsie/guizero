from guizero import App, PushButton, Text

def get_folder():
    file_name.value = app.select_folder()

app = App()

PushButton(app, command=get_folder, text="Get folder")
file_name = Text(app)

app.display()