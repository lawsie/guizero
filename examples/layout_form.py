from guizero import App, Text, TextBox, Combo, PushButton, Box

app = App()

Text(app, text="My form")

form = Box(app, width="fill", layout="grid")
form.border = True

Text(form, text="Title", grid=[0,0], align="right")
TextBox(form, grid=[1,0])

Text(form, text="Name", grid=[0,1], align="right")
TextBox(form, grid=[1,1])

Text(form, text="Age", grid=[0,2], align="right")
TextBox(form, grid=[1,2])

buttons = Box(app, width="fill", align="bottom")

PushButton(buttons, text="Ok", align="left")
PushButton(buttons, text="Cancel", align="left")

app.display()