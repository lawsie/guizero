try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
from .Box import Box
from .RadioButton import RadioButton

    
class ButtonGroup(Box):

    def __init__(self, master, options, selected, command=None, grid=None, align=None):  
              
        self.selected = StringVar()
        self.selected.set(str(selected))    # Should be the hidden value not the text
        self.description = "[ButtonGroup] object with selected option \"" + self.selected.get() + "\""
        self.options = []   # List of RadioButton objects

        # Init the box
        try:    
            super().__init__(master, manager="auto")
        except AttributeError:
            utils.error_format( self.description + "\n" + 
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")

        for button in options:
            rbutton = RadioButton(self, text=button[0], value=button[1], variable=self.selected)
            print (rbutton.description)

            # Add a command if there was one
            if command is not None:
                rbutton.config(command=command)

            # Track this object
            self.options.append(rbutton)

            # Pack this object
            utils.auto_pack(rbutton, self, grid, align)
        
    # Get selected value
    def get(self):
        return self.selected.get()

    # Set selected value
    def set(self, value):
        self.selected.set(str(value))

    # To help with debugging - return list of text/value pairs
    def get_group_as_list(self):
        list_of_options = []
        for option in self.options:
            list_of_options.append([option.text, option.value])
        return list_of_options
        
        

        

   
