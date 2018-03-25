from tkinter import Entry, StringVar, Text, END
from tkinter.scrolledtext import ScrolledText
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

    def __init__(self, master, text="", width=10, height=1, grid=None, align=None, visible=True, enabled=True, multiline=False, scrollbar=False):

        self._master = master
        self._grid = grid
        self._align = align

        self._multiline = multiline
        self._height = height

        # Description of this object (for friendly error messages)
        self.description = "[TextBox] object with text \"" + str(text) + "\""

        # Set up controlling string variable
        self._text = StringVar()
        self._text.set( str(text) )

        # Create a tk object for the text box
        if multiline:
            if scrollbar:
                self.tk = ScrolledText(master.tk, width=width, height=height)
            else:
                self.tk = Text(master.tk, width=width, height=height)
            self.tk.insert(END,self._text.get())
        else:
            self.tk = Entry(master.tk, textvariable=self._text, width=width)

        self.visible = visible
        self.enabled = enabled

    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        if self._multiline:
            return self.tk.get(1.0,END)
        else:
            return self._text.get()

    @value.setter
    def value(self, value):
        self._text.set( str(value) )
        if self._multiline:
            self.tk.delete(1.0,END)
            self.tk.insert(END,self._text.get())
        self.description = "[TextBox] object with text \"" + str(value) + "\""

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if self._multiline:
            self._height = value
            self.tk.config(height=value)
        else:
            utils.error_format("Cannot change the height of a single line TextBox{}".format(self.description))
        

    # METHODS
    # -------------------------------------------
    # Clear text box
    def clear(self):
        self.value = ""

    # Append text
    def append(self, text):
        self.value = self.value + str(text)


    # DEPRECATED METHODS
    # --------------------------------------------
    # Returns the text
    def get(self):
        return self.value
        utils.deprecated("TextBox get() is deprecated. Please use the value property instead.")

    # Sets the text
    def set(self, text):
        self.value = text
        utils.deprecated("TextBox set() is deprecated. Please use the value property instead.")
