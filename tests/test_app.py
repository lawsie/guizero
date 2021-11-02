import pytest
from threading import Event
from guizero import App, Text, Picture, system_config
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
    icon_test)

def test_default_values():
    a = App()
    assert a.title == "guizero"
    assert a.width == 500
    assert a.height == 500
    assert a.layout == "auto"
    assert a.description > ""
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

def test_when_resized():
    
    a = App()

    resize_event = Event()
    def callback():
        resize_event.set()

    def callback_params(event):
        assert event.width == 503
        assert event.height == 504
        resize_event.set()


    a.when_resized = callback
    a.resize(501, 502)
    assert resize_event.wait(1)
    resize_event.clear()
    
    a.when_resized = callback_params
    a.resize(503, 504)
    assert resize_event.wait(1)
    resize_event.clear()

    a.when_resized = None
    a.resize(505, 506)
    assert not resize_event.wait(0.1)

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

def test_icon():
    a = App()
    icon_test(a, "../examples/guizero.gif")
    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_icon_jpg():
    a = App()
    icon_test(a, "../examples/guizero.jpg")
    a.destroy()