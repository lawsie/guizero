from tkinter import Canvas, BOTH, Frame
from . import utilities as utils

class Waffle:

    def __init__(self, master, height=3, width=3, dim=20, pad=5, color="white", dotty=False, remember=True, grid=None, align=None, command=None):

    	# Description of this object (for friendly error messages)
        self.description = "[Waffle] object ("+str(height)+"x"+str(width)+")"

        self.command = command
        self.height = height       # How many pixels high
        self.width = width         # How many pixels wide
        self.pixel_size = dim      # Size of one pixel
        self.pad = pad             # How much padding between pixels
        self._color = color        # Start color of the whole waffle
        self.dotty = dotty         # A dotty waffle will display circles
        self.save_colors = []

        # Set up a pixel array to remember the pixel colours if remember was True
        self.save_colors = [[color for row in range(self.width)] for col in range(self.height)]

        # Calculate how big this canvas will be
        self.c_height = self.width*(self.pixel_size+self.pad)
        self.c_width = self.width*(self.pixel_size+self.pad)

        # Create a tk Frame object within this object which will be the waffle
        self.tk = Frame(master)

        # Create an internal canvas to draw the waffle on
        self.canvas = Canvas(self.tk, height=self.c_height, width=self.c_width)

        # Draw the pixels on the canvas
        self._draw(self._color)

        # Pack the canvas into this Waffle object
        self.canvas.pack(fill=BOTH, expand=1)

        # Bind the left mouse click to the canvas so we can click on the waffle
        self.canvas.bind("<Button-1>", self._clicked_on)

        # Pack this box into its layout
        utils.auto_pack(self, master, grid, align)

    # METHODS
    # -------------------------------------------

    # Internal use only
    def _draw(self, color):
        # Draw the pixels on the canvas
        currx = self.pad
        curry = self.pad

        for y in range(self.height):
            for x in range(self.width):
                if self.dotty == False:
                    self.canvas.create_rectangle(currx, curry, currx+self.pixel_size, curry+self.pixel_size, fill=color)
                else:
                    self.canvas.create_oval(currx, curry, currx+self.pixel_size, curry+self.pixel_size, fill=color)
                currx = currx + self.pixel_size + self.pad
            curry = curry + self.pixel_size + self.pad
            currx = self.pad

    # Sets the colour of the whole waffle
    def set_all(self, color):
        self._color = str(color)
        self._draw(self._color)
        self.save_colors = [[self._color for row in range(self.width)] for col in range(self.height)]

    # Sets a single pixel
    def set_pixel(self, x, y, color):
        if x >= self.width:
            utils.error_format("The x value "+ str(x) + " is off the edge of the waffle")
        elif y >= self.width:
            utils.error_format("The y value "+ str(y) + " is off the edge of the waffle")
        else:
            locate_x = (self.pixel_size + self.pad) * int(x) + self.pad
            locate_y = (self.pixel_size + self.pad) * int(y) + self.pad
            if self.dotty == False:
                self.canvas.create_rectangle(locate_x, locate_y, locate_x+self.pixel_size, locate_y+self.pixel_size, fill=color)
            else:
                self.canvas.create_oval(locate_x, locate_y, locate_x+self.pixel_size, locate_y+self.pixel_size, fill=color)

            # Update the saved colours
            self.save_colors[y][x] = color

    # Returns the colour value of a pixel if set
    def get_pixel(self, x, y):
        return self.save_colors[y][x]

    # Returns a 2D list of all colours in the waffle
    def get_all(self):
        return self.save_colors

    # Internal use only
    # Detect x,y coords of where the user clicked
    def _clicked_on(self,e):
        canvas = e.widget
        x = canvas.canvasx(e.x)
        y = canvas.canvasy(e.y)
        pixel_x = int(x/(self.pixel_size+self.pad))
        pixel_y = int(y/(self.pixel_size+self.pad))
        if self.command:
            self.command(pixel_x,pixel_y)
