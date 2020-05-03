from . import utilities as utils
from tkinter.font import Font
from tkinter import TclError


class ScheduleMixin():
    _callback = {}
    def after(self, time, function, args = []):
        """Call `function` after `time` milliseconds."""
        callback_id = self.tk.after(time, self._call_wrapper, time, function, *args)
        self._callback[function] = [callback_id, False]

    def repeat(self, time, function, args = []):
        """Repeat `function` every `time` milliseconds."""
        callback_id = self.tk.after(time, self._call_wrapper, time, function, *args)
        self._callback[function] = [callback_id, True]

    def cancel(self, function):
        """Cancel the scheduled `function` calls."""
        if function in self._callback.keys():
            callback_id = self._callback[function][0]
            self.tk.after_cancel(callback_id)
            self._callback.pop(function)
        else:
            utils.error_format("Could not cancel function - it doesnt exist, it may have already run")

    def _call_wrapper(self, time, function, *args):
        """Fired by tk.after, gets the callback and either executes the function and cancels or repeats"""
        if function in self._callback.keys():
            repeat = self._callback[function][1]
            if repeat:
                # setup the call back again and update the id
                callback_id = self.tk.after(time, self._call_wrapper, time, function, *args)
                self._callback[function][0] = callback_id
            else:
                # remove it from the call back dictionary
                self._callback.pop(function)
        # execute the function
        function(*args)


class DestroyMixin():
    def destroy(self):
        """Destroy the object."""
        self.tk.destroy()


class EnableMixin():
    @property
    def enabled(self):
        state = self._get_tk_config("state")
        return state == "normal" or state == "active"

    @enabled.setter
    def enabled(self, value):
        if value:
            self.enable()
        else:
            self.disable()

    def disable(self):
        """Disable the widget."""
        self._set_tk_config("state", "disabled")

    def enable(self):
        """Enable the widget."""
        self._set_tk_config("state", "normal")


class FocusMixin():
    def focus(self):
        """Give focus to the widget."""
        self.tk.focus_set()


