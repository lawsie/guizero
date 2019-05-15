from tkinter.simpledialog import askstring

def askquestion(title, question, initial_value=None, **kw):
    return askstring(title, question, initialvalue=initial_value, **kw)
