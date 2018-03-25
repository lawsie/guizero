from tkinter import Entry, StringVar, END
from .mixins import WidgetMixin
from .tkmixins import (
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    TextMixin, 
    ColorMixin, 
    SizeMixin, 
    ReprMixin)
from . import utilities as utils

class TextBox(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    TextMixin,
    DisplayMixin,
    ColorMixin,
    SizeMixin,
    ReprMixin):

    def __init__(self, master, text="", width=10, grid=None, align=None, visible=True):

        self._master = master
        self._grid = grid
        self._align = align

        # Description of this object (for friendly error messages)
        self.description = "[TextBox] object with text \"" + str(text) + "\""

        # Set up controlling string variable
        self._text = StringVar()
        self._text.set( str(text) )

        # Create a tk Label object within this object
        self.tk = Entry(master.tk, textvariable=self._text, width=width)

        self.visible = visible

    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        return self._text.get()

    @value.setter
    def value(self, value):
        self._text.set( str(value) )
        self.description = "[Text] object with text \"" + str(value) + "\""

    @property
    def height(self):
        utils.error_format("{} doesn't have a height".format(self.description))

    @height.setter
    def height(self, value):
        utils.error_format("Cannot change height for {}".format(self.description))
        

    # METHODS
    # -------------------------------------------
    # Clear text box
    def clear(self):
        self.value = ""

    # Append text
    def append(self, text):
        self.value = self.value + str(text)
        self.description = "[Text] object with text \"" + self.value + "\""


    # DEPRECATED METHODS
    # --------------------------------------------
    # Returns the text
    def get(self):
        return self._text.get()
        utils.deprecated("TextBox get() is deprecated. Please use the value property instead.")

    # Sets the text
    def set(self, text):
        self._text.set( str(text) )
        self.description = "[Text] object with text \"" + str(text) + "\""
        utils.deprecated("TextBox set() is deprecated. Please use the value property instead.")
