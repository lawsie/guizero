from guizero import App, Combo, Text

app = App("Font picker")

Text(app, "Pick a font")

def change_font():
    app.font = font_picker.value

font_picker = Combo(
    app, 
    options=app.fonts, 
    selected=app.font,
    command=change_font
    )

app.display()