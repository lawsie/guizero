try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
    
class Box(Frame):

    def __init__(self, master, layout="auto", grid=None, align=None):    	

    	# Description of this object (for friendly error messages)
        self.description = "[Box] object (may also contain other objects)"

        try:
            super().__init__(master)
        except AttributeError:
            utils.error_format("Failed to initialise [Box] object")

        # Store this object's layout manager
        self.layout_manager = layout
       
        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)
