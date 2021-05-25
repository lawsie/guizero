from guizero import App, TextBox, Text
from tkinter import INSERT

def key_pressed(key):
    print("key pressed {}".format(key))
    print("textbox value = {}".format(textbox.value))
    print("cursor pos = {}".format(textbox.tk.index(INSERT)))

app = App()
text = Text(app, text="Enter some text")
textbox = TextBox(app, width=40, command=key_pressed)
app.display()