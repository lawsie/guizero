from guizero import App, TextBox, PushButton, Text, info

def go():
    info("hi", "hi " + textbox.value)

app = App()
text = Text(app, text="Enter your name")
textbox = TextBox(app, width=40)
button = PushButton(app, text="Hi", command=go)
app.display()
