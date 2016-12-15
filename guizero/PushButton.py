try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
    
class PushButton(Button):

    def __init__(self, master, command, args=None, text="Button", icon=None, pady=10, padx=10, grid=None, align=None):

        # Description of this object (for friendly error messages)
        self.description = "[PushButton] object with text \"" + str(text) + "\""

        # Attempt to instantiate the object and raise an error if failed
        try:
            super().__init__(master)
        except AttributeError:
            utils.error_format( self.description + "\n" + 
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")

        # If the args string was not blank, convert to allow args
        if args is not None:            
            command = utils.with_args(command, *args)


        # Try to instantiate a picture
        if icon is not None:
            try:
                img = PhotoImage(file=icon)  
                self.icon = img
                self.config(image=img, command=command, pady=pady, padx=padx)
            except:
                utils.error_format("Image import error - image must be a gif, check correct path")

        else:
            # Initial config on setup 
            self.config(text=text, command=command, pady=pady, padx=padx)
            
        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)


    # Change command
    def change_command(self, newcommand):
        self.config(command=newcommand)

    # Change text
    def set_text(self, text):
        self.config(text=text)

    # Change padding
    def padding(self, padx, pady):
        self.config(padx=padx, pady=pady)
