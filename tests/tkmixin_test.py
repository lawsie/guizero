from threading import Event
from time import sleep

def schedule_after_test(app, widget):
    callback_event = Event()
    def callback():
        callback_event.set()
    assert not callback_event.is_set()
    widget.after(0, callback)
    # call tk to update the app
    app.tk.update()
    assert callback_event.is_set()
    #widget.cancel(callback)

def schedule_repeat_test(app, widget):
    callback_event = Event()
    def callback():
        callback_event.set()
        widget.cancel(callback)
    assert not callback_event.is_set()
    widget.repeat(0, callback)
    # call tk to update the app
    app.tk.update()
    assert callback_event.is_set()

def destroy_test(widget):
    assert widget.tk.winfo_exists()
    widget.destroy()
    assert not widget.tk.winfo_exists()
    
def enable_test(widget):
    assert widget.enabled
    widget.enabled = False
    assert not widget.enabled
    widget.enabled = True
    assert widget.enabled
    widget.disable()
    assert not widget.enabled
    widget.enable()
    assert widget.enabled

# doesn't work under pytest, app always returns None from focus_get() run 
# direct from Python it works fine.
def focus_test(app, widget):
    app.focus()    
    app.tk.update()
    assert app.tk.focus_get() == app.tk
    
    widget.focus()
    app.tk.update()
    assert app.tk.focus_get() == widget.tk

def display_test(widget):
    assert widget.visible
    widget.visible = False
    assert not widget.visible
    widget.visible = True
    assert widget.visible
    widget.hide()
    assert not widget.visible
    widget.show()
    assert widget.visible
    
def color_test(widget):
    widget.bg = "red"
    assert widget.bg == "red"
    widget.bg = "#ff0000"
    assert widget.bg == "#ff0000"
    widget.bg = (255, 0, 0)
    assert widget.bg == "#ff0000"
    
def size_pixel_test(widget):
    widget.width = 666
    assert widget.width == 666
    widget.height = 666
    assert widget.height == 666

def size_text_test(widget):
    widget.width = 30
    assert widget.width == 30
    widget.height = 10
    assert widget.height == 10
    
def text_test(widget):
    widget.font = "times new roman"
    assert widget.font == "Times New Roman"
    
    widget.text_color = "red"
    assert widget.text_color == "red"
    widget.text_color = "#ff0000"
    assert widget.text_color == "#ff0000"
    widget.text_color = (255, 0, 0)
    assert widget.text_color == "#ff0000"

    widget.text_size = 16
    assert widget.text_size == 16
    
