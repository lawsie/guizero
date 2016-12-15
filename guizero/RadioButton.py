try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils

# Only to be used as part of button group
# unless you want to externally create a controlling variable StringVar()
# Does NOT create an internal StringVar() as this is handled by the ButtonGroup class
class RadioButton(Radiobutton):

    def __init__(self, master, text, value, variable, command=None, grid=None, align=None):  
      
        self.description = "[RadioButton] object with option=\"" + str(text) + "\" value=\"" + str(value) + "\""
        self.text = text
        self.value = value        
        
        try:
            super().__init__(master, text=text, value=value, variable=variable)
            utils.auto_pack(self, master, grid, align)
        

        except AttributeError:
            utils.error_format( self.description + "\n" + 
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")

        

        

   
