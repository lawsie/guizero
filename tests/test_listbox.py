from threading import Event
from guizero import App, ListBox
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
    l = ListBox(a)
    assert l.master == a
    assert l.value == None
    assert l.items == []
    assert l.grid == None
    assert l.align == None
    assert l.visible == True
    assert l.enabled == True
    assert l._listbox._multiselect == False
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    l = ListBox(
        a,
        ["foo", "bar"],
        selected = "bar",
        grid = [0,1],
        align = "top",
        width=10,
        height=11)

    assert l.value == "bar"
    assert l.items == ["foo", "bar"]
    assert l.grid[0] == 0
    assert l.grid[1] == 1
    assert l.align == "top"
    assert l.width == 10
    assert l.height == 11

    a.destroy()

def test_multi_alt_values():
    a = App(layout = "grid")
    l = ListBox(
        a,
        ["foo", "bar"],
        selected = ["bar"],
        grid = [0,1],
        align = "top",
        multiselect = True)

    assert l.value == ["bar"]
    assert l.items == ["foo", "bar"]
    assert l.grid[0] == 0
    assert l.grid[1] == 1
    assert l.align == "top"
    assert l._listbox._multiselect == True
    a.destroy()

def test_getters_setters():
    a = App()
    l = ListBox(a, ["foo", "bar"])

    assert l.value == None
    l.value = "bar"
    assert l.value == "bar"

    a.destroy()

def test_multi_getters_setters():
    a = App()
    l = ListBox(a, ["foo", "bar"], multiselect=True)

    assert l.value == None
    l.value = ["bar"]
    assert l.value == ["bar"]
    l.value = ["bar", "foo"]
    # test selected values are in value
    assert all(x in l.value for x in ['bar', 'foo'])

    a.destroy()

def test_append():
    a = App()
    l = ListBox(a, ["foo", "bar"])

    assert l.items == ["foo", "bar"]
    l.append("car")
    assert l.items == ["foo", "bar", "car"]

    a.destroy()

def test_insert():
    a = App()
    l = ListBox(a, ["foo", "bar"])

    assert l.items == ["foo", "bar"]
    l.insert(1, "car")
    assert l.items == ["foo", "car", "bar"]

    a.destroy()

def test_remove():
    a = App()
    l = ListBox(a, ["foo", "bar", "foo"])

    assert l.items == ["foo", "bar", "foo"]
    l.remove("foo")
    assert l.items == ["bar", "foo"]

    a.destroy()

def test_clear():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    assert l.items == ["foo", "bar"]
    l.clear()
    assert l.items == []

    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    l = ListBox(a, ["foo", "bar"], command = callback)
    assert not callback_event.is_set()

    l._listbox._command_callback()
    assert callback_event.is_set()

    a.destroy()

def test_command_with_parameter():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "bar"
        callback_event.set()

    l = ListBox(a, ["foo", "bar"], command = callback)
    l.value = "bar"
    assert not callback_event.is_set()

    l._listbox._command_callback()
    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    l = ListBox(a, ["foo", "bar"])

    l._listbox._command_callback()
    assert not callback_event.is_set()

    l.update_command(callback)
    l._listbox._command_callback()
    assert callback_event.is_set()
    callback_event.clear()

    l.update_command(None)
    l._listbox._command_callback()
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_parameter():
    a = App()

    callback_event = Event()
    def callback(value):
        assert l.value == "foo"
        callback_event.set()

    l = ListBox(a, ["foo", "bar"])
    l.value = "foo"

    l.update_command(callback)

    l._listbox._command_callback()
    assert callback_event.is_set()

    a.destroy()

def test_after_schedule():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    schedule_after_test(a, l)
    a.destroy()

def test_repeat_schedule():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    schedule_repeat_test(a, l)
    a.destroy()

def test_destroy():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    destroy_test(l)
    a.destroy()

def test_enable():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    enable_test(l)
    a.destroy()

def test_display():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    display_test(l)
    a.destroy()

def test_text():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    text_test(l)
    a.destroy()

def test_color():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    color_test(l)
    a.destroy()

def test_size():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    size_text_test(l)
    size_fill_test(l)
    a.destroy()

def test_events():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    events_test(l)
    a.destroy()

def test_cascaded_properties():
    a = App()
    l = ListBox(a, ["foo", "bar"])
    cascaded_properties_test(a, l, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: ListBox(a, ["foo", "bar"]), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = ListBox(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = ListBox(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = ListBox(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = ListBox(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()