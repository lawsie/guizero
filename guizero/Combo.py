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

    def __init__(
        self,
        master,
        options=[],
        selected=None,
        command=None,
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None):
        """
        Creates a Combo

        :param Container master:
            The Container (App, Box, etc) the Combo will belong too.

        :param List option:
            A list of strings to populate the Combo, defaults to an empty list.

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

        :param int width:
            The starting width of the widget. Defaults to `None` and will auto
            size.

        :param int height:
            The starting height of the widget. Defaults to `None` and will auto
            size.
        """

        # Maintain a list of options (as strings, to avoid problems comparing)
        self._options = [str(x) for x in options]

        description = "[Combo] object with options  " + str(self._options)

        # Store currently selected item
        self._selected = StringVar()

        # Create a tk OptionMenu object within this object
        if len(self._options) == 0:
            tk = OptionMenu(master.tk, self._selected, None, command=self._command_callback)
        else:
            tk = OptionMenu(master.tk, self._selected, *self._options, command=self._command_callback)

        # Create the combo menu object
        self._combo_menu = ComboMenu(tk["menu"])

        super(Combo, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        # Remove the thick highlight when the bg is a different color
        self._set_tk_config("highlightthickness", 0)

        # Set the selected item
        if selected is None:
            # set the first option
            self._set_option_by_index(0)
        else:
            self._set_option(selected)

        self._default = selected

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
        value = str(value)
        if not self._set_option(value):
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
        if self._default is None:
            if not self._set_option_by_index(0):
                utils.error_format(self.description + "\n" +
                "Unable to select default option as the Combo is empty")

        else:
            if not self._set_option(self._default):
                utils.error_format( self.description + "\n" +
                "Unable to select default option as it doesnt exist in the Combo")

    def append(self, option):
        """
        Appends a new `option` to the end of the Combo.

        :param string option:
            The option to append to the Combo.
        """
        self.insert(len(self._options), option)

    def insert(self, index, option):
        """
        Insert a new `option` in the Combo at `index`.

        :param int option:
            The index of where to insert the option.

        :param string option:
            The option to insert into to the Combo.
        """
        option = str(option)
        self._options.insert(index, option)
        # if this is the first option, set it.
        if len(self._options) == 1:
            self.value = option

        self._refresh_options()

    def remove(self, option):
        """
        Removes the first `option` from the Combo.

        Returns `True` if an item was removed.

        :param string option:
            The option to remove from the Combo.
        """
        if option in self._options:
            if len(self._options) == 1:
                # this is the last option in the list so clear it
                self.clear()
            else:
                self._options.remove(option)
                self._refresh_options()
                # have we just removed the selected option?
                # if so set it to the first option
                if option == self.value:
                    self._set_option(self._options[0])
            return True
        else:
            return False

    # Clear all options from the box
    def clear(self):
        """
        Clears all the options in a Combo
        """
        self._options = []
        self._combo_menu.tk.delete(0, END)
        self._selected.set("")

    def _refresh_options(self):
        # save which option was selected
        selected = self.value

        self._combo_menu.tk.delete(0, END)

        # Re-add all options
        # This uses an internal tk method _setit which is a bit naughty
        for item in self._options:
            self._combo_menu.tk.add_command(label=item, command=_setit(self._selected, item, self._command_callback))

        self.description = "[Combo] object with options  " + str(self._options)

        # set the option which was previously selected
        self._set_option(selected)

    def _set_option(self, value):
        """
        Sets a single option in the Combo, returning True if it was able too.
        """
        if len(self._options) > 0:
            if value in self._options:
                self._selected.set(value)
                return True
            else:
                return False
        else:
            return False

    def _set_option_by_index(self, index):
        """
        Sets a single option in the Combo by its index, returning True if it was able too.
        """
        if index < len(self._options):
            self._selected.set(self._options[index])
            return True
        else:
            return False

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
            The callback function to call, it can accept 0 or 1 parameters.

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

        self.append(option)
        self.value = option

        utils.deprecated("Combo add_option() is deprecated. Please use append() instead.")
