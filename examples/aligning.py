from guizero import App, Box, Text, PushButton

a = App()

top_box = Box(a, width=500, height=100, align="top")
top_box.border = True

Text(top_box, text="left", align="left")
Text(top_box, text="right", align="right")
Text(top_box, text="top", align="top")
Text(top_box, text="bottom", align="bottom")

a_box = Box(a, width=500, height=100)
a_box.border = True

PushButton(a_box, text="side", align="left")
PushButton(a_box, text="by", align="left")
PushButton(a_box, text="side", align="left")

a_box_in_a_box = Box(a_box, align="right")
a_box_in_a_box.border = True
Text(a_box, text="a box on the right", align="right")
PushButton(a_box_in_a_box, text="on top", align="top")
PushButton(a_box_in_a_box, text="of each other", align="top")

full_button = PushButton(a, text="full button", width="fill", height="fill")

bottom_box = Box(a, width=500, height=100, align="bottom", layout="grid")
bottom_box.border = True

for x in range(16):
    for y in range(4):
        Text(bottom_box, text="{}.{}".format(x,y), grid=[x,y])

Text(a, text="numbers in a grid at the bottom", align="bottom")

a.display()