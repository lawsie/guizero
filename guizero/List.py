try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
    
class List(Listbox):

    def __init__(self, master, items, selected=None, grid=None, align=None):

        # Description of this object (for friendly error messages)
        self.description = "[List] object with default selection \"" + str(selected) + "\""    

        # Maintain a list of items (as strings, to avoid problems comparing)
        self.items = [str(x) for x in items]

        # Instantiate the object
        try:
            super().__init__(master, command=command)
        except AttributeError:
                utils.error_format(self.description + "\n" +
                "No options for [List] were provided")

        #Place items in the list
        for item in items:
            self.insert(END, item)

        # Select an item if specified
        ## TODO make the selected item select.
        if selected is not None and len(items) > 0:
            try:
                index = self.items.index(selected)
                self.select_set(index)
            except ValueError:
                utils.error_format(self.description + "\n" +
                                   "Selected item not found in [List]")
        
        #else:
        #    self.selected.set( str(selected) )
       
        # Pack or grid self 
        utils.auto_pack(self, master, grid, align)

    # Add an option to the list
    def add_item(self, item):
        self.items.append(item)
        self.insert(END, item)#

    # Clear all options from list
    def clear(self):
        self.items = []
        self.delete(0,END)

    # Returns currently selected option 
    def get_item(self):
        #return self.get(SEL)
        return self.get(self.curselection()[0])

    # Sets currently selected option (if it exists in the list)
    def set(self, text):
        if text in self.items:
            index = self.items.index(selected)
            self.select_set(index)
        else:
            utils.error_format("Tried to set selected [List] item to a value not in the list" )



       
