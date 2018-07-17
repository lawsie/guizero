"""
Abstract classes for guizero.
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
    GridMixin,
    EventsMixin)

from . import utilities as utils
from .event import EventManager


class Base():

    def __init__(self, tk):
        """
        The base class for all components in guizero.
        """
        self._tk = tk
        self._tk_defaults = {}
        
        # store the tk widgets default keys
        for key in self.tk.keys():
            self._tk_defaults[key] = self.tk[key]
            
    @property
    def tk(self):
        """
        Returns the tk widget.
        """
        return self._tk

    def _has_tk_config(self, key):
        return key in self.tk.keys()

    def _get_tk_config(self, key, default=False):
        """
        Gets the config from the widget's tk object.

        :param string key:
            The tk config key.

        :param bool default:
            Returns the default value for this key. Defaults to `False`.
        """
        if default:
            return self._tk_defaults[key]
        else:
            return self.tk[key]

    def _set_tk_config(self, keys, value):
        """
        Gets the config from the widget's tk object

        :param string/List keys:
            The tk config key or a list of tk keys.

        :param variable value:
            The value to set. If the value is `None`, the config value will be
            reset to its default.
        """

        # if a single key is passed, convert to list
        if isinstance(keys, str):
            keys = [keys]

        # loop through all the keys
        for key in keys:
            if key in self.tk.keys():
                if value is None:
                    # reset to default
                    self.tk[key] = self._tk_defaults[key]
                else:
                    self.tk[key] = value


class Component(
    Base,
    ScheduleMixin,
    DestroyMixin,
    FocusMixin,
    ColorMixin,
    EventsMixin):

    def __init__(self, master, tk, description):
        """
        An abstract class for a component in guizero.
        """ 
        super(Component, self).__init__(tk)

        self._master = master
        self._description = description
        self._events = EventManager(self, tk)
        
        # check the master
        if self.master is not None:
            if isinstance(master, Container):
                self.master._add_child(self)
            else:
                utils.raise_error("{}\nMaster is not an [App], [Window] or [Box]".format(description))

    @property
    def master(self):
        """
        Returns the master (container) of this widget, or `None` if it doesn't have one.
        """
        return self._master

    @property
    def description(self):
        """
        Sets and returns the description for the widget.
        """
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __repr__(self):
        return self.description

    @property
    def events(self):
        """
        Returns the EventManager which can be used to set custom event handlers.
        """
        return self._events

    def destroy(self):
        """
        Destroy the tk widget.
        """
        # if this widget has a master remove the it from the master
        if self.master is not None:
            self.master._remove_child(self)

        self.tk.destroy()


class Container(Component):

    def __init__(self, master, tk, description, layout):
        """
        An abstract class for a container which can hold other widgets.
        """
        super(Container, self).__init__(master, tk, description)
        self._children = []
        self._layout_manager = layout
        self._bg = None
        self._text_color = None
        self._text_size = None
        self._font = None
        self._enabled = True

        # inherit from master
        if self.master is not None:
            self.bg = master.bg
            self.text_color = master.text_color
            self.text_size = master.text_size
            self.font = master.font

    @property
    def layout(self):
        """
        Returns the layout type used by this container.
        """
        return self._layout_manager

    @property
    def bg(self):
        """
        Sets or returns the background color of the container.
        """
        return self._bg

    @bg.setter
    def bg(self, value):
        self._bg = utils.convert_color(value)
        super(Container, self.__class__).bg.fset(self, self._bg)
        # cascade bg to child widgets
        for child in self.children:
            if isinstance(child, (Container, Widget)):
                child.bg = self._bg

    @property
    def text_color(self):
        """
        Sets and returns the text color to be used by the widgets 
        in the container.

        If set to None (the default) any widgets added to this container
        will use the default text color
        """
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        self._text_color = utils.convert_color(value)
        # cascade text color to child widgets
        for child in self.children:
            if isinstance(child, (Container, TextWidget)):
                child.text_color = self.text_color

    @property
    def text_size(self):
        """
        Sets and returns the text size to be used by the widgets 
        in the container.

        If set to None (the default) any widgets added to this container
        will use the default text size
        """
        return self._text_size

    @text_size.setter
    def text_size(self, value):
        self._text_size = value
        # cascade text color to child widgets
        for child in self.children:
            if isinstance(child, (Container, TextWidget)):
                child.text_size = self.text_size

    @property
    def font(self):
        """
        Sets and returns the font to be used by the widgets 
        in the container.

        If set to None (the default) any widgets added to this container
        will use the default font
        """
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        # cascade text color to child widgets
        for child in self.children:
            if isinstance(child, (Container, TextWidget)):
                child.font = self.font

    @property
    def children(self):
        """
        Returns a list of children widgets
        """
        return self._children

    def _add_child(self, child):
        """
        Associates a child widget with this widget.

        Child widgets are used to cascaded to properties (e.g. bg)
        """
        self.children.append(child)

    def _remove_child(self, child):
        """
        Removes a child widgets association with this widget.
        """
        self.children.remove(child)

    @property
    def enabled(self):
        """
        Sets or Returns the enabled status of this container.

        Setting the property will change the enabled status of all
        widgets in this container
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value:
            self.enable()
        else:
            self.disable()
    
    def disable(self):
        """
        Disable all the widgets in this container
        """
        self._enabled = False
        for child in self.children:
            if isinstance(child, (Container, Widget)):
                child.disable()

    def enable(self):
        """
        Enable all the widgets in this container
        """
        self._enabled = True
        for child in self.children:
            if isinstance(child, (Container, Widget)):
                child.enable()


