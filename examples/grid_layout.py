from guizero import App, PushButton

def print_pos(x, y):
    print("{}, {}".format(x, y))
    b00.show()

app = App(layout="grid")

b00 = PushButton(app, print_pos, text="0,0", args=[0,0], grid=[0,0])
b01 = PushButton(app, print_pos, text="0,1", args=[0,1], grid=[0,1])
b10 = PushButton(app, print_pos, text="1,0", args=[1,0], grid=[1,0])
b11 = PushButton(app, print_pos, text="1,1", args=[1,1], grid=[1,1])

b00.hide()


app.display()