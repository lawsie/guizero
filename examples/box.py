from guizero import App, Box, Text

app = App()
box = Box(app)
text = Text(box, text="hi")

app.display()

