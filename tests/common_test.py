from threading import Event
from time import sleep
from unittest.mock import MagicMock

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
    
def events_test(widget):

    events_to_test = (
        ("when_clicked", "<when_clicked>"),
        ("when_left_button_pressed", "<when_left_button_pressed>"),
        ("when_left_button_released", "<when_left_button_released>"),
        ("when_right_button_pressed", "<when_right_button_pressed>"),
        ("when_right_button_released", "<when_right_button_released>"),
        ("when_key_pressed", "<when_key_pressed>"),
        ("when_key_released", "<when_key_released>"),
        ("when_mouse_enters", "<when_mouse_enters>"),
        ("when_mouse_leaves", "<when_mouse_leaves>"),
        ("when_mouse_dragged", "<when_mouse_dragged>"),
    )

    callback_event = Event()
    def callback():
        callback_event.set()

    callback_with_param_event = Event()
    def callback_with_param(e):
        assert e.widget == widget
        assert e.key == "A"
        assert e.x == 1
        assert e.y == 2
        assert e.display_x == 3
        assert e.display_y == 4
        callback_with_param_event.set()

    for event_to_test in events_to_test:
        # set the when_attribute to the callback
        setattr(widget, event_to_test[0], callback)
        assert not callback_event.is_set()
        # mock the event
        mock_event(widget, event_to_test[1], "A", 1, 2, 3, 4)
        assert callback_event.is_set()

        callback_with_param_event.clear()
        # set the when_attribute to the callback with a parameter
        setattr(widget, event_to_test[0], callback_with_param)
        assert not callback_with_param_event.is_set()
        # mock the event
        mock_event(widget, event_to_test[1], "A", 1, 2, 3, 4)
        assert callback_with_param_event.is_set()

        callback_event.clear()
        callback_with_param_event.clear()
        # set the when_attribute to None
        setattr(widget, event_to_test[0], None)
        mock_event(widget, event_to_test[1], "A", 1, 2, 3, 4)
        # make sure its not called
        assert not callback_event.is_set()
        assert not callback_with_param_event.is_set()

def mock_event(widget, ref, key, x, y, display_x, display_y):
    # you cant invoke a tk event so we will mock it 
    # create a mock event

    # get the event callback
    event_callback = widget.events._refs[ref]
    
    # mock a tk event
    tk_event = MagicMock()
    tk_event.char = key
    tk_event.x = x
    tk_event.y = y
    tk_event.x_root = display_x
    tk_event.y_root = display_y
    
    # call the event callback
    event_callback._event_callback(tk_event)
