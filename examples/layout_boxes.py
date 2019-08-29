from guizero import App, Box, Text, TextBox
app = App()

def reallign():
    f.grid[1] = 1
    l.grid = [0,0]
    buttons_box.align="top"
    title_box.align="bottom"
    f.align = "left"

title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="title")

buttons_box = Box(app, width="fill", align="bottom", border=True)
Text(buttons_box, text="buttons")

options_box = Box(app, height="fill", align="right", border=True)
Text(options_box, text="options")

content_box = Box(app, align="top", width="fill", border=True)
Text(content_box, text="content")

form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
f = Text(form_box, grid=[0,0], text="form", align="right")
l = Text(form_box, grid=[0,1], text="label        x")
TextBox(form_box, grid=[1,1], text="data", width="fill")

app.after(1000, reallign)

app.display()