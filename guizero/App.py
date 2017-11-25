from sys import exit
from tkinter import Tk

from . import utilities as utils


class App:
    def __init__(
                 self,
                 title="guizero",
                 width=500,
                 height=500,
                 layout="auto",
                 bgcolor=None,
                 bg=None
                ):
        self.tk = Tk()
        self.tk.title(str(title))
        self.tk.geometry(str(width)+"x"+str(height))
        self._layout_manager = layout  # Only behaves differently for "grid"

        if bg is not None:
            self.tk.configure(background=str(bg))
        elif bgcolor is not None:
            self.tk.configure(background=str(bgcolor))
            utils.deprecated(
                "App 'bgcolor' constructor argument is deprecated. Please use bg instead."
            )

    # PROPERTIES
    # -----------------------------------

    @property
    def title(self):
        """Get the window's title."""
        return self.tk.wm_title()

    @title.setter
    def title(self, text):
        """Set the window's title."""
        self.tk.wm_title(str(text))

    @property
    def bg(self):
        """Get the window's background color."""
        return self.tk.cget("background")

    @bg.setter
    def bg(self, color):
        """Set the window's background color."""
        self.tk.configure(background=str(color))

    @property
    def height(self):
        """Get the window's height, in pixels."""
        self.tk.update()
        return self.tk.winfo_height()

    @height.setter
    def height(self, height):
        """Set the window's height, in pixels."""
        self.tk.update()
        self.tk.geometry(self.width+"x"+str(height))

    @property
    def width(self):
        """Get the window's width, in pixels."""
        self.tk.update()
        return self.tk.winfo_width()

    @width.setter
    def width(self, width):
        """Set the window's width, in pixels."""
        self.tk.update()
        self.tk.geometry(str(width)+"x"+str(self.height))

    # METHODS
    # --------------------------------------

    def display(self):
        """Display the application."""
        self.tk.mainloop()

    def on_close(self, command):
        """Call `command` when the window is closed."""
        self.tk.wm_protocol("WM_DELETE_WINDOW", command)

    # Destroys the window and exits the program
    def destroy(self):
        """Destroy the window and exit the program."""
        self.tk.destroy()
        exit(1)

    # DEPRECATED METHODS
    # ------------------------------------

    def set_title(self, title):
        """Set the window's title.
        <Deprecated, use the title property instead>
        """
        self.tk.title(str(title))
        utils.deprecated(
            "App set_title() is deprecated. Please use the title property instead."
        )

    def bgcolor(self, color):
        """Set the window's background color.
        <Deprecated, use the bg property instead>
        """
        self.tk.configure(background=str(color))
        utils.deprecated(
            "App bgcolor() is deprecated. Please use the bg property instead."
        )
