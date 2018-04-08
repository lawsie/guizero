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
        # execute the function
        function(*args)
        if function in self._callback.keys():
            repeat = self._callback[function][1]
            if repeat:
                # setup the call back again and update the id
                callback_id = self.tk.after(time, self._call_wrapper, time, function, *args)
                self._callback[function][0] = callback_id
            else:
                # remove it from the call back dictionary
                self._callback.pop(function)


class DestroyMixin():
    def destroy(self):
        """Destroy the object."""
        self.tk.destroy()


class EnableMixin():    
    @property
    def enabled(self):
        button_state = self.tk.cget("state")
        return button_state == "normal" or button_state == "active"

    @enabled.setter
    def enabled(self, value):
        if value:
            self.enable()
        else:
            self.disable()
    
    def disable(self):
        """Disable the widget."""
        self.tk.configure(state="disabled")

    def enable(self):
        """Enable the widget."""
        self.tk.configure(state="normal")


class FocusMixin():
    def focus(self):
        """Give focus to the widget."""
        self.tk.focus_set()


class DisplayMixin():

    @property
    def visible(self):
        return self._visible
    
    @visible.setter
    def visible(self, value):
        if value:
            self.show()
        else:
            self.hide()

    def hide(self):
        """Hide the widget."""
        if self.master.layout == "grid":
            self.tk.grid_forget()
        else:
            self.tk.pack_forget()
        self._visible = False

    def show(self):
        """Show the widget."""
        utils.auto_pack(self, self.master, self.grid, self.align)
        self._visible = True


class TextMixin():

    # Get the font object for this widget 
    def _get_font(self):
        # get the font in use for the widget
        f = Font(self.tk, self.tk.cget("font"))
        # configure() returns a dictionary of font attributes
        return f.configure()

    # Get the text colour as a string
    @property
    def text_color(self):
        return (self.tk.cget("fg"))

    # Set the text colour
    @text_color.setter
    def text_color(self, color):
        self.tk.config(fg=utils.convert_color(color))

    # Get the current font as a string
    @property
    def font(self):
        f = self._get_font()
        return (f["family"])

    # Set the current font
    @font.setter
    def font(self, font):
        self.tk.config(font=(font, self.text_size))

    # Get the current text size as an integer
    @property
    def text_size(self):
        f = self._get_font()
        return (f["size"])

    # Set the font size
    @text_size.setter
    def text_size(self, size):
        self.tk.config(font=(self.font, size))


class ColorMixin():
    # Get the background colour as a string
    @property
    def bg(self):
        return (self.tk.cget("bg"))

    # Set the background colour
    @bg.setter
    def bg(self, color):
        self.tk.config(bg=utils.convert_color(color))


class SizeMixin():
    @property
    def width(self):
        return int(self.tk.cget("width"))

    @width.setter
    def width(self, value):
        self.tk.config(width=value)

    @property
    def height(self):
        return int(self.tk.cget("height"))

    @height.setter
    def height(self, value):
        self.tk.config(height=value)


class GridMixin():

    @property
    def grid(self):
        """
        Returns `[x,y]` coordinates of this widget.
        """
        return self._grid

    @property
    def align(self):
        """
        Returns the alignment of this widget within its grid location.
        """
        return self._align


class EventsMixin():

    @property
    def when_clicked(self):
        return self.events.get_event("<when_clicked>")

    @when_clicked.setter
    def when_clicked(self, value):
        self.events.set_event("<when_clicked>", "<ButtonPress-1>", value)

    @property
    def when_left_button_pressed(self):
        return self.events.get_event("<when_left_button_pressed>")

    @when_left_button_pressed.setter
    def when_left_button_pressed(self, value):
        self.events.set_event("<when_left_button_pressed>", "<ButtonPress-1>", value)

    @property
    def when_left_button_released(self):
        return self.events.get_event("<when_left_button_released>")

    @when_left_button_released.setter
    def when_left_button_released(self, value):
        self.events.set_event("<when_left_button_released>", "<ButtonRelease-1>", value)

    @property
    def when_right_button_pressed(self):
        return self.events.get_event("<when_right_button_pressed>")

    @when_right_button_pressed.setter
    def when_right_button_pressed(self, value):
        self.events.set_event("<when_right_button_pressed>", "<ButtonPress-3>", value)

    @property
    def when_right_button_released(self):
        return self.events.get_event("<when_right_button_released>")

    @when_right_button_released.setter
    def when_right_button_released(self, value):
        self.events.set_event("<when_right_button_released>", "<ButtonRelease-3>", value)

    @property
    def when_key_pressed(self):
        return self.events.get_event("<when_key_pressed>")

    @when_key_pressed.setter
    def when_key_pressed(self, value):
        self.events.set_event("<when_key_pressed>", "<KeyPress>", value)

    @property
    def when_key_released(self):
        return self.events.get_event("<when_key_released>")

    @when_key_released.setter
    def when_key_released(self, value):
        self.events.set_event("<when_key_released>", "<KeyRelease>", value)

    @property
    def when_mouse_enters(self):
        return self.events.get_event("<when_mouse_enters>")

    @when_mouse_enters.setter
    def when_mouse_enters(self, value):
        self.events.set_event("<when_mouse_enters>", "<Enter>", value)

    @property
    def when_mouse_leaves(self):
        return self.events.get_event("<when_mouse_leaves>")

    @when_mouse_leaves.setter
    def when_mouse_leaves(self, value):
        self.events.set_event("<when_mouse_leaves>", "<Leave>", value)

    @property
    def when_mouse_moved(self):
        return self.events.get_event("<when_mouse_moved>")
    
    @when_mouse_moved.setter
    def when_mouse_moved(self, value):
        self.events.set_event("<when_mouse_moved>", "<Motion>", value)

    @property
    def when_mouse_dragged(self):
        return self.events.get_event("<when_mouse_dragged>")

    @when_mouse_dragged.setter
    def when_mouse_dragged(self, value):
        self.events.set_event("<when_mouse_dragged>", "<B1-Motion>", value)