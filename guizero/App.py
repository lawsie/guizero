from tkinter import Tk, Toplevel
from .mixins import ContainerMixin
from .tkmixins import ScheduleMixin, FocusMixin, ReprMixin

from . import utilities as utils

class App(
    ContainerMixin,
    ScheduleMixin,
    FocusMixin, 
    ReprMixin):

    _main_app = None

    def __init__(self, title="guizero", width=500, height=500, layout="auto", bgcolor=None, bg=None):

        # If this is the first app to be created, create Tk
        if App._main_app is None:
            self.tk = Tk()
            App._main_app = self
        else:
            self.tk = Toplevel(App._main_app.tk)
            utils.error_format("There should only be 1 guizero App, use Window to create multiple windows.")
        
        # Initial setup
        self.description = "[App] object"
        self.tk.title( str(title) )
        self.tk.geometry(str(width)+"x"+str(height))
        self._layout_manager = layout  # Only behaves differently for "grid"
        self._visible = True

        # bg overrides deprecated bgcolor
        if bg is not None:
            self.bg = bg
        elif bgcolor is not None:
            self.bg = bgcolor
            utils.deprecated("App 'bgcolor' constructor argument is deprecated. Please use bg instead.")
       
        self.tk.update()
            
    # PROPERTIES
    # -----------------------------------

    # The title text
    @property
    def title(self):
        return self.tk.title()

    @title.setter
    def title(self, text):
        self.tk.title( str(text) )

    # The background colour of the app
    @property
    def bg(self):
        return self.tk.cget("background")

    @bg.setter
    def bg(self, color):
        self.tk.configure(background=utils.convert_color(color))

    # The height of the window
    @property
    def height(self):
        return self.tk.winfo_height()

    @height.setter
    def height(self, height):
        self.tk.geometry(str(self.tk.winfo_width())+"x"+str(height))
        self.tk.update()

    # The width of the window
    @property
    def width(self):
        return self.tk.winfo_width()

    @width.setter
    def width(self, width):
        self.tk.geometry(str(width)+"x"+str(self.tk.winfo_height()))
        self.tk.update()

    @property
    def visible(self):
        return self._visible
    
    @visible.setter
    def visible(self, value):
        if value:
            self.show()
        else:
            self.hide()

    # METHODS
    # --------------------------------------

    # Alias of mainloop with friendlier name
    def display(self):
        self.tk.mainloop()

    # Do `command` when the window is closed
    def on_close(self, command):
        self.tk.wm_protocol("WM_DELETE_WINDOW", command)

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
