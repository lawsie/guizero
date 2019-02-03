from tkinter import *

root = Tk()

root.geometry("300x300")
f = Frame(root)
f["bg"] = "red"
#f["height"] = 200
f["width"] = 200

w = Label(f, text="label")
w["bg"] = "green"

w.pack()

f.pack_propagate(True)
#f.pack(side="bottom", fill="x")
f.pack(side="top", fill="y")

mainloop()

# propagate rules
# if width or height is greater than 0 = False
