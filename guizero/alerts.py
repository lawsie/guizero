from tkinter import messagebox
# Generates alerts


def warn(title, text):
    """
    Alert type warning.

    :param string title:
        String with the title to be apply.
    :param string text:
        String with the text to be displayed.
    :return:
        Nothing.
    """
    messagebox.showwarning(title, text)


def info(title, text):
    """
    Alert type info

    :param string title:
        String with the title to be apply.
    :param string text:
        String with the text to be displayed.
    :return:
        Nothing.
    """
    messagebox.showinfo(title, text)


def error(title, text):
    """
    Alert type error

    :param string title:
        String with the title to be apply.
    :param string text:
        String with the text to be displayed.
    :return:
        Nothing.
    """
    messagebox.showerror(title, text)


def yesno(title, text):
    """
    Alert type yes or no

    :param string title:
        String with the title to be apply.
    :param string text:
        String with the text to be displayed.
    :return:
        Nothing.
    """
    return messagebox.askyesno(title, text)
