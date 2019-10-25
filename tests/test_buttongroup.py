from threading import Event
from guizero import App, ButtonGroup
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
    b = ButtonGroup(a, ["foo", "bar"])
    assert b.master == a
    assert b.value == "foo"
    assert b.value_text == "foo"
    assert b.grid == None
    assert b.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    b = ButtonGroup(
        a,
        ["foo", "bar"],
        "bar",
        grid = [0,1],
        align = "top",
        width=11,
        height=10)

    assert b.value == "bar"
    assert b.value_text == "bar"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    assert b.width == 11
    assert b.height == 10
    a.destroy()

def test_2d_options_list():
    a = App()
    b = ButtonGroup(a, [["foo", "f"], ["bar", "b"]])
    assert b.value == "f"
    assert b.value_text == "foo"
    a.destroy()

def test_getters_setters():
    a = App()
    b = ButtonGroup(a, ["foo", ["bar", "b"]])
    assert b.value == "foo"
    assert b.value_text == "foo"

    b.value = "b"
    assert b.value == "b"
    assert b.value_text == "bar"

    b.value_text = "foo"
    assert b.value == "foo"
    assert b.value_text == "foo"

    a.destroy()

def test_append():
    a = App()
    b = ButtonGroup(a, [["foo", "f"], ["bar", "b"]])

    assert b.options == [["foo", "f"], ["bar", "b"]]

    b.append("car")
    assert b.options == [["foo", "f"], ["bar", "b"], ["car", "car"]]

    b.append(["lah", "l"])
    assert b.options == [["foo", "f"], ["bar", "b"], ["car", "car"], ["lah", "l"]]

    a.destroy()

def test_insert():
    a = App()
    b = ButtonGroup(a, [["foo", "f"], ["bar", "b"]])

    assert b.options == [["foo", "f"], ["bar", "b"]]

    b.insert(1, "car")
    assert b.options == [["foo", "f"], ["car", "car"], ["bar", "b"]]

    b.insert(2, ["lah", "l"])
    assert b.options == [["foo", "f"], ["car", "car"], ["lah", "l"], ["bar", "b"]]

    a.destroy()

def test_remove():
    a = App()
    b = ButtonGroup(a, [["foo", "f"], ["bar", "b"], ["car", "c"]])

    assert b.options == [["foo", "f"], ["bar", "b"], ["car", "c"]]
    b.remove("f")
    assert b.options == [["bar", "b"], ["car", "c"]]

    a.destroy()

def test_clear():
    a = App()
    b = ButtonGroup(a, [["foo", "f"], ["bar", "b"]])

    b.clear()
    assert len(b.options) == 0
    assert b.value == ""

    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        assert b.value == "bar"
        assert b.value_text == "bar"
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"], command = callback)

    assert not callback_event.is_set()
    b._rbuttons[1].tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_command_with_args():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        assert b.value == "bar"
        assert b.value_text == "bar"
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"], command = callback, args = ["foo"])

    b._rbuttons[1].tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"])

    b._rbuttons[1].tk.invoke()
    assert not callback_event.is_set()

    b.update_command(callback)
    b._rbuttons[1].tk.invoke()
    assert callback_event.is_set()
    callback_event.clear()

    b.update_command(None)
    b._rbuttons[1].tk.invoke()
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_args():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"])

    b.update_command(callback, ["foo"])
    b._rbuttons[1].tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_after_schedule():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    schedule_after_test(a, b)
    a.destroy()

def test_repeat_schedule():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    schedule_repeat_test(a, b)
    a.destroy()

def test_destroy():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    destroy_test(b)
    a.destroy()

def test_enable():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    enable_test(b)
    a.destroy()

def test_display():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    display_test(b)
    a.destroy()

def test_text():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    text_test(b)
    a.destroy()

def test_color():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    color_test(b)
    a.destroy()

def test_size():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    size_text_test(b)
    size_fill_test(b)
    a.destroy()

def test_events():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    events_test(b)
    a.destroy()

def test_cascaded_properties():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    cascaded_properties_test(a, b, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: ButtonGroup(a, ["foo", "bar"]), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = ButtonGroup(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = ButtonGroup(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = ButtonGroup(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = ButtonGroup(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()
