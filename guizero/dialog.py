from tkinter import messagebox, filedialog
from tkinter.simpledialog import askstring
from . import utilities as utils
import os.path

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

def select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False, master=None):
    """
    Display a box to select a file to open or save.

    If Open or Save is pressed the filename path is returned.

    If Cancel is pressed `None` is returned.

    :param string title:
        The title to be displayed on the box. Defaults to 'Select file'.
    :param string folder:
        The initial folder to open. Defaults to '.'.
    :param list filetypes:
        A list of file descriptions and wildcards of file types to display. 
        Provide as a list of lists e.g. ::
            filetypes=[["Text documents", "*.txt"], ["CSV files", "*.csv"]]
    :param boolean save:
        The default value for the response box.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        The path of filename selected or `None`.
    """
    if not os.path.isdir(folder):
        utils.error_format("The folder '{}' specified for select_file does not exist.".format(folder))
        folder = "."
    
    if save:
        return filedialog.asksaveasfilename(
            title=title, 
            filetypes=filetypes, 
            initialdir=folder, 
            parent=None if master is None else master.tk)
    else:
        return filedialog.askopenfilename(
            title=title, 
            filetypes=filetypes, 
            initialdir=folder, 
            parent=None if master is None else master.tk)

def select_folder(title="Select folder", folder=".", master=None):
    """
    Display a box to select a folder.

    If a folder is selected the folder path is returned, otherwise `None` is returned.

    :param string title:
        The title to be displayed on the box. Defaults to 'Select file'.
    :param string folder:
        The initial folder to open. Defaults to '.'.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        The path of folder selected or `None`.
    """
    if not os.path.isdir(folder):
        utils.error_format("The folder '{}' specified for select_folder does not exist.".format(folder))
        folder = "."
    
    return filedialog.askdirectory(title=title, initialdir=folder, parent=None if master is None else master.tk)