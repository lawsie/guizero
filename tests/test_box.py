from guizero import App, Box
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    display_test, 
    color_test, 
    size_pixel_test)

def test_default_values():
    a = App()
    b = Box(a)
    assert b.master == a
    assert b.layout == "auto"
    assert b.grid == None
    assert b.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    b = Box(a, layout="grid", grid=[0,1], align="top")
    assert b.layout == "grid"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    a.destroy()

def test_after_schedule():
    a = App()
    b = Box(a)
    schedule_after_test(a, b)
    a.destroy()

def test_repeat_schedule():
    a = App()
    b = Box(a)
    schedule_repeat_test(a, b)
    a.destroy()

def test_destroy():
    a = App()
    b = Box(a)
    destroy_test(b)
    a.destroy()

def test_display():
    a = App()
    b = Box(a)
    display_test(b)
    a.destroy()

def test_color():
    a = App()
    b = Box(a)
    color_test(b)
    a.destroy()

def test_size():
    a = App()
    b = Box(a)
    size_pixel_test(b)
    a.destroy()
