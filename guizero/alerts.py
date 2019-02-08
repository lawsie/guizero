from tkinter import messagebox
# Generates alerts


def warn(title, text):
    """
    Display a warning message box.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :return:
        None.
    """
    messagebox.showwarning(title, text)


def info(title, text):
    """
    Display an info message box.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :return:
        None.
    """
    messagebox.showinfo(title, text)


def error(title, text):
    """
    Display an error message box.

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :return:
        None.
    """
    messagebox.showerror(title, text)


def yesno(title, text):
    """
    Alert type yes or no

    :param string title:
        The title to be displayed on the box.
    :param string text:
        The text to be displayed on the box.
    :return:
        True if 'yes', False if 'no'
    """
    return messagebox.askyesno(title, text)
