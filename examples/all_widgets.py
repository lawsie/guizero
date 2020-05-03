from guizero import *

app = App()

box = Box(app, border=True, width=150, height=25)
Text(box, text="Box")

choice = ButtonGroup(app, options=["A", "button", "group"])

checkbox = CheckBox(app, text="Checkbox")

combo = Combo(app, options=["Combo", "o", "m", "b", "o"])

drawing = Drawing(app, width=150, height=30)
drawing.bg="green"
drawing.rectangle(5, 5, 145, 25, color="blue")
drawing.oval(7, 7, 23, 23, color="white")
drawing.rectangle(25, 7, 39, 23, color="yellow")
drawing.oval(120, 7, 142, 23, color="purple")
drawing.text(50, 5, "Drawing", color="white")

listbox = ListBox(app, items=["ListBox", "of", "items"])

picture = Picture(app, image="guizero.gif")




app.display()   
