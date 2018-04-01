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
    )

def test_default_values():
    a = App()
    c = Combo(a, ["foo", "bar"])
    assert c.master == a
    assert c.value == "foo"
    assert c.grid == None
    assert c.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    c = Combo(
        a, 
        ["foo", "bar"],
        selected = "bar",
        grid = [0,1], 
        align = "top")
    
    assert c.value == "bar"
    assert c.grid[0] == 0
    assert c.grid[1] == 1
    assert c.align == "top"
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
    c = Combo(a, ["foo", "bar"], selected="bar")
    
    assert c.value == "bar"
    c.value = "foo"
    assert c.value == "foo"
    c.select_default()
    assert c.value == "bar"

    a.destroy()

def test_add_option():
    a = App()
    c = Combo(a, ["foo", "bar"])
    
    assert c.value == "foo"
    c.add_option("car")
    assert c.value == "car"

    a.destroy()

def test_clear():
    a = App()
    c = Combo(a, ["foo", "bar"])

    c.clear()
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
    a.destroy()
