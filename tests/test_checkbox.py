from threading import Event
from guizero import App, CheckBox
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    enable_test,
    display_test,
    text_test,
    color_test,
    size_text_test,
    size_fill_test,
    events_test,
    cascaded_properties_test,
    inherited_properties_test,
    grid_layout_test,
    auto_layout_test
    )

def test_default_values():
    a = App()
    c = CheckBox(a, "foo")
    assert c.master == a
    assert c.text == "foo"
    assert c.grid == None
    assert c.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    c = CheckBox(
        a,
        text = "foo",
        grid = [0,1],
        align = "top",
        width = 10,
        height = 11)

    assert c.text == "foo"
    assert c.grid[0] == 0
    assert c.grid[1] == 1
    assert c.align == "top"
    assert c.width == 10
    assert c.height == 11
    a.destroy()

def test_getters_setters():
    a = App()
    c = CheckBox(a, "foo")

    assert c.text == "foo"
    c.text = "bar"
    assert c.text == "bar"

    assert not c.value
    c.value = True
    assert c.value

    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    c = CheckBox(a, "foo", command = callback)
    assert not callback_event.is_set()
    c.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_command_with_args():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    c = CheckBox(a, "foo", command = callback, args = ["foo"])

    c.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    c = CheckBox(a, "foo")

    c.tk.invoke()
    assert not callback_event.is_set()

    c.update_command(callback)
    c.tk.invoke()
    assert callback_event.is_set()
    callback_event.clear()

    c.update_command(None)
    c.tk.invoke()
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_args():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    c = CheckBox(a, "foo")

    c.update_command(callback, ["foo"])
    c.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_toggle():
    a = App()
    c = CheckBox(a, "foo")

    assert not c.value
    c.toggle()
    assert c.value
    c.toggle()
    assert not c.value

    a.destroy()

def test_after_schedule():
    a = App()
    c = CheckBox(a, "foo")
    schedule_after_test(a, c)
    a.destroy()

def test_repeat_schedule():
    a = App()
    c = CheckBox(a, "foo")
    schedule_repeat_test(a, c)
    a.destroy()

def test_destroy():
    a = App()
    c = CheckBox(a, "foo")
    destroy_test(c)
    a.destroy()

def test_enable():
    a = App()
    c = CheckBox(a, "foo")
    enable_test(c)
    a.destroy()

def test_display():
    a = App()
    c = CheckBox(a, "foo")
    display_test(c)
    a.destroy()

def test_text():
    a = App()
    c = CheckBox(a, "foo")
    text_test(c)
    a.destroy()

def test_color():
    a = App()
    c = CheckBox(a, "foo")
    color_test(c)
    a.destroy()

def test_size():
    a = App()
    c = CheckBox(a, "foo")
    size_text_test(c)
    size_fill_test(c)
    a.destroy()

def test_events():
    a = App()
    c = CheckBox(a, "foo")
    events_test(c)
    a.destroy()

def test_cascaded_properties():
    a = App()
    c = CheckBox(a, "foo")
    cascaded_properties_test(a, c, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: CheckBox(a, "foo"), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = CheckBox(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = CheckBox(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = CheckBox(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = CheckBox(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()