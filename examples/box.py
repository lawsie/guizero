from guizero import App, Box, Text

app = App()
box = Box(app, width=150, height=150)
box.bg = "red"

text = Text(box, text="hello")
app.display()

