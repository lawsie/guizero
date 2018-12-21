from guizero import App, Box, Text, PushButton, Combo, Slider

def switch_screen(switch_to):
    hide_all()
    switch_to.show()

def hide_all():
    for screen in all_screens:
        screen.hide()


app = App("Multi box app", layout="grid")

# Create a blank list to hold all the different screens
all_screens = []

# Create a box to contain the menu buttons
menu = Box(app, grid=[0,0], layout="grid")
menu.tk.width = 900
menu.bg = "red"

# Option 1 box
option1 = Box(app, grid=[1,1])
text1 = Text(option1, text="This is the first page of stuff")
combo = Combo(option1, options=["Beef", "Chicken", "Fish", "Vegetarian"])
all_screens.append(option1)

# Option 2 box
option2 = Box(app, grid=[1,1])
text2 = Text(option2, text="This is the second page of stuff")
slider = Slider(option2)
all_screens.append(option2)

# Add the screens to the menu box
option1_button = PushButton(menu, text="Option 1", command=switch_screen, args=[option1], grid=[0,0], align="left")
option2_button = PushButton(menu, text="Option 2", command=switch_screen, args=[option2], grid=[1,0], align="left")

# Hide all screens and then show the first one
hide_all()
all_screens[0].show()

app.display()
