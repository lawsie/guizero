from guizero import App, Box, Text, TextBox
app = App()

title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="title")

buttons_box = Box(app, width="fill", align="bottom", border=True)
Text(buttons_box, text="buttons")

options_box = Box(app, height="fill", align="right", border=True)
Text(options_box, text="options")

content_box = Box(app, align="top", width="fill", border=True)
Text(content_box, text="content")

form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
Text(form_box, grid=[0,0], text="form", align="right")
Text(form_box, grid=[0,1], text="label", align="left")
TextBox(form_box, grid=[1,1], text="data", width="fill")

app.display()