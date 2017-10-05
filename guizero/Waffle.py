from tkinter import Canvas, BOTH, Frame

from . import utilities as utils
    
class Waffle(Frame):

    def __init__(self, master, height=3, width=3, dim=20, pad=5, color="white", dotty=False, remember=False, grid=None, align=None, command=None):    	

    	# Description of this object (for friendly error messages)
        self.description = "[Waffle] object ("+str(height)+"x"+str(width)+")"

        self.command = command
        self.height = height
        self.width = width
        self.dim = dim
        self.pad = pad
        self.color = color
        self.dotty = dotty              # A dotty waffle will display circles not squares
        self.save_colors = []          # Defaults to not remembering pixel colours to save memory
        self.remember = remember

        # Set up a pixel array to remember the pixel colours if remember was True
        if self.remember:
            for row in range(self.width):
                new_row = []
                for col in range(self.height):
                    new_row.append(self.color)
                self.save_colors.append(new_row)


        # Calculate how big this canvas will be
        self.c_height = self.width*(self.dim+self.pad)
        self.c_width = self.width*(self.dim+self.pad)

        # Attempt to create this object                
        try:
            super().__init__(master)
        except AttributeError:
            utils.error_format("Failed to initialise [Waffle] object")

       
        # Create an internal canvas
        currx = self.pad
        curry = self.pad

        self.canvas = Canvas(self, height=self.c_height, width=self.c_width)

        # Draw the pixels on the canvas
        for y in range(self.height):
            for x in range(self.width):
                if self.dotty == False:
                    self.canvas.create_rectangle(currx, curry, currx+self.dim, curry+self.dim, fill=self.color)
                else:
                    self.canvas.create_oval(currx, curry, currx+self.dim, curry+self.dim, fill=self.color)
                currx = currx + self.dim + self.pad
            curry = curry + self.dim + self.pad
            currx = self.pad


        # Pack the canvas into this Waffle object
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.bind("<Button-1>", self.clicked_on)


        # Pack this box into its layout 
        utils.auto_pack(self, master, grid, align)

    # Sets the whole screen with dots
    def set_all(self, color):

        self.color = str(color)
        
        currx = self.pad
        curry = self.pad
        
        # Draw the pixels on the canvas
        for y in range(self.height):
            for x in range(self.width):
                if self.dotty == False:
                    self.canvas.create_rectangle(currx, curry, currx+self.dim, curry+self.dim, fill=self.color, outline="")
                else:
                    self.canvas.create_oval(currx, curry, currx+self.dim, curry+self.dim, fill=self.color, outline="")
                currx = currx + self.dim + self.pad
            curry = curry + self.dim + self.pad
            currx = self.pad

        # Save all to the memory if set to True
        if self.remember:
            for row in range(self.width):
                for col in range(self.height):
                    self.save_colors[row][col] = self.color


    # Sets a single pixel
    def set_pixel(self, x, y, color):
        if x >= self.width:
            utils.error_format("The x value "+ str(x) + " is off the edge of the waffle")
        elif y >= self.width:
            utils.error_format("The y value "+ str(y) + " is off the edge of the waffle")
        else:
            locate_x = (self.dim + self.pad) * int(x) + self.pad
            locate_y = (self.dim + self.pad) * int(y) + self.pad
            if self.dotty == False:
                self.canvas.create_rectangle(locate_x, locate_y, locate_x+self.dim, locate_y+self.dim, fill=color)
               
            else:
                self.canvas.create_oval(locate_x, locate_y, locate_x+self.dim, locate_y+self.dim, fill=color)

            # Update the grid if we have been asked to remember the colours
            if self.remember:
                self.save_colors[x][y] = color

    # Returns the colour value of a pixel if set
    def get_pixel(self, x, y):

        if self.remember == False:
            utils.error_format("You used get_pixel() on a [Waffle] which has no memory.\nIf you would like your [Waffle] to remember colors, set remember=True when you create the Waffle")
        else:
            return self.save_colors[x][y]

    # Returns a 2d list of all colours in the waffle
    def get_all(self):
        
        if self.remember == False:
            utils.error_format("You used get_all() on a [Waffle] which has no memory.\nIf you would like your [Waffle] to remember colors, set remember=True when you create the Waffle")
        else:
            return self.save_colors

    # Detect x,y coords of where the user clicked
    def clicked_on(self,e):
        canvas = e.widget
        x = canvas.canvasx(e.x)
        y = canvas.canvasy(e.y)
        pixel_x = int(x/(self.dim+self.pad))
        pixel_y = int(y/(self.dim+self.pad))
        if self.command:
            self.command(pixel_x,pixel_y)
