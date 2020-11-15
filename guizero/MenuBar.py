from tkinter import Menu
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin
from . import utilities as utils
from .base import Component
from .App import App
from .Window import Window

class MenuBar(Component):

    def __init__(self, master, menu=None, toplevel=None, options=None):

        """
        Creates a MenuBar

        :param Container master:
            The Container (App, Box, etc) the MenuBar will belong too.

        :param Dictionary menu:
            A 2D dictionary of:
                - submenus,
                - with each submenu being a dict of options
                - and each option being a command 

            e.g ::

                menu={
                    "File": {
                        "File option 1": file_function,
                        "File option 2": file_function
                    },
                    "Edit": {
                        "Edit option 1": edit_function,
                        "Edit option 2": edit_function
                    }
                }

        :param List toplevel:
            DEPRECATED: Use menu instead.
            A list of strings to populate the top level menu options.

        :param List options:
            DEPRECATED: Use menu instead.
            A 3D list of:
                - submenus,
                - with each submenu being a list of options
                - and each option being a text/command pair 

            e.g ::

                options=[
                        [ ["File option 1", file_function], ["File option 2", file_function] ],
                        [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
                    ]
        """

        if not isinstance(master, (App, Window)):
            utils.error_format("The [MenuBar] must have an [App] or [Window] object as its master")

        description = "[MenuBar] object "

        # Create a tk Menu object within this object
        tk = Menu(master.tk)

        super(MenuBar, self).__init__(master, tk, description, False)

        # Keep track of submenu objects
        self._sub_menus = []

        # If menu is a list, then legacy parameters have been used as none-kwargs.
        if isinstance(menu, (list, tuple)):
            # Just double-check as options may have been a kwarg even if toplevel wasn't.
            if options is None:
                options = toplevel

            toplevel = menu
            menu = None

        # Legacy support, this is exactly the same as the old code.
        if menu is None:
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

        # Create all the top level menus
        else:
            for toplevel_label in menu:
                # Create this submenu
                new_menu = Menu(self.tk, tearoff=0)

                # Populate the drop down menu with the items/commands from the list
                for item_label in menu[toplevel_label]:
                    new_menu.add_command(label=item_label, command=menu[toplevel_label][item_label])

                # Append to the submenus list
                self._sub_menus.append(new_menu)

                # Add to the menu bar
                self.tk.add_cascade(label=toplevel_label, menu=self._sub_menus[-1])

       	# Set this as the menu for the master object
       	master.tk.config(menu=self.tk)

    @property
    def bg(self):
        """
        Sets the background color of the widget.

        Note - some operating systems dont allow the background color of the 
        menu bar to be changed. 
        """
        return super(MenuBar, self.__class__).bg.fget(self)

    # Set the background colour
    @bg.setter
    def bg(self, color):
        super(MenuBar, self.__class__).bg.fset(self, color)
        for sub_menu in self._sub_menus:
            sub_menu["bg"] = utils.convert_color(color)
    