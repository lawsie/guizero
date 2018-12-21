from guizero import App, Box, Text

app = App()
box = Box(app, width=150, height=150)
text = Text(box, text="hello")
app.display()
