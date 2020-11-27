from threading import Event
from guizero import App, Combo
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
    c = Combo(a, ["foo", "bar"])
    assert c.master == a
    assert c.value == "foo"
    assert c.grid == None
    assert c.align == None
    assert a.description > ""
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    c = Combo(
        a,
        ["foo", "bar"],
        selected = "bar",
        grid = [0,1],
        align = "top",
        width=10,
        height=11)

    assert c.value == "bar"
    assert c.grid[0] == 0
    assert c.grid[1] == 1
    assert c.align == "top"
    assert c.width == 10
    assert c.height == 11
    a.destroy()

def test_no_options():
    a = App()
    c = Combo(a)

    assert c.value == ""
    assert len(c.options) == 0

    c.append("foo")
    assert c.value == "foo"

    a.destroy()

def test_getters_setters():
    a = App()
    c = Combo(a, ["foo", "bar"])

    assert c.value == "foo"
    c.value = "bar"
    assert c.value == "bar"

    a.destroy()

def test_select_default():
    a = App()
    c1 = Combo(a, ["foo", "bar"], selected="bar")
    c2 = Combo(a, ["foo", "bar"])

    assert c1.value == "bar"
    c1.value = "foo"
    assert c1.value == "foo"
    c1.select_default()
    assert c1.value == "bar"

    assert c2.value == "foo"
    c2.value = "bar"
    assert c2.value == "bar"
    c2.select_default()
    assert c2.value == "foo"

    a.destroy()

def test_append():
    a = App()
    c = Combo(a, ["foo", "bar"])

    assert c.options == ["foo", "bar"]
    c.append("car")
    assert c.options == ["foo", "bar", "car"]

    a.destroy()

def test_insert():
    a = App()
    c = Combo(a, ["foo", "bar"])

    assert c.options == ["foo", "bar"]
    c.insert(1, "car")
    assert c.options == ["foo", "car", "bar"]

    a.destroy()

def test_remove():
    a = App()
    c = Combo(a, ["foo", "bar", "foo"])

    assert c.options == ["foo", "bar", "foo"]
    c.remove("foo")
    assert c.options == ["bar", "foo"]

    a.destroy()

def test_clear():
    a = App()
    c = Combo(a, ["foo", "bar"])

    c.clear()
    assert len(c.options) == 0
    assert c.value == ""

    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    c = Combo(a, ["foo", "bar"], command = callback)
    assert not callback_event.is_set()
    # you cant invoke a tk optionmenu - this is better than no tests!
    c._command_callback(c.value)
    assert callback_event.is_set()

    a.destroy()

def test_command_with_parameter():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    c = Combo(a, ["foo", "bar"], command = callback)
    assert not callback_event.is_set()

    c._command_callback(c.value)
    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    c = Combo(a, ["foo", "bar"])

    c._command_callback(c.value)
    assert not callback_event.is_set()

    c.update_command(callback)
    c._command_callback(c.value)
    assert callback_event.is_set()
    callback_event.clear()

    c.update_command(None)
    c._command_callback(c.value)
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_parameter():
    a = App()

    callback_event = Event()
    def callback(value):
        assert c.value == "foo"
        callback_event.set()

    c = Combo(a, ["foo", "bar"])

    c.update_command(callback)

    c._command_callback(c.value)
    assert callback_event.is_set()

    a.destroy()

def test_after_schedule():
    a = App()
    c = Combo(a, ["foo", "bar"])
    schedule_after_test(a, c)
    a.destroy()

def test_repeat_schedule():
    a = App()
    c = Combo(a, ["foo", "bar"])
    schedule_repeat_test(a, c)
    a.destroy()

def test_destroy():
    a = App()
    c = Combo(a, ["foo", "bar"])
    destroy_test(c)
    a.destroy()

def test_enable():
    a = App()
    c = Combo(a, ["foo", "bar"])
    enable_test(c)
    a.destroy()

def test_display():
    a = App()
    c = Combo(a, ["foo", "bar"])
    display_test(c)
    a.destroy()

def test_text():
    a = App()
    c = Combo(a, ["foo", "bar"])
    text_test(c)
    a.destroy()

def test_color():
    a = App()
    c = Combo(a, ["foo", "bar"])
    color_test(c)
    a.destroy()

def test_size():
    a = App()
    c = Combo(a, ["foo", "bar"])
    size_text_test(c)
    size_fill_test(c)
    a.destroy()

def test_events():
    a = App()
    c = Combo(a, ["foo", "bar"])
    events_test(c)
    a.destroy()

def test_cascaded_properties():
    a = App()
    c = Combo(a, ["foo", "bar"])
    cascaded_properties_test(a, c, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: Combo(a, ["foo", "bar"]), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = Combo(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = Combo(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = Combo(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = Combo(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()
