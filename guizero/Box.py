from tkinter import Frame
from . import utilities as utils
from .base import ContainerWidget

class Box(ContainerWidget):

    def __init__(
        self, 
        master, 
        layout="auto", 
        grid=None, 
        align=None, 
        visible=True, 
        enabled=None, 
        width=None, 
        height=None):
        """
        Creates a Box

        :param Container master:
            The Container (App, Box, etc) the Box will belong too.

        :param string layout:
            The layout the Box should use "auto" or "grid. Defaults to "auto".

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
        """

        self._grid = grid
        self._align = align
        
        description = "[Box] object (may also contain other objects)"
        
        tk = Frame(master.tk)

        super(Box, self).__init__(master, tk, description, layout, grid, align, visible, enabled, width, height)

        self.resize(width, height)
            
    def resize(self, width, height):
        """
        Resizes the widget.

        :param int width:
            The width of the widget.

        :param int height:
            The height of the widget.
        """
        if width is None:
            width = 0
        
        if height is None:
            height = 0

        if width == 0 and height == 0:
            self.tk.pack_propagate(True)
        elif width > 0 and height > 0:
            self.tk.pack_propagate(False)
        else:
            utils.error_format("You must specify a width and a height for a Box")

        super(Box, self).resize(width, height)

    @property
    def border(self):
        """
        Sets or returns the border thickness. 
        
        `0` or `False` is no border.
        `True` or value > 1 sets a border

        """
        return self._get_tk_config("highlightthickness")

    @border.setter
    def border(self, value):
        self.set_border(value, "black")
        
    def set_border(self, thickness, color="black"):
        """
        Sets the border thickness and color.

        :param int thickness:
            The thickenss of the border.

        :param str color:
            The color of the border.
        """
        self._set_tk_config("highlightthickness", thickness)
        self._set_tk_config("highlightbackground", utils.convert_color(color))
