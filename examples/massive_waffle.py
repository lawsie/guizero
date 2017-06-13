from guizero import App, Waffle
from tkinter import Canvas, BOTH
import random

# Changes the colour of a randomly chosen pixel to a random colour value
def change_color():
    x = random.randint(1, big_waffle.width-1)
    y = random.randint(1, big_waffle.height-1)
    try:
        rgb = "#%02x%02x%02x" % ( random.randint(0,255), random.randint(0,255), random.randint(0, 255))
        big_waffle.set_pixel(x, y, rgb)
    except:
        print("Oops, something went wrong")

    # Wait 10ms and call this function again
    app.after(10, change_color)


app = App("Waffle!", height=50*20, width=50*20)

# Create a waffle 80x80 with circular pixels 10x10 and 2px padding between them
big_waffle = Waffle(app, height=80, width=80, dim=10, pad=2, dotty=True)

# Call the function once to start it off...
change_color()

app.display()
