from tkinter import Tk, Toplevel
from .mixins import ContainerMixin, MasterMixin
from .tkmixins import ScheduleMixin, FocusMixin, DestroyMixin, ReprMixin

from . import utilities as utils

class Window(
    ContainerMixin,
    MasterMixin,
    ScheduleMixin,
    FocusMixin,
    DestroyMixin, 
    ReprMixin):

    _main_app = None

    def __init__(self, master, title="guizero", width=500, height=500, layout="auto", bg=None, visible=True):

        self.tk = Toplevel(master.tk)
        
        # Initial setup
        self._master = master
        self.description = "[Window] object"
        self.tk.title( str(title) )
        self.tk.geometry(str(width)+"x"+str(height))
        self._layout_manager = layout  # Only behaves differently for "grid"
        self._on_close = None
        self._modal = False
        
        self.bg = bg

        # Window manages delete_window otherwise if the X is used to close the window
        # it destroys it and it cant be shown again
        self.tk.wm_protocol("WM_DELETE_WINDOW", self._close_window)
        
        self.visible = visible
        
        self.tk.update()
        
    
    def _close_window(self):
        if self._on_close is None:
            self.hide()
        else:
            self._on_close()

    # PROPERTIES
    # -----------------------------------

    # The title text
    @property
    def title(self):
        return self.tk.title()

    @title.setter
    def title(self, text):
        self.tk.title( str(text) )

    # The background colour of the window
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

    # Do `command` when the window is closed
    def on_close(self, command):
        self._on_close = command

    def hide(self):
        """Hide the app."""
        self.tk.withdraw()
        self._visible = False
        if self._modal:
            self.tk.grab_release()

    def show(self, wait = False):
        """Show the widget."""
        self.tk.deiconify()
        self._visible = True
        self._modal = wait
        if self._modal:
            self.tk.grab_set()
        
