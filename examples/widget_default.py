from guizero import App, Text, TextBox, Slider, PushButton, Box

def change():
    a.bg = "red"
    tb.width = 20
    t.height = 5
    t.text_color = "blue"
    t.font = "courier new"
    t.text_size = 20
    s.width = 150
    p.width = 20
    pb.width = 100
    p.height = 2
    pb.height = 100
    b.bg = "white"

def reset():
    # by setting a widget property to None it restores its original value
    a.bg = None
    tb.width = None
    t.height = None
    t.text_color = None
    t.font = None
    t.text_size = None
    s.width = None
    p.width = None
    pb.width = None
    p.height = None
    pb.height = None
    b.bg = None

a = App()
tb = TextBox(a)
s = Slider(a)
p = PushButton(a)
pb = PushButton(a, image="guizero.gif")
t = Text(a, "Widget settings")
b = Box(a, layout="grid")
change_button = PushButton(b, text="change", command=change, grid=[0,0], align="left")
reset_button = PushButton(b, text="reset", command=reset, grid=[1,0], align="right")

a.display()
