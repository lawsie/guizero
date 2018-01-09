from guizero import App, Waffle
#from tkinter import Canvas, BOTH

def change_pixel(x,y):
    if big_waffle.get_pixel(x,y) == 'white':
        big_waffle.set_pixel(x, y, "red")
    else:
        big_waffle.set_pixel(x, y, "white")

app = App("Waffle!", height=50*20, width=50*20)


# Create a waffle 80x80 with circular pixels 10x10 and 2px padding between them
big_waffle = Waffle(app, height=80, width=80, dim=10, pad=2, dotty=True, remember=True,command=change_pixel)


app.display()
