from guizero import App, ButtonGroup, CheckBox, Combo, PushButton, Slider, Text, TextBox

a = App(title="colors")
text = Text(a, text="colors")
check = CheckBox(a, "check me")
combo = Combo(a, ["red", "blue"])
button = PushButton(a)
slider = Slider(a)
textbox = TextBox(a, text="or colours")

a.bg = "pink"
text.text_size = 30
text.font = "verdana"
check.bg = "red"
combo.bg = "blue"
combo.text_color = "green"
combo.text_size = 24
button.bg = "black"
button.text_color = "white"
button.font = "arial"
button.text_size = 18
slider.bg = "yellow"
textbox.bg = "cyan"
textbox.font = "courier"
textbox.text_color = "purple"

a.display()