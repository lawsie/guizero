from guizero import App, Box, Combo, PushButton, Text

def set_box_borders(app, thickness, color):
   # go through app widgets
    for child in app.children:
        # is widget a box
        if isinstance(child, Box):
            child.set_border(thickness, color)

app = App()
b1 = Box(app, border=True)
t = Text(b1, "Change box borders")

b2 = Box(app, border=True)
color = Combo(b2, options=["red", "green", "blue", "black"], selected="black")
change_button = PushButton(b2, text="Change", command=lambda: set_box_borders(app, 2, color.value))

app.display()