class DisplayMixin():

    @property
    def visible(self):
        """
        Sets or returns whether the widget is visible.
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        if value:
            self.show()
        else:
            self.hide()

    def hide(self):
        """Hide the widget."""
        self._visible = False
        self.master.display_widgets()

    def show(self):
        """Show the widget."""
        self._visible = True
        self.master.display_widgets()


class TextMixin():

    FG_KEYS = [
        "fg",
        "activeforeground",
    ]

    # Get the font object for this widget
    def _get_font(self, default = False):
        # get the font in use for the widget
        f = Font(self.tk, self._get_tk_config("font", default=default))
        # configure() returns a dictionary of font attributes
        return f.configure()

    # Get the text colour as a string
    @property
    def text_color(self):
        """
        Sets or returns the text color of the widget.
        """
        return self._get_tk_config("fg")

    # Set the text colour
    @text_color.setter
    def text_color(self, color):
        self._set_tk_config(self.FG_KEYS, utils.convert_color(color))

    # Get the current font as a string
    @property
    def font(self):
        """
        Set or returns the font the widget is using.
        """
        f = self._get_font()
        return (f["family"])

    # Set the current font
    @font.setter
    def font(self, font):
        if font is None:
            # get the font from the default font
            f = self._get_font(default = True)
            font = f["family"]

        self._set_tk_config("font", (font, self.text_size))

    # Get the current text size as an integer
    @property
    def text_size(self):
        """
        Sets or returns the text size of the widget.
        """
        f = self._get_font()
        return (f["size"])

    # Set the font size
    @text_size.setter
    def text_size(self, size):
        if size is None:
            # get the size from the default font
            f = self._get_font(default = True)
            size = f["size"]

        self._set_tk_config("font", (self.font, size))


class ColorMixin():

    # these are the widget keys which will get set when the background is changed
    BG_KEYS = [
        "bg",
        "activebackground",
        "selectcolor",
        "troughcolor",
    ]

    # Get the background colour as a string
    @property
    def bg(self):
        """
        Sets the background color of the widget.
        """
        return self._get_tk_config("bg")

    # Set the background colour
    @bg.setter
    def bg(self, color):
        self._set_tk_config(self.BG_KEYS, utils.convert_color(color))


class SizeMixin():
    @property
    def width(self):
        """
        Sets or returns the width of the widget.
        """
        return self._width

    @width.setter
    def width(self, value):
        self.resize(value, self._height)

    @property
    def height(self):
        """
        Sets or returns the height of the widget.
        """
        return self._height

    @height.setter
    def height(self, value):
        self.resize(self._width, value)

    def resize(self, width, height):
        """
        Resizes the widget.

        :param int width:
            The width of the widget.

        :param int height:
            The height of the widget.
        """
        self._width = width
        self._height = height
        if width != "fill":
            self._set_tk_config("width", width)
        if height != "fill":
            self._set_tk_config("height", height)
        if width == "fill" or height == "fill":
            self.master.display_widgets()


class LayoutMixin():
    @property
    def grid(self):
        """
        Sets or returns `[x,y]` coordinates of this widget.
        """
        return self._grid

    @grid.setter
    def grid(self, value):
        self._update_grid(value)
        self.master.display_widgets()

    def _update_grid(self, grid):
        """
        Validates a Widgets grid property and stores it as a TriggeredList
        which will call the masters display_widgets method when it is changed
        """
        self._grid = None
        if self.master.layout == "grid":
            # validate the grid
            if grid is None:
                utils.error_format("{} will not be displayed because it has a missing grid reference.".format(self.description))
            elif not isinstance(grid, (list, tuple)):
                utils.error_format("{} will not be displayed because the grid reference is not a list or tuple.".format(self.description))
            # Can have 2 values (just coords) or 4 values (coords and col/rowspan)
            elif (len(grid) != 2 and len(grid) != 4):
                utils.error_format("{} will not be displayed because the grid reference should be either grid=[x, y] or grid=[x, y, columnspan, rowspan].".format(self.description))
            else:
                # convert the grid to a trackable list
                self._grid = utils.TriggeredList(grid, on_change=self.master.display_widgets)
        else:
            if grid is not None:
                utils.error_format("A grid is not required for {} as it is not using a 'grid' layout.".format(self.description))

    @property
    def align(self):
        """
        Returns the alignment of this widget within its grid location.
        """
        return self._align

    @align.setter
    def align(self, value):
        self._update_align(value)
        self.master.display_widgets()

    def _update_align(self, align):
        """
        Validates a widgets align property
        """
        self._align = None
        if align is not None:
            if align in ["top", "bottom", "left", "right"]:
                self._align = align
            else:
                utils.error_format("Invalid align value ('{}') for {}\nShould be: top, bottom, left or right".format(
                    align,
                    self.description
                ))


class EventsMixin():

    @property
    def when_clicked(self):
        """
        Sets or returns the function called when the widget is clicked.
        """
        return self.events.get_event("<when_clicked>")

    @when_clicked.setter
    def when_clicked(self, value):
        self.events.set_event("<when_clicked>", "<ButtonPress-1>", value)

    @property
    def when_left_button_pressed(self):
        """
        Sets or returns the function called when the left mouse button is
        pressed.
        """
        return self.events.get_event("<when_left_button_pressed>")

    @when_left_button_pressed.setter
    def when_left_button_pressed(self, value):
        self.events.set_event("<when_left_button_pressed>", "<ButtonPress-1>", value)

    @property
    def when_left_button_released(self):
        """
        Sets or returns the function called when the left mouse button is
        released.
        """
        return self.events.get_event("<when_left_button_released>")

    @when_left_button_released.setter
    def when_left_button_released(self, value):
        self.events.set_event("<when_left_button_released>", "<ButtonRelease-1>", value)

    @property
    def when_right_button_pressed(self):
        """
        Sets or returns the function called when the right mouse button is
        pressed.
        """
        return self.events.get_event("<when_right_button_pressed>")

    @when_right_button_pressed.setter
    def when_right_button_pressed(self, value):
        self.events.set_event("<when_right_button_pressed>", "<ButtonPress-3>", value)

    @property
    def when_right_button_released(self):
        """
        Sets or returns the function called when the right mouse button is
        released.
        """
        return self.events.get_event("<when_right_button_released>")

    @when_right_button_released.setter
    def when_right_button_released(self, value):
        self.events.set_event("<when_right_button_released>", "<ButtonRelease-3>", value)

    @property
    def when_key_pressed(self):
        """
        Sets or returns the function called when a key is pressed.
        """
        return self.events.get_event("<when_key_pressed>")

    @when_key_pressed.setter
    def when_key_pressed(self, value):
        self.events.set_event("<when_key_pressed>", "<KeyPress>", value)

    @property
    def when_key_released(self):
        """
        Sets or returns the function called when a key is released.
        """
        return self.events.get_event("<when_key_released>")

    @when_key_released.setter
    def when_key_released(self, value):
        self.events.set_event("<when_key_released>", "<KeyRelease>", value)

    @property
    def when_mouse_enters(self):
        """
        Sets or returns the function called when the mouse pointer enters
        the widget.
        """
        return self.events.get_event("<when_mouse_enters>")

    @when_mouse_enters.setter
    def when_mouse_enters(self, value):
        self.events.set_event("<when_mouse_enters>", "<Enter>", value)

    @property
    def when_mouse_leaves(self):
        """
        Sets or returns the function called when the mouse pointer leaves
        the widget.
        """
        return self.events.get_event("<when_mouse_leaves>")

    @when_mouse_leaves.setter
    def when_mouse_leaves(self, value):
        self.events.set_event("<when_mouse_leaves>", "<Leave>", value)

    @property
    def when_mouse_moved(self):
        """
        Sets or returns the function called when the mouse pointers moves.
        """
        return self.events.get_event("<when_mouse_moved>")

    @when_mouse_moved.setter
    def when_mouse_moved(self, value):
        self.events.set_event("<when_mouse_moved>", "<Motion>", value)

    @property
    def when_mouse_dragged(self):
        """
        Sets or returns the function called when the mouse pointer is dragged
        (moved with the left button pressed).
        """
        return self.events.get_event("<when_mouse_dragged>")

    @when_mouse_dragged.setter
    def when_mouse_dragged(self, value):
        self.events.set_event("<when_mouse_dragged>", "<B1-Motion>", value)
