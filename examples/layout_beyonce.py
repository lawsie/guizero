from guizero import App, PushButton, Text, Box

app = App()

top_box = Box(app, align="top", width="fill")
PushButton(top_box, text="to the left", align="left")
PushButton(top_box, text="to the left", align="left")

Text(app, text="everything you own", align="top")

left_box = Box(app, align="left")
left_box.border = True
Text(left_box, text="in a box to the left")

app.display()