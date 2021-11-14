from tkinter import LabelFrame
from . import utilities as utils
from .base import ContainerTextWidget
from .event import EventManager

class TitleBox(ContainerTextWidget):

    def __init__(
        self,
        master,
        title="Name",
        layout="auto",
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None,
        border=1):
        """
        Creates a TitleBox

        :param Container master:
            The Container (App, TitleBox, etc) the TitleBox will belong too.

        :param string title:
            The text to be displayed on the box title. Defaults to "Name".

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
            value > 1 sets a border. The default is `1`.
        """

        description = "[TitleBox] object (may also contain other objects)"
        self._title = str(title)
        self._border = border;
        if border is None or border < 1:
            self._border = 1;
        # border = 1 has a weird behavior, so it is avoided
        tk = LabelFrame(master.tk, text=self._title, bd=self._border + 1);

        super(TitleBox, self).__init__(master, tk, layout, grid, align, visible, enabled, width, height)

        self.resize(width, height)

    @property
    def border(self):
        """
        Sets or returns the border thickness.

        `0` or `False` is no border.
        `True` or value > 1 sets a border

        """
        return self._get_tk_config("bd") - 1

    @border.setter
    def border(self, value):
        self.set_border(value)

    def set_border(self, thickness):
        """
        Sets the border thickness and color.

        :param int thickness:
            The thickenss of the border.
        """
        if thickness < 1:
            self._set_tk_config("bd", 2)
        else:
            self._set_tk_config("bd", thickness + 1)

    def resize(self, width, height):
        """
        Resizes the widget.

        :param int width:
            The width of the widget.

        :param int height:
            The height of the widget.
        """
        self._set_propagation(width, height)

        super(TitleBox, self).resize(width, height)

    @property
    def title(self):
        return self._get_tk_config("text")

    @title.setter
    def title(self, value):
        self.set_title(value)

    def set_title(self, value):
        if value is not "":
            self._set_tk_config("text", value)
