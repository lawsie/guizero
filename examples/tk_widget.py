from guizero import App, Text
from tkinter import Spinbox
from tkinter.ttk import Progressbar

a = App(title="Using tk widgets")

Text(a, text="Spinbox")

sp = Spinbox(from_=0, to=10)
a.add_tk_widget(sp)

Text(a, text="and Progressbar")

pb = Progressbar()
a.add_tk_widget(pb)
pb.start()

text_2 = Text(a, text="in guizero")

a.display()