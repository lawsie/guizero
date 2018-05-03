from tkinter import Listbox, END, BROWSE, EXTENDED
from . import utilities as utils
from .base import TextWidget

class ListBox(TextWidget):

    def __init__(self, master, items=None, selected=None, command=None, grid=None, align=None, visible=True, enabled=None, multiselect=False):
        """
        Creates a ListBox
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

        # Select the selected items
        if selected is not None:
            self.value = selected

        # The command associated with this combo
        #self.update_command(command)

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
        pass

    def append(self, item):
        """
        Appends a new `item` to the end of the ListBox.
        """
        pass

    def remove(self, item):
        """
        Removes an `item` from the ListBox.
        """
        pass

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