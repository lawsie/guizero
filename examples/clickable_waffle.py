from guizero import App, Waffle, PushButton

def change_pixel(x,y):
    if big_waffle.get_pixel(x,y) == 'white':
        big_waffle.set_pixel(x, y, "red")
    else:
        big_waffle.set_pixel(x, y, "white")

app = App("Waffle!", height=50*20, width=50*20)

big_waffle = Waffle(app, height=40, width=40, dim=10, pad=2, dotty=True, command=change_pixel)
enable_button = PushButton(app, big_waffle.enable, text="Enable")
disable_button = PushButton(app, big_waffle.disable, text="Disable")

app.display()
