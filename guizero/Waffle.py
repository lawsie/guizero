from tkinter import Canvas, BOTH, Frame
from . import utilities as utils
from .base import Widget
from .event import EventManager

class Waffle(Widget):

    def __init__(
        self, 
        master, 
        height=3, 
        width=3, 
        dim=20, 
        pad=5, 
        color="white", 
        dotty=False, 
        grid=None, 
        align=None, 
        command=None,  
        visible=True, 
        enabled=None, 
        bg=None):

        description = "[Waffle] object ({}x{})".format(height, width)

        # Create a tk Frame object within this object which will be the waffle
        tk = Frame(master.tk)

        # self._height = height       # How many pixels high
        # self._width = width         # How many pixels wide
        self._pixel_size = dim      # Size of one pixel
        self._pad = pad             # How much padding between pixels
        self._color = utils.convert_color(color)        # Start color of the whole waffle
        self._dotty = dotty         # A dotty waffle will display circles
        self._waffle_pixels = {}
        self._canvas = None

        super(Waffle, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        if bg is not None:
            self.bg = bg

        self.update_command(command)

        #override the event manager so it uses the canvas not the frame
        self._events = EventManager(self, self._canvas)

        # Bind the left mouse click to the canvas so we can click on the waffle
        self.events.set_event("<Waffle.ButtonPress-1>", "<ButtonPress-1>", self._clicked_on)


    # METHODS
    # -------------------------------------------

    # Internal use only
    def _create_waffle(self):
        if self._height == "fill" or self._width == "fill":
            utils.raise_error("{}\nCannot use 'fill' for width and height.".format(self.description))
            
        self._create_canvas()
        self._size_waffle()
        self._draw_waffle()

    def _create_canvas(self):
        # if the canvas exists, clear it and destroy it
        if self._canvas:
            self._canvas.delete("all")
            self._canvas.destroy()

        #size the canvas
        self._c_height = (self._height * (self._pixel_size + self._pad)) + (self._pad * 2)
        self._c_width = self._width * (self._pixel_size + self._pad) + (self._pad * 2)

        # create the canvas and pack it into the waffle frame
        self._canvas = Canvas(self.tk, height=self._c_height, width=self._c_width, bd=0, highlightthickness=0)
        self._canvas.pack(fill=BOTH, expand=1)

        # rebind any events as they would have been lost when the canvas
        # was destroyed
        self.events.rebind_events(self._canvas)

        # fill the canvas background
        self._canvas.create_rectangle(0, 0, self._c_width, self._c_height, fill=self.bg, outline=self.bg)

    # sizes or resizes the waffle, maintaining the state of existing pixels
    def _size_waffle(self):
        # create new pixels
        new_waffle_pixels = {}
        currx = self._pad
        curry = self._pad

        for x in range(self._width):
            for y in range(self._height):
                if (x,y) in self._waffle_pixels.keys():
                    # if pixel already exist, reuse it and update the values
                    old_pixel = self._waffle_pixels[(x,y)]
                    new_waffle_pixels[x,y] = WafflePixel(
                        x, y,
                        self._canvas, currx, curry,
                        self._pixel_size,
                        old_pixel.dotty,
                        old_pixel.color)
                else:
                    # create a new celpixell
                    new_waffle_pixels[x,y] = WafflePixel(
                        x, y,
                        self._canvas, currx, curry,
                        self._pixel_size,
                        self._dotty,
                        self._color)

                curry += self._pixel_size + self._pad

            currx += self._pixel_size + self._pad
            curry = self._pad

        self._waffle_pixels = new_waffle_pixels

    def _draw_waffle(self):
        currx = self._pad
        curry = self._pad
        # draw the waffle from the waffle_cells
        for x in range(self._width):
            for y in range(self._height):
                cell = self._waffle_pixels[x,y]
                cell.draw()
                curry += self._pixel_size + self._pad

            currx += self._pixel_size + self._pad
            curry = self._pad

    # Sets the colour of the whole waffle
    def set_all(self, color):
        for x in range(self._width):
            for y in range(self._height):
                self._waffle_pixels[x,y].color = color

    # Sets a single pixel
    def set_pixel(self, x, y, color):
        if self.pixel(x, y):
            self._waffle_pixels[x,y].color = color

    # Returns the colour value of a pixel if set
    def get_pixel(self, x, y):
        if self.pixel(x, y):
            return self._waffle_pixels[x,y].color

    # Returns a 2D list of all colours in the waffle
    def get_all(self):
        all_pixels = []
        for y in range(self._height):
            row = []
            for x in range(self._width):
                row.append(self._waffle_pixels[x,y].color)
            all_pixels.append(row)
        return all_pixels

    # Internal use only
    # Detect x,y coords of where the user clicked
    def _clicked_on(self,e):
        # you can only click on the waffle if its enabled
        if self._enabled:
            canvas = e.tk_event.widget
            x = canvas.canvasx(e.tk_event.x)
            y = canvas.canvasy(e.tk_event.y)
            pixel_x = int(x / (self._pixel_size + self._pad))
            pixel_y = int(y / (self._pixel_size + self._pad))
            if self._command:
                args_expected = utils.no_args_expected(self._command)
                if args_expected == 0:
                    self._command()
                elif args_expected == 2:
                    self._command(pixel_x,pixel_y)
                else:
                    utils.error_format("Waffle command function must accept either 0 or 2 arguments.\nThe current command has {} arguments.".format(args_expected))

    def update_command(self, command):
        if command is None:
            self._command = lambda: None
        else:
            self._command = command

    # Returns a WafflePixel object
    def pixel(self, x, y):
        if (x,y) in self._waffle_pixels.keys():
            _pixel = self._waffle_pixels[x,y]
        else:
            utils.error_format("Pixel x={} y={} is off the edge of the waffle".format(x, y))
            _pixel = None
        return _pixel

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def disable(self):
        """Disable the widget."""
        self._enabled = False

    def enable(self):
        """Enable the widget."""
        self._enabled = True

    def resize(self, width, height):
        if self._width != width or self._height != height:
            self._width = width
            self._height = height
            self._create_waffle()

    @property
    def pixel_size(self):
        return self._pixel_size

    @pixel_size.setter
    def pixel_size(self, value):
        if self._pixel_size != value:
            self._pixel_size = value
            self._create_waffle()

    @property
    def pad(self):
        return self._pad

    @pad.setter
    def pad(self, value):
        if self._pad != value:
            self._pad = value
            self._create_waffle()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        old_color = self._color
        self._color = utils.convert_color(value)
        for x in range(self._width):
            for y in range(self._height):
                if self._waffle_pixels[x,y].color == old_color:
                    self._waffle_pixels[x,y].color = self._color

    @property
    def dotty(self):
        return self._dotty

    @dotty.setter
    def dotty(self, value):
        self._dotty = value
        for x in range(self._width):
            for y in range(self._height):
                self._waffle_pixels[x,y].dotty = self._dotty

    # Get the background colour
    @property
    def bg(self):
        return super(Waffle, self.__class__).bg.fget(self)

    # Set the background colour
    @bg.setter
    def bg(self, value):
        # only change the color if we need too as it requires
        # redrawing the canvas
        if self.bg != value:
            value = utils.convert_color(value)
            super(Waffle, self.__class__).bg.fset(self, value)
            self._create_waffle()

    def reset(self):
        # reset all the colors and dottiness
        self.set_all(self._color)
        self.dotty = self._dotty

    def __getitem__(self, index):
        return self._waffle_pixels[index]

class WafflePixel():
    def __init__(self, x, y, canvas, canvas_x, canvas_y, size, dotty, color):
        self._x = x
        self._y = y
        self._canvas = canvas
        self._canvas_x = canvas_x
        self._canvas_y = canvas_y
        self._size = size
        self._dotty = dotty
        self._color = color
        self._drawn_object = None

    def draw(self):

        # if the object has been drawn before delete it
        if self._drawn_object:
            self._canvas.delete(self._drawn_object)

        if self._dotty == False:
            self._drawn_object = self._canvas.create_rectangle(
                self._canvas_x, self._canvas_y,
                self._canvas_x + self._size, self._canvas_y + self._size,
                fill=self._color)
        else:
            self._drawn_object = self._canvas.create_oval(
                self._canvas_x, self._canvas_y,
                self._canvas_x + self._size, self._canvas_y + self._size,
                fill=self._color)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def canvas_x(self):
        return self._canvas_x

    @property
    def canvas_y(self):
        return self._canvas_x

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = utils.convert_color(value)
        self._canvas.itemconfig(self._drawn_object, fill=self._color)

    @property
    def dotty(self):
        return self._dotty

    @dotty.setter
    def dotty(self, value):
        self._dotty = value
        self.draw()
