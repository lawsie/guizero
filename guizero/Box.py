from tkinter import Frame
from . import utilities as utils
from .base import ContainerWidget

class Box(ContainerWidget):

    def __init__(self, master, layout="auto", grid=None, align=None, visible=True, enabled=None):

        self._grid = grid
        self._align = align

        description = "[Box] object (may also contain other objects)"
        
        tk = Frame(master.tk)

        super(Box, self).__init__(master, tk, description, layout, grid, align, visible, enabled)
        
        self.visible = visible
    
