from guizero import App, TextBox, Text
from tkinter import INSERT

def key_pressed(key):
    details.value = "key pressed = {}, cursor pos = {}".format(
        textbox.value, 
        textbox.cursor_position
        )

app = App()
text = Text(app, text="Enter some text")
textbox = TextBox(app, width=40, command=key_pressed)
details = Text(app)
app.display()