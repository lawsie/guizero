from guizero import App, Drawing, PushButton

a = App()

# create drawing object
d = Drawing(a, width="fill", height="fill")
d.bg = "light blue"

# drawing the shapes
d.rectangle(10, 10, 200, 200, width=10, fill_color="grey")
d.circle(50, 50, 15, fill_color="blue")
d.circle(150, 50, 15, fill_color="blue")
d.rectangle(20,160,190,170, color="red", fill_color="black")

a.display()
