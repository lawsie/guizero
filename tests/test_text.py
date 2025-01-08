from guizero import App, Text
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
    TEST_FONT,
    grid_layout_test,
    auto_layout_test
    )

def test_default_values():
    a = App()
    t = Text(a)
    assert t.master == a
    assert t.grid == None
    assert t.align == None
    assert t.size == 12
    assert t.text_color == "black"
    assert t.text_bold == False
    assert t.text_italic == False
    assert t.text_underline == False
    assert t.text_overstrike == False
    assert t.value == ""
    assert a.description > ""
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    t = Text(
        a,
        text="foo",
        size = 14,
        color="green",
        bg="red",
        font=TEST_FONT,
        grid = [0,1],
        align="top",
        width = 10,
        height = 11,
        bold=True,
        italic=True,
        underline=True,
        overstrike=True)

    assert t.master == a
    assert t.grid[0] == 0
    assert t.grid[1] == 1
    assert t.align == "top"
    assert t.size == 14
    assert t.text_color == "green"
    assert t.bg == "red"
    assert t.font == TEST_FONT
    assert t.value == "foo"
    assert t.width == 10
    assert t.height == 11
    assert t.bold == True
    assert t.italic == True
    assert t.underline == True
    assert t.overstrike == True
    a.destroy()

def test_getters_setters():
    a = App()
    t = Text(a)
    t.value = "foo"
    assert t.value == "foo"
    t.size = 18
    assert t.size == 18
    t.bold = True
    assert t.bold == True
    t.italic = True
    assert t.italic == True
    t.underline = True
    assert t.underline == True
    t.overstrike = True
    assert t.overstrike == True
    a.destroy()

def test_clear():
    a = App()
    t = Text(a, text = "foo")
    t.clear()
    assert t.value == ""
    a.destroy()

def test_append():
    a = App()
    t = Text(a, text = "foo")
    t.append("bar")
    assert t.value == "foobar"
    a.destroy()

def test_after_schedule():
    a = App()
    t = Text(a)
    schedule_after_test(a, t)
    a.destroy()

def test_repeat_schedule():
    a = App()
    t = Text(a)
    schedule_repeat_test(a, t)
    a.destroy()

def test_destroy():
    a = App()
    t = Text(a)
    destroy_test(t)
    a.destroy()

def test_enable():
    a = App()
    t = Text(a)
    enable_test(t)
    a.destroy()

def test_display():
    a = App()
    t = Text(a)
    display_test(t)
    a.destroy()

def test_text():
    a = App()
    # default values
    t = Text(a, color=None, size=None, font=None, bold=None, italic=None, underline=None, overstrike=None)
    text_test(t)
    a.destroy()

def test_color():
    a = App()
    t = Text(a)
    color_test(t)
    a.destroy()

def test_size():
    a = App()
    t = Text(a)
    size_text_test(t)
    size_fill_test(t)
    a.destroy()

def test_events():
    a = App()
    t = Text(a)
    events_test(t)
    a.destroy()

def test_cascaded_properties():
    a = App()
    t = Text(a)
    cascaded_properties_test(a, t, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    t = Text(a)
    inherited_properties_test(a, lambda: Text(a), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = Text(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = Text(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = Text(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = Text(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()