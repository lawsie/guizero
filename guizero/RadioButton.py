from tkinter import Radiobutton
from . import utilities as utils
from .base import TextWidget

# Only to be used as part of button group
# unless you want to externally create a controlling variable StringVar()
# Does NOT create an internal StringVar() as this is handled by the ButtonGroup class
class RadioButton(TextWidget):

    def __init__(self, master, text, value, variable, command=None, grid=None, align=None, visible=True, enabled=None):

        description = "[RadioButton] object with option=\"" + str(text) + "\" value=\"" + str(value) + "\""
        self._text = text
        self._value = value

        # `variable` is the externally passed StringVar keeping track of which
        # option was selected. This class should not be instantiated by a user
        # unless they know what they are doing.
        tk = Radiobutton(master.tk, text=self._text, value=self._value, variable=variable)

        super(RadioButton, self).__init__(master, tk, description, grid, align, visible, enabled, None, None)

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
        self.description = "[RadioButton] object with option=\"" + self._text + "\" value=\"" + str(value) + "\""

    # The text from this button
    @property
    def text(self):
        return (self._text)

    @text.setter
    def text(self, text):
        self._text = str(text)
        self.tk.config(text=self._text)
        self.description = "[RadioButton] object with option=\"" + str(text) + "\" value=\"" + self._value + "\""
