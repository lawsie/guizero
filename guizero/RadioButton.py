from tkinter import Radiobutton
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

# Only to be used as part of button group
# unless you want to externally create a controlling variable StringVar()
# Does NOT create an internal StringVar() as this is handled by the ButtonGroup class
class RadioButton(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ReprMixin):

    def __init__(self, master, text, value, variable, command=None, grid=None, align=None):

        self._master = master
        self._grid = grid
        self._align = align
        self._visible = True

        self.description = "[RadioButton] object with option=\"" + str(text) + "\" value=\"" + str(value) + "\""
        self._text = text
        self._value = value

        # `variable` is the externally passed StringVar keeping track of which
        # option was selected. This class should not be instantiated by a user
        # unless they know what they are doing.
        self.tk = Radiobutton(master.tk, text=self._text, value=self._value, variable=variable)


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
