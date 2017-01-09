try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
from .guizerocontroleventcore import GuiZeroControlEventCore


class Combo(OptionMenu, GuiZeroControlEventCore):

    def __init__(self, master, options, selected=None, command=None, grid=None, align=None):

        # If a command is specified, the function MUST take one positional argument
        # as it will be auto-given the current value of the Combo
        # You can only specify a command for a OptionMenu at init

        # Description of this object (for friendly error messages)
        self.description = "[Combo] object with default selection \"" + str(selected) + "\""    

        # Maintain a list of options (as strings, to avoid problems comparing)
        self.options = [str(x) for x in options]           

        # Store currently selected item
        self.selected = StringVar()

        # Set the first item in the list as default
        if selected is None and len(options) > 0:                     
            self.selected.set( str(options[0]) )
            
        else:
            self.selected.set( str(selected) )

        # Instantiate the object
        try:
            super().__init__(master, self.selected, *options, command=command)
        except AttributeError:
                utils.error_format(self.description + "\n" +
                "No options for [Combo] were provided")
               
       
        # Pack or grid self 
        utils.auto_pack(self, master, grid, align)

    # Returns currently selected option 
    def get(self):
        return self.selected.get()

    # Sets currently selected option (if it exists in the list)
    def set(self, text):
        if text in self.options:
            self.selected.set( str(text) )
        else:
            utils.error_format("Tried to set [Combo] option to a value not in the list" )

    # Resets the combo box to the first option being selected
    def select_default(self):
        try:
            self.selected.set( self.options[0] )
        except IndexError:
            utils.error_format( self.description + "\n" + 
            "There are no options in the [Combo] box to be selected")

    # Add an option to the combo
    def add_option(self, option):
        self.options.append( str(option) )
        self.children["menu"].add_command(label=option, command="") # Don't do any command
        self.selected.set( str(option) )        

    # Clear all options from a combo
    def clear(self):
        self.options = []
        self.children["menu"].delete(0, END)
        self.selected.set("")