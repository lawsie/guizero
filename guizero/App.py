from tkinter import Tk
from .mixins import ContainerMixin
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin, ReprMixin

from . import utilities as utils

class App(
    ContainerMixin,
    ScheduleMixin, 
    DestroyMixin, 
    FocusMixin, 
    ReprMixin):

    def __init__(self, title="guizero", width=500, height=500, layout="auto", bgcolor=None, bg=None):

        self.tk = Tk()

        # Initial setup
        self.tk.title( str(title) )
        self.tk.geometry(str(width)+"x"+str(height))
        self._layout_manager = layout  # Only behaves differently for "grid"

        # bg overrides deprecated bgcolor
        if bg is not None:
            self.tk.configure(background=str(bg))
        elif bgcolor is not None:
            self.tk.configure(background=str(bgcolor))
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
        self.tk.configure(background=str(color))

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

    # METHODS
    # --------------------------------------

    # Alias of mainloop with friendlier name
    def display(self):
        self.tk.mainloop()

    # Do `command` when the window is closed
    def on_close(self, command):
        self.tk.wm_protocol("WM_DELETE_WINDOW", command)


    # DEPRECATED METHODS
    # ------------------------------------

    # Set the title of the window
    def set_title(self, title):
        self.tk.title( str(title) )
        utils.deprecated("App set_title() is deprecated. Please use the title property instead.")

    # Change the background colour
    def bgcolor(self, color):
        self.tk.configure(background=str(color))
        utils.deprecated("App bgcolor() is deprecated. Please use the bg property instead.")
