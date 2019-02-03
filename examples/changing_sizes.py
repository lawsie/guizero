from guizero import App, TextBox, Text, Slider, PushButton, Picture, Combo, CheckBox, ButtonGroup, Box

app = App(title="different sizes", width = 700, height=700)

text = Text(app, "lets change some sizes", width=20, height=2)

text_box = TextBox(app, "some text", width=50)

slider = Slider(app, width=300, height=30)

button = PushButton(app, width=20, height=2)

pic = Picture(app, image="guizero.gif", width=400, height=50)

combo = Combo(app, ["martin", "laura", "rik"], width="fill", height="fill")

check = CheckBox(app, "tick me", width=20, height=3)
check.bg = "blue"

button_group = ButtonGroup(app, ["cheese", "onion", "crisps"], 1, width=20, height=9)
button_group.bg = "darkgrey"

box = Box(app, width=100, height=100)
box.border = True

box.bg = "red"

app.display()