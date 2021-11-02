import pytest
from threading import Event
from time import sleep
from unittest.mock import MagicMock
from guizero import Text, Picture
from tkinter import Spinbox

# find a suitable font to test with
SUITABLE_FONTS = ["Times New Roman", "Liberation Serif", "Impact", "FreeSans"]
TEST_FONT = None
from tkinter import Tk, font
root = Tk()
available_fonts = font.families()
root.destroy()

for suitable_font in SUITABLE_FONTS:
    if suitable_font in available_fonts:
        TEST_FONT = suitable_font
        break

if TEST_FONT is None:
    pytest.exit("A suitable test font could not be found.")

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
    default = widget.bg
    widget.bg = "red"
    assert widget.bg == "red"
    widget.bg = "#ff0000"
    assert widget.bg == "#ff0000"
    widget.bg = (255, 0, 0)
    assert widget.bg == "#ff0000"
    widget.bg = None
    assert widget.bg == default

def size_pixel_test(widget):
    default = widget.width
    widget.width = 666
    assert widget.width == 666
    widget.width = None
    assert widget.width == default

    default = widget.height
    widget.height = 666
    assert widget.height == 666
    widget.height = None
    assert widget.height == default

def size_text_test(widget):
    default = widget.width
    widget.width = 30
    assert widget.width == 30
    widget.width = None
    assert widget.width == default

    default = widget.height
    widget.height = 10
    assert widget.height == 10
    widget.height = None
    assert widget.height == default

def size_fill_test(widget):
    default = widget.width
    widget.width = "fill"
    assert widget.width == "fill"
    widget.width = None
    assert widget.width == default

    default = widget.height
    widget.height = "fill"
    assert widget.height == "fill"
    widget.height = None
    assert widget.height == default

def text_test(widget):
    default = widget.font
    widget.font = TEST_FONT
    assert widget.font == TEST_FONT
    widget.font = None
    assert widget.font == default

    default = widget.text_color
    widget.text_color = "red"
    assert widget.text_color == "red"
    widget.text_color = "#ff0000"
    assert widget.text_color == "#ff0000"
    widget.text_color = (255, 0, 0)
    assert widget.text_color == "#ff0000"
    widget.text_color = None
    assert widget.text_color == default

    default = widget.text_size
    widget.text_size = 16
    assert widget.text_size == 16
    widget.text_size = None
    assert widget.text_size == default

