from guizero import *

def check1():
    print("1 check box:",cb1.value)
    print("1 text box:", tb1.value)
    print("1 combo option:", combo1.value)

def check2():
    print("2 check box:",cb2.value)
    print("2 text box:", tb2.value)
    print("2 combo option:", combo2.value)

def check(window):
    print("window {} clicked".format(window))
    print("1 - chk={} txt={} cmb={}".format(
        cb1.value,
        tb1.value,
        combo1.value
        ))
    print("2 - chk={} txt={} cmb={}".format(
        cb2.value,
        tb2.value,
        combo2.value
        ))


window1 = App(title="Window 1")

cb1 = CheckBox(window1, text="X")
tb1 = TextBox(window1, grid=[0, 1])
combo1 = Combo(window1, options=["one", "two", "three"])
pb1 = PushButton(window1, text="Click Here", command=check, args = [1])


window2 = App(title="Window 2")

cb2 = CheckBox(window2, text="X")
tb2 = TextBox(window2, grid=[0, 1])
combo2 = Combo(window2, options=["one", "two", "three"], command=check)

pb2 = PushButton(window2, text="Click Here", command=check, args = [2])

window1.display()
