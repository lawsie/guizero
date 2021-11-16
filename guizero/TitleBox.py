from tkinter import LabelFrame
from . import utilities as utils
from .base import ContainerTextWidget

class TitleBox(ContainerTextWidget):

    def __init__(
        self,
        master,
        text,
        layout="auto",
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None,
        border=2):
        """
        Creates a TitleBox

        :param Container master:
            The Container (App, Box, etc) the TitleBox will belong too.

        :param string text:
            The text to be displayed on the box title.

        :param string layout:
            The layout the TitleBox should use "auto" or "grid. Defaults to "auto".

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to `None`.

        :param callback args:
            A list of arguments to pass to the widgets `command`, defaults to
            `None`.

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        :param bool enabled:
            If the widget should be enabled, defaults to `None`. If `None`
            the value is inherited from the master.

        :param int width:
            The starting width of the widget. Defaults to `None` and will auto
            size. If not `None`, both the width and height need to be set.

        :param int height:
            The starting height of the widget. Defaults to `None` and will auto
            size. If not `None`, both the width and height need to be set.

        :param int border:
            Sets the border thickness. `0` or `False` is no border. `True` or
            value > 1 sets a border. The default is `2`.
        """
        description = "[TitleBox] object (may also contain other objects)"

        tk = LabelFrame(master.tk, text=str(text), bd=border)

        super().__init__(master, tk, layout, grid, align, visible, enabled, width, height)

        self.resize(width, height)

    @property
    def border(self):
        """
        Sets or returns the border thickness.

        `0` or `False` is no border.
        `True` or value > 1 sets a border

        """
        return self._get_tk_config("bd")

    @border.setter
    def border(self, value):
        self._set_tk_config("bd", value)

    @property
    def text(self):
        """
        Sets of returns the text used in the title
        """
        return self._get_tk_config("text")

    @text.setter
    def text(self, value):
        self._set_tk_config("text", value)

    def resize(self, width, height):
        """
        Resizes the widget.

        :param int width:
            The width of the widget.

        :param int height:
            The height of the widget.
        """
        self._set_propagation(width, height)

        super().resize(width, height)
