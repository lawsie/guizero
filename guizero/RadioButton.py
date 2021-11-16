from tkinter import Radiobutton
from . import utilities as utils
from .base import TextWidget

# Only to be used as part of button group
# unless you want to externally create a controlling variable StringVar()
# Does NOT create an internal StringVar() as this is handled by the ButtonGroup class
class RadioButton(TextWidget):

    def __init__(self, master, text, value, variable, command=None, grid=None, align=None, visible=True, enabled=None):

        self._text = text
        self._value = value

        # `variable` is the externally passed StringVar keeping track of which
        # option was selected. This class should not be instantiated by a user
        # unless they know what they are doing.
        tk = Radiobutton(master.tk, text=self._text, value=self._value, variable=variable)

        super().__init__(master, tk, grid, align, visible, enabled, None, None)

    # PROPERTIES
    # -----------------------------------

    # The value of this button
    @property
    def value(self):
        return (self._value)

    @value.setter
    def value(self, value):
        self._value = str(value)
        self.tk.config(value=str(value))

    # The text from this button
    @property
    def text(self):
        return (self._text)

    @text.setter
    def text(self, text):
        self._text = str(text)
        self.tk.config(text=self._text)

    @property
    def description(self):
        """
        Returns the description for the widget.
        """
        return "[RadioButton] object with option={} value={}".format(self.text, self.value)