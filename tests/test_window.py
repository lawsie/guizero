from threading import Event
from guizero import App, Window, Text
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    display_test,
    events_test,
    )

def test_default_values():
    a = App()
    w = Window(a)
    assert w.title == "guizero"
    assert w.width == 500
    assert w.height == 500
    assert w.layout == "auto"
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
    w.destroy()

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

def test_events():
    a = App()
    w = Window(a)
    events_test(w)
    a.destroy()

def test_cascading_properties():
    a = App()
    w = Window(a)
    t = Text(w)

    a.bg = "red"
    a.text_color = "purple"
    assert w.bg == "red"
    assert w.text_color == "purple"
    assert t.bg == "red"
    assert t.text_color == "purple"

    w.bg = "green"
    w.text_color = "yellow"
    assert a.bg == "red"
    assert a.text_color == "purple"
    assert w.bg == "green"
    assert w.text_color == "yellow"
    assert t.bg == "green"
    assert t.text_color == "yellow"

    a.destroy()

def test_inherited_properties():
    a = App()
    a.bg = "red"
    a.text_color = "purple"
    
    w = Window(a)
    assert w.bg == "red"
    assert w.text_color == "purple"

    w.bg = "green"
    w.text_color = "yellow"

    t = Text(w)
    assert t.bg == "green"
    assert t.text_color == "yellow"

    a.destroy()
