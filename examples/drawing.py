from guizero import App, Drawing

a = App(width = 370, height=700)

# create drawing object
d = Drawing(a, width="fill", height="fill")
d.bg = "light blue"

# draw the shapes
d.rectangle(10, 10, 60, 60)
d.rectangle(70, 10, 120, 60, color="yellow")
d.rectangle(130, 10, 180, 60, color="yellow", outline=True)
d.rectangle(190, 10, 240, 60, color="yellow", outline=5)
d.rectangle(250, 10, 300, 60, color="yellow", outline=5, outline_color="green")
d.rectangle(310, 10, 360, 60, color=None, outline=5, outline_color="red")

d.oval(10, 100, 60, 150)
d.oval(70, 100, 120, 200, color="yellow")
d.oval(130, 100, 240, 150, color="yellow", outline=True)
d.oval(130, 160, 240, 210, color="yellow", outline=5)
d.oval(250, 100, 300, 150, color="yellow", outline=5, outline_color="green")
d.oval(310, 100, 360, 150, color=None, outline=5, outline_color="red")

d.line(10, 250, 60, 250)
d.line(70, 250, 120, 250, color="yellow")
d.line(130, 250, 240, 250, width=5)
d.line(250, 250, 300, 250, width=5, color="green")
d.line(310, 250, 360, 250, width=5, color="red")

d.polygon(10, 300, 60, 300, 40, 350, 10, 350)
d.polygon(70, 300, 120, 300, 100, 350, 70, 350, color="yellow")
d.polygon(130, 300, 180, 300, 160, 350, 130, 350, color="yellow", outline=True)
d.polygon(190, 300, 240, 300, 220, 350, 190, 350, color="yellow", outline=5)
d.polygon(250, 300, 300, 300, 280, 350, 250, 350, color="yellow", outline=5, outline_color="green")
d.polygon(310, 300, 360, 300, 340, 350, 310, 350, color=None, outline=5, outline_color="green")

d.triangle(10, 400, 60, 400, 10, 450)
d.triangle(70, 400, 120, 400, 70, 450, color="yellow")
d.triangle(130, 400, 180, 400, 130, 450, color="yellow", outline=True)
d.triangle(190, 400, 240, 400, 190, 450, color="yellow", outline=5)
d.triangle(250, 400, 300, 400, 250, 450, color="yellow", outline=5, outline_color="green")
d.triangle(310, 400, 360, 400, 310, 450, color=None, outline=5, outline_color="green")

d.image(10, 500, "guizero.png", width=350, height=100)

d.text(10, 600, "guizero")
d.text(110, 600, "guizero", font="times new roman")
d.text(210, 600, "guizero", size=24)
d.text(10, 650, "this is a some text which goes over the width and is wrapped", font="arial", size=16, max_width=350)

a.display()
