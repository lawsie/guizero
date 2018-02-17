from guizero import App, ButtonGroup, CheckBox, Combo, PushButton, Slider, Text, TextBox

a = App(title="colors")
text = Text(a, text="colors")
check = CheckBox(a, "check me")
combo = Combo(a, ["red", "blue"])
button = PushButton(a)
slider = Slider(a)
textbox = TextBox(a, text="or colours")
bgroup = ButtonGroup(a, ["cheese", "ham", "salad"], 1)

a.bg = (255,255,0)
text.text_color = "red"
text.text_size = 30
text.font = "verdana"
text.bg = "green"
check.bg = "#d41789"
combo.bg = "blue"
combo.text_color = "green"
combo.text_size = 24
button.bg = "black"
button.text_color = (255,0,255)
button.font = "arial"
button.text_size = 18
slider.bg = (123,234,12)
textbox.bg = "cyan"
textbox.font = "courier"
textbox.text_color = "#FF0000"
bgroup.bg = "yellow"
bgroup.text_color = "#e62112"
bgroup.font = "book antiqua"
a.display()