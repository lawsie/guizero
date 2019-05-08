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
    LayoutMixin,
    EventsMixin)

from . import utilities as utils
from .event import EventManager
from tkinter import BOTH, X, Y, YES
from . import utilities as utils


class Base():

    def __init__(self, tk):
        """
        Base class for all components in guizero.

        :param tk:
            Top level widget instance of Tkinter which usually is the main window of the application

        :return:
            None.
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

        :return:
            tk widget
        """
        return self._tk

    def _has_tk_config(self, key):
        """
        Checks whether the key is configured or not.

        :param key: Key

        :return:
            Keys in tk.keys
        """
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

    def __init__(self, master, tk, description, displayable):
        """
        An abstract class for a component in guizero.
        """
        super(Component, self).__init__(tk)

        self._master = master
        self._description = description
        self._events = EventManager(self, tk)
        self._displayable = displayable

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

        :return:
            Master container of widget, 'None' if it doesn't exists.
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

    @property
    def displayable(self):
        """
        Returns whether the Component can be displayed (packed or gridded)

        Note: this is only used by MenuBar and is a candidate for refactoring
        """
        return self._displayable

    def destroy(self):
        """
        Destroy the tk widget.
        """
        # if this widget has a master remove the it from the master
        if self.master is not None:
            self.master._remove_child(self)

        self.tk.destroy()


class Container(Component):

    def __init__(self, master, tk, description, layout, displayable):
        """
        An abstract class for a container which can hold other widgets.
        """
        super(Container, self).__init__(master, tk, description, displayable)
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

    def add_tk_widget(self, tk_widget, grid=None, align=None, visible=True, enabled=None, width=None, height=None):
        """
        Adds a tk widget into a guizero container.

        :param tkinter.Widget tk_widget:
            The Container (App, Box, etc) the tk widget will belong too.

        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the grid, defaults to None.

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        :param bool enabled:
            If the widget should be enabled, defaults to `None`. If `None`
            the value is inherited from the master.

        :param int width:
            The starting width of the widget. Defaults to `None` and will auto
            size.

        :param int height:
            The starting height of the widget. Defaults to `None` and will auto
            size.
        """
        # raise a warning if the tk widgets master is not this container
        if self.tk is not tk_widget.master:
            utils.error_format("The tk widget's master is not '{}'.\nIt may not display correctly.".format(self.description))
        return Widget(self, tk_widget, "tk widget", grid, align, visible, enabled, width, height)

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

    def display_widgets(self):
        """
        Displays all the widgets associated with this Container.

        Should be called when the widgets need to be "re-packed/gridded".
        """
        # All widgets are removed and then recreated to ensure the order they
        # were created is the order they are displayed.

        for child in self.children:

            if child.displayable:

                # forget the widget
                if self.layout != "grid":
                    child.tk.pack_forget()
                else:
                    child.tk.grid_forget()

                # display the widget
                if child.visible:
                    if self.layout != "grid":
                        self._pack_widget(child)
                    else:
                        self._grid_widget(child)

    def _pack_widget(self, widget):
        pack_params={}

        if widget.width == "fill" and widget.height == "fill":
            pack_params["fill"] = BOTH
            pack_params["expand"] = YES
        elif widget.width == "fill":
            pack_params["fill"] = X
        elif widget.height == "fill":
            pack_params["fill"] = Y

        if widget.align is not None:
            if widget.align in ["top", "bottom", "left", "right"]:
                pack_params["side"] = widget.align
            else:
                utils.error_format("Invalid align value ('{}') for {}\nShould be: top, bottom, left or right".format(
                    widget.align,
                    widget.description
                ))

        # this is to cater for scenario's where the frame will not expand to fill the container
        # if aligned - tk weirdness.
        if pack_params.get("side") is None and pack_params.get("fill") == Y:
            pack_params["expand"] = YES

        if pack_params.get("side") in ["top", "bottom"] and pack_params.get("fill") == Y:
            pack_params["expand"] = YES

        if pack_params.get("side") in ["left", "right"] and pack_params.get("fill") == X:
            pack_params["expand"] = YES

        widget.tk.pack(**pack_params)

    def _grid_widget(self, widget):
        # If they failed to specify grid coords
        if widget.grid is None:
            utils.error_format("{} will not be displayed because it has a missing grid reference.".format(widget.description))
        elif type(widget.grid) is not list:
            utils.error_format("{} will not be displayed because the grid reference is not a list.".format(widget.description))
        # Can have 2 values (just coords) or 4 values (coords and col/rowspan)
        elif (len(widget.grid) != 2 and len(widget.grid) != 4):
            utils.error_format("{} will not be displayed because the grid reference should be either grid=[x, y] or grid=[x, y, columnspan, rowspan].".format(widget.description))
        else:
            grid_params = {
                "column": widget.grid[0],
                "row": widget.grid[1]
            }

            # Just check we have more than 2 as we have already checked it's a multiple of two previously
            if len(widget.grid) > 2:
                grid_params["columnspan"] = widget.grid[2]
                grid_params["rowspan"] = widget.grid[3]

            if widget.align is not None:
                directions = {"top": "N", "bottom": "S", "left": "W", "right": "E"}
                if widget.align in directions.keys():
                    grid_params["sticky"] = directions[widget.align]
                else:
                    utils.error_format("Invalid align value ('{}') for {}\nShould be: top, bottom, left or right".format(
                    widget.align,
                    widget.description
                ))

            widget.tk.grid(**grid_params)

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
        super(BaseWindow, self).__init__(master, tk, description, layout, False)

        # Initial setup
        self.tk.title( str(title) )
        self.tk.geometry(str(width)+"x"+str(height))
        self._on_close = None
        self._full_screen = False

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

    # Whether the window is full screen or not
    @property
    def full_screen(self):
        """
        Sets or returns the visibility of the window
        """
        return self._full_screen

    @full_screen.setter
    def full_screen(self, make_full_screen):
        if make_full_screen:
            self.set_full_screen()
        else:
            self.exit_full_screen()

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

    def set_full_screen(self, keybind="<Escape>"):
        """Make this window full screen and bind the Escape key (or given key) to exit full screen mode"""
        self.tk.attributes("-fullscreen", True)
        self._full_screen = True
        self.events.set_event("<FullScreen.Escape>", keybind, self.exit_full_screen)

    def exit_full_screen(self):
        """Change from full screen to windowed mode and remove key binding"""
        self.tk.attributes("-fullscreen", False)
        self._full_screen = False
        self.events.remove_event("<FullScreen.Escape>")


