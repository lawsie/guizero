from guizero import App, Window, PushButton
from guizero.utilities import GUIZeroImage
from tkinter import PhotoImage


app = App(title="Main window")
app.icon = "guizero.gif"

window = Window(app, title="2nd window", visible=False)

open_window_button = PushButton(app, text="Open window", command=window.show)

close_window_button = PushButton(window, text="Close", command=window.hide)

app.display()

