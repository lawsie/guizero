from threading import Event
from guizero import App, Window
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