class Widget(
    Component,
    EnableMixin,
    DisplayMixin,
    SizeMixin,
    LayoutMixin):

    def __init__(self, master, tk, description, grid, align, visible, enabled, width, height):
        """
        The base class for a widget which is an interactable component e.g. `Picture`
        """
        super(Widget, self).__init__(master,tk, description, True)
        self._grid = grid
        self._align = align
        self._width = width
        self._height = height
        self.visible = visible
        self.enabled = enabled

        # inherit from master
        self.bg = master.bg
        if enabled is None:
            self.enabled = master.enabled
        else:
            self.enabled = enabled

        self.resize(width, height)


class TextWidget(
    Widget,
    TextMixin):

    def __init__(self, master, tk, description, grid, align, visible, enabled, width, height):
        """
        The base class for a widget which contains or has text e.g. ``Text`, `PushButton`
        """
        super(TextWidget, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        #inherit from master
        self.text_color = master.text_color
        self.text_size = master.text_size
        self.font = master.font


class ContainerWidget(
    Container,
    EnableMixin,
    DisplayMixin,
    SizeMixin,
    LayoutMixin):

    def __init__(self, master, tk, description, layout, grid, align, visible, enabled, width, height):
        """
        The base class for a widget which is also a container e.g. `Box`, `ButtonGroup`
        """
        super(ContainerWidget, self).__init__(master,tk, description, layout, True)
        self._grid = grid
        self._align = align
        self._width = width
        self._height = height
        self.visible = visible

        #inherit from master
        if enabled is None:
            self.enabled = master.enabled
        else:
            self.enabled = enabled

    def _set_propagation(self, width, height):
        """
        Set the propagation value of the tk widget dependent on the width and height

        :param int width:
            The width of the widget.

        :param int height:
            The height of the widget.
        """
        if width is None:
            width = 0

        if height is None:
            height = 0

        # set the propagate value
        propagate_function = self.tk.pack_propagate
        if self.layout == "grid":
            propagate_function = self.tk.grid_propagate

        propagate_value = True

        # if height or width > 0 need to stop propagation
        if isinstance(width, int):
            if width > 0:
                propagate_value = False
        if isinstance(height, int):
            if height > 0:
                propagate_value = False

        # if you specify a height or width you must specify they other
        # (unless its a fill)
        if isinstance(width, int) and isinstance(height, int):
            if (width == 0 and height > 0) or (height == 0 and width > 0):
                 utils.error_format("You must specify a width and a height for {}".format(self.description))

        propagate_function(propagate_value)


class ContainerTextWidget(
    ContainerWidget,
    TextMixin):

    def __init__(self, master, tk, description, layout, grid, align, visible, enabled, width, height):
        """
        The base class for a widget which is also a container and contains text
        e.g. `ButtonGroup`
        """
        super(ContainerTextWidget, self).__init__(master, tk, description, layout, grid, align, visible, enabled, width, height)
