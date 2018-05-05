from tkinter import Listbox, END, BROWSE, EXTENDED
from . import utilities as utils
from .base import TextWidget

class ListBox(TextWidget):

    def __init__(self, master, items=None, selected=None, command=None, grid=None, align=None, visible=True, enabled=None, multiselect=False):
        """
        Creates a ListBox

        :param Container master:
            The Container (App, Box, etc) the ListBox will belong too.

        :param List items:
            A list of strings to populate the ListBox, defaults to `None`.

        :param string selected:
            The item in the ListBox to select, defaults to `None`. 

        :param callback command:
            The callback function to call when the ListBox changes,
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

        :param bool multiselect:
            If ListBox should allow multiple items to be selected, defaults
            to `False`.
        """

        description = "[ListBox] object"
        self._multiselect = multiselect
        
        # Create a tk OptionMenu object within this object
        mode = EXTENDED if multiselect else BROWSE
        # exportselection=0 allows you to select from more than 1 Listbox
        tk = Listbox(master.tk, selectmode=mode, exportselection=0)

        # Add the items
        if items is not None:
            for item in items:
                tk.insert(END, item)

        super(ListBox, self).__init__(master, tk, description, grid, align, visible, enabled)

        self.events.set_event("<ListBox.ListboxSelect>", "<<ListboxSelect>>", self._command_callback)

        # Select the selected items
        if selected is not None:
            self.value = selected

        # The command associated with this combo
        self.update_command(command)

    @property
    def value(self):
        """
        Sets or returns the items selected in a ListBox

        `None` if 0 items are selected.

        If the ListBox is a `multiselect`, `value` is a tuple of items selected, 
        if not `value` is a single integer.
        """
        if len(self.tk.curselection()) > 0:
            if self._multiselect:
                return [self.tk.get(selected) for selected in self.tk.curselection()]
            else:
                return self.tk.get(self.tk.curselection()[0])
        else:
            return None

    @value.setter
    def value(self, value):
        self.tk.selection_clear(0, self.tk.size() - 1)

        # go through all the items and select those in `value`
        for index in range(self.tk.size()):
            if self._multiselect:
                for item in value:
                    if self.tk.get(index) == item:
                        self.tk.select_set(index)
            else:
                if self.tk.get(index) == value:
                    self.tk.select_set(index)

    def insert(self, index, item):
        """
        Insert a new `item` at `index`
        """
        self.tk.insert(index, item)

    def append(self, item):
        """
        Appends a new `item` to the end of the ListBox.
        """
        self.tk.insert(END, item)

    def remove(self, item):
        """
        Removes the first `item` from the ListBox.

        Returns `True` if an item was removed.
        """
        for index in range(len(self.items)):
            if item == self.items[index]:
                self.tk.delete(index)
                return True

        return False

    def clear(self):
        """
        Clears all the items in a ListBox
        """
        self.tk.delete(0, END)

    @property
    def items(self):
        """
        Returns a list of items in the ListBox 
        """
        return [self.tk.get(index) for index in range(self.tk.size())]

    def _command_callback(self):
        if self._command:
            args_expected = utils.no_args_expected(self._command)
            if args_expected == 0:
                self._command()
            elif args_expected == 1:
                self._command(self.value)
            else:
                utils.error_format("Combo command function must accept either 0 or 1 arguments.\nThe current command has {} arguments.".format(args_expected))

    def update_command(self, command):
        """
        Updates the callback command which is called when the ListBox
        changes. 
        
        Setting to `None` stops the callback.

        :param callback command:
            The callback function to call, it can ccept 0 or 1 parameters.

            If it accepts 1 parameter the `value` of the ListBox will be 
            passed.
        """
        if command is None:
            self._command = lambda: None
        else:
            self._command = command