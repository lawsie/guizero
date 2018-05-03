from guizero import App, PushButton, ListBox
from tkinter import Listbox, END, MULTIPLE, EXTENDED


def show_list():
    #listbox.selection_clear(0, listbox.size()-1)
    #print(listbox.curselection())
    #selected = listbox.curselection()[0]

    #print(selected)
    #print(listbox.get(selected))
    print(listbox.value)
    print(mlistbox.value)
    listbox.value = None
    mlistbox.value = ["six", "seven"]
    #gzlistbox.value = (0,1)

a = App()

# listbox = Listbox(a.tk, selectmode=EXTENDED)
# listbox.pack()

# listbox.insert(END, "one")
# listbox.insert(END, "two")
# listbox.insert(END, "three")
# listbox.insert(END, "four")
# listbox.insert(END, "five")

# listbox.insert(0, "hello")
#listbox.select_set("ahkj")
#listbox.select_set(2)

listbox = ListBox(a, items=["one", "two", "three", "four", "five"], selected="three")
mlistbox = ListBox(a, items=["six", "seven", "eight", "nine", "ten"], multiselect=True, selected=["ten", "six"])
print(mlistbox.items)

b = PushButton(a, command=show_list)
a.display()