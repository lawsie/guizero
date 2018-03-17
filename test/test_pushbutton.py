from threading import Event
from guizero import App, PushButton
from tkmixin_test import (
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
    b = PushButton(a)
    assert b.master == a
    assert b.text == "Button"
    assert b.grid == None
    assert b.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    b = PushButton(
        a, 
        text = "foo", 
        grid = [0,1], 
        align = "top")
    
    assert b.text == "foo"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    a.destroy()

def test_getters_setters():
    a = App()
    b = PushButton(a, text = "foo")
    assert b.text == "foo"
    b.text = "bar"
    assert b.text == "bar"
    a.destroy()

def test_command():
    a = App()
    
    callback_event = Event()
    def callback():
        callback_event.set()

    b = PushButton(a, command = callback)
    assert not callback_event.is_set()
    b.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_command_with_args():
    a = App()
    
    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    b = PushButton(a, command = callback, args = ["foo"])
    
    b.tk.invoke()
    assert callback_event.is_set()

    a.destroy()
    
def test_update_command():
    a = App()
    
    callback_event = Event()
    def callback():
        callback_event.set()

    b = PushButton(a)
    
    b.tk.invoke()
    assert not callback_event.is_set()
    
    b.update_command(callback)
    b.tk.invoke()
    assert callback_event.is_set()
    callback_event.clear()

    b.update_command(None)
    b.tk.invoke()
    assert not callback_event.is_set()
    
    a.destroy()

def test_update_command_with_args():
    a = App()
    
    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    b = PushButton(a)
    
    b.update_command(callback, ["foo"])
    b.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_toggle():
    a = App()
    b = PushButton(a)
    assert b.enabled
    b.toggle()
    assert not b.enabled
    b.toggle()
    assert b.enabled
    
def test_after_schedule():
    a = App()
    b = PushButton(a)
    schedule_after_test(a, b)
    a.destroy()

def test_repeat_schedule():
    a = App()
    b = PushButton(a)
    schedule_repeat_test(a, b)
    a.destroy()

def test_destroy_mixin():
    a = App()
    b = PushButton(a)
    destroy_test(b)
    a.destroy()

def test_enable_mixin():
    a = App()
    b = PushButton(a)
    enable_test(b)
    a.destroy()

def test_display_mixin():
    a = App()
    b = PushButton(a)
    display_test(b)
    a.destroy()

def test_display_mixin():
    a = App()
    b = PushButton(a)
    display_test(b)
    a.destroy()

def test_text():
    a = App()
    b = PushButton(a)
    text_test(b)
    a.destroy()

def test_color():
    a = App()
    b = PushButton(a)
    color_test(b)
    a.destroy()

def test_size():
    a = App()
    b = PushButton(a)
    size_text_test(b)
    a.destroy()
