from tkinter import messagebox
from tkinter.simpledialog import askstring

def warn(title, text, master=None):
    """
    Display a warning message box.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        None.
    """
    messagebox.showwarning(title, text, parent=None if master is None else master.tk)

def info(title, text, master=None):
    """
    Display an info message box.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        None.
    """
    messagebox.showinfo(title, text, parent=None if master is None else master.tk)

def error(title, text, master=None):
    """
    Display an error message box.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        None.
    """
    messagebox.showerror(title, text, parent=None if master is None else master.tk)

def yesno(title, text, master=None):
    """
    Alert type yes or no

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        True if 'yes', False if 'no'
    """
    return messagebox.askyesno(title, text, parent=None if master is None else master.tk)

def question(title, question, initial_value=None, master=None):
    """
    Display a question box which can accept a text response.

    If Ok is pressed the value entered into the box is returned.

    If Cancel is pressed `None` is returned.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :param string initial_value:
        The default value for the response box.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        The value entered or `None`.
    """
    return askstring(title, question, initialvalue=initial_value, parent=None if master is None else master.tk)
