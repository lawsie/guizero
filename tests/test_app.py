from guizero import App, Text, Picture
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    display_test,
    events_test,
    cascading_enable_test,
    cascading_properties_test,
    inheriting_properties_test,
    full_screen_test,
    add_tk_widget_test)

def test_default_values():
    a = App()
    assert a.title == "guizero"
    assert a.width == 500
    assert a.height == 500
    assert a.layout == "auto"
    a.destroy()

def test_alt_values():
    a = App(title = "foo", width = 666, height = 666, layout="grid")
    assert a.title == "foo"
    assert a.width == 666
    assert a.height == 666
    assert a.layout == "grid"
    a.destroy()

def test_getters_setters():
    a = App()
    a.title = "bar"
    assert a.title == "bar"
    a.bg = "red"
    assert a.bg == "red"
    a.height = 666
    assert a.height == 666
    a.width = 666
    assert a.width == 666
    a.destroy()

def test_update():
    a = App()
    # just testing it doesnt fail
    a.update()
    a.destroy()

def test_after_schedule():
    a = App()
    schedule_after_test(a, a)
    a.destroy()

def test_repeat_schedule():
    a = App()
    schedule_repeat_test(a, a)
    a.destroy()

def test_display():
    a = App()
    display_test(a)
    a.destroy()

def test_enable():
    a = App()
    t = Text(a)
    cascading_enable_test(a)
    a.destroy()

def test_events():
    a = App()
    events_test(a)
    a.destroy()

def test_cascading_properties():
    a = App()
    cascading_properties_test(a)
    a.destroy()

def test_inheriting_properties():
    a = App()
    inheriting_properties_test(a)
    a.destroy()

def test_full_screen():
    a = App()
    full_screen_test(a)
    a.destroy()

def test_add_tk_widget():
    a = App()
    add_tk_widget_test(a)
    a.destroy()