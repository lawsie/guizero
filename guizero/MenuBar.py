from tkinter import Menu
from .mixins import MasterMixin
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin, ReprMixin
from . import utilities as utils
from .App import App

class MenuBar(
    MasterMixin, 
    ScheduleMixin, 
    DestroyMixin, 
    FocusMixin, 
    ReprMixin):

    def __init__(self, master, toplevel, options):

        self._master = master

        if not isinstance(master, App):
            utils.error_format("The [MenuBar] must have the [App] object as its master")

        # Create a tk Menu object within this object
        self.tk = Menu(master.tk)

        # Keep track of submenu objects
        self._sub_menus = []

        # Description of this object (for friendly error messages)
        self.description = "[MenuBar] object "

        # Create all the top level menus
        for i in range(len(toplevel)):
            # Create this submenu
            new_menu = Menu(self.tk, tearoff=0)

            # Populate the drop down menu with the items/commands from the list
            for menu_item in options[i]:
                new_menu.add_command(label=menu_item[0], command=menu_item[1])

            # Append to the submenus list
            self._sub_menus.append(new_menu)

            # Add to the menu bar
            self.tk.add_cascade(label=toplevel[i], menu=self._sub_menus[i])

       	# Set this as the menu for the main App object
       	master.tk.config(menu=self.tk)
