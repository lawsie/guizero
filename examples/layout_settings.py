from guizero import App, Box, ListBox, CheckBox, Combo, PushButton

app = App()

list_boxes = Box(app, width="fill")
ListBox(list_boxes, items=["Times New Roman", "Courier", "Verdana"], align="left", width="fill")
ListBox(list_boxes, items=["Regular", "Italic", "Bold", "Bold Italic"], align="left", width="fill")
ListBox(list_boxes, items=["8", "10", "12", "14", "16", "18"], align="left", width="fill")

combos = Box(app, width="fill")
combos.border = True
Combo(combos, options=["red", "green", "blue", "yellow"], align="left")
Combo(combos, options=["underline", "double underline"], align="right")

checks = Box(app, width="fill")
checks.border = True
CheckBox(checks, text="strike-through", align="left")
CheckBox(checks, text="double strike-through", align="left")
CheckBox(checks, text="sub-script", align="left")

buttons = Box(app, width="fill", align="bottom")
PushButton(buttons, text="Default", align="left")
PushButton(buttons, text="Ok", align="right")
PushButton(buttons, text="Cancel", align="right")

app.display()
