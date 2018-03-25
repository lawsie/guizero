from tkinter import OptionMenu, StringVar, END, _setit
from .mixins import WidgetMixin
from .tkmixins import (
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    TextMixin, 
    ColorMixin, 
    SizeMixin,
    ReprMixin)
from . import utilities as utils

class Combo(
    WidgetMixin,
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    TextMixin,
    ColorMixin,
    SizeMixin, 
    ReprMixin):

    def __init__(self, master, options, selected=None, command=None, grid=None, align=None, visible=True):

        self._master = master
        self._grid = grid
        self._align = align

        # Maintain a list of options (as strings, to avoid problems comparing)
        self._options = [str(x) for x in options]

        # Description of this object (for friendly error messages)
        self.description = "[Combo] object with options  " + str(self._options)

        # Store currently selected item
        self._selected = StringVar()

        # Set the first item in the list as default
        if selected is None and len(options) > 0:
            self._selected.set( str(options[0]) )
            self._default = str(options[0])

        else:
            self._selected.set( str(selected) )
            self._default = str(selected)

        # Create a tk OptionMenu object within this object
        self.tk = OptionMenu(master.tk, self._selected, *self._options, command=self._command_callback)

        # The command associated with this combo
        self.update_command(command)

        self.visible = visible

    # PROPERTIES
    # ----------------------------------
    # The selected text value
    @property
    def value(self):
        return self._selected.get()

    @value.setter
    def value(self, value):
        if value in self._options:
            self._selected.set( str(value) )
        else:
            utils.error_format("Tried to set " + self.description + " to option \"" + str(value) + "\", which does not exist" )

    # METHODS
    # -------------------------------------------

    # Resets the combo box to the original "selected" value from the constructor
    # (or the first value if no selected value was specified)
    def select_default(self):
        try:
            self._selected.set( self._default )
        except IndexError:
            utils.error_format( self.description + "\n" +
            "There are no options in the [Combo] box to be selected")

    # Add an option to the combo
    def add_option(self, option):

        # Add to the internal list
        self._options.append( str(option) )
        # self.children["menu"].add_command(label=option, command=self._command)

        # Delete all options
        menu = self.tk.children["menu"]
        menu.delete(0, 'end')

        # Re-add all options
        # This uses an internal tk method _setit which is a bit naughty
        for item in self._options:
            menu.add_command(label=item, command=_setit(self._selected, item, self._command_callback))

        self.description = "[Combo] object with options  " + str(self._options)

        # Set the new option as selected
        self._selected.set( str(option) )


    # Clear all options from the box
    def clear(self):
        self._options = []
        self.tk.children["menu"].delete(0, END)
        self._selected.set("")

    def _command_callback(self, value):
        if self._command:
            args_expected = utils.no_args_expected(self._command)
            if args_expected == 0:
                self._command()
            elif args_expected == 1:
                self._command(value)
            else:
                utils.error_format("Combo command function must accept either 0 or 1 arguments.\nThe current command has {} arguments.".format(args_expected))

    def update_command(self, command):
        if command is None:
            self._command = lambda: None
        else:
            self._command = command
            
    # DEPRECATED METHODS
    # --------------------------------------------

    # Returns currently selected option
    def get(self):
        return self._selected.get()
        utils.deprecated("Combo get() is deprecated. Please use the value property instead.")

    # Sets currently selected option (if it exists in the list)
    def set(self, text):
        if text in self._options:
            self._selected.set( str(text) )
        else:
            utils.error_format("Tried to set " + self.description + " to option \"" + str(text) + "\", which does not exist" )
        utils.deprecated("Combo set() is deprecated. Please use the value property instead.")
