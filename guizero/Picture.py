
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

        # Instantiate label object which will contain image
        self.tk = Label(master.tk)

        self.value = image

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)

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
        img = utils.open_image(image)
        if img:
            # ok...  Unless self._image is set to img Picture doesnt work... I have no idea why! 
            # There must be tkinter weirdness going on
            self._image = img
            
            self.tk.config(image=img)    

    @property
    def width(self):
        return self._image.width()

    @width.setter
    def width(self, value):
        self.tk.config(width=value)
        
    @property
    def height(self):
        return self._image.height()

    @height.setter
    def height(self, value):
        self.tk.config(height=value)

    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the image to something new
    def set(self, image):
        self.value = image
        utils.deprecated("Picture set() is deprecated. Please use the value property instead.")
