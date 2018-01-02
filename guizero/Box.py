from tkinter import Frame
from .mixins import MasterMixin
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

class Box(
    MasterMixin,
    ScheduleMixin, 
    DestroyMixin, 
    FocusMixin, 
    DisplayMixin, 
    ReprMixin):

    def __init__(self, master, layout="auto", grid=None, align=None):

        self._master = master

    	# Description of this object (for friendly error messages)
        self.description = "[Box] object (may also contain other objects)"
        
        self.tk = Frame(master.tk)

        # Store this object's layout manager
        self._layout_manager = layout

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)
