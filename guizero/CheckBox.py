from tkinter import Checkbutton, IntVar
from . import utilities as utils
from .base import TextWidget

class CheckBox(TextWidget):

    def __init__(
        self,
        master,
        text="",
        command=None,
        grid=None,
        align=None,
        args=None,
        visible=True,
        enabled=None,
        width=None,
        height=None):
        """
        Creates a CheckBox

        :param Container master:
            The Container (App, Box, etc) the CheckBox will belong too.

        :param string selected:
            The text required for the checkbox. Defaults to "".

        :param callback command:
            The callback function to call when the CheckBox changes.

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to None.

        :param callback args:
            A list of arguments to pass to the widgets `command`, defaults to
            `None`.

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

        description = "[CheckBox] object with text \"" + text + "\""

        self._text = str(text)
        self._value = IntVar()
        tk = Checkbutton(master.tk, text=text, variable=self._value)

        super(CheckBox, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        # Set the command callback
        self.tk.config(command=self._command_callback)
        self.update_command(command, args)

    # PROPERTIES
    # ----------------------------------
    # Whether the box is checked or not
    @property
    def value(self):
        """
        Sets or returns the value of the CheckBox.
        """
        return (self._value.get())

    # Set whether the box is checked or not
    @value.setter
    def value(self, value):
        try:
            value = int(value)
            if value in [0, 1]:
                self._value.set(value)

        except ValueError:
            utils.error_format("You can only set the value of " + self.description + " to either 0 (not checked) or 1 (checked)")

    # The text associated with this box
    @property
    def text(self):
        """
        Sets or returns the text of the CheckBox.
        """
        return (self._text)

    # Set whether the box is checked or not
    @text.setter
    def text(self, text):
        self._text = str(text)
        self.tk.config(text=self._text)
        self.description = "[CheckBox] object with text \"" + str(self._text) + "\""

    # METHODS
    # -------------------------------------------

    def toggle(self):
        """
        Toggles the value of the CheckBox.
        """
        self.tk.toggle()

    def update_command(self, command, args=None):
        """
        Updates the callback command which is called when the Combo
        changes.

        Setting to `None` stops the callback.

        :param callback command:
            The callback function to call.

        :param args list:
            A list of argument values to pass to the callback. Defaults to
            `None`.
        """
        if command is None:
            self._command = lambda: None
        else:
            if args is None:
                self._command = command
            else:
                self._command = utils.with_args(command, *args)

    def _command_callback(self):
        self._command()
