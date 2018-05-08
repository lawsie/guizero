from guizero import App, PushButton, ListBox, Text
from tkinter import Listbox, END, MULTIPLE, EXTENDED

def changed(value):
    t.value = value

def show_list():
    t.value = listbox.value + " " + str(mlistbox.value)

def key_pressed(data):
    print(data)

a = App()

listbox = ListBox(
    a, 
    items=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"], 
    selected="one", 
    command=changed,
    scrollbar=True)

mlistbox = ListBox(
    a, 
    items=["ah", "bee", "see", "dee", "ei"], 
    multiselect=True, 
    selected=["see", "ei"], 
    command=changed)

b = PushButton(a, text="show values", command=show_list)
t = Text(a)

a.display()