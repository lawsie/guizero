from tkinter import Label, StringVar
from . import utilities as utils
from .base import TextWidget

class Text(TextWidget):

    def __init__(
        self,
        master,
        text="",
        size=None,
        color=None,
        bg=None,
        font=None,
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None,
        bold=None,
        italic=None,
        underline=None,
        overstrike=None):

        self._text = str(text)
        tk = Label(master.tk, text=text)
        super().__init__(master, tk, grid, align, visible, enabled, width, height)

        # setup defaults
        if bg:
            self.bg = bg
        
        if size is not None:
            self.text_size = size

        if font is not None:
            self.font = font

        if color is not None:
            self.text_color = color

        if bold is not None:
            self.text_bold = bold

        if italic is not None:
            self.text_italic = italic

        if underline is not None:
            self.text_underline = underline

        if overstrike is not None:
            self.text_overstrike = overstrike

    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        return (self._text)

    @value.setter
    def value(self, value):
        self.tk.config(text=value)
        self._text = str(value)

    # The font size
    @property
    def size(self):
        return self.text_size

    @size.setter
    def size(self, size):
        self.text_size = size

    # The font weight
    @property
    def bold(self):
        return self.text_bold

    @bold.setter
    def bold(self, bold):
        self.text_bold = bold

    # The font slant
    @property
    def italic(self):
        return self.text_italic

    @italic.setter
    def italic(self, italic):
        self.text_italic = italic

    # The font underline
    @property
    def underline(self):
        return self.text_underline

    @underline.setter
    def underline(self, underline):
        self.text_underline = underline

    # The font overstrike
    @property
    def overstrike(self):
        return self.text_overstrike

    @overstrike.setter
    def overstrike(self, overstrike):
        self.text_overstrike = overstrike

    @property
    def description(self):
        """
        Returns the description for the widget.
        """
        return "[Text] object with text '{}'".format(self.value)

    # METHODS
    # -------------------------------------------

    # Clear text (set to empty string)
    def clear(self):
        self._text = ""
        self.tk.config(text="")

    # Append some text onto the end of the existing text
    def append(self, text):
        new_text = self._text + str(text)
        self._text = new_text
        self.tk.config(text=new_text)

