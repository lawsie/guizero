
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
        self._image_source = image
        self._image = None
        self._image_player = None
        self._width = None
        self._height = None

        # Instantiate label object which will contain image
        self.tk = Label(master.tk)

        # create the image
        if image:
            self._load_image()

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)

    def _load_image(self):
        # stop any animation which might still be playing
        if self._image_player:
            self._image_player.stop()

        # load the image and set its properties
        self._image = utils.GUIZeroImage(self._image_source, self._width, self._height)

        self._width = self._image.width
        self._height = self._image.height

        # if its an animation, start it up
        if self._image.animation:
            self._image_player = utils.AnimationPlayer(self, self._image, self._update_tk_image)
        else:
            self._update_tk_image(self._image.tk_image)
        
        self.tk.config(width=self._width)
        self.tk.config(height=self._height)
        
    def _update_tk_image(self, tk_image):
        self.tk.config(image=tk_image)

    # PROPERTIES
    # ----------------------------------
    # Get the filename of the image
    @property
    def value(self):
        return self._image.image_source

    # Set the image to a given file
    @value.setter
    def value(self, image_source):
        self._image_source = image_source
        self._load_image()

    @property
    def image(self):
        return self.value

    # Set the image to a given file
    @image.setter
    def image(self, image_source):
        self.value = image_source

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._load_image()
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._load_image()

    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the image to something new
    def set(self, image):
        self.value = image
        utils.deprecated("Picture set() is deprecated. Please use the value property instead.")
