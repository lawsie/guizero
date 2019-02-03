from tkinter import Button, StringVar, DISABLED, NORMAL
from . import utilities as utils
from .base import TextWidget

class PushButton(TextWidget):
    def __init__(
        self,
        master,
        command=None,
        args=None,
        text="Button",
        image=None,
        pady=10,
        padx=10,
        grid=None,
        align=None,
        icon=None,
        visible=True,
        enabled=None,
        width=None,
        height=None):

        description = "[PushButton] object with text \"" + text + "\""

        self._value = 0
        self._image_source = icon
        self._image_source = image
        self._image = None
        self._image_height = None
        self._image_width = None
        self._image_player = None

        # Create a tk Button object within this object
        self._text = StringVar()
        self._text.set(text)
        tk = Button(master.tk, textvariable=self._text, command=self._command_callback)

        super(PushButton, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        # Add padding if necessary
        self.tk.config(pady=pady, padx=padx)

        # Setup events for press and release
        self.events.set_event("<PushButton.ButtonPress-1>", "<ButtonPress-1>", self._on_press)
        self.events.set_event("<PushButton.ButtonRelease-1>", "<ButtonRelease-1>", self._on_release)

        self.update_command(command, args)

        if image:
            self._load_image()
        else:
            if icon:
                self._load_image()
                utils.deprecated("PushButton 'icon' constructor argument is deprecated. Please use image instead.")

    def _load_image(self):
        if self._height == "fill" or self._width == "fill":
            utils.raise_error("{}\nCannot use 'fill' for width and height when using a image.".format(self.description))

        # stop any animation which might still be playing
        if self._image_player:
            self._image_player.stop()

        self._image = utils.GUIZeroImage(self._image_source, self._width, self._height)

        # update the tk image
        # if its an animation, start it up
        if self._image.animation:
            self._image_player = utils.AnimationPlayer(self, self._image, self._update_tk_image)
        else:
            self._update_tk_image(self._image.tk_image)

        # set the width and height of the widget to match the image if they are None
        super(PushButton, self.__class__).resize(
            self, 
            self._image.width if self.width is None else self.width, 
            self._image.height if self.height is None else self.height)

    def _update_tk_image(self, tk_image):
        self.tk.config(image=tk_image)

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

    @property
    def image(self):
        return self._image.image_source

    @image.setter
    def image(self, value):
        self._image_source = value
        self._load_image()


    def resize(self, width, height):
        super(PushButton, self.__class__).resize(self, width, height)
        
        if self._image:
            self._load_image()        

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

    # Change padding
    def padding(self, padx, pady):
        self.tk.config(padx=padx, pady=pady)

    def toggle(self):
        self.enabled = not self.enabled

    def update_command(self, command, args=None):
        if command is None:
            self._command = lambda: None
        else:
            if args is None:
                self._command = command
            else:
                self._command = utils.with_args(command, *args)

    def _command_callback(self):
        self._command()

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

    # Change command - needs the name of a function and optional args as a list
    def change_command(self, newcommand, args=None):
        self.update_command(newcommand, args)
        utils.deprecated("PushButton change_command() is deprecated - renamed to update_command()")

    # Set the icon
    def icon(self, icon):
        self.image = icon
        utils.deprecated("PushButton icon() is deprecated - use the image property instead.")
