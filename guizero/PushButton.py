from tkinter import Button, PhotoImage, StringVar, DISABLED, NORMAL
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

class PushButton(
    WidgetMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    ReprMixin):

    def __init__(self, master, command, args=None, text="Button", icon=None, pady=10, padx=10, grid=None, align=None):

        self._master = master
        self._grid = grid
        self._align = align
        self._visible = True

        self._text = StringVar()
        self._text.set(text)
        self._current_font = "Arial"
        self._font_size = 11
        self._value = 0
        self.change_command(command, args)
        
        # Description of this object (for friendly error messages)
        self.description = "[PushButton] object with text \"" + self._text.get() + "\""

        # Create a tk Button object within this object
        self.tk = Button(master.tk, textvariable=self._text)

        # Add padding if necessary
        self.tk.config(pady=pady, padx=padx)

        # Setup events for press and release
        self.tk.bind("<ButtonPress>", self._on_press)
        self.tk.bind("<ButtonRelease>", self._on_release) 

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
    # Get the value of the button (pressed, released) 
    @property
    def value(self):
        return self._value

    # Get the text on the button
    @property
    def text(self):
        return (self._text.get())

    # Set the text on the button
    @text.setter
    def text(self, value):
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
        return (self._current_font)

    # Set the current font
    @font.setter
    def font(self, font):
        self._current_font = font
        self.tk.config(font=(self._current_font, self._font_size))

    # Get the current text size as an integer
    @property
    def text_size(self):
        return (self._font_size)

    # Set the font size
    @text_size.setter
    def text_size(self, size):
        self._font_size = int(size)
        self.tk.config(font=(self._current_font, self._font_size))

    # Get the current height as an integer (does not include padding)
    @property
    def height(self):
        return int(self.tk.cget("height"))

    # Set the height
    @height.setter
    def height(self, height_px):
        self.tk.config(height=int(height_px))

    # Get the current width as an integer (does not include padding)
    @property
    def width(self):
        return int(self.tk.cget("width"))

    # Set the height
    @width.setter
    def width(self, width_px):
        self.tk.config(width=int(width_px))


    # METHODS
    # -------------------------------------------
    # Internal use only
    # Called when the button is pressed
    def _on_press(self, event):
        if self.enabled:
            self._value = 1
        
    # Called when the button is released
    def _on_release(self, event):
        if self.enabled:
            self._value = 0
            self._command()
        
    # Change command - needs the name of a function and optional args as a list
    def change_command(self, newcommand, args=None):
        if args is None:
            self._command = newcommand
        else:
            # If the args LIST was not blank, allow args
            self._command = utils.with_args(newcommand, *args)

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

    def toggle(self):
        self.enabled = not self.enabled

    # DEPRECATED
    # -------------------------------------------
    # Change text
    def set_text(self, text):
        self.text = text
        utils.deprecated("PushButton set_text() is deprecated. Please use the value property instead.")

    # Toggle button state - renamed to just toggle
    def toggle_state(self):
        self.toggle()
        utils.deprecated("PushButton toggle_state() is deprecated - renamed to toggle()")