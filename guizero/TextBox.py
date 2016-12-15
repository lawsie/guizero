try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
    
class TextBox(Entry):

    def __init__(self, master, text="", width=10, grid=None, align=None):
        
        # Description of this object (for friendly error messages)
        self.description = "[TextBox] object with text \"" + str(text) + "\""

        # Attempt to instantiate the object and raise an error if failed
        try:
            super().__init__(master)
        except AttributeError:
            utils.error_format( self.description + "\n" + 
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")         

        # Set up controlling string variable
        self.string_var = StringVar()
        self.string_var.set( str(text) )

        # Initial config on setup  
        self.config(textvariable=self.string_var, width=width)
        
        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)
            
    # Clear text box 
    def clear(self):
        self.delete(0, END)
    
    # Returns the text
    def get(self):
        return self.string_var.get()

    # Sets the StringVar
    def set(self, text):
        self.string_var.set( str(text) )

    # Append text
    def append(self, text):
        self.string_var.set( self.string_var.get() + str(text) )
        
