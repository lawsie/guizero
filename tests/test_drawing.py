from threading import Event
from guizero import App, Drawing
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    enable_test,
    display_test,
    events_test,
    cascaded_properties_test,
    inherited_properties_test,
    grid_layout_test,
    auto_layout_test
    )

def test_default_values():
    a = App()
    d = Drawing(a)
    assert d.master == a
    assert d.grid == None
    assert d.align == None
    assert d.width == 100
    assert d.height == 100
    assert a.description > ""
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    d = Drawing(
        a,
        grid = [0,1],
        align = "top",
        width = 10,
        height = 11)

    assert d.grid[0] == 0
    assert d.grid[1] == 1
    assert d.align == "top"
    assert d.width == 10
    assert d.height == 11
    a.destroy()

def test_after_schedule():
    a = App()
    d = Drawing(a)
    schedule_after_test(a, d)
    a.destroy()

def test_repeat_schedule():
    a = App()
    d = Drawing(a)
    schedule_repeat_test(a, d)
    a.destroy()

def test_destroy():
    a = App()
    d = Drawing(a)
    destroy_test(d)
    a.destroy()

def test_enable():
    a = App()
    d = Drawing(a)
    enable_test(d)
    a.destroy()

def test_display():
    a = App()
    d = Drawing(a)
    display_test(d)
    a.destroy()

def test_cascaded_properties():
    a = App()
    d = Drawing(a)
    cascaded_properties_test(a, d, False)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: Drawing(a), False)
    a.destroy()

def test_line():
    a = App()
    d = Drawing(a)    
    id = d.line(1,2,3,4)
    assert id > 0
    a.destroy()

def test_oval():
    a = App()
    d = Drawing(a)
    id = d.oval(1,2,3,4)
    assert id > 0
    a.destroy()

def test_rectangle():
    a = App()
    d = Drawing(a)
    id = d.rectangle(1,2,3,4)
    assert id > 0
    a.destroy()

def test_polygon():
    a = App()
    d = Drawing(a)
    id = d.polygon(1,2,3,4,5,6,7,8)
    assert id > 0
    a.destroy()

def test_triangle():
    a = App()
    d = Drawing(a)
    id = d.triangle(1,2,3,4,5,6)
    assert id > 0
    a.destroy()

def test_image():
    a = App()
    d = Drawing(a)
    id = d.image(1,2,"../examples/guizero.gif")
    assert id > 0
    a.destroy()

def test_text():
    a = App()
    d = Drawing(a)
    id = d.text(1,2,"foo")
    assert id > 0
    a.destroy()

def test_delete():
    a = App()
    d = Drawing(a)
    id1 = d.line(1,2,3,4)
    id2 = d.oval(1,2,3,4)
    assert len(d.tk.find_all()) == 2
    d.delete(id1)
    assert len(d.tk.find_all()) == 1
    d.delete(id2)
    assert len(d.tk.find_all()) == 0
    a.destroy()

def test_clear():
    a = App()
    d = Drawing(a)
    d.line(1,2,3,4)
    d.oval(1,2,3,4)
    assert len(d.tk.find_all()) == 2
    d.clear()
    assert len(d.tk.find_all()) == 0
    a.destroy()

def test_auto_layout():
    a = App()
    w = Drawing(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = Drawing(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = Drawing(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = Drawing(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()