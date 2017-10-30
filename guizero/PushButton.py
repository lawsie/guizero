from tkinter import Button, PhotoImage, StringVar, DISABLED, NORMAL
from . import utilities as utils

class PushButton:

    def __init__(self, master, command, args=None, text="Button", icon=None, pady=10, padx=10, grid=None, align=None):

        self._text = StringVar()
        self._text.set(text)
        self.current_font = "Arial"
        self.current_size = 11

        # Description of this object (for friendly error messages)
        self.description = "[PushButton] object with text \"" + self._text.get() + "\""

        # Create a tk Button object within this object
        self.tk = Button(master, textvariable=self._text)

        # If the args LIST was not blank, convert to allow args
        if args is not None:
            command = utils.with_args(command, *args)

        # Add command and padding if necessary
        self.tk.config(command=command, pady=pady, padx=padx)

        # Try to instantiate a picture
        if icon is not None:
            try:
                self._icon = PhotoImage(file=icon)
                self.tk.config(image=self._icon)
            except AttributeError:
                utils.error_format("Image import error - image must be a gif, check correct path")


        # Pack or grid depending on parent
        try:
            utils.auto_pack(self, master, grid, align)
        except AttributeError:
            utils.error_format( self.description + "\n" +
            "Could not add to interface - check first argument is [App] or [Box]")

    # PROPERTIES
    # ----------------------------------
    # Get the text on the button
    @property
    def value(self):
        return (self._text.get())

    # Set the text on the button
    @value.setter
    def value(self, value):
        self._text.set(str(value))
        self.description = "[Text] object with text \"" + str(value) + "\""

    # Get the text colour as a string
    @property
    def text_color(self):
        return (self.tk.cget("fg"))

    # Set the text colour
    @text_color.setter
    def text_color(self, color):
        self.tk.config(fg=color)

    # Get the background colour as a string
    @property
    def bg(self):
        return (self.tk.cget("bg"))

    # Set the background colour
    @bg.setter
    def bg(self, color):
        self.tk.config(bg=color)

    # Get the current font as a string
    @property
    def font(self):
        return (self.current_font)

    # Set the current font
    @font.setter
    def font(self, font):
        self.current_font = font
        self.tk.config(font=(self.current_font, self.current_size))

    # Get the current font size as an integer
    @property
    def size(self):
        return (self.current_size)

    # Set the font size
    @size.setter
    def size(self, size):
        self.current_size = int(size)
        self.tk.config(font=(self.current_font, self.current_size))

    # METHODS
    # -------------------------------------------

    # Change command - needs the name of a function and optional args as a list
    def change_command(self, newcommand, args=None):
        if args is not None:
            newcommand = utils.with_args(newcommand, *args)
        self.tk.config(command=newcommand)

    # Contributed by jezdean
    # -----------------------
    # Enable Button
    def enable(self):
        self.tk.config(state=NORMAL)

    # Disable Button
    def disable(self):
        self.tk.config(state=DISABLED)

    # Toggle button state
    def toggle_state(self):
        button_state = self.tk.cget("state")
        if button_state == "disabled":
            self.enable()
        elif button_state == "normal":
            self.disable()

    # Change padding
    def padding(self, padx, pady):
        self.tk.config(padx=padx, pady=pady)

    # Set the icon
    def icon(self, icon):
        try:
            img = PhotoImage(file=icon)
            self._icon = img
            self.tk.config(image=img)
        except AttributeError:
            utils.error_format("Image import error - image must be a gif, check correct path")


    # DEPRECATED
    # -------------------------------------------
    # Change text
    def set_text(self, text):
        self._text.set(str(text))
        self.description = "[Text] object with text \"" + str(text) + "\""
        utils.deprecated("set_text() is deprecated. Please use the value property instead.")
