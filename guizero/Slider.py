from tkinter import Scale, HORIZONTAL, VERTICAL
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

class Slider(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ReprMixin):

    def __init__(self, master, start=0, end=100, horizontal=True, command=None, grid=None, align=None):

        # If you specify a command to the slider, it must take one argument as it will be given
        # the slider's current value

        self._master = master
        self._grid = grid
        self._align = align
        self._visible = True

        # Description of this object (for friendly error messages)
        self.description = "[Slider] object from " + str(start) + " to " + str(end)

        # Set the direction
        orient = HORIZONTAL if horizontal else VERTICAL

        # Create a tk Scale object within this object
        self.tk = Scale(master.tk, from_=start, to=end, orient=orient, command=command)

        # Pack this object
        try:
            utils.auto_pack(self, master, grid, align)
       	except AttributeError:
            utils.error_format( self.description + "\n" +
            "Could not add to interface - check first argument is [App] or [Box]")

    # PROPERTIES
    # ----------------
    # Get/set the value
    @property
    def value(self):
        return (self.tk.get())

    @value.setter
    def value(self, value):
        self.tk.set(value)

    # METHODS
    # ----------------
    # Calls the given function when the slider value is changed
    def add_command(self, command):
        self.tk.config(command=command)
