from guizero import *

# Functions you write that are called by widgets
def donothing():
	rockstar.value = name.value + " " + pokemon.value
	name_label.color = "pink"


# Initialise your app
# OPTIONAL manager auto/grid(str), title(str), height(int), width(int)
app = App("grid")

# Set up your menu structure. Only allows for one level menus, no cascading within menus
file_options = [ ["File1", donothing], ["file2", donothing] ]
edit_options = [ ["edit1", donothing], ["edit2", donothing] ]


# You can only give the Menubar as a master the main App object
menubar = MenuBar(app, ["File", "Edit"], [file_options, edit_options] )


# You can configure columns/rows in the app to have a min width
app.tk.columnconfigure(1, minsize=200, pad=5)
app.tk.rowconfigure(1, pad=20)


# Any inner component can have a grid [0,0] reference and an optional alignment (top, bottom, left, right)

# Create a piece of text
# master(obj), OPTIONAL text(str), size(int), colour(str), font(str)
name_label = Text(app, text="What is your name?", grid=[1,1], align="right")

# Create a text box
# OPTIONAL text(str), width(int)
name = TextBox(app, width=30, grid=[1,2])


pokemon_label = Text(app, "What's your favourite Pokemon?", grid=[2,1], align="right")

# Create a combo box
# master(obj), options (list), selected item(str)
pokemon = Combo(app, ["Zapdos", "Gyarados", "Weedle"], grid=[2,2], align="left")

# Create a button
# master(obj), text(str), command(function), OPTIONAL padx(int), pady(int)
button = PushButton(app, donothing, text="Button!", grid=[3,2], align="left")

rockstar = Text(app, grid=[4,2], align="left")



app.display()
