from guizero import App, Text
from tkinter import Label, Entry

a = App()
text_1 = Text(a, text="text 1")

label = Label(a.tk, text="label")
a.add_tk_widget(entry)

entry = Entry(a.tk)
guizero_entry = a.add_tk_widget(entry, height=10, width=60, enabled=False, visible=False)

a.after(1000, guizero_entry.show)
a.add_tk_widget(label)
text_2 = Text(a, text="text 2")

a.display()