from guizero import App, Window, PushButton

app = App(title="Main window")

window = Window(app, title="2nd window")
window.hide()

modal_window = Window(app, title="modal window")
modal_window.hide()

open_window_button = PushButton(app, text="Open window", command=window.show)
open_modal_button = PushButton(app, text="Open modal window", command=modal_window.show, args = [True])

close_window_button = PushButton(window, text="Close", command=window.hide)

close_modal_button = PushButton(modal_window, text="Close", command=modal_window.hide)

app.display()

