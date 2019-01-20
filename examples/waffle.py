from guizero import App, Waffle, PushButton

def clicked(x,y):
    waffle.set_pixel(x,y,"red")
    print("{}.{}".format(x,y))
    print(waffle.get_all())
    waffle.width = 5
    waffle.height = 5
    waffle.pixel_size = 50
    waffle.dotty = True
    waffle.pad = 25
    waffle.color = "green"

app = App()
waffle = Waffle(app, command = clicked, height = 15, width = 15)
waffle.bg=(255,255,0)
waffle.set_all("red")
waffle.set_pixel(0,0,"blue")
waffle.set_pixel(8,1,"#00ff00")
waffle.set_pixel(3,4,"blue")
waffle.pixel(1,2).dotty = True
print(waffle[8,1].color)

button = PushButton(app, command= waffle.reset)

app.display()
