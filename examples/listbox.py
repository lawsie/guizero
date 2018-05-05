from guizero import App, PushButton, ListBox, Text
from tkinter import Listbox, END, MULTIPLE, EXTENDED

def changed(value):
    t.value = value

def show_list():
    t.value = listbox.value + " " + str(mlistbox.value)

a = App()

listbox = ListBox(a, items=["one", "two", "three", "four", "three", "five"], selected="one", command=changed)
mlistbox = ListBox(a, items=["six", "seven", "eight", "nine", "ten"], multiselect=True, selected=["ten", "nine"], command=changed)
b = PushButton(a, text="show values", command=show_list)
t = Text(a)

a.display()