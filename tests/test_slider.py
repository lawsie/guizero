from threading import Event
from guizero import App, Slider
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    enable_test,
    display_test,
    text_test,
    color_test,
    size_pixel_test,
    size_fill_test,
    events_test,
    cascaded_properties_test,
    inherited_properties_test,
    grid_layout_test,
    auto_layout_test
    )

def test_default_values():
    a = App()
    s = Slider(a)
    assert s.tk.cget("from") == 0
    assert s.tk.cget("to") == 100
    assert s.tk.cget("orient") == "horizontal"
    assert s.master == a
    assert s.grid == None
    assert s.align == None
    assert a.description > ""
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    s = Slider(
        a,
        start=10,
        end=20,
        horizontal=False,
        grid = [0,1],
        align = "top",
        width=10,
        height=11)

    assert s.tk.cget("from") == 10
    assert s.tk.cget("to") == 20
    assert s.tk.cget("orient") == "vertical"
    assert s.grid[0] == 0
    assert s.grid[1] == 1
    assert s.align == "top"
    assert s.width == 10
    assert s.height == 11
    a.destroy()

def test_getters_setters():
    a = App()
    s = Slider(a)

    assert s.value == 0
    s.value = 10
    assert s.value == 10

    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    s = Slider(a, command = callback)
    assert not callback_event.is_set()
    # you cant invoke a tk scale - this is better than no tests!
    s._command_callback(s.value)
    assert callback_event.is_set()

    a.destroy()

def test_command_with_parameter():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == 0
        callback_event.set()

    s = Slider(a, command = callback)
    assert not callback_event.is_set()

    s._command_callback(s.value)
    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    s = Slider(a)

    s._command_callback(s.value)
    assert not callback_event.is_set()

    s.update_command(callback)
    s._command_callback(s.value)
    assert callback_event.is_set()
    callback_event.clear()

    s.update_command(None)
    s._command_callback(s.value)
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_parameter():
    a = App()

    callback_event = Event()
    def callback(value):
        assert s.value == 0
        callback_event.set()

    s = Slider(a)

    s.update_command(callback)

    s._command_callback(s.value)
    assert callback_event.is_set()

    a.destroy()

def test_after_schedule():
    a = App()
    s = Slider(a)
    schedule_after_test(a, s)
    a.destroy()

def test_repeat_schedule():
    a = App()
    s = Slider(a)
    schedule_repeat_test(a, s)
    a.destroy()

def test_destroy():
    a = App()
    s = Slider(a)
    destroy_test(s)
    a.destroy()

def test_enable():
    a = App()
    s = Slider(a)
    enable_test(s)
    a.destroy()

def test_display():
    a = App()
    s = Slider(a)
    display_test(s)
    a.destroy()

def test_text():
    a = App()
    s = Slider(a)
    text_test(s)
    a.destroy()

def test_color():
    a = App()
    s = Slider(a)
    color_test(s)
    a.destroy()

def test_size():
    a = App()
    s = Slider(a)
    size_pixel_test(s)
    size_fill_test(s)
    a.destroy()

def test_events():
    a = App()
    s = Slider(a)
    events_test(s)
    a.destroy()

def test_cascaded_properties():
    a = App()
    s = Slider(a)
    cascaded_properties_test(a, s, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: Slider(a), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = Slider(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = Slider(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = Slider(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = Slider(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()