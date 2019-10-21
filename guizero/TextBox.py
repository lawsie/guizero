from tkinter import Entry, StringVar, Text, END
from tkinter.scrolledtext import ScrolledText
from . import utilities as utils
from .base import TextWidget

class TextBox(TextWidget):

    def __init__(
        self,
        master,
        text="",
        width=10,
        height=1,
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        multiline=False,
        scrollbar=False,
        command=None,
        hide_text=False):

        description = "[TextBox] object with text \"" + str(text) + "\""

        self._multiline = multiline
        
        # Set up controlling string variable
        self._text = StringVar()
        self._text.set( str(text) )

        # Create a tk object for the text box
        if multiline:
            if scrollbar:
                tk = ScrolledText(master.tk, wrap="word")
            else:
                tk = Text(master.tk)
            tk.insert(END,self._text.get())
        else:
            tk = Entry(master.tk, textvariable=self._text)

        super(TextBox, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        self.hide_text = hide_text
        self.update_command(command)

        # Bind the key pressed event
        self.events.set_event("<TextBox.KeyRelease>", "<KeyRelease>", self._key_released)

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

    def resize(self, width, height):
        self._width = width
        if width != "fill":
            self._set_tk_config("width", width)

        if height is not None:
            if self._multiline:
                self._height = height
                if height != "fill":
                    self.tk.config(height=height)
            else:
                if isinstance(height, int):
                    if height > 1:
                        utils.error_format("Cannot change the height of a single line TextBox{}".format(self.description))

    @property
    def hide_text(self):
        return self._hide_text

    @hide_text.setter
    def hide_text(self, value):
        self._hide_text = value

        if value == True:
            show_value = "*"
        elif value == False:
            show_value = ""
        else:
            show_value = value
        
        self._set_tk_config("show", show_value)

    # METHODS
    # -------------------------------------------
    def _key_released(self, event):
        if self._command:
            args_expected = utils.no_args_expected(self._command)
            if args_expected == 0:
                self._command()
            elif args_expected == 1:
                self._command(event.key)
            else:
                utils.error_format("TextBox command function must accept either 0 or 1 arguments.\nThe current command has {} arguments.".format(args_expected))

    def update_command(self, command):
        if command is None:
            self._command = lambda: None
        else:
            self._command = command

    # Clear text box
    def clear(self):
        self.value = ""

    # Append text
    def append(self, text):
        self.value = self.value + str(text)

