from guizero import App, Box, Text
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    display_test,
    color_test,
    size_pixel_test,
    size_fill_test,
    events_test,
    cascading_enable_test,
    cascading_properties_test,
    inheriting_properties_test,
    add_tk_widget_test,
    grid_layout_test,
    auto_layout_test
    )

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
    b = Box(a, layout="grid", grid=[0,1], align="top", width=10, height=11)
    assert b.layout == "grid"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    assert b.width == 10
    assert b.height == 11
    a.destroy()

def test_border():
    a = App()
    b = Box(a)
    assert not b.border
    assert b.border == 0

    b.border = True
    assert b.border
    assert b.border == 1
    assert b._get_tk_config("highlightbackground") == "black"

    b.border = False
    assert not b.border

    b.border = 10
    assert b.border
    assert b.border == 10

    b.set_border(11, "red")
    assert b.border
    assert b.border == 11
    assert b._get_tk_config("highlightbackground") == "red"
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
    size_fill_test(b)
    a.destroy()

def test_enable():
    a = App()
    b = Box(a)
    t = Text(b)
    cascading_enable_test(a)
    cascading_enable_test(b)
    a.destroy()

def test_events():
    a = App()
    b = Box(a)
    events_test(b)
    a.destroy()

def test_cascading_properties():
    a = App()
    b = Box(a)
    cascading_properties_test(b)
    a.destroy()

def test_inheriting_properties():
    a = App()
    b = Box(a)
    inheriting_properties_test(b)
    a.destroy()

def test_add_tk_widget():
    a = App()
    add_tk_widget_test(a)
    a.destroy()

def test_auto_layout():
    a = App()
    w = Box(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = Box(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = Box(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = Box(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()
