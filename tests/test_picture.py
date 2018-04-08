import pytest
from guizero import App, Picture, system_config
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    enable_test,
    display_test,
    text_test,
    color_test,
    events_test,
    )

def test_default_values():
    a = App()
    p = Picture(a)
    assert p.master == a
    assert p.image == None
    assert p.grid == None
    assert p.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    p = Picture(
        a,
        image = "../examples/guizero.gif",
        grid = [0,1], 
        align = "top")
    assert p.image == "../examples/guizero.gif"
    assert p._image.tk_image is not None
    assert p.grid[0] == 0
    assert p.grid[1] == 1
    assert p.align == "top"
    a.destroy()

def test_getters_setters():
    a = App()
    p = Picture(a)
    
    assert p.image == None
    p.image = "../examples/guizero.gif"
    assert p.image == "../examples/guizero.gif"
    assert p._image.tk_image is not None
    p.width = 100
    assert p.width == 100
    p.height = 100
    assert p.height == 100

    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_jpg():
    a = App()
    p = Picture(a, image = "../examples/guizero.jpg")
    
    assert p.image == "../examples/guizero.jpg"
    assert p._image.tk_image is not None
    assert p._image.pil_image is not None

    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_animated_picture():
    a = App()
    p = Picture(a, image = "../examples/guizero_flash.gif")
    
    assert p._image.tk_image is not None
    assert p._image.pil_image is not None
    assert p._image.animation
    assert p._image_player.running

    a.destroy()

def test_picture_tkobject():
    from tkinter import PhotoImage
    
    a = App()
    photo_image = PhotoImage(file="../examples/guizero.gif")
    p = Picture(a, image=photo_image)
    assert p.image == photo_image
    assert p._image.tk_image is not None
    a.destroy()

@pytest.mark.skipif(system_config.PIL_available == False,
                    reason="PIL not available")
def test_picture_pilobject():
    from PIL import Image
    
    a = App()
    pil_image = Image.open("../examples/guizero.gif")
    p = Picture(a, image=pil_image)
    assert p.image == pil_image
    assert p._image.tk_image is not None
    assert p._image.pil_image is not None
    a.destroy()

def test_after_schedule():
    a = App()
    p = Picture(a)
    schedule_after_test(a, p)
    a.destroy()

def test_repeat_schedule():
    a = App()
    p = Picture(a)
    schedule_repeat_test(a, p)
    a.destroy()

def test_destroy():
    a = App()
    p = Picture(a)
    destroy_test(p)
    a.destroy()

def test_enable():
    a = App()
    p = Picture(a)
    enable_test(p)
    a.destroy()

def test_display():
    a = App()
    p = Picture(a)
    display_test(p)
    a.destroy()

def test_color():
    a = App()
    p = Picture(a)
    color_test(p)
    a.destroy()

def test_events():
    a = App()
    p = Picture(a)
    events_test(p)
    a.destroy()