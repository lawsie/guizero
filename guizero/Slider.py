from tkinter import Scale, HORIZONTAL, VERTICAL
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ColorMixin, ReprMixin
from . import utilities as utils

class Slider(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ColorMixin,
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
        self.tk = Scale(master.tk, from_=start, to=end, orient=orient, command=self._command_callback)

        self.update_command(command)

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
    
    def _command_callback(self, value):
        if self._command:
            args_expected = utils.no_args_expected(self._command)
            if args_expected == 0:
                self._command()
            elif args_expected == 1:
                self._command(value)
            else:
                utils.error_format("Slider command function must accept either 0 or 1 arguments.\nThe current command has {} arguments.".format(args_expected))

    def update_command(self, command):
        if command is None:
            self._command = lambda: None
        else:
            self._command = command

    # DEPRECATED
    # -------------------------------------------
        
    def add_command(self, command):
        self.update_command(command)
        utils.deprecated("Slider add_command() is deprecated - renamed to update_command()")
