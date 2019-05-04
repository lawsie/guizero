from guizero import App, Text
a = App()

t1 = Text(a)
t1.value = "{}, {}, {}".format(t1.font, t1.text_size, t1.text_color)

t2 = Text(a, color=None, size=None, font=None)
t2.value = "{}, {}, {}".format(t2.font, t2.text_size, t2.text_color)

a.display()