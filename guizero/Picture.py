
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

    def _load_image(self):
        img = utils.open_image(self._image_path, self._width, self._height)
        if img:
            self._width = img.width()
            self.tk.config(width=self._width)
            self._height = img.height()
            self.tk.config(height=self._height)
            
            # ok...  Unless self._image is set to img Picture doesnt work... I have no idea why! 
            # There must be tkinter weirdness going on
            self._image = img
            self.tk.config(image=img)
        
    # PROPERTIES
    # ----------------------------------
    # Get the filename of the image
    @property
    def value(self):
        return (self._image_path)

    # Set the image to a given file
    @value.setter
    def value(self, image):
        self._image_path = image
        self.description = "[Picture] object \"" + str(self._image_path) + "\""
        self._load_image()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.tk.config(width=value)
        self._load_image()
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.tk.config(height=value)
        self._load_image()

    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the image to something new
    def set(self, image):
        self.value = image
        utils.deprecated("Picture set() is deprecated. Please use the value property instead.")
