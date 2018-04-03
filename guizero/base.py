"""
Abstract classes for guizero
"""
from .tkmixins import (
    ScheduleMixin, 
    DestroyMixin, 
    EnableMixin, 
    FocusMixin, 
    DisplayMixin, 
    TextMixin, 
    ColorMixin, 
    SizeMixin,
    GridMixin)

from . import utilities as utils
from .event import EventManager

class Base(
    ScheduleMixin,
    DestroyMixin,
    FocusMixin):

    def __init__(self, master, tk, description):
        """
        The base class for all components in guizero
        """    
        self._master = master
        self._tk = tk
        self._description = description

        self._event_manager = EventManager(self._tk)
        
    @property
    def master(self):
        """
        Returns the master (container) of this widget, or `None` if it doesn't have one.
        """
        return self._master

    @property
    def tk(self):
        """
        Returns the tk widget.
        """
        return self._tk

    @property
    def description(self):
        """
        Sets and returns the description for the widget
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __repr__(self):
        return self.description

    @property
    def when_clicked(self):
        return self._event_manager.get_event("<Button-1>")

    @when_clicked.setter
    def when_clicked(self, value):
        self._event_manager.set_event("<Button-1>", value)

    @property
    def when_key_pressed(self):
        return self._event_manager.get_event("<Key>")

    @when_key_pressed.setter
    def when_key_pressed(self, value):
        self._event_manager.set_event("<Key>", value)

    @property
    def when_mouse_over(self):
        return self._event_manager.get_event("<Enter>")

    @when_mouse_over.setter
    def when_mouse_over(self, value):
        self._event_manager.set_event("<Enter>", value)

    @property
    def when_mouse_moved(self):
        return self._event_manager.get_event("<Motion>")

    @when_mouse_moved.setter
    def when_mouse_moved(self, value):
        self._event_manager.set_event("<Motion>", value)


class Container(Base):

    def __init__(self, master, tk, description, layout):
        """
        An abstract class for a container which can hold other widgets
        """
        self._layout_manager = layout
        super(Container, self).__init__(master, tk, description)

    @property
    def layout(self):
        """
        Returns the layout type used by this container.
        """
        return self._layout_manager


class BaseWindow(Container):

    def __init__(self, master, tk, description, title, width, height, layout, bg, visible):
        """
        Base class for objects which use windows (e.g. App and Window)
        """

        super(BaseWindow, self).__init__(master, tk, description, layout)

        # Initial setup
        self.tk.title( str(title) )
        self.tk.geometry(str(width)+"x"+str(height))
        self._on_close = None

        self.bg = bg

        self.tk.wm_protocol("WM_DELETE_WINDOW", self._close_window)

        self.visible = visible
        
        self.tk.update()
    
    # PROPERTIES
    # -----------------------------------

    # The title text
    @property
    def title(self):
        """
        Sets or returns the title displayed in the title bar.
        """
        return self.tk.title()

    @title.setter
    def title(self, text):
        self.tk.title( str(text) )

    # The background colour of the window
    @property
    def bg(self):
        """
        Sets or returns the background color of the window.
        """
        return self.tk.cget("background")

    @bg.setter
    def bg(self, color):
        self.tk.configure(background=utils.convert_color(color))

    # The height of the window
    @property
    def height(self):
        """
        Sets or returns the height of the window
        """
        return self.tk.winfo_height()

    @height.setter
    def height(self, height):
        self.tk.geometry(str(self.tk.winfo_width())+"x"+str(height))
        self.tk.update()

    # The width of the window
    @property
    def width(self):
        """
        Sets or returns the width of the window
        """
        return self.tk.winfo_width()

    @width.setter
    def width(self, width):
        self.tk.geometry(str(width)+"x"+str(self.tk.winfo_height()))
        self.tk.update()

    @property
    def visible(self):
        """
        Sets or returns the visibility of the window
        """
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


class Widget(
    Base,
    EnableMixin, 
    DisplayMixin, 
    ColorMixin,
    SizeMixin,
    GridMixin):

    def __init__(self, master, tk, description, grid, align, visible, enabled):
        """
        The base class for a widget which is an interactable component.
        """
        super(Widget, self).__init__(master,tk, description)
        self._grid = grid
        self._align = align
        self.visible = visible
        self.enabled = enabled


class TextWidget(
    Widget,
    TextMixin):

    def __init__(self, master, tk, description, grid, align, visible, enabled):
        """
        The base class for a widget which contains or has text
        """    
        super(TextWidget, self).__init__(master, tk, description, grid, align, visible, enabled)


class ContainerWidget(
    Container,
    EnableMixin, 
    DisplayMixin, 
    ColorMixin,
    SizeMixin,
    GridMixin):

    def __init__(self, master, tk, description, layout, grid, align, visible, enabled):
        """
        The base class for a widget which is also a container.
        """
        super(ContainerWidget, self).__init__(master,tk, description, layout)
        self._grid = grid
        self._align = align
        self.visible = visible
        self.enabled = enabled

