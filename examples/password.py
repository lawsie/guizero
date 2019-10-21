from guizero import App, Text, TextBox

app = App()
text = Text(app, text="Enter password")
password = TextBox(app, hide_text=True)
app.display()
