try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
from .App import App
    
class MenuBar(Menu):

    def __init__(self, master, toplevel, options):

        if type(master) is not App:
            utils.error_format("The [MenuBar] must have the [App] object as its master")
        
        super().__init__(master)

        # Keep track of submenu objects
        self.sub_menus = []

        # Description of this object (for friendly error messages)
        self.description = "[MenuBar] object "

        # Create all the top level menus
       	for i in range(len(toplevel)):

            # Create this submenu
            new_menu = Menu(self, tearoff=0)

            # Populate the drop down menu with the items/commands from the list
            for menu_item in options[i]:
                new_menu.add_command(label=menu_item[0], command=menu_item[1])
            
            # Append to the submenus list
            self.sub_menus.append(new_menu)
            
            # Add to the menu bar
            self.add_cascade(label=toplevel[i], menu=self.sub_menus[i])

       	# Set this as the menu for the main App object
       	master.config(menu=self)

