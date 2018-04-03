from tkinter import Tk, Toplevel
from .base import BaseWindow
from . import utilities as utils

class App(BaseWindow):

    _main_app = None

    def __init__(self, title="guizero", width=500, height=500, layout="auto", bgcolor=None, bg=None, visible=True):
        
        description = "[App] object"

        # If this is the first app to be created, create Tk
        if App._main_app is None:
            tk = Tk()
            App._main_app = self
        else:
            tk = Toplevel(App._main_app.tk)
            utils.error_format("There should only be 1 guizero App, use Window to create multiple windows.")
                
        # bg overrides deprecated bgcolor
        if bgcolor is not None:
            bg = bgcolor
            utils.deprecated("App 'bgcolor' constructor argument is deprecated. Please use bg instead.")
       
        super(App, self).__init__(
            None, 
            tk,
            description,
            title,
            width,
            height,
            layout,
            bg, 
            visible)

    def _close_window(self):
        if self._on_close is None:
            self.destroy()
        else:
            self._on_close()

    # METHODS
    # --------------------------------------

    # Alias of mainloop with friendlier name
    def display(self):
        self.tk.mainloop()

    def destroy(self):
        """Destroy the object."""
        # if this is the main_app - set the _main_app class variable to `None`.
        if self == App._main_app:
            App._main_app = None
        self.tk.destroy()

    def hide(self):
        """Hide the app."""
        self.tk.withdraw()
        self._visible = False

    def show(self):
        """Show the widget."""
        self.tk.deiconify()
        self._visible = True

    # DEPRECATED METHODS
    # ------------------------------------

    # Set the title of the window
    def set_title(self, title):
        self.title = title
        utils.deprecated("App set_title() is deprecated. Please use the title property instead.")

    # Change the background colour
    def bgcolor(self, color):
        self.bg = color
        utils.deprecated("App bgcolor() is deprecated. Please use the bg property instead.")
