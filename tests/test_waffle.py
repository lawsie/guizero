from guizero import App, Waffle
from threading import Event
from unittest.mock import MagicMock
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    enable_test,
    display_test,
    color_test,
    events_test,
    cascaded_properties_test,
    inherited_properties_test,
    grid_layout_test,
    auto_layout_test
    )

def test_default_values():
    a = App()
    w = Waffle(a)
    assert w.master == a
    assert w.grid == None
    assert w.align == None
    assert w.width == 3
    assert w.height == 3
    assert w.pixel_size == 20
    assert w.pad == 5
    assert w.color == "white"
    assert w.dotty == False
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    w = Waffle(
        a,
        height = 10,
        width = 11,
        dim = 12,
        pad = 13,
        color = "red",
        grid = [0,1],
        align = "top",
        dotty = True,
        bg = "green"
        )
    assert w.master == a
    assert w.grid[0] == 0
    assert w.grid[1] == 1
    assert w.align == "top"
    assert w.height == 10
    assert w.width == 11
    assert w.pixel_size == 12
    assert w.pad == 13
    assert w.color == "red"
    assert w.dotty == True
    assert w.bg == "green"
    a.destroy()

def test_getters_setters():
    a = App()
    w = Waffle(a)

    w.width = 10
    assert w.width == 10
    w.height = 11
    assert w.height == 11
    w.pixel_size = 12
    assert w.pixel_size == 12
    w.pad = 13
    assert w.pad == 13
    w.color = "red"
    assert w.color == "red"
    w.dotty = True
    assert w.dotty == True

    a.destroy()

def test_set_get_all():
    from itertools import chain

    a = App()
    w = Waffle(a)

    w.set_all("red")
    # turn 2d list into 1d list
    pixels = chain.from_iterable(zip(*w.get_all()))

    count = 0
    for pixel in pixels:
        assert pixel == "red"
        count += 1

    assert count == w.width * w.height

    a.destroy()

def test_set_get_pixel():
    a = App()
    w = Waffle(a)

    w.set_pixel(0,0, "red")
    assert w.get_pixel(0,0) == "red"

    a.destroy()

def test_pixel_getters_setters():
    a = App()
    w = Waffle(a)

    pixel = w[0,1]
    assert pixel.x == 0
    assert pixel.y == 1
    assert pixel.size == w.pixel_size
    assert pixel.color == w.color
    assert pixel.dotty == w.dotty

    pixel.color = "red"
    assert pixel.color == "red"

    pixel.dotty = True
    assert pixel.dotty

    a.destroy()

def test_reset():
    from itertools import chain

    a = App()
    w = Waffle(a)

    w.set_pixel(0, 1, "red")
    w.reset()

    pixels = chain.from_iterable(zip(*w.get_all()))

    count = 0
    for pixel in pixels:
        assert pixel == w.color
        count += 1

    assert count == w.width * w.height

    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    w = Waffle(a, command = callback)
    assert not callback_event.is_set()

    mock_waffle_clicked(w)

    assert callback_event.is_set()

    a.destroy()

def test_command_with_parameters():
    a = App()

    callback_event = Event()
    def callback(x, y):
        assert x == 0
        assert y == 1
        callback_event.set()

    w = Waffle(a, command = callback)
    assert not callback_event.is_set()

    mock_waffle_clicked(w)

    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    w = Waffle(a)

    mock_waffle_clicked(w)
    assert not callback_event.is_set()

    w.update_command(callback)
    mock_waffle_clicked(w)
    assert callback_event.is_set()
    callback_event.clear()

    w.update_command(None)
    mock_waffle_clicked(w)
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_parameters():
    a = App()

    callback_event = Event()
    def callback(x, y):
        assert x == 0
        assert y == 1
        callback_event.set()

    w = Waffle(a)

    w.update_command(callback)

    mock_waffle_clicked(w)
    assert callback_event.is_set()

    a.destroy()

def mock_waffle_clicked(w):
    # you cant invoke a tk canvas - this is better than no tests!
    # create a mock event
    ev = MagicMock()
    ev.widget = w
    ev.tk_event.widget = w._canvas
    ev.tk_event.x = 1
    # make sure the y is 1 pixel down
    ev.tk_event.y = 1 + w.pixel_size + w.pad
    w._clicked_on(ev)

def test_after_schedule():
    a = App()
    w = Waffle(a)
    schedule_after_test(a, w)
    a.destroy()

def test_repeat_schedule():
    a = App()
    w = Waffle(a)
    schedule_repeat_test(a, w)
    a.destroy()

def test_destroy():
    a = App()
    w = Waffle(a)
    destroy_test(w)
    a.destroy()

def test_enable():
    a = App()
    w = Waffle(a)
    enable_test(w)
    a.destroy()

def test_display():
    a = App()
    w = Waffle(a)
    display_test(w)
    a.destroy()

def test_color():
    a = App()
    w = Waffle(a)
    color_test(w)
    a.destroy()

def test_events():
    a = App()
    w = Waffle(a)
    events_test(w)
    a.destroy()

def test_cascaded_properties():
    a = App()
    w = Waffle(a)
    cascaded_properties_test(a, w, False)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: Waffle(a), False)
    a.destroy()

def test_auto_layout():
    a = App()
    w = Waffle(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = Waffle(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = Waffle(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = Waffle(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()