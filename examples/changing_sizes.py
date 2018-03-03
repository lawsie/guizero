from guizero import App, TextBox, Text, Slider, PushButton, Picture, Combo, CheckBox, ButtonGroup, Box

app = App(title="different sizes", width = 700, height=700)

text = Text(app, "lets change some sizes")
text.width = 30
text.height = 2

text_box = TextBox(app, "some text")
text_box.width = 50
text_box.height = 2

slider = Slider(app)
slider.width = 300
slider.height = 30  

button = PushButton(app)
button.width = 20
button.height= 2

pic = Picture(app, image="guizero.gif")
pic.width = 400
pic.height = 50

combo = Combo(app, ["martin", "laura", "rik"])
combo.width = 50
combo.height = 2

check = CheckBox(app, "tick me")
check.width = 17
check.height = 2

button_group = ButtonGroup(app, ["cheese", "onion", "crisps"], 1)
button_group.width = 35
button_group.height = 9
button_group.bg = "darkgrey"

box = Box(app)

#box_text = Text(box, "some text in a box")

box.width = 100
box.height = 100    

box.bg = "red"

app.display()