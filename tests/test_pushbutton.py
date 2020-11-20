import pytest
from threading import Event
from guizero import App, PushButton, system_config
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
    b = PushButton(a)
    assert b.master == a
    assert b.text == "Button"
    assert b.grid == None
    assert b.align == None
    assert a.description > ""
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    b = PushButton(
        a,
        text = "foo",
        grid = [0,1],
        align = "top",
        width = 10,
        height = 11)

    assert b.text == "foo"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    assert b.width == 10
    assert b.height == 11
    a.destroy()

def test_getters_setters():
    a = App()
    b = PushButton(a, text = "foo")
    assert b.text == "foo"
    b.text = "bar"
    assert b.text == "bar"
    a.destroy()

def test_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    b = PushButton(a, command = callback)
    assert not callback_event.is_set()
    b.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_command_with_args():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    b = PushButton(a, command = callback, args = ["foo"])

    b.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_update_command():
    a = App()

    callback_event = Event()
    def callback():
        callback_event.set()

    b = PushButton(a)

    b.tk.invoke()
    assert not callback_event.is_set()

    b.update_command(callback)
    b.tk.invoke()
    assert callback_event.is_set()
    callback_event.clear()

    b.update_command(None)
    b.tk.invoke()
    assert not callback_event.is_set()

    a.destroy()

def test_update_command_with_args():
    a = App()

    callback_event = Event()
    def callback(value):
        assert value == "foo"
        callback_event.set()

    b = PushButton(a)

    b.update_command(callback, ["foo"])
    b.tk.invoke()
    assert callback_event.is_set()

    a.destroy()

def test_toggle():
    a = App()
    b = PushButton(a)
    assert b.enabled
    b.toggle()
    assert not b.enabled
    b.toggle()
    assert b.enabled
    a.destroy()

def test_picture_gif():
    a = App()
    b = PushButton(a, image="../examples/guizero.gif")
    assert b.image == "../examples/guizero.gif"
    assert b._image.tk_image is not None
    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_picture_jpg():
    a = App()
    b = PushButton(a, image="../examples/guizero.jpg")
    assert b.image == "../examples/guizero.jpg"
    assert b._image.tk_image is not None
    assert b._image.pil_image is not None
    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_animated_picture():
    a = App()
    b = PushButton(a, image="../examples/guizero_flash.gif")
    assert b.image == "../examples/guizero_flash.gif"
    assert b._image.tk_image is not None
    assert b._image.pil_image is not None
    assert b._image.animation
    assert b._image_player.running
    a.destroy()

def test_picture_tkobject():
    from tkinter import PhotoImage

    a = App()
    photo_image = PhotoImage(file="../examples/guizero.gif")
    b = PushButton(a, image=photo_image)
    assert b.image == photo_image
    assert b._image.tk_image is not None
    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_picture_pilobject():
    from PIL import Image

    a = App()
    pil_image = Image.open("../examples/guizero.gif")
    b = PushButton(a, image=pil_image)
    assert b.image == pil_image
    assert b._image.tk_image is not None
    assert b._image.pil_image is not None
    a.destroy()

def test_after_schedule():
    a = App()
    b = PushButton(a)
    schedule_after_test(a, b)
    a.destroy()

def test_repeat_schedule():
    a = App()
    b = PushButton(a)
    schedule_repeat_test(a, b)
    a.destroy()

def test_destroy():
    a = App()
    b = PushButton(a)
    destroy_test(b)
    a.destroy()

def test_enable():
    a = App()
    b = PushButton(a)
    enable_test(b)
    a.destroy()

def test_display():
    a = App()
    b = PushButton(a)
    display_test(b)
    a.destroy()

def test_text():
    a = App()
    b = PushButton(a)
    text_test(b)
    a.destroy()

def test_color():
    a = App()
    b = PushButton(a)
    color_test(b)
    a.destroy()

def test_size():
    a = App()
    b = PushButton(a)
    size_text_test(b)
    size_fill_test(b)
    a.destroy()

def test_events():
    a = App()
    p = PushButton(a)
    events_test(p)
    a.destroy()

def test_cascaded_properties():
    a = App()
    p = PushButton(a)
    cascaded_properties_test(a, p, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: PushButton(a), True)
    a.destroy()

def test_auto_layout():
    a = App()
    w = PushButton(a)
    auto_layout_test(w, None)
    a.destroy()

def test_grid_layout():
    a = App(layout="grid")
    
    w = PushButton(a, grid=[1,2])
    grid_layout_test(w, 1, 2, 1, 1, None)
    
    ws = PushButton(a, grid=[1,2,3,4])
    grid_layout_test(ws, 1, 2, 3, 4, None)

    wa = PushButton(a, grid=[1,2], align="top")
    grid_layout_test(wa, 1, 2, 1, 1, "top")
    
    a.destroy()