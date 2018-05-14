from tkinter import Frame, StringVar
from . import utilities as utils
from .base import ContainerWidget
from .tkmixins import TextMixin
from .RadioButton import RadioButton
from .event import EventManager

class ButtonGroup(
    ContainerWidget, 
    TextMixin):

    def __init__(self, master, options, selected=None, horizontal=False, command=None, grid=None, align=None, args=None, visible=True, enabled=None):
        
        description = "[ButtonGroup] object with selected option \"" + str(selected) + "\""

        self._options = []   # List of RadioButton objects
        self._text_size = None
        self._font = None

        # Create a Tk frame object to contain the RadioButton objects
        tk = Frame(master.tk)

        # Set (using StringVar set() method) the selected option **number**
        self._selected = StringVar(master=tk.winfo_toplevel())

        # ButtonGroup uses "grid" internally to sort the RadioButtons
        super(ButtonGroup, self).__init__(master, tk, description, "grid", grid, align, visible, enabled)

        # Position the radio buttons in the Frame
        gridx = 0
        gridy = 0

        # Loop through the list given, creating a RadioButton object from each
        # Defaults to setting the hidden value to the same as the text

        for button in options:
            # If only a 1D list was provided, auto number the items FROM 1
            if not isinstance(button, list):
                button = [button, options.index(button)+1]

            # Which way the buttons go
            if horizontal:
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
                visible=visible, 
                enabled=enabled)

            # Add this radio button to the internal list
            self._options.append(rbutton)

            # Set the callback
            rbutton.tk.config(command=self._command_callback)

        # set the initial value
        if selected is None:
            self.value = self._options[0].value
        else:
            self.value = selected

        # Add a command if there was one
        self.update_command(command, args)

        # override the event manager and associate the button group and the
        # radio buttons to it
        option_tks = [option.tk for option in self._options]
        self._events = EventManager(self, self.tk, *option_tks)

    # PROPERTIES
    # -----------------------------------

    # Gets the selected value (1, 2, 3 etc.)
    @property
    def value(self):
        return (self._selected.get())

    # Sets which option is selected (if it doesn't exist, nothing is selected)
    @value.setter
    def value(self, value):
        self._selected.set(str(value))

    # Gets the text of the currently selected option
    @property
    def value_text(self):
        search = self._selected.get() # a string containing the selected option
        # This is a bit nasty - suggestions welcome
        for item in self._options:
            if item.value == search:
                return item.text
        return ""

    # Selects the option for the value_text provided
    @value_text.setter
    def value_text(self, value):
        for item in self._options:
            if item.text == value:
                self.value = item.value
    
    @property
    def width(self):
        if len(self._options) > 0:
            return self._options[0].width

    @width.setter
    def width(self, value):
        for item in self._options:
            item.width = value
        
    @property
    def height(self):
        if len(self._options) > 0:
            return self._options[0].height * len(self._options)

    @height.setter
    def height(self, value):
        if value % len(self._options) != 0:
            # if the height doesnt divide by the number of radio buttons give a warning
            button_height = int(round(value / len(self._options)))
            new_height = button_height * len(self._options)
            utils.error_format("ButtonGroup height '{}' doesn't divide by the number of buttons '{}' setting height to '{}'.".format(value, len(self._options), new_height))
        else:
            button_height = int(value / len(self._options))

        for item in self._options:
            item.height = button_height
        

    # METHODS
    # -----------------------------------

    # To help with debugging - return list of text/value pairs
    def get_group_as_list(self):
        return [[option.text, option.value] for option in self._options]

    def update_command(self, command, args=None):
        if command is None:
            self._command = lambda: None
        else:
            if args is None:
                self._command = command
            else:
                self._command = utils.with_args(command, *args)
    
    def _command_callback(self):
        self._command()

    # DEPRECATED METHODS
    # -----------------------------------
    # Get selected value (e.g. 1, 2, 3)
    def get(self):
        return self._selected.get()
        utils.deprecated("ButtonGroup get() is deprecated. Please use the value property instead.")

    # Set which option is selected
    def set(self, value):
        self._selected.set(str(value))
        utils.deprecated("ButtonGroup set() is deprecated. Please use the value property instead.")
    