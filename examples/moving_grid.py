from guizero import App, Text, PushButton
from random import randint

a = App("dynamically changing grid", layout="grid")
a.text_size = 40
t = []

def dance():
    for l in t:
        x = l.grid[0] - 1
        if x < 0:
            x = 4

        l.grid = (x, l.grid[1])

for x in range(5):
    for y in range(5):
        t.append(Text(a,
            text="{}.{}".format(x,y),
            grid=[x,y],
            color=(randint(100,255), randint(100,255), randint(100,255))))

a.repeat(250, dance)

a.display()
