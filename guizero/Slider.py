from tkinter import Scale, HORIZONTAL, VERTICAL
from . import utilities as utils
from .base import TextWidget

class Slider(TextWidget):

    def __init__(
        self, 
        master, 
        start=0, 
        end=100, 
        horizontal=True, 
        command=None, 
        grid=None, 
        align=None, 
        visible=True, 
        enabled=None, 
        width=None, 
        height=None):

        # Set the direction
        self._horizontal = horizontal
        orient = HORIZONTAL if horizontal else VERTICAL

        # Create a tk Scale object within this object
        tk = Scale(master.tk, from_=start, to=end, orient=orient, command=self._command_callback)

        super().__init__(master, tk, grid, align, visible, enabled, width, height)

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
    
    # Add ability to set start and end as properties 
    @property
    def start(self):
        return self._get_tk_config("from")

    @start.setter
    def start(self, value):
        self._set_tk_config("from", value)

    @property
    def end(self):
        return self._get_tk_config("to")

    @end.setter
    def end(self, value):
        self._set_tk_config("to", value)
    
    # Resize
    def resize(self, width, height):
        self._set_width(width)
        self._set_height(height)
        if width == "fill" or height == "fill":
            self.master.display_widgets()
    
    def _set_width(self, width):
        self._width = width
        if width != "fill":
            if self._horizontal:
                self._set_tk_config("length", width)
            else:
                self._set_tk_config("width", width)
    
    def _set_height(self, height):
        self._height = height
        if height != "fill":
            if self._horizontal:
                self._set_tk_config("width", height)
            else:
                self._set_tk_config("length", height)

    @property
    def description(self):
        """
        Returns the description for the widget.
        """
        return f"[Slider] object from {self.start} to {self.end}"

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
