try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
    
class CheckBox(Checkbutton):

    def __init__(self, master, text, command=None, grid=None, align=None):  
      
        self.text = str(text)
        self.description = "[CheckBox] object with text " + self.text
        self.value = IntVar()

        try:
            super().__init__(master, text=self.text, variable=self.value)
        except AttributeError:
            utils.error_format( self.description + "\n" + 
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")

        try:
            utils.auto_pack(self, master, grid, align)
       	except AttributeError:
            utils.error_format( self.description + "\n" +
            "Could not add to interface - check first argument is [App] or [Box]")

        # Add a command if there was one
        if command is not None:
            self.config(command=command)

    # Return text associated with this checkbox
    def get_text(self):
        return self.text

    # Return the value (1 or 0) of the box
    def get_value(self):
        return self.value.get()

    # Already a built in toggle() function

    # Change text
    def change_text(self, newtext):
        self.text = str(newtext)
        self.config(text=self.text)
        self.description = "[CheckBox] object with text " + str(self.text) 