from guizero import App, Text

a = App()
a.font = "courier new"

t1 = Text(a)
t1.value = "{}, {}, {}".format(t1.font, t1.text_size, t1.text_color)

t2 = Text(a, font="arial")
t2.value = "{}, {}, {}".format(t2.font, t2.text_size, t2.text_color)

t3 = Text(a, color="red", size=8, font="verdana", bold=True, italic=True)
t3.value = "{}, {}, {}, {}, {}".format(t3.font, t3.text_size, t3.text_color, t3.text_bold, t3.text_italic)

t4 = Text(a, underline=True)
t4.value = "{}, {}, {}".format(t4.font, t4.text_size, t4.text_underline)

t5 = Text(a, overstrike=True)
t5.value = "{}, {}, {}".format(t5.font, t5.text_size, t5.text_overstrike)
a.display()