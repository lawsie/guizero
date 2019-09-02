from guizero import App, Text

a = App()
a.font = "courier new"

t1 = Text(a)
t1.value = "{}, {}, {}".format(t1.font, t1.text_size, t1.text_color)

t2 = Text(a, font="arial")
t2.value = "{}, {}, {}".format(t2.font, t2.text_size, t2.text_color)

t3 = Text(a, color="red", size=8, font="verdana")
t3.value = "{}, {}, {}".format(t3.font, t3.text_size, t3.text_color)
a.display()