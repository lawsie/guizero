from guizero import App, TextBox, PushButton, Text, info
from tkinter.font import Font

def go():
    info("hi", "hi " + textbox.value)

def key_pressed(key):
    print("key pressed {}".format(key))
    print("value = {}".format(textbox.value))

app = App()
text = Text(app, text="Enter your name")
textbox = TextBox(app, width=40)
textbox.update_command(key_pressed)
button = PushButton(app, text="Hi", command=go)
app.display()
