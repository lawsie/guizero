import tkinter as tk


class _Widget:
    _display_cache = {}
    _callback = {}

    def _get_display_type(self):
        if not tk.grid_info():
            return "pack"
        return "grid"

    def after(self, time, function):
        """Call `function` after `time` milliseconds."""
        self.tk.after(time, function)

    def cancel(self, function):
        """Cancel the scheduled `function` calls."""
        self._callback[function] = False

    def destroy(self):
        """Destroy the widget."""
        self.tk.destroy()

    def disable(self):
        """Disable the widget."""
        self.tk.configure(state="disabled")

    def enable(self):
        """Enable the widget."""
        self.tk.configure(state="enabled")

    def focus(self):
        """Give focus to the widget."""
        self.tk.focus_set()

    def hide(self):
        """Hide the widget."""
        display_type = self._get_display_type()
        if display_type == "pack":
            self.tk.pack_forget()
        else:
            self.tk.grid_forget()

    def repeat(self, time, function):
        """Repeat `function` every `time` milliseconds."""
        self._callback[function] = True

        def _call_wrapper():
            if self._callback[function]:
                function()
                self.tk.after(time, _call_wrapper)
            else:
                return

        self.tk.after(time, _call_wrapper)

    def show(self):
        """Show the widget."""
        display_type = self._get_display_type()
        if display_type == "pack":
            self.tk.pack(**self._display_cache)
        else:
            self.tk.grid(**self._display_cache)

    def __repr__(self):
        return self.description
