import pytest
from threading import Event
from guizero import App, Window, Text, system_config
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    display_test,
    events_test,
    cascading_enable_test,
    cascading_properties_test,
    inheriting_properties_test,
    full_screen_test,
    add_tk_widget_test,
    icon_test
    )

def test_default_values():
    a = App()
    w = Window(a)
    assert w.title == "guizero"
    assert w.width == 500
    assert w.height == 500
    assert w.layout == "auto"
    assert a.description > ""
    a.destroy()

def test_alt_values():
    a = App()
    w = Window(a, title = "foo", width = 666, height = 666, layout="grid")
    assert w.title == "foo"
    assert w.width == 666
    assert w.height == 666
    assert w.layout == "grid"
    a.destroy()

def test_getters_setters():
    a = App()
    w = Window(a)
    w.title = "bar"
    assert w.title == "bar"
    w.bg = "red"
    assert w.bg == "red"
    w.height = 666
    assert w.height == 666
    w.width = 666
    assert w.width == 666
    a.destroy()

def test_update():
    a = App()
    w = Window(a)
    # just testing it doesnt fail
    w.update()
    a.destroy()

def test_after_schedule():
    a = App()
    w = Window(a)
    schedule_after_test(a, w)
    a.destroy()

def test_repeat_schedule():
    a = App()
    w = Window(a)
    schedule_repeat_test(a, w)
    a.destroy()

def test_display():
    a = App()
    w = Window(a)
    display_test(w)
    a.destroy()

def test_enable():
    a = App()
    w = Window(a)
    t = Text(w)
    cascading_enable_test(a)
    cascading_enable_test(w)
    a.destroy()

def test_events():
    a = App()
    w = Window(a)
    events_test(w)
    a.destroy()

def test_cascading_properties():
    a = App()
    w = Window(a)
    cascading_properties_test(w)
    a.destroy()

def test_inheriting_properties():
    a = App()
    w = Window(a)
    inheriting_properties_test(w)
    a.destroy()

def test_full_screen():
    a = App()
    w = Window(a)
    full_screen_test(w)
    a.destroy()

def test_add_tk_widget():
    a = App()
    add_tk_widget_test(a)
    a.destroy()

def test_icon():
    a = App()
    w = Window(a)
    icon_test(w, "../examples/guizero.gif")
    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_icon_jpg():
    a = App()
    w = Window(a)
    icon_test(w, "../examples/guizero.jpg")
    a.destroy()