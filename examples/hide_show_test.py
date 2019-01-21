from guizero import App, Box, Text, PushButton

def hide1():
    t1.hide()

def show1():
    t1.show()

def hide2():
    t2.hide()

def show2():
    t2.show()

def destroy3():
    t3.destroy()

def hide(widget):
    widget.hide()

def show(widget):
    widget.show()

a = App()
b = Box(a, layout="grid")
b.border = True

t1 = Text(a, text="1")
t2 = Text(a, text="2")
t3 = Text(a, text="3")

ta = Text(b, text="aa", grid=[0,0], align="left")
tb = Text(b, text="bbb", grid=[1,0])
tc = Text(b, text="cccc", grid=[2,0])
tc = Text(b, text="ddddd", grid=[0,1])

pbb = Box(a, layout="grid")

b1h = PushButton(pbb, text="hide 1", grid=[0,1], command=hide, args=[t1])
b1s = PushButton(pbb, text="show 1", grid=[1,1], command=show, args=[t1])
b2h = PushButton(pbb, text="hide 2", grid=[2,1], command=hide, args=[t2])
b2s = PushButton(pbb, text="show 2", grid=[3,1], command=show, args=[t2])
bah = PushButton(pbb, text="hide a", grid=[0,0], command=hide, args=[ta])
bas = PushButton(pbb, text="show a", grid=[1,0], command=show, args=[ta])
bbh = PushButton(pbb, text="hide b", grid=[2,0], command=hide, args=[tb])
bbs = PushButton(pbb, text="show b", grid=[3,0], command=show, args=[tb])

a.display()
