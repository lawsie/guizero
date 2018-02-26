
from tkinter import Label, PhotoImage, TclError
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ColorMixin, ReprMixin
from . import utilities as utils
from .config import system_config

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
        if image:
            try:
                img = PhotoImage(master=self.tk.winfo_toplevel(), file=image)

                # ok...  Unless self._image is set to img Picture doesnt work... I have no idea why! 
                # There must be tkinter weirdness going on
                self._image = img
                
                self.tk.config(image=img)
                
            except:
                utils.error_format("Image import error '{}' - check the file path and image type is {}".format(str(self._image_path),"/".join(system_config.supported_image_types)))

    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the image to something new
    def set(self, image):
        self.value = image
        utils.deprecated("Picture set() is deprecated. Please use the value property instead.")
