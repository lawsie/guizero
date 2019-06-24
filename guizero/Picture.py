from tkinter import Label
from . import utilities as utils
from .base import Widget

class Picture(Widget):

    def __init__(
        self, 
        master, 
        image=None, 
        grid=None, 
        align=None, 
        visible=True, 
        enabled=None, 
        width=None, 
        height=None):

        """
        Creates a Picture

        :param Container master:
            The Container (App, Box, etc) the Picture will belong to.

        :param string image:
            A string containing the image to display, defaults to `None`.

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to None.

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        :param bool enabled:
            If the widget should be enabled, defaults to `None`. If `None`
            the value is inherited from the master.

        :param int width:
            The starting width of the widget. Defaults to `None` and will auto
            size.

        :param int height:
            The starting height of the widget. Defaults to `None` and will auto
            size.
        """

        description = "[Picture] object"

        self._image_source = image
        self._image = None
        self._image_player = None

        # Instantiate label object which will contain image
        tk = Label(master.tk)

        super(Picture, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        # create the image
        self._load_image()

    def _load_image(self):
        if self._height == "fill" or self._width == "fill":
            utils.raise_error("{}\nCannot use 'fill' for width and height.".format(self.description))

        if self._image_source is not None:

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
        """
        Gets or sets the file path, tkinter.PhotoImage or PIL.Image you wish to display
        """
        if self._image:
            return self._image.image_source
        else:
            return None

    # Set the image to a given file
    @value.setter
    def value(self, image_source):
        self._image_source = image_source
        self._load_image()

    @property
    def image(self):
        """
        Gets or sets the file path, tkinter.PhotoImage or PIL.Image you wish to display
        """
        return self.value

    # Set the image to a given file
    @image.setter
    def image(self, image_source):
        self.value = image_source

    def resize(self, width, height):
        self._width = width
        self._height = height
        self._load_image()
