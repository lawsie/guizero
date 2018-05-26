from tkinter import OptionMenu, StringVar, END, _setit
from . import utilities as utils
from .base import Base, TextWidget
from .tkmixins import ColorMixin, TextMixin


class ComboMenu(Base, ColorMixin, TextMixin):

    def __init__(self, tk):
        """
        Internal class for managing the little menu which pops up when the 
        combo box is opened
        """
        super(ComboMenu, self).__init__(tk)


class Combo(TextWidget):

    def __init__(self, master, options, selected=None, command=None, grid=None, align=None, visible=True, enabled=None):
        """
        Creates a Combo

        :param Container master:
            The Container (App, Box, etc) the Combo will belong too.

        :param List option:
            A list of strings to populate the Combo.

        :param string selected:
            The item in the Combo to select, defaults to `None`. 

        :param callback command:
            The callback function to call when the Combo changes,
            defaults to `None`.

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to None.

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        :param bool enabled:
            If the widget should be enabled, defaults to `None`. If `None`
            the value is inherited from the master.
        """

        # Maintain a list of options (as strings, to avoid problems comparing)
        self._options = [str(x) for x in options]

        description = "[Combo] object with options  " + str(self._options)

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
        tk = OptionMenu(master.tk, self._selected, *self._options, command=self._command_callback)

        # Remove the thick highlight when the bg is a different color
        tk["highlightthickness"] = 0

        # Create the combo menu object
        self._combo_menu = ComboMenu(tk["menu"])

        super(Combo, self).__init__(master, tk, description, grid, align, visible, enabled)

        # The command associated with this combo
        self.update_command(command)

    # PROPERTIES
    # ----------------------------------
    # The selected text value
    @property
    def value(self):
        """
        Sets or returns the option selected in a Combo.
        """
        return self._selected.get()

    @value.setter
    def value(self, value):
        if value in self._options:
            self._selected.set( str(value) )
        else:
            utils.error_format("Tried to set " + self.description + " to option \"" + str(value) + "\", which does not exist" )

    @property
    def bg(self):
        """
        Sets or returns the background color of the widget.
        """
        return super(Combo, self.__class__).bg.fget(self)
        
    @bg.setter
    def bg(self, value):
        super(Combo, self.__class__).bg.fset(self, value)
        self._combo_menu.bg = value

    @property
    def text_color(self):
        """
        Sets or returns the text color used by the widget.
        """
        return super(Combo, self.__class__).text_color.fget(self)
        
    @text_color.setter
    def text_color(self, value):
        super(Combo, self.__class__).text_color.fset(self, value)
        self._combo_menu.text_color = value

    @property
    def text_size(self):
        """
        Sets or returns the text size used by the widget.
        """
        return super(Combo, self.__class__).text_size.fget(self)
        
    @text_size.setter
    def text_size(self, value):
        super(Combo, self.__class__).text_size.fset(self, value)
        self._combo_menu.text_size = value
    
    @property
    def font(self):
        """
        Sets or returns the font used by the widget.
        """
        return super(Combo, self.__class__).font.fget(self)
        
    @font.setter
    def font(self, value):
        super(Combo, self.__class__).font.fset(self, value)
        self._combo_menu.font = value

    @property
    def options(self):
        """
        Returns a list of options in the Combo 
        """
        return self._options

    # METHODS
    # -------------------------------------------

    # Resets the combo box to the original "selected" value from the constructor
    # (or the first value if no selected value was specified)
    def select_default(self):
        """
        Resets the combo box to the original "selected" value from the 
        constructor (or the first value if no selected value was specified).
        """
        try:
            self._selected.set( self._default )
        except IndexError:
            utils.error_format( self.description + "\n" +
            "There are no options in the [Combo] box to be selected")

    def append(self, option):
        """
        Appends a new `option` to the end of the Combo.

        :param string option:
            The option to append to the Combo. 
        """
        self._options.append(str(option))
        self._refresh_options()

    def insert(self, index, option):
        """
        Insert a new `option` in the Combo at `index`.

        :param int option:
            The index of where to insert the option. 

        :param string option:
            The option to insert into to the Combo. 
        """
        self._options.insert(index, str(option))
        self._refresh_options()

    def remove(self, option):
        """
        Removes the first `option` from the Combo.

        Returns `True` if an item was removed.

        :param string option:
            The option to remove from the Combo. 
        """
        if option in self._options:
            self._options.remove(option)
            self._refresh_options()
            return True
        else:
            return False

    def _refresh_options(self):
        # save which option was selected
        selected = self.value

        menu = self.tk.children["menu"]
        menu.delete(0, END)

        # Re-add all options
        # This uses an internal tk method _setit which is a bit naughty
        for item in self._options:
            menu.add_command(label=item, command=_setit(self._selected, item, self._command_callback))

        self.description = "[Combo] object with options  " + str(self._options)

        # set the option
        self._selected.set(selected)

    # Clear all options from the box
    def clear(self):
        """
        Clears all the options in a Combo
        """
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
        """
        Updates the callback command which is called when the Combo
        changes. 
        
        Setting to `None` stops the callback.

        :param callback command:
            The callback function to call, it can ccept 0 or 1 parameters.

            If it accepts 1 parameter the `value` of the Combo will be 
            passed.
        """
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

        utils.deprecated("Combo add_option() is deprecated. Please use append() or insert() instead.")
