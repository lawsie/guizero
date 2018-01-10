from tkinter import Label, PhotoImage, TclError
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

## See if PIL is installed
#try:
#    from PIL import Image, ImageTk
#except ImportError:
#    utils.error_format("You will only be able to display GIF images as you do not have the PIL library.")


class Picture(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ReprMixin):

    def __init__(self, master, image, grid=None, align=None):

        self._master = master
        self._grid = grid
        self._align = align
        self._visible = True

        # The image name as a string
        self._image_name = str(image)

        # Description of this object (for friendly error messages)
        self.description = "[Picture] object \"" + self._image_name + "\""

        # Instantiate label object which will contain image
        self.tk = Label(master.tk)

        try:
            img = PhotoImage(master=self.tk.winfo_toplevel(), file=image)
            self._image = img
            self.tk.config(image=self._image)

        except TclError:
            self.tk.config(text="Image "+ self._image_name +" failed to load")
            utils.error_format("Image import error - " + str(image) +" must be a GIF, check correct path")

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)

    # PROPERTIES
    # ----------------------------------
    # Get the filename of the image
    @property
    def value(self):
        return (self._image_name)

    # Set the image to a given file
    @value.setter
    def value(self, image):
        try:
            img = PhotoImage(master=self.tk.winfo_toplevel(), file=image)
            self._image = img
            self.tk.config(image=self._image)
            self._image_name = str(image)
            self.description = "[Picture] object \"" + str(image) + "\""
        except:
            utils.error_format("Image import error - " + str(image) +" must be a GIF, check correct path")


    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the image to something new
    def set(self, image):
        try:
            img = PhotoImage(master=self.tk.winfo_toplevel(), file=image)
            self._image = img
            self.tk.config(image=self._image)
            self._image_name = str(image)
            self.description = "[Picture] object \"" + str(image) + "\""
        except:
            utils.error_format("Image import error - " + str(image) +" must be a GIF, check correct path")
        utils.deprecated("Picture set() is deprecated. Please use the value property instead.")
