from guizero import App, TextBox
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
    t = TextBox(a)
    assert t.master == a
    assert t.grid == None
    assert t.align == None
    assert t.width == 10
    assert t.value == ""
    a.destroy() 

def test_alt_values():
    a = App(layout = "grid")
    t = TextBox(
        a, 
        text="foo", 
        width = 20,
        grid = [0,1], 
        align="top",
        multiline=True,
        scrollbar=True)

    assert t.master == a
    assert t.grid[0] == 0
    assert t.grid[1] == 1
    assert t.align == "top"
    assert t.value == "foo\n"
    assert t.width == 20
    a.destroy()

def test_getters_setters():
    a = App()
    t = TextBox(a)
    t.value = "foo"
    assert t.value == "foo"
    a.destroy()

def test_clear():
    a = App()
    t = TextBox(a, text = "foo")
    t.clear()
    assert t.value == ""
    a.destroy()

def test_append():
    a = App()
    t = TextBox(a, text = "foo")
    t.append("bar")
    assert t.value == "foobar"
    a.destroy()

def test_after_schedule():
    a = App()
    t = TextBox(a)
    schedule_after_test(a, t)
    a.destroy()

def test_repeat_schedule():
    a = App()
    t = TextBox(a)
    schedule_repeat_test(a, t)
    a.destroy()

def test_destroy():
    a = App()
    t = TextBox(a)
    destroy_test(t)
    a.destroy()

def test_enable():
    a = App()
    t = TextBox(a)
    enable_test(t)
    a.destroy()

def test_display():
    a = App()
    t = TextBox(a)
    display_test(t)
    a.destroy()

def test_text():
    a = App()
    t = TextBox(a)
    text_test(t)
    a.destroy()

def test_color():
    a = App()
    t = TextBox(a)
    color_test(t)
    a.destroy()

def test_width():
    a = App()
    t = TextBox(a)
    t.width = 30
    assert t.width == 30
    a.destroy()

def test_height():
    a = App()
    
    t1 = TextBox(a)
    t1.height = 10
    #cant change height of single line text box
    assert t1.height == 1

    t2 = TextBox(a, multiline=True)
    t2.height = 10
    assert t2.height == 10

    a.destroy()

def test_events():
    a = App()
    t = TextBox(a)
    events_test(t)
    a.destroy()