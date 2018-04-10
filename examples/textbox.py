from guizero import App, TextBox, PushButton, Text, alerts
from tkinter.font import Font

def go():
    alerts.info("hi", "hi " + textbox.value)

def key_pressed(key):
    print("key pressed {}".format(key))    

app = App()
text = Text(app, text="Enter your name")
textbox = TextBox(app)
textbox.update_command(key_pressed)
button = PushButton(app, text="Hi", command=go)
app.display()