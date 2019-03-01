from tkinter import Canvas, BOTH, ALL, PhotoImage
from . import utilities as utils
from .base import Widget
from .event import EventManager

class Drawing(Widget):

    def __init__(self, master, height=100, width=100, grid=None, align=None, command=None, visible=True, enabled=None, bg=None):

        # list to hold references to images, otherwise tk destroys them
        self._images = []

        description = "[Drawing] object"

        tk = Canvas(master.tk, height=100, width=100, bd=0, highlightthickness=0)

        super(Drawing, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

    def line(self, x1, y1, x2, y2, color="black", width=1):
        self.tk.create_line(
            x1, y1, x2, y2, 
            width = width,
            fill = "" if color is None else utils.convert_color(color)
            )

    def oval(self, x1, y1, x2, y2, color="black", outline=False, outline_color="black"):
        self.tk.create_oval(
            x1, y1, x2, y2, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def rectangle(self, x1, y1, x2, y2, color="black", outline=False, outline_color="black"):
        self.tk.create_rectangle(
            x1, y1, x2, y2, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def polygon(self, *coords, color="black", outline=False, outline_color="black"):
        self.tk.create_polygon(
            *coords, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def triangle(self, x1, y1, x2, y2, x3, y3, color="black", outline=False, outline_color="black"):
        self.polygon(x1, y1, x2, y2, x3, y3, color=color, outline=outline, outline_color=outline_color)

    def image(self, x, y, image, width=None, height=None):

        # load the image and add to the list (otherwise tk destroys the reference to them!)
        _image = utils.GUIZeroImage(image, width, height)
        self._images.append(_image)
        self.tk.create_image(x, y, image=_image.tk_image, anchor="nw")
        
    def circle_old(self, x, y, radius, width=1, color="black", fill_color=None):
        
        self.tk.create_oval(
            x - radius, y - radius, 
            x + radius, y + radius,
            outline = "" if color is None else color,
            width = 0 if width is None else width,
            fill = "" if fill_color is None else fill_color
            )
    
    def clear(self):
        self._images.clear()
        self.tk.delete(ALL)
