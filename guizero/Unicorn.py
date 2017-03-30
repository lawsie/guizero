from tkinter import Canvas, BOTH, Frame

from . import utilities as utils
    
class Unicorn(Frame):

    def __init__(self, master, height=3, width=3, dim=20, pad=5, color="white", grid=None, align=None):    	

    	# Description of this object (for friendly error messages)
        self.description = "[Unicorn] object ("+str(height)+"x"+str(width)+")"

        self.height = height
        self.width = width
        self.dim = dim
        self.pad = pad
        self.color = color

        # Calculate how big this canvas will be
        self.c_height = self.width*(self.dim+self.pad)
        self.c_width = self.width*(self.dim+self.pad)

        # Attempt to create this object                
        try:
            super().__init__(master)
        except AttributeError:
            utils.error_format("Failed to initialise [Unicorn] object")

       
        # Create an internal canvas
        currx = self.pad
        curry = self.pad

        self.canvas = Canvas(self, height=self.c_height, width=self.c_width)

        # Draw the pixels on the canvas
        for y in range(self.height):
            for x in range(self.width):
                self.canvas.create_rectangle(currx, curry, currx+self.dim, curry+self.dim, fill=self.color)
                currx = currx + self.dim + self.pad
            curry = curry + self.dim + self.pad
            currx = self.pad


        # Pack the canvas into this Unicorn object
        self.canvas.pack(fill=BOTH, expand=1)


        # Pack this box into its layout 
        utils.auto_pack(self, master, grid, align)


    def set_all(self, color):

        self.color = str(color)
        
        currx = self.pad
        curry = self.pad
        
        # Draw the pixels on the canvas
        for y in range(self.height):
            for x in range(self.width):
                self.canvas.create_rectangle(currx, curry, currx+self.dim, curry+self.dim, fill=self.color, outline="")
                currx = currx + self.dim + self.pad
            curry = curry + self.dim + self.pad
            currx = self.pad


    def set_pixel(self, x, y, color):
        if x > self.width:
            utils.error_format("The x value "+ str(x) + " is off the grid")
        elif y > self.width:
            utils.error_format("The y value "+ str(y) + " is off the grid")
        else:
            locate_x = (self.dim + self.pad) * (int(x)-1) + self.pad
            locate_y = (self.dim + self.pad) * (int(y)-1) + self.pad
            self.canvas.create_rectangle(locate_x, locate_y, locate_x+self.dim, locate_y+self.dim, fill=color)
        
