from guizero import App, PushButton, Slider

def print_pos(x, y):
    print("{}, {}".format(x, y))

def print_bottom():
    print("bottom button")

def hide():
    b00.hide()
    b01.hide()
    b10.hide()
    b11.hide()
    b_bottom.hide()
    
def show():
    b00.show()
    b01.show()
    b10.show()
    b11.show()
    b_bottom.show()
    
app = App(layout="grid")

b00 = PushButton(app, print_pos, text="0,0", args=[0,0], grid=[0,0])
b01 = PushButton(app, print_pos, text="0,1", args=[0,1], grid=[0,1])
b10 = PushButton(app, print_pos, text="1,0", args=[1,0], grid=[1,0])
b11 = PushButton(app, print_pos, text="1,1", args=[1,1], grid=[1,1])

b_bottom = PushButton(app, print_bottom, text="span the bottom", grid=[0,2,2,1])

b_hide = PushButton(app, hide, text="hide", grid=[0,3])
b_show = PushButton(app, show, text="show", grid=[1,3])

app.display()