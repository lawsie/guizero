from tkinter import Canvas, BOTH, Frame
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin, DisplayMixin, SizeMixin, ReprMixin
from . import utilities as utils

class Waffle(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    FocusMixin, 
    DisplayMixin, 
    ReprMixin):

    def __init__(self, master, height=3, width=3, dim=20, pad=5, color="white", dotty=False, grid=None, align=None, command=None, remember=True):

        self._master = master
        self._grid = grid
        self._align = align
        self._visible = True

    	# Description of this object (for friendly error messages)
        self.description = "[Waffle] object ("+str(height)+"x"+str(width)+")"

        self._command = command
        self._height = height       # How many pixels high
        self._width = width         # How many pixels wide
        self._pixel_size = dim      # Size of one pixel
        self._pad = pad             # How much padding between pixels
        self._color = color        # Start color of the whole waffle
        self._dotty = dotty         # A dotty waffle will display circles
        self._save_canvas = []      # Where the Waffle objects will be stored

        # Calculate how big this canvas will be
        self._c_height = self._width*(self._pixel_size+self._pad)
        self._c_width = self._width*(self._pixel_size+self._pad)

        # Create a tk Frame object within this object which will be the waffle
        self.tk = Frame(master.tk)

        # Create an internal canvas to draw the waffle on
        self._canvas = Canvas(self.tk, height=self._c_height, width=self._c_width)

        # Draw the pixels on the canvas
        self._draw(self._color)

        # Pack the canvas into this Waffle object
        self._canvas.pack(fill=BOTH, expand=1)

        # Bind the left mouse click to the canvas so we can click on the waffle
        self._canvas.bind("<Button-1>", self._clicked_on)

        # Pack this box into its layout
        utils.auto_pack(self, master, grid, align)

    # METHODS
    # -------------------------------------------

    # Internal use only
    def _draw(self, color):
        # Draw the pixels on the canvas
        currx = self._pad
        curry = self._pad

        for y in range(self._height):
            row = []
            for x in range(self._width):
                if self._dotty == False:
                    obj = self._canvas.create_rectangle(currx, curry, currx+self._pixel_size, curry+self._pixel_size, fill=color)
                else:
                    obj = self._canvas.create_oval(currx, curry, currx+self._pixel_size, curry+self._pixel_size, fill=color)
                currx = currx + self._pixel_size + self._pad
                row.append(obj)
            curry = curry + self._pixel_size + self._pad
            currx = self._pad
            self._save_canvas.append(row)

    # Sets the colour of the whole waffle
    def set_all(self, color):
        self.color = str(color)
        # Draw the pixels on the canvas
        for y in range(self._height):
            for x in range(self._width):
                obj = self._save_canvas[y][x]
                self._canvas.itemconfig(obj,fill=color)

    # Sets a single pixel
    def set_pixel(self, x, y, color):
        if x >= self._width:
            utils.error_format("The x value "+ str(x) + " is off the edge of the waffle")
        elif y >= self._width:
            utils.error_format("The y value "+ str(y) + " is off the edge of the waffle")
        else:
            obj = self._save_canvas[y][x]
            self._canvas.itemconfig(obj,fill=color)

    # Returns the colour value of a pixel if set
    def get_pixel(self, x, y):
        obj = self._save_canvas[y][x]
        return self._canvas.itemcget(obj,'fill')

    # Returns a 2D list of all colours in the waffle
    def get_all(self):
        all_pixels = []
        for y in range(self._height):
            row = []
            for x in range(self._width):
                obj = self._save_canvas[y][x]
                row.append(self._canvas.itemcget(obj,'fill'))
            all_pixels.append(row)
        return all_pixels

    # Internal use only
    # Detect x,y coords of where the user clicked
    def _clicked_on(self,e):
        canvas = e.widget
        x = canvas.canvasx(e.x)
        y = canvas.canvasy(e.y)
        pixel_x = int(x/(self._pixel_size+self._pad))
        pixel_y = int(y/(self._pixel_size+self._pad))
        if self._command:
            self._command(pixel_x,pixel_y)

    # PROPERTIES
    # ----------------------------------
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def pixel_size(self):
        return self._pixel_size

    @pixel_size.setter
    def pixel_size(self, value):
        self._pixel_size = value

    @property
    def pad(self):
        return self._pad

    @pad.setter
    def pad(self, value):
        self._pad = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def dotty(self):
        return self._dotty

    @dotty.setter
    def dotty(self, value):
        self._dotty = value
