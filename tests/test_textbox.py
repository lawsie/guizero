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
    size_fill_test,
    events_test,
    cascaded_properties_test,
    inherited_properties_test,
    grid_layout_test,
    auto_layout_test
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

    default_width = t.width
    t.width = 30
    assert t.width == 30
    t.width = "fill"
    assert t.width == "fill" 

    a.destroy()

def test_height():
    a = App()

    t1 = TextBox(a)
    t1.height = 10
    #cant change height of single line text box
    assert t1.height == 1

    t2 = TextBox(a, multiline=True)
    default_height = t2.height
    t2.height = 10
    assert t2.height == 10
    t2.height = "fill"
    assert t2.height == "fill"

    a.destroy()

def test_events():
    a = App()
    t = TextBox(a)
    events_test(t)
    a.destroy()

def test_cascaded_properties():
    a = App()
    t = TextBox(a)
    cascaded_properties_test(a, t, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: TextBox(a), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = TextBox(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = TextBox(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = TextBox(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = TextBox(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()