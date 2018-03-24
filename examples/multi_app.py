from guizero import *

# it is possible to create multiple apps
# guizero will present a warning as you should use Window()
# to create multi window applications

def check(window):
    print("app {} clicked".format(window))
    print("1 - txt={} ".format(tb1.value))
    print("2 - txt={} ".format(tb2.value))

app1 = App(title="App 1")
tb1 = TextBox(app1, grid=[0, 1])
pb1 = PushButton(app1, command=check, args = [1])

app2 = App(title="App 2")
tb2 = TextBox(app2, grid=[0, 1])
pb2 = PushButton(app2, command=check, args = [2])

app1.display()