def events_test(widget):

    events_to_test = (
        ("when_clicked", "<when_clicked>"),
        ("when_double_clicked", "<when_double_clicked>"),
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
        assert e.width == 5
        assert e.height == 6
        callback_with_param_event.set()

    for event_to_test in events_to_test:
        # set the when_attribute to the callback
        setattr(widget, event_to_test[0], callback)
        assert not callback_event.is_set()
        # mock the event
        mock_event(widget, event_to_test[1], "A", 1, 2, 3, 4, 5, 6)
        assert callback_event.is_set()

        callback_with_param_event.clear()
        # set the when_attribute to the callback with a parameter
        setattr(widget, event_to_test[0], callback_with_param)
        assert not callback_with_param_event.is_set()
        # mock the event
        mock_event(widget, event_to_test[1], "A", 1, 2, 3, 4, 5, 6)
        assert callback_with_param_event.is_set()

        callback_event.clear()
        callback_with_param_event.clear()
        # set the when_attribute to None
        setattr(widget, event_to_test[0], None)
        mock_event(widget, event_to_test[1], "A", 1, 2, 3, 4, 5, 6)
        # make sure its not called
        assert not callback_event.is_set()
        assert not callback_with_param_event.is_set()

def mock_event(widget, ref, key, x, y, display_x, display_y, width, height):
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
    tk_event.width = width
    tk_event.height = height

    # call the event callback
    event_callback._event_callback(tk_event)

def cascaded_properties_test(container, widget, text):
    container.bg = "red"
    container.enabled = False
    assert widget.bg == "red"
    assert not widget.enabled

    if text:
        container.text_color = "purple"
        assert widget.text_color == "purple"
        container.text_size = 16
        assert widget.text_size == 16

def inherited_properties_test(container, widget_create, text):
    container.bg = "red"
    container.enabled = False
    if text:
        container.text_color = "purple"
        container.text_size = 16

    w = widget_create()

    assert w.bg == "red"
    assert not container.enabled
    if text:
        assert w.text_color == "purple"
        assert w.text_size == 16

def cascading_enable_test(container):

    def check_children(container, test_value):
        for child in container.children:
            assert child.enabled == test_value

    assert container.enabled
    check_children(container, True)

    container.enabled = False
    assert not container.enabled
    check_children(container, False)

    container.enabled = True
    assert container.enabled
    check_children(container, True)

    container.disable()
    assert not container.enabled
    check_children(container, False)

    container.enable()
    assert container.enabled
    check_children(container, True)

def cascading_properties_test(container):
    t = Text(container, color=None, size=None, font=None)
    p = Picture(container)

    container.bg = "red"
    container.text_color = "purple"
    container.text_size = 16
    container.font = TEST_FONT
    container.enabled = False

    assert t.bg == "red"
    assert t.text_color == "purple"
    assert t.text_size == 16
    assert t.font == TEST_FONT
    assert t.enabled == False
    assert p.bg == "red"
    assert p.enabled == False

    # test that destroying widgets removes them as children
    p.destroy()
    container.bg = "green"
    assert t.bg == "green"

def inheriting_properties_test(container):
    container.bg = "red"
    container.text_color = "purple"
    container.text_size = 16
    container.font = TEST_FONT
    container.enabled = False

    t = Text(container, color=None, size=None, font=None)
    assert t.bg == "red"
    assert t.text_color == "purple"
    assert t.text_size == 16
    assert t.font == TEST_FONT
    assert not t.enabled

    p = Picture(container)
    assert p.bg == "red"
    assert not p.enabled

def full_screen_test(window):
    assert window.full_screen == False
    window.full_screen = True
    assert window.full_screen == True
    window.full_screen = False
    assert window.full_screen == False
    window.set_full_screen()
    assert window.full_screen == True
    window.exit_full_screen()
    assert window.full_screen == False

def add_tk_widget_test(container):
    s = Spinbox(from_=0, to=10)
    sw = container.add_tk_widget(s)
    assert s is not None
    assert sw is not None
    assert sw.grid is None
    assert sw.align is None
    assert sw.enabled
    assert sw.visible
    assert sw.width is None
    assert sw.height is None
    
    s2 = Spinbox(from_=0, to=10)
    sw = container.add_tk_widget(s2, align="left", visible=False, enabled=False, width="fill", height="fill")
    assert s is not None
    assert sw is not None
    assert sw.align == "left"
    assert not sw.enabled
    assert not sw.visible
    assert sw.width == "fill"
    assert sw.height == "fill"

def auto_layout_test(widget, align):
    
    assert widget.master.layout == "auto"
    side = "top" if align is None else align
    assert widget.tk.pack_info()["side"] == side

    widget.align = "left"
    assert widget.tk.pack_info()["side"] == "left"

    widget.align = "right"
    assert widget.tk.pack_info()["side"] == "right"

    widget.align = "top"
    assert widget.tk.pack_info()["side"] == "top"

    widget.align = "bottom"
    assert widget.tk.pack_info()["side"] == "bottom"

def grid_layout_test(widget, x, y, col_span, row_span, align):

    sticky = {"top": "n", "bottom": "s", "left": "w", "right": "e", None: ""}

    # test initial values
    assert widget.master.layout == "grid"
    assert int(widget.tk.grid_info()["column"]) == x
    assert int(widget.tk.grid_info()["row"]) == y
    assert int(widget.tk.grid_info()["columnspan"]) == col_span
    assert int(widget.tk.grid_info()["rowspan"]) == row_span
    assert widget.tk.grid_info()["sticky"] == sticky[align]

    # change grid values
    widget.grid[0] = 3
    widget.grid[1] = 4
    assert int(widget.tk.grid_info()["column"]) == 3
    assert int(widget.tk.grid_info()["row"]) == 4
    assert int(widget.tk.grid_info()["columnspan"]) == col_span
    assert int(widget.tk.grid_info()["rowspan"]) == row_span
    assert widget.tk.grid_info()["sticky"] == sticky[align]

    widget.grid = [5,6]
    assert int(widget.tk.grid_info()["column"]) == 5
    assert int(widget.tk.grid_info()["row"]) == 6
    assert int(widget.tk.grid_info()["columnspan"]) == 1
    assert int(widget.tk.grid_info()["rowspan"]) == 1
    assert widget.tk.grid_info()["sticky"] == sticky[align]

    widget.grid = (7,8)
    assert int(widget.tk.grid_info()["column"]) == 7
    assert int(widget.tk.grid_info()["row"]) == 8
    assert int(widget.tk.grid_info()["columnspan"]) == 1
    assert int(widget.tk.grid_info()["rowspan"]) == 1
    assert widget.tk.grid_info()["sticky"] == sticky[align]

    # change span
    widget.grid = [9, 10, 11, 12]
    assert int(widget.tk.grid_info()["column"]) == 9
    assert int(widget.tk.grid_info()["row"]) == 10
    assert int(widget.tk.grid_info()["columnspan"]) == 11
    assert int(widget.tk.grid_info()["rowspan"]) == 12
    assert widget.tk.grid_info()["sticky"] == sticky[align]

    # change align
    widget.align = "left"
    assert widget.tk.grid_info()["sticky"] == sticky["left"]

def icon_test(widget, file_name):
    widget.icon = file_name
    assert widget.icon == file_name
    assert widget._icon.tk_image is not None