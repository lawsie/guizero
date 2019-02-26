from guizero import App, Drawing

a = App()

# create drawing object
d = Drawing(a, width="fill", height="fill")
d.bg = "light blue"

# drawing the shapes
d.rectangle(10, 10, 60, 60)
d.rectangle(70, 10, 120, 60, color="yellow")
d.rectangle(130, 10, 180, 60, color="yellow", outline=True)
d.rectangle(190, 10, 240, 60, color="yellow", outline=5)
d.rectangle(250, 10, 300, 60, color="yellow", outline=5, outline_color="green")
d.rectangle(310, 10, 360, 60, color=None, outline=5, outline_color="red")

#d.circle(50, 50, 15, fill_color="blue")
#d.circle(150, 50, 15, fill_color="blue")
#d.rectangle(20,160,190,170, color="red", fill_color="black")

a.display()
