from tkinter import messagebox
# Generates alerts

def warn(title, text):
    messagebox.showwarning(title,text)

def info(title, text):
    messagebox.showinfo(title,text)

def error(title, text):
    messagebox.showerror(title, text)

def yesno(title, text):
    return messagebox.askyesno(title, text)
