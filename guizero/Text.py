from tkinter import Label, StringVar
from . import utilities as utils
from .base import TextWidget

class Text(TextWidget):

    def __init__(
        self,
        master,
        text="",
        size=12,
        color="black",
        bg=None,
        font="Helvetica",
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None):

        description = "[Text] object with text \"" + str(text) + "\""

        self._text = str(text)
        tk = Label(master.tk, text=text)
        super(Text, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        # setup defaults
        if bg:
            self.bg = bg
        
        if size is not None:
            self.text_size = size

        if font is not None:
            self.font = font

        if color is not None:
            self.text_color = color

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
        self.description = "[Text] object with text \"" + str(value) + "\""

    # The font size
    @property
    def size(self):
        return self.text_size

    @size.setter
    def size(self, size):
        self.text_size = size


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
        self.description = "[Text] object with text \"" + new_text + "\""


    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the text colour
    def color(self, color):
        self.text_color = color
        utils.deprecated("Text color() is deprecated. Please use the text_color property instead.")

    # Set the font
    def font_face(self, font):
        self.font = font
        utils.deprecated("Text font_face() is deprecated. Please use font property instead.")

    # Set the font size
    def font_size(self, size):
        self.size = size
        utils.deprecated("Text font_size() is deprecated. Please use the size property instead.")

     # Returns the text
    def get(self):
        return self._text
        utils.deprecated("Text get() is deprecated. Please use the value property instead.")

    # Sets the text
    def set(self, text):
        self._text = str(text)
        self.tk.config(text=self._text)
        self.description = "[Text] object with text \"" + str(text) + "\""
        utils.deprecated("Text set() is deprecated. Please use the value property instead.")
