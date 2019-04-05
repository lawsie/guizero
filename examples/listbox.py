from guizero import App, ListBox, Text

def change_color(value):
    t.text_color = value

def update_text():
    if mlistbox.value is None:
        t.value = "Its a ListBox"
    else:
        t.value = "Its a " + " ".join(mlistbox.value) + " ListBox"

a = App()

t = Text(a, text="Its a ListBox", color="black")

listbox = ListBox(
    a,
    items=["red", "green", "blue", "yellow", "purple", "turquoise", "pink", "orange", "black", "brown", "cyan"],
    selected="black",
    command=change_color,
    scrollbar=True,
    width="fill",
    height=150)

mlistbox = ListBox(
    a,
    items=["really", "slightly", "brilliant", "interesting", "but", "and", "rubbish", "stupid"],
    multiselect=True,
    command=update_text,
    width="fill",
    height="fill")

a.display()
