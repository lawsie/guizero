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
    size_text_test,
    events_test,
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
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    s = Slider(
        a, 
        start=10,
        end=20,
        horizontal=False,
        grid = [0,1], 
        align = "top")
    
    assert s.tk.cget("from") == 10
    assert s.tk.cget("to") == 20
    assert s.tk.cget("orient") == "vertical"
    assert s.grid[0] == 0
    assert s.grid[1] == 1
    assert s.align == "top"
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
    size_text_test(s)
    a.destroy()

def test_events():
    a = App()
    s = Slider(a)
    events_test(s)
    a.destroy()