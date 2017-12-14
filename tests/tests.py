"""
Automated GUI testing for Guizero (https://github.com/lawsie/guizero).
Bug tracker:

Problem statement                 Fixed y/n
-------------------------------------------
* `gz.Combo.value` setter         n
  doesn't check if `str(value)`
  in `self._options`
-------------------------------------------
* `value_text` setter in          n
  `gz.ButtonGroup` is confusing
-------------------------------------------
* `gz.Combo.__init__` raises      n
  `tk.TclError` when `options`
  argument is an empty list
-------------------------------------------
* `gz.ButtonGroup` `enable`       n
  and `disable` fail because
  it's a `tk.Frame` object
-------------------------------------------
* Some widgets don't provide      n
  a way to test for callback
  (e.g. `tk.Checkbox`,
  `tk.OptionMenu`)
-------------------------------------------
* Add a verbosity setting for     n
  testing (aka disable Guizero
  warnings for testing)
-------------------------------------------
* We're not testing deprecated    n
  methods
-------------------------------------------
* `gz._Widget.enable` `TclError`  y
  'enabled' -> 'normal'
-------------------------------------------
* `horizontal` argument behaves   y
  unexpectedly in
  `gz.ButtonGroup.__init__`
-------------------------------------------
* tk.update in `gz.App.__init__`  y
  and `gz.App` properties
"""

import os
import tkinter as tk
import unittest

import guizero as gz


def _images_available():
    """Return True if the .gif image is available, else False."""
    return os.path.isfile("img.gif") and os.path.isfile("img1.gif")


class TestGuizeroApp(unittest.TestCase):
    def test_constructor(self):
        app = gz.App()

        title = app.tk.title()
        width = app.tk.winfo_width()
        height = app.tk.winfo_height()
        background = app.tk.cget("background")

        self.assertEqual(title, "guizero")
        self.assertEqual(width, 500)
        self.assertEqual(height, 500)
        self.assertEqual(background, "systemWindowBody")

    def test_properties(self):
        app = gz.App()

        title = app.tk.title()
        width = app.tk.winfo_width()
        height = app.tk.winfo_height()
        background = app.tk.cget("background")

        self.assertEqual(app.title, title)
        self.assertEqual(app.width, width)
        self.assertEqual(app.height, height)
        self.assertEqual(app.bg, background)

        app.title = "test"
        app.width = 600
        app.height = 600
        app.bg = "red"

        self.assertEqual(app.title, "test")
        self.assertEqual(app.width, 600)
        self.assertEqual(app.height, 600)
        self.assertEqual(app.bg, "red")

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


class TestGuizeroBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = gz.App()

    def test_constructor(self):
        box = gz.Box(master=self._app)

    def test_properties(self):
        pass

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


class TestGuizeroButtonGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = gz.App()

    def test_constructor(self):
        called = False

        def _callback():
            nonlocal called
            called = True

        buttongroup = gz.ButtonGroup(
            master=self._app,
            options=[["test", "0"], ["test1", "1"]],
            selected="1",
            horizontal=True,
            command=_callback
        )

        value = buttongroup._selected.get()
        for radiobutton in buttongroup._options:
            if radiobutton.tk.cget("value") == value:
                value_text = radiobutton.tk.cget("text")
                break
        else:
            value_text = ""

        self.assertEqual(value, "1")
        self.assertEqual(value_text, "test1")

        buttongroup._options[0].tk.invoke()
        self.assertTrue(called)

    def test_properties(self):
        buttongroup = gz.ButtonGroup(
            master=self._app,
            options=[["test", "0"], ["test1", "1"]],
            selected="1",
            horizontal=True
        )

        value = buttongroup._selected.get()
        for radiobutton in buttongroup._options:
            if str(radiobutton.tk.cget("value")) == value:
                value_text = radiobutton.tk.cget("text")
                break
        else:
            value_text = ""

        self.assertEqual(buttongroup.value, value)
        self.assertEqual(buttongroup.value_text, value_text)

        buttongroup.value = "0"
        # Hesitant to test the `ButtonGroup.value_text` property here
        # since it's an extremely awkward thing to use
        # TODO: Open issue

        self.assertEqual(buttongroup.value, "0")
        self.assertEqual(buttongroup.value_text, "test")

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


class TestGuizeroCheckBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = gz.App()

    def test_constructor(self):
        called = False

        def _callback():
            nonlocal called
            called = True

        checkbox = gz.CheckBox(
            master=self._app,
            text="test",
            command=_callback
        )

        text = checkbox.tk.cget("text")

        self.assertEqual(text, "test")

        checkbox.tk.invoke()
        self.assertTrue(called)

    def test_properties(self):
        checkbox = gz.CheckBox(
            master=self._app,
            text="test"
        )

        value = checkbox._value.get()
        text = checkbox.tk.cget("text")

        self.assertEqual(checkbox.value, value)
        self.assertEqual(checkbox.text, text)

        checkbox.value = 1
        checkbox.text = "test1"

        self.assertEqual(checkbox.value, 1)
        self.assertEqual(checkbox.text, "test1")

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


class TestGuizeroCombo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = gz.App()

    def test_constructor(self):
        combo = gz.Combo(
            master=self._app,
            options=["test", "test1", "test2"],
            selected="test3"
        )

    def test_properties(self):
        combo = gz.Combo(
            master=self._app,
            options=["test", "test1", "test2"],
            selected="test3"
        )

        value = combo._selected.get()

        self.assertEqual(combo.value, value)

        combo.value = "test1"

        self.assertEqual(combo.value, "test1")

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


class TestGuizeroMenuBar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = gz.App()

    def test_constructor(self):
        menubar = gz.MenuBar(
            master=self._app,
            toplevel=["test", "test1", "test2"],
            options=[
                [["test::test", lambda: None]],
                [["test1::test1", lambda: None]],
                [["test2::test2", lambda: None]]
            ]
        )

    def test_properties(self):
        pass

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


@unittest.skipUnless(_images_available(), "images not available")
class TestGuizeroPicture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._app = gz.App()

    def test_constructor(self):
        picture = gz.Picture(
            master=self._app,
            image="img.gif"
        )

    def test_properties(self):
        picture = gz.Picture(
            master=self._app,
            image="img.gif"
        )

        image_name = picture._image_name

        self.assertEqual(picture.value, image_name)

        picture.value = "img1.gif"

        self.assertEqual(picture.value, "img1.gif")

    @unittest.skip("Not implemented")
    def test_methods(self):
        pass


def main():
    unittest.main()

if __name__ == "__main__":
    main()
