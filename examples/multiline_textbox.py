from guizero import App, TextBox, PushButton, Text

def show():
    output.value = textbox.value

app = App()
textbox = TextBox(app, multiline=True, height=10, width=50, scrollbar=True)
textbox.value = "hello\ngoodbye\nno way\nthis is a very long stream of text, very long indeed, the best long line of text, its super bigly and very long, I dont think it could possibly be any better particularly as it was created by someone who is super good at creating long lines of text."
button = PushButton(app, text="Print", command=show)
output = Text(app)
app.display()