from guizero import App, PushButton, Text, CheckBox

def get_file():
    file_name.value = app.select_file(filetypes=[["All files", "*.*"], ["Text documents", "*.txt"]], save=save.value)

app = App()

save = CheckBox(app, text="save")
PushButton(app, command=get_file, text="Get file")
file_name = Text(app)

app.display()