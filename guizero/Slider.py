try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
    
class Slider(Scale):

    def __init__(self, master, start=0, end=100, orient=HORIZONTAL, command=None, grid=None, align=None):  

        # If you specify a command to the slider, it must take one argument as it will be given
        # the slider's current value

        # Description of this object (for friendly error messages)
        self.description = "[Slider] object from " + str(start) + " to " + str(end)    

        try:
            super().__init__(master, from_=start, to=end, orient=orient, command=command)
        except AttributeError:
            utils.error_format( self.description + "\n" + 
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")

        try:
            utils.auto_pack(self, master, grid, align)
       	except AttributeError:
            utils.error_format( self.description + "\n" +
            "Could not add to interface - check first argument is [App] or [Box]")


    # Calls the given function when the slider value is changed
    def add_command(self, command):
        self.config(command=command)

    # Gets the current slider value
    #def get(self):
    #    return self.get()