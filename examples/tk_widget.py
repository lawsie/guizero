from guizero import App, Box, Text
from tkinter import Spinbox
from tkinter.ttk import Progressbar

app = App(title="Using tk widgets")

Text(app, text="Spinbox")

# add a spinbox widget to the app
sp = Spinbox(from_=0, to=10)
app.add_tk_widget(sp)

Text(app, text="and Progressbar")

box = Box(app, border=True)

# add a progress bar to the boc
pb = Progressbar(box.tk)
box.add_tk_widget(pb)
pb.start()

Text(app, text="in guizero")

app.display()