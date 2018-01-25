from guizero import App, TextBox, PushButton, Text, alerts
from tkinter.font import Font

def go():
    alerts.info("hi", "hi " + textbox.value)
    
app = App()
text = Text(app, text="Enter your name")
textbox = TextBox(app)
button = PushButton(app, text="Hi", command=go)
app.display()