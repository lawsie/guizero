from guizero import App, PushButton, Text, CheckBox

def get_file():
    file_returned = app.select_file(filetypes=[["All files", "*.*"], ["Text documents", "*.txt"]], save=save.value)
    file_name.value = file_returned

app = App()

save = CheckBox(app, text="save")
PushButton(app, command=get_file, text="Get file")
file_name = Text(app)

app.display()