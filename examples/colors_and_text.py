from guizero import App, Box, ButtonGroup, CheckBox, Combo, PushButton, Slider, Text, TextBox

a = App(title="colors")
text = Text(a, text="colors")
check = CheckBox(a, "check me")
combo = Combo(a, ["red", "blue"])
button = PushButton(a)
slider = Slider(a)
b = Box(a)
textbox = TextBox(b, text="or colours")
bgroup = ButtonGroup(b, ["cheese", "ham", "salad"], 1)

#a.bg = (255,255,0)
text.text_color = "red"
text.text_size = 30
text.font = "verdana"
#text.bg = "green"
check.bg = "#d41789"
combo.bg = "blue"
combo.text_color = None
combo.text_size = 24
#button.bg = "black"
button.text_color = (255,0,255)
button.font = "arial"
button.text_size = 18
slider.bg = (123,234,12)
#textbox.bg = "cyan"
textbox.font = "courier"
textbox.text_color = "#FF0000"
b.bg = "cyan"
b.font = "wingdings"
#bgroup.bg = "yellow"
bgroup.text_color = "#e62112"
bgroup.text_color = None
bgroup.font = "book antiqua"

#a.bg = (255,0,25)
#a.font = "wingdings"
a.text_color = (255,253,12)
b.text_color = "purple"
b.text_size = 18

a.display()