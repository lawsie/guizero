from guizero import App, Text
from tkinter import Label, Entry, Spinbox
from tkinter.ttk import Progressbar

a = App()
a.bg = "light blue"

text_1 = Text(a, text="text 1")

label = Label(a.tk, text="label")
a.add_tk_widget(label)

entry = Entry(a.tk)
guizero_entry = a.add_tk_widget(entry, height=10, width=60, enabled=False, visible=False)
a.after(1000, guizero_entry.show)

sp = Spinbox(from_=0, to=10)
a.add_tk_widget(sp)

pb = Progressbar()
a.add_tk_widget(pb)
pb.start()

text_2 = Text(a, text="text 2")

a.display()