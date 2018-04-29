from guizero import App, Text, Picture
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    display_test,
    events_test)

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

def test_events():
    a = App()
    events_test(a)
    a.destroy()

def test_cascading_properties():
    a = App()
    t = Text(a)
    p = Picture(a)

    a.bg = "red"
    a.text_color = "purple"
    a.text_size = 16
    a.font = "Times New Roman"

    assert t.bg == "red"
    assert t.text_color == "purple"
    assert t.text_size == 16
    assert t.font == "Times New Roman"
    assert p.bg == "red"

    # test that destroying widgets removes them as children
    p.destroy()
    a.bg = "green"
    assert t.bg == "green"

    a.destroy()

def test_inherited_properties():
    a = App()

    a.bg = "red"
    a.text_color = "purple"
    a.text_size = 16
    a.font = "Times New Roman"

    t = Text(a)
    assert t.bg == "red"
    assert t.text_color == "purple"
    assert t.text_size == 16
    assert t.font == "Times New Roman"

    p = Picture(a)
    assert p.bg == "red"

    a.destroy()