from tkinter import Scale, HORIZONTAL, VERTICAL
from . import utilities as utils
from .base import TextWidget

class Slider(TextWidget):

    def __init__(self, master, start=0, end=100, horizontal=True, command=None, grid=None, align=None, visible=True, enabled=True):

        description = "[Slider] object from " + str(start) + " to " + str(end)

        # Set the direction
        orient = HORIZONTAL if horizontal else VERTICAL

        # Create a tk Scale object within this object
        tk = Scale(master.tk, from_=start, to=end, orient=orient, command=self._command_callback)

        super(Slider, self).__init__(master, tk, description, grid, align, visible, enabled)

        self.update_command(command)

    # PROPERTIES
    # ----------------
    # Get/set the value
    @property
    def value(self):
        return (self.tk.get())

    @value.setter
    def value(self, value):
        self.tk.set(value)

    @property
    def width(self):
        return self.tk.cget("length")

    @width.setter
    def width(self, value):
        self.tk.config(length=value)

    @property
    def height(self):
        return self.tk.cget("width")

    @height.setter
    def height(self, value):
        self.tk.config(width=value)


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
