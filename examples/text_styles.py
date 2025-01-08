from guizero import App, Text

app = App(title="Different text properties")

plain = Text(app, text="Plain")
bold = Text(app, text="Bold", bold=True)
italic = Text(app, text="Italic", italic=True)
underline = Text(app, text="Underline", underline=True)
overstrike = Text(app, text="Overstrike", overstrike=True)

app.display()
