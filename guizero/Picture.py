
from tkinter import Label
from .mixins import WidgetMixin
from .tkmixins import (
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ColorMixin,
    ReprMixin)
from . import utilities as utils

class Picture(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ColorMixin,
    ReprMixin):

    def __init__(self, master, image=None, grid=None, align=None):

        self._master = master
        self._grid = grid
        self._align = align
        self._visible = True
        self._width = None
        self._height = None

        # Instantiate label object which will contain image
        self.tk = Label(master.tk)

        self.value = image

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)

    def _load_image(self, image_path, width, height):
        img = utils.open_image(image_path, width, height)
        if img:
            # the image was loaded
            self._image_path = image_path
            self.description = "[Picture] object \"" + str(self._image_path) + "\""
        
            #set the dimensions
            if width is None:
                self._width = img.width()
            else: 
                self._width = width
            
            if height is None:
                self._height = img.height()
            else:
                self._height = height 

            # put the image into the label 
            self.tk.config(image=img)
            self.tk.config(width=self._width)
            self.tk.config(height=self._height)
            
            # The tk PhotoImage object needs to be referenced by an internal variable
            # otherwise the garbage collector destroys it, even though it is referenced
            # by the tk label widget.
            self._image = img

    # PROPERTIES
    # ----------------------------------
    # Get the filename of the image
    @property
    def value(self):
        return (self._image_path)

    # Set the image to a given file
    @value.setter
    def value(self, image):
        self._load_image(image, self._width, self._height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._load_image(self._image_path, value, self._height)
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._load_image(self._image_path, self._width, value)

    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the image to something new
    def set(self, image):
        self.value = image
        utils.deprecated("Picture set() is deprecated. Please use the value property instead.")