class BaseWindow(Container):

    def __init__(self, master, tk, description, title, width, height, layout, bg, visible):
        """
        Base class for objects which use windows e.g. `App` and `Window`
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

    def hide(self):
        """Hide the window."""
        self.tk.withdraw()
        self._visible = False

    def show(self):
        """Show the window."""
        self.tk.deiconify()
        self._visible = True

    def _close_window(self):
        if self._on_close is None:
            self.destroy()
        else:
            self._on_close()

    def update(self):
        self.tk.update()


class Widget(
    Component,
    EnableMixin, 
    DisplayMixin, 
    SizeMixin,
    GridMixin):

    def __init__(self, master, tk, description, grid, align, visible, enabled):
        """
        The base class for a widget which is an interactable component e.g. `Picture`
        """
        super(Widget, self).__init__(master,tk, description)
        self._grid = grid
        self._align = align
        self.visible = visible
        self.enabled = enabled

        # inherit from master
        self.bg = master.bg
        if enabled is None:
            self.enabled = master.enabled
        else:
            self.enabled = enabled


class TextWidget(
    Widget,
    TextMixin):

    def __init__(self, master, tk, description, grid, align, visible, enabled):
        """
        The base class for a widget which contains or has text e.g. ``Text`, `PushButton`
        """    
        super(TextWidget, self).__init__(master, tk, description, grid, align, visible, enabled)

        #inherit from master
        self.text_color = master.text_color
        self.text_size = master.text_size
        self.font = master.font
        

class ContainerWidget(
    Container,
    EnableMixin, 
    DisplayMixin,
    SizeMixin,
    GridMixin):

    def __init__(self, master, tk, description, layout, grid, align, visible, enabled):
        """
        The base class for a widget which is also a container e.g. `Box` 
        """
        super(ContainerWidget, self).__init__(master,tk, description, layout)
        self._grid = grid
        self._align = align
        self.visible = visible

        #inherit from master
        if enabled is None:
            self.enabled = master.enabled
        else:
            self.enabled = enabled

class ContainerTextWidget(
    ContainerWidget, 
    TextMixin):

    def __init__(self, master, tk, description, layout, grid, align, visible, enabled):
        """
        The base class for a widget which is also a container and contains text 
        e.g. `ButtonGroup`
        """
        super(ContainerTextWidget, self).__init__(master, tk, description, layout, grid, align, visible, enabled)
