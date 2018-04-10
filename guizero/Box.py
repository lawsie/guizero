from tkinter import Frame
from . import utilities as utils
from .base import ContainerWidget

class Box(ContainerWidget):

    def __init__(self, master, layout="auto", grid=None, align=None, visible=True):

        self._grid = grid
        self._align = align

        description = "[Box] object (may also contain other objects)"
        
        tk = Frame(master.tk)

        super(Box, self).__init__(master, tk, description, layout, grid, align, visible, True)
        
        self.visible = visible
    
    # Box enable / disable functions need implementing
    @property
    def enabled(self):
        return True

    @enabled.setter
    def enabled(self, value):
        if value:
            self.enable()
        else:
            self.disable()
    
    def disable(self):
        """Disable the widget."""
        utils.error_format("A [Box] cannot be disabled")

    def enable(self):
        """Enable the widget."""
        pass
