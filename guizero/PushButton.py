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

        """
        Creates a PushButton

        :param Container master:
            The Container (App, Box, etc) the Picture will belong to.

        :param function command:
            A string containing the image to display, defaults to `None`.

        :param List args:
            A list of arguments to pass to the command. Defaults to `None`.

        :param string text:
            The text to display on the button, defaults to `Button`.

        :param string image:
            A string containing the image to display, defaults to `None`.
            If an image is specified, this overrides any text set to display
            on the button.

        :param int padx:
            The amount of horizontal padding the button should have. Defaults to 10.

        :param int pady:
            The amount of vertical padding the button should have. Defaults to 10.

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to None.

        :param string icon:
            A string containing the image to display, defaults to `None`.
            If an image is specified, this overrides any text set to display
            on the button. (DEPRECATED)

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        :param bool enabled:
            If the widget should be enabled, defaults to `None`. If `None`
            the value is inherited from the master.

        :param int width:
            The starting width of the widget. Defaults to `None` and will auto
            size.

        :param int height:
            The starting height of the widget. Defaults to `None` and will auto
            size.
        """


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
