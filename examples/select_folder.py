from guizero import App, PushButton, Text

def get_folder():
    folder_returned = app.select_folder()
    folder_name.value = folder_returned

app = App()

PushButton(app, command=get_folder, text="Get folder")
folder_name = Text(app)

app.display()