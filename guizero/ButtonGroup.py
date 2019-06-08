from tkinter import Frame, StringVar
from . import utilities as utils
from .base import ContainerTextWidget
from .tkmixins import TextMixin
from .RadioButton import RadioButton
from .event import EventManager

class ButtonGroup(ContainerTextWidget):

    def __init__(
        self,
        master,
        options=[],
        selected=None,
        horizontal=False,
        command=None,
        grid=None,
        align=None,
        args=None,
        visible=True,
        enabled=None,
        width=None,
        height=None):
        """
        Creates a ButtonGroup

        :param Container master:
            The Container (App, Box, etc) the ButtonGroup will belong too.

        :param List option:
            A list of options to append to the ButtonGroup. If a 2D list is
            specified, the first element is the text, the second is the value,
            defaults to an empty list.

        :param string selected:
            The item in the ButtonGroup to select, defaults to `None`.

        :param string horizontal:
            If the ButtonGroup is to be displayed horizontally, defaults to
            `True`.

        :param callback command:
            The callback function to call when the ButtonGroup changes,
            defaults to `None`.

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to None.

        :param callback args:
            A list of arguments to pass to the widgets `command`, defaults to
            `None`.

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

        description = "[ButtonGroup] object with selected option \"" + str(selected) + "\""

        self._rbuttons = []   # List of RadioButton objects
        self._text_size = None
        self._font = None
        self._horizontal = horizontal

        # Create a Tk frame object to contain the RadioButton objects
        tk = Frame(master.tk)

        # Set (using StringVar set() method) the selected option **number**
        self._selected = StringVar(master=tk.winfo_toplevel())

        # ButtonGroup uses "grid" internally to sort the RadioButtons
        super(ButtonGroup, self).__init__(master, tk, description, "grid", grid, align, visible, enabled, width, height)

        # Loop through the list given and setup the options
        self._options = []
        for option in options:
            self._options.append(self._parse_option(option))

        self._refresh_options()

        # set the initial value
        if selected is None and len(self._options) > 0:
            self.value = self._options[0][1]
        else:
            self.value = selected

        # Add a command if there was one
        self.update_command(command, args)

        # override the event manager and associate the button group and the
        # radio buttons to it
        option_tks = [option.tk for option in self._rbuttons]
        self._events = EventManager(self, self.tk, *option_tks)

        # now the ButtonGroup is populate it, size it
        self.resize(width, height)

    def _parse_option(self, option):
        # If only a 1D  was provided, use the text value as a key
        if not isinstance(option, list):
            return [option, option]
        else:
            return [option[0], option[1]]

    def _refresh_options(self):
        # destroy any existing radio buttons
        for button in self._rbuttons:
            button.destroy()
        self._rbuttons = []

        gridx = 0
        gridy = 0

        for button in self._options:
            # Which way the buttons go
            if self._horizontal:
                gridx += 1
            else:
                gridy += 1

            # Create a radio button object
            rbutton = RadioButton(
                self,
                text=str(button[0]),
                value=str(button[1]),
                variable=self._selected,
                grid=[gridx, gridy],
                align="left",
                visible=self.visible,
                enabled=self.enabled)

            # Add this radio button to the internal list
            self._rbuttons.append(rbutton)

            # Set the callback
            rbutton.tk.config(command=self._command_callback)

    # PROPERTIES
    # -----------------------------------

    # Gets the selected value (1, 2, 3 etc.)
    @property
    def value(self):
        """
        Sets or returns the option selected in a ButtonGroup.
        """
        return (self._selected.get())

    # Sets which option is selected (if it doesn't exist, nothing is selected)
    @value.setter
    def value(self, value):
        self._selected.set(str(value))

    # Gets the text of the currently selected option
    @property
    def value_text(self):
        """
        Sets or returns the option selected in a ButtonGroup by its text value.
        """
        search = self._selected.get() # a string containing the selected option
        # This is a bit nasty - suggestions welcome
        for item in self._rbuttons:
            if item.value == search:
                return item.text
        return ""

    # Selects the option for the value_text provided
    @value_text.setter
    def value_text(self, value):
        for item in self._rbuttons:
            if item.text == value:
                self.value = item.value

    def resize(self, width, height):
        """
        Resizes the widget.

        :param int width:
            The width of the widget.

        :param int height:
            The height of the widget.
        """
        self._width = width
        self._height = height

        # update radio buttons width
        for item in self._rbuttons:
            item.width = width

        # update radio buttons height
        if len(self._rbuttons) > 0:
            # work out the height of a button
            button_height = height
            
            if isinstance(height, int):
                if height % len(self._rbuttons) != 0:
                    # if the height doesnt divide by the number of radio buttons give a warning
                    button_height = int(round(height / len(self._rbuttons)))
                    new_height = button_height * len(self._rbuttons)
                    utils.error_format("ButtonGroup height '{}' doesn't divide by the number of buttons '{}' setting height to '{}'.".format(height, len(self._rbuttons), new_height))
                else:
                    button_height = int(height / len(self._rbuttons))
            
            for item in self._rbuttons:
                item.height = button_height

        super(ButtonGroup, self).resize(width, height)

    @property
    def options(self):
        """
        Returns a list of options in the ButtonGroup
        """
        return self._options

    # METHODS
    # -----------------------------------

    def append(self, option):
        """
        Appends a new `option` to the end of the ButtonGroup.

        :param string/List option:
            The option to append to the ButtonGroup. If a 2D list is specified,
            the first element is the text, the second is the value.
        """
        self._options.append(self._parse_option(option))
        self._refresh_options()
        self.resize(self._width, self._height)

    def insert(self, index, option):
        """
        Insert a new `option` in the ButtonGroup at `index`.

        :param int option:
            The index of where to insert the option.

        :param string/List option:
            The option to append to the ButtonGroup. If a 2D list is specified,
            the first element is the text, the second is the value.
        """
        self._options.insert(index, self._parse_option(option))
        self._refresh_options()
        self.resize(self._width, self._height)

    def remove(self, option):
        """
        Removes the first `option` from the ButtonGroup.

        Returns `True` if an item was removed.

        :param string option:
            The value of the option to remove from the ButtonGroup.
        """
        for existing_option in self._options:
            if existing_option[1] == option:
                self._options.remove(existing_option)
                self._refresh_options()
                return True
        return False

    def clear(self):
        """
        Clears all the options in a Combo
        """
        self._options = []
        self._refresh_options()
        self.value = ""

    # To help with debugging - return list of text/value pairs
    def get_group_as_list(self):
        return [[option.text, option.value] for option in self._rbuttons]

    def update_command(self, command, args=None):
        """
        Updates the callback command which is called when the ButtonGroup
        changes.

        Setting to `None` stops the callback.

        :param callback command:
            The callback function to call.

        :param callback args:
            A list of arguments to pass to the widgets `command`, defaults to
            `None`.
        """
        if command is None:
            self._command = lambda: None
        else:
            if args is None:
                self._command = command
            else:
                self._command = utils.with_args(command, *args)

    def _command_callback(self):
        self._command()

 