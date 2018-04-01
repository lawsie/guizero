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
        align = "top")
    
    assert c.text == "foo"
    assert c.grid[0] == 0
    assert c.grid[1] == 1
    assert c.align == "top"
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
    a.destroy()
