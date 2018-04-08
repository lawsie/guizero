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
    events_test,
    )

def test_default_values():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    assert b.master == a
    assert b.value == "1"
    assert b.value_text == "foo"
    assert b.grid == None
    assert b.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    b = ButtonGroup(
        a, 
        ["foo", "bar"], 
        2,
        grid = [0,1], 
        align = "top")
    
    assert b.value == "2"
    assert b.value_text == "bar"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    a.destroy()

def test_2d_options_list():
    a = App()
    b = ButtonGroup(a, [["foo", "f"], ["bar", "b"]])
    assert b.value == "f"
    assert b.value_text == "foo"
    a.destroy()

def test_getters_setters():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    assert b.value == "1"
    assert b.value_text == "foo"
    
    b.value = 2
    assert b.value == "2"
    assert b.value_text == "bar"

    b.value_text = "foo"
    assert b.value == "1"
    assert b.value_text == "foo"

    a.destroy()

def test_command():
    a = App()
    
    callback_event = Event()
    def callback():
        assert b.value == "2"
        assert b.value_text == "bar"
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"], command = callback)
    
    assert not callback_event.is_set()
    b._options[1].tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_command_with_args():
    a = App()
    
    callback_event = Event()
    def callback(value):
        assert value == "foo"
        assert b.value == "2"
        assert b.value_text == "bar"
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"], command = callback, args = ["foo"])
    
    b._options[1].tk.invoke()
    assert callback_event.is_set()

    a.destroy()
    
def test_update_command():
    a = App()
    
    callback_event = Event()
    def callback():
        callback_event.set()

    b = ButtonGroup(a, ["foo", "bar"])
    
    b._options[1].tk.invoke()
    assert not callback_event.is_set()
    
    b.update_command(callback)
    b._options[1].tk.invoke()
    assert callback_event.is_set()
    callback_event.clear()

    b.update_command(None)
    b._options[1].tk.invoke()
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
    b._options[1].tk.invoke()
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
    a.destroy()

def test_events():
    a = App()
    b = ButtonGroup(a, ["foo", "bar"])
    events_test(b)
    a.destroy()