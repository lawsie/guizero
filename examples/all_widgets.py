from guizero import *

# app = App(width=225, height=100)
app = App(width=225, height=130)

Box(app, width="fill", align="top", height=15)
Box(app, width="fill", align="bottom", height=15)

# box = Box(app, width=150, height=25)
# Text(box, text="Text in a Box")

# box = Box(app, border=True, width=150, height=25)
# Text(box, text="A Box with a border")

# choice = ButtonGroup(app, options=["cheese", "ham", "salad"])

# checkbox = CheckBox(app, text="salad ?")

# combo = Combo(app, options=["cheese", "ham", "salad"])

# drawing = Drawing(app, width=150, height=30)
# drawing.bg="green"
# drawing.rectangle(5, 5, 145, 25, color="blue")
# drawing.oval(7, 7, 23, 23, color="white")
# drawing.rectangle(25, 7, 39, 23, color="yellow")
# drawing.oval(120, 7, 142, 23, color="purple")
# drawing.text(50, 5, "Drawing", color="white")

# listbox = ListBox(app, items=["cheese", "ham", "salad"], height="fill")

# picture = Picture(app, image="guizero.png", height=100, width=200)

# def do_nothing():
#     print("button pressed")

# button = PushButton(app, command=do_nothing)

# slider = Slider(app)

# text = Text(app, text="Hello World")

# textbox = TextBox(app)

# waffle = Waffle(app)

window = Window(app, width=210, height=100)

app.display()   
