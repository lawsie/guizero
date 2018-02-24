from guizero import App, CheckBox

def checked():
    print(check.value)

app = App()
check = CheckBox(app, "check this", command=checked)
check.update_command(None)
app.display()