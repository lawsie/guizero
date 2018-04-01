from guizero import App, Window, PushButton

app = App(title="Main window")

window = Window(app, title="2nd window", visible=False)

modal_window = Window(app, title="modal window", visible=False)

def open_modal():
    modal_window.show(True)

def close_modal():
    modal_window.hide()

open_window_button = PushButton(app, text="Open window", command=window.show)
open_modal_button = PushButton(app, text="Open modal window", command=open_modal)

close_window_button = PushButton(window, text="Close", command=window.hide)

close_modal_button = PushButton(modal_window, text="Close", command=close_modal)

app.display()

