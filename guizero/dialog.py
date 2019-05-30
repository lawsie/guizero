from tkinter.simpledialog import askstring

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
    :return:
        The value entered or `None`.
    """
    return askstring(title, question, initialvalue=initial_value, parent=None if master is None else master.tk)